#!/usr/bin/env python3
"""ESA WorldCover → admin-level land-cover areas and 2020→2021 change, per country.

Derived product for the Climate Data Hub (GCF Prep Facility Theme 6, AgWise cropland fraction).
Reads the 10 m WorldCover COGs straight from the public S3 bucket (no mirror), rasterises the
Atlas GAUL 2024 adm2 polygons on the WorldCover grid window by window, and accumulates
area-weighted class counts. Outputs (Parquet + CSV):

  worldcover_admin_area_<ISO3>      admin0/1/2 × year × class → area_ha, share
  worldcover_admin_change_<ISO3>    admin0/1/2 × class_2020 × class_2021 → area_ha (transition matrix)
  worldcover_admin_cropland_<ISO3>  admin0/1/2 × year → cropland_ha, cropland_share (class 40) — AgWise
  worldcover_admin_<ISO3>.json      method, inputs, caveats, run metadata

Usage:
  python worldcover_admin.py TGO --out out/
  python worldcover_admin.py KEN --out out/ --boundaries /path/atlas_gaul24_a2_africa.parquet

Inputs (all public, anonymous):
  s3://esa-worldcover/v100/2020/map/ESA_WorldCover_10m_2020_v100_<TILE>_Map.tif   (CC BY 4.0)
  s3://esa-worldcover/v200/2021/map/ESA_WorldCover_10m_2021_v200_<TILE>_Map.tif
  https://esa-worldcover.s3.eu-central-1.amazonaws.com/esa_worldcover_grid.geojson
  https://digital-atlas.s3.amazonaws.com/domain=boundaries/type=admin/source=gaul2024/region=africa/
      processing=analysis-ready/level=adm2/atlas_gaul24_a2_africa.parquet                 (GAUL 2024)

Caveat carried into the sidecar: v100 (2020) and v200 (2021) were produced with different
algorithm versions, so 2020→2021 change mixes real change with method change (ESA's own warning).
Publish the change table, flag it `not_recommended_for: trend claims`.

Dependencies: rasterio, numpy, pandas, pyarrow, shapely (no geopandas, no GDAL CLI needed).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import math
import sys
import time
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import rasterio
from rasterio import features, windows
from shapely import STRtree, from_wkb, box

log = logging.getLogger("worldcover_admin")

GRID_URL = "https://esa-worldcover.s3.eu-central-1.amazonaws.com/esa_worldcover_grid.geojson"
BOUNDARIES_URL = ("https://digital-atlas.s3.amazonaws.com/domain=boundaries/type=admin/source=gaul2024/"
                  "region=africa/processing=analysis-ready/level=adm2/atlas_gaul24_a2_africa.parquet")
VERSIONS = {2020: "v100", 2021: "v200"}
CLASSES = {10: "Tree cover", 20: "Shrubland", 30: "Grassland", 40: "Cropland", 50: "Built-up",
           60: "Bare / sparse vegetation", 70: "Snow and ice", 80: "Permanent water bodies",
           90: "Herbaceous wetland", 95: "Mangroves", 100: "Moss and lichen"}
R_EARTH = 6371008.8  # m, mean radius


def tile_url(year: int, tile: str) -> str:
    v = VERSIONS[year]
    return f"s3://esa-worldcover/{v}/{year}/map/ESA_WorldCover_10m_{year}_{v}_{tile}_Map.tif"


def load_boundaries(path: Path | None, iso3: str) -> pd.DataFrame:
    """GAUL 2024 adm2 rows for one country, geometries as shapely objects."""
    if path is None or not Path(path).exists():
        path = Path("gaul24_a2_africa.parquet")
        if not path.exists():
            log.info("downloading adm2 boundaries (~91 MB) → %s", path)
            urllib.request.urlretrieve(BOUNDARIES_URL, path)
    t = pq.read_table(path)
    df = t.to_pandas()
    df = df[df["iso3"] == iso3].copy()
    if df.empty:
        raise SystemExit(f"no adm2 rows for {iso3} in {path}")
    df["geom"] = [from_wkb(g) for g in df["geometry"]]
    for c in ("gaul0_code", "gaul1_code", "gaul2_code"):
        df[c] = df[c].astype("int64")
    df = df.reset_index(drop=True)
    df["adm_idx"] = np.arange(1, len(df) + 1, dtype=np.uint32)  # 0 = outside
    log.info("%s: %d adm2 units, %d adm1", iso3, len(df), df["gaul1_code"].nunique())
    return df.drop(columns=["geometry"])


def tiles_for_bbox(bbox) -> list[str]:
    with urllib.request.urlopen(GRID_URL) as r:
        grid = json.load(r)
    b = box(*bbox)
    out = []
    for f in grid["features"]:
        xs = [p[0] for p in f["geometry"]["coordinates"][0]]
        ys = [p[1] for p in f["geometry"]["coordinates"][0]]
        if box(min(xs), min(ys), max(xs), max(ys)).intersects(b):
            out.append(f["properties"]["ll_tile"])
    return sorted(out)


def pixel_area_ha(transform, win) -> np.ndarray:
    """Per-row pixel area (ha) for a window on a lat/lon grid: dlat*dlon*R²*cos(lat)."""
    dlon = abs(transform.a)
    dlat = abs(transform.e)
    rows = np.arange(win.row_off, win.row_off + win.height)
    lat = transform.f + transform.e * (rows + 0.5)
    area_m2 = (math.radians(dlat) * R_EARTH) * (math.radians(dlon) * R_EARTH) * np.cos(np.radians(lat))
    return (area_m2 / 10_000.0).astype(np.float64)


def run(iso3: str, out: Path, boundaries: Path | None, block: int = 2048) -> None:
    t0 = time.time()
    adm = load_boundaries(boundaries, iso3)
    geoms = list(adm["geom"])
    tree = STRtree(geoms)
    minx = min(g.bounds[0] for g in geoms); miny = min(g.bounds[1] for g in geoms)
    maxx = max(g.bounds[2] for g in geoms); maxy = max(g.bounds[3] for g in geoms)
    bbox = (minx, miny, maxx, maxy)
    tiles = tiles_for_bbox(bbox)
    log.info("bbox %s → tiles %s", [round(v, 3) for v in bbox], tiles)

    # accumulator: (adm_idx, lc2020, lc2021) -> ha
    acc: dict[tuple[int, int, int], float] = {}
    env = rasterio.Env(AWS_NO_SIGN_REQUEST="YES", GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR",
                       CPL_VSIL_CURL_ALLOWED_EXTENSIONS=".tif", GDAL_HTTP_MAX_RETRY="5", GDAL_HTTP_RETRY_DELAY="2")
    n_win = 0
    with env:
        for tile in tiles:
            with rasterio.open(tile_url(2020, tile)) as a, rasterio.open(tile_url(2021, tile)) as b:
                assert a.transform == b.transform and a.shape == b.shape, f"grid mismatch in {tile}"
                tr = a.transform
                # window covering the country bbox within this tile
                full = windows.from_bounds(*bbox, transform=tr).round_offsets().round_lengths()
                full = full.intersection(windows.Window(0, 0, a.width, a.height))
                if full.width <= 0 or full.height <= 0:
                    continue
                for roff in range(int(full.row_off), int(full.row_off + full.height), block):
                    for coff in range(int(full.col_off), int(full.col_off + full.width), block):
                        win = windows.Window(coff, roff, min(block, int(full.col_off + full.width) - coff),
                                             min(block, int(full.row_off + full.height) - roff))
                        wb = windows.bounds(win, tr)
                        hits = tree.query(box(*wb))
                        if len(hits) == 0:
                            continue
                        wtr = windows.transform(win, tr)
                        shapes = [(geoms[i], int(adm.at[i, "adm_idx"])) for i in hits]
                        ids = features.rasterize(shapes, out_shape=(int(win.height), int(win.width)),
                                                 transform=wtr, fill=0, dtype="uint32", all_touched=False)
                        if not ids.any():
                            continue
                        lc0 = a.read(1, window=win)
                        lc1 = b.read(1, window=win)
                        area = pixel_area_ha(tr, win)  # per row
                        m = ids > 0
                        key = (ids[m].astype(np.int64) << 16) | (lc0[m].astype(np.int64) << 8) | lc1[m].astype(np.int64)
                        w = np.broadcast_to(area[:, None], ids.shape)[m]
                        uk, inv = np.unique(key, return_inverse=True)
                        sums = np.bincount(inv, weights=w)
                        for k, s in zip(uk.tolist(), sums.tolist()):
                            acc[k] = acc.get(k, 0.0) + s
                        n_win += 1
                        if n_win % 25 == 0:
                            log.info("  %s windows done (%.0fs)", n_win, time.time() - t0)
    log.info("zonal pass done: %d windows, %d (adm,lc20,lc21) cells, %.0fs", n_win, len(acc), time.time() - t0)

    # long table at adm2
    rows = []
    for k, ha in acc.items():
        rows.append((k >> 16, (k >> 8) & 0xFF, k & 0xFF, ha))
    cell = pd.DataFrame(rows, columns=["adm_idx", "lc2020", "lc2021", "area_ha"])
    meta_cols = ["iso3", "admin0_name", "admin1_name", "admin2_name", "gaul0_code", "gaul1_code", "gaul2_code"]
    cell = cell.merge(adm[["adm_idx"] + meta_cols], on="adm_idx", how="left")

    def by_level(df: pd.DataFrame, keys: list[str], level: int) -> pd.DataFrame:
        g = df.groupby(["iso3", "admin0_name", "gaul0_code"] + keys, dropna=False)
        return g.sum(numeric_only=True).reset_index().assign(admin_level=level)

    levels = [
        (0, []),
        (1, ["admin1_name", "gaul1_code"]),
        (2, ["admin1_name", "gaul1_code", "admin2_name", "gaul2_code"]),
    ]
    # change (transition) table
    change_parts, area_parts = [], []
    for lvl, keys in levels:
        c = cell.groupby(["iso3", "admin0_name", "gaul0_code"] + keys + ["lc2020", "lc2021"], dropna=False)["area_ha"].sum().reset_index()
        c["admin_level"] = lvl
        change_parts.append(c)
        for year, col in ((2020, "lc2020"), (2021, "lc2021")):
            a_ = cell.groupby(["iso3", "admin0_name", "gaul0_code"] + keys + [col], dropna=False)["area_ha"].sum().reset_index()
            a_ = a_.rename(columns={col: "lc_class"})
            a_["year"] = year
            a_["admin_level"] = lvl
            area_parts.append(a_)
    change = pd.concat(change_parts, ignore_index=True)
    area = pd.concat(area_parts, ignore_index=True)
    for df in (change, area):
        for c in ("admin1_name", "gaul1_code", "admin2_name", "gaul2_code"):
            if c not in df:
                df[c] = pd.NA
    area["lc_label"] = area["lc_class"].map(CLASSES).fillna("No data / outside")
    change["lc2020_label"] = change["lc2020"].map(CLASSES).fillna("No data")
    change["lc2021_label"] = change["lc2021"].map(CLASSES).fillna("No data")
    tot = area.groupby(["admin_level", "gaul0_code", "gaul1_code", "gaul2_code", "year"], dropna=False)["area_ha"].transform("sum")
    area["share"] = area["area_ha"] / tot
    area["version"] = area["year"].map(VERSIONS)
    crop = area[area["lc_class"] == 40][["iso3", "admin_level", "admin0_name", "gaul0_code", "admin1_name", "gaul1_code",
                                          "admin2_name", "gaul2_code", "year", "area_ha", "share"]]
    crop = crop.rename(columns={"area_ha": "cropland_ha", "share": "cropland_share"})

    order = ["iso3", "admin_level", "admin0_name", "gaul0_code", "admin1_name", "gaul1_code", "admin2_name", "gaul2_code"]
    area = area[order + ["year", "version", "lc_class", "lc_label", "area_ha", "share"]].sort_values(order + ["year", "lc_class"])
    change = change[order + ["lc2020", "lc2020_label", "lc2021", "lc2021_label", "area_ha"]].sort_values(order + ["lc2020", "lc2021"])

    out.mkdir(parents=True, exist_ok=True)
    for name, df in (("worldcover_admin_area", area), ("worldcover_admin_change", change), ("worldcover_admin_cropland", crop)):
        df.to_parquet(out / f"{name}_{iso3}.parquet", index=False)
        df.to_csv(out / f"{name}_{iso3}.csv", index=False)
    side = {
        "id": f"worldcover-admin-{iso3.lower()}",
        "title": f"ESA WorldCover admin-level land-cover areas and 2020→2021 change — {iso3}",
        "run_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "inputs": {"worldcover": [tile_url(y, t) for y in VERSIONS for t in tiles],
                   "boundaries": BOUNDARIES_URL, "tile_grid": GRID_URL},
        "method": ("adm2 polygons (GAUL 2024, Atlas analysis-ready) rasterised on the WorldCover 1/12000° grid per "
                   f"{block}×{block} window (all_touched=False, pixel assigned to the polygon containing its centre); "
                   "pixel area = R²·Δlat·Δlon·cos(lat) in ha; class areas and 2020→2021 transitions summed per adm2, "
                   "then aggregated to adm1/adm0 by GAUL code. No-data (0) kept as class 0."),
        "classes": CLASSES,
        "licence": {"worldcover": "CC BY 4.0 (ESA WorldCover; cite v100 DOI 10.5281/zenodo.5571936, v200 DOI 10.5281/zenodo.7254221)",
                    "boundaries": "GAUL 2024 via Atlas"},
        "caveats": ["2020 (v100) and 2021 (v200) use different algorithm versions: change mixes real land-cover change "
                    "with method change (ESA WorldCover product note). not_recommended_for: trend claims.",
                    "Centre-pixel assignment at 10 m: boundary pixels are attributed to one unit; areas sum to the "
                    "rasterised country, not to the vector area."],
        "stats": {"adm2_units": int(len(adm)), "windows": n_win, "cells": len(acc),
                  "country_area_ha_2021": float(area[(area.admin_level == 0) & (area.year == 2021)]["area_ha"].sum()),
                  "seconds": round(time.time() - t0, 1)},
    }
    (out / f"worldcover_admin_{iso3}.json").write_text(json.dumps(side, indent=2, ensure_ascii=False))
    log.info("wrote %s (%.0fs)", out, time.time() - t0)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("iso3")
    ap.add_argument("--out", default="out")
    ap.add_argument("--boundaries", default=None, help="local copy of atlas_gaul24_a2_africa.parquet (downloaded if absent)")
    ap.add_argument("--block", type=int, default=2048)
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if a.verbose else logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    run(a.iso3.upper(), Path(a.out), Path(a.boundaries) if a.boundaries else None, a.block)


if __name__ == "__main__":
    sys.exit(main())
