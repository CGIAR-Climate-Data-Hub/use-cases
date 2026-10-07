#!/usr/bin/env python3
"""CHIRPS v3 daily (Hugging Face Zarr cube) → admin-level rainfall baseline, anomalies and trend.

Theme 1 of the GCF climate rationale, for ANY country 60°S–60°N — the CR notebook's observed
rainfall is Africa-only. Reads Andrés Aguilar's redistribution of CHIRPS v3.0 daily (`rnl`
flavour) straight from Hugging Face (Zarr v3, CC0), rasterises the Atlas GAUL 2024 adm2 polygons
on the 0.05° CHIRPS grid, and writes per adm0/1/2:

  chirps_admin_annual_<ISO3>        year × unit → ptot_mm, anomaly_mm, anomaly_pct (vs 1991–2020)
  chirps_admin_summary_<ISO3>       unit → baseline mean/SD, Theil–Sen trend (mm/decade), Mann–Kendall p,
                                    last-5-year mean anomaly, wettest/driest year
  chirps_admin_monthly_clim_<ISO3>  unit × month → 1991–2020 mean monthly total (seasonality)
  chirps_admin_<ISO3>.json          inputs, method, caveats, run stats

Usage:
  python chirps_admin.py SYR --out out/ [--boundaries gaul24_a2_africa.parquet] [--start 1981 --end 2025]

Source: https://huggingface.co/datasets/aaguilar90/chirps-v3-daily-rnl (CC0; CDH v0.3.0 record beside the data).
Boundaries: Atlas GAUL 2024 adm2 (Africa parquet). For countries outside Africa pass a GAUL 2024
adm2 file with the same columns (iso3, admin0/1/2_name, gaul0/1/2_code, geometry WKB) via --boundaries.

Dependencies: zarr>=3, xarray, numpy, pandas, pyarrow, shapely, rasterio, scipy. No dask needed.
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
import xarray as xr
from rasterio import features
from rasterio.transform import from_origin
from scipy import stats
from shapely import from_wkb

log = logging.getLogger("chirps_admin")

ZARR_URL = "https://huggingface.co/datasets/aaguilar90/chirps-v3-daily-rnl/resolve/main/chirps-v3-daily-rnl.zarr"
BOUNDARIES_URL = ("https://digital-atlas.s3.amazonaws.com/domain=boundaries/type=admin/source=gaul2024/"
                  "region=africa/processing=analysis-ready/level=adm2/atlas_gaul24_a2_africa.parquet")
LICENCE = "CC0-1.0 (CHIRPS v3.0, Climate Hazards Center; HF redistribution by A. Aguilar, Alliance)"
RES = 0.05
BASE0, BASE1 = 1991, 2020
R_EARTH = 6371008.8


def load_boundaries(path: Path | None, iso3: str) -> pd.DataFrame:
    if path is None or not Path(path).exists():
        path = Path("gaul24_a2_africa.parquet")
        if not path.exists():
            log.info("downloading adm2 boundaries (~91 MB) → %s", path)
            urllib.request.urlretrieve(BOUNDARIES_URL, path)
    df = pq.read_table(path).to_pandas()
    # Accept the raw global GAUL 2024 schema (iso3_code, gaul0_name …) as well as the Atlas analysis-ready one.
    df = df.rename(columns={"iso3_code": "iso3", "gaul0_name": "admin0_name", "gaul1_name": "admin1_name", "gaul2_name": "admin2_name"})
    df = df[df["iso3"] == iso3].copy()
    if df.empty:
        raise SystemExit(f"no adm2 rows for {iso3} in {path} (outside Africa? pass --boundaries with a GAUL 2024 adm2 extract)")
    df["geom"] = [from_wkb(g) for g in df["geometry"]]
    for c in ("gaul0_code", "gaul1_code", "gaul2_code"):
        df[c] = df[c].astype("int64")
    df = df.reset_index(drop=True)
    df["adm_idx"] = np.arange(1, len(df) + 1, dtype=np.int32)
    return df.drop(columns=["geometry"])


def rasterize_units(adm: pd.DataFrame, lats: np.ndarray, lons: np.ndarray) -> np.ndarray:
    """adm2 index raster on the CHIRPS sub-grid (lat descending). Units with no centre pixel get the
    pixel under their centroid so small adm2s are not silently dropped."""
    tr = from_origin(lons[0] - RES / 2, lats[0] + RES / 2, RES, RES)
    ids = features.rasterize([(g, int(i)) for g, i in zip(adm["geom"], adm["adm_idx"])],
                             out_shape=(len(lats), len(lons)), transform=tr, fill=0, dtype="int32", all_touched=False)
    missing = set(adm["adm_idx"]) - set(np.unique(ids))
    for i in missing:
        c = adm.loc[adm.adm_idx == i, "geom"].iloc[0].centroid
        r = int(round((lats[0] - c.y) / RES)); col = int(round((c.x - lons[0]) / RES))
        if 0 <= r < len(lats) and 0 <= col < len(lons):
            ids[r, col] = i
    log.info("rasterised %d adm2 units on %dx%d grid (%d needed centroid fallback)", len(adm), *ids.shape, len(missing))
    return ids


def run(iso3: str, out: Path, boundaries: Path | None, start: int, end: int) -> None:
    t0 = time.time()
    adm = load_boundaries(boundaries, iso3)
    minx = min(g.bounds[0] for g in adm.geom); miny = min(g.bounds[1] for g in adm.geom)
    maxx = max(g.bounds[2] for g in adm.geom); maxy = max(g.bounds[3] for g in adm.geom)
    ds = xr.open_zarr(ZARR_URL, consolidated=True, chunks=None)
    sub = ds.precip.sel(lat=slice(maxy + RES, miny - RES), lon=slice(minx - RES, maxx + RES))
    lats, lons = sub.lat.values, sub.lon.values
    ids = rasterize_units(adm, lats, lons)
    area = (math.radians(RES) * R_EARTH) ** 2 * np.cos(np.radians(lats))[:, None] * np.ones((1, len(lons)))
    m = ids > 0
    n_units = int(adm.adm_idx.max())

    def zonal(arr2d: np.ndarray) -> np.ndarray:
        """Area-weighted mean per adm_idx (1..n) ignoring NaN. Returns array len n+1 (0 unused)."""
        v = arr2d[m]; w = area[m]; k = ids[m]
        ok = ~np.isnan(v)
        num = np.bincount(k[ok], weights=(v * w)[ok], minlength=n_units + 1)
        den = np.bincount(k[ok], weights=w[ok], minlength=n_units + 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            return np.where(den > 0, num / den, np.nan)

    years = list(range(start, end + 1))
    annual = np.full((len(years), n_units + 1), np.nan)
    monthly = np.full((12, n_units + 1), np.nan)
    mcount = np.zeros(12)
    for yi, y in enumerate(years):
        t1 = time.time()
        da = sub.sel(time=slice(f"{y}-01-01", f"{y}-12-31")).load()
        if da.time.size < 360:
            log.warning("year %d has %d days — skipped", y, da.time.size)
            continue
        annual[yi] = zonal(da.sum("time", min_count=1).values)
        if BASE0 <= y <= BASE1:
            mon = da.groupby("time.month").sum("time", min_count=1)
            for mi in range(12):
                z = zonal(mon.sel(month=mi + 1).values)
                monthly[mi] = np.nansum(np.vstack([monthly[mi], z]), axis=0) if mcount[mi] else z
            mcount += 1
        log.info("  %d done (%.1fs)", y, time.time() - t1)
    monthly = monthly / np.where(mcount > 0, mcount, np.nan)[:, None]

    # adm2 long table → aggregate upwards by area-weighted mean (weights = unit area in grid)
    unit_area = np.bincount(ids[m], weights=area[m], minlength=n_units + 1)
    meta = adm[["adm_idx", "iso3", "admin0_name", "admin1_name", "admin2_name", "gaul0_code", "gaul1_code", "gaul2_code"]]
    rows = []
    for yi, y in enumerate(years):
        for i in range(1, n_units + 1):
            rows.append((i, y, annual[yi, i]))
    a2 = pd.DataFrame(rows, columns=["adm_idx", "year", "ptot_mm"]).merge(meta, on="adm_idx")
    a2["w"] = a2["adm_idx"].map(lambda i: unit_area[i])
    # GAUL 2024 carries disputed territories (e.g. Bir Tawil, Hala'ib Triangle for EGY) as separate gaul0 codes
    # under the same iso3. adm0 is computed over the main gaul0 code only; disputed units stay at adm1/adm2 with a flag.
    main_g0 = int(adm["gaul0_code"].mode().iloc[0])
    a2["disputed"] = a2["gaul0_code"] != main_g0
    n_disputed = int(adm[adm["gaul0_code"] != main_g0].shape[0])

    def wmean(x: pd.DataFrame) -> float:
        w = x["w"].to_numpy(dtype=float)
        v = x["ptot_mm"].to_numpy(dtype=float)
        return float(np.average(v, weights=w)) if w.sum() > 0 else float(v.mean())  # units with no grid area fall back to a plain mean

    def agg(df, keys, level):
        d = df.dropna(subset=["ptot_mm"])
        if level == 0:
            d = d[~d["disputed"]]
        g = d.groupby(["iso3", "admin0_name", "gaul0_code"] + keys + ["year"], dropna=False)
        o = g.apply(wmean, include_groups=False).reset_index(name="ptot_mm")
        o["admin_level"] = level
        o["disputed"] = o["gaul0_code"] != main_g0
        return o

    parts = [agg(a2, [], 0), agg(a2, ["admin1_name", "gaul1_code"], 1), agg(a2, ["admin1_name", "gaul1_code", "admin2_name", "gaul2_code"], 2)]
    ann = pd.concat(parts, ignore_index=True)
    for c in ("admin1_name", "gaul1_code", "admin2_name", "gaul2_code"):
        if c not in ann:
            ann[c] = pd.NA
    key = ["admin_level", "gaul0_code", "gaul1_code", "gaul2_code"]
    base = ann[(ann.year >= BASE0) & (ann.year <= BASE1)].groupby(key, dropna=False)["ptot_mm"].agg(baseline_mean="mean", baseline_sd="std", baseline_n="count").reset_index()
    ann = ann.merge(base, on=key, how="left")
    ann["anomaly_mm"] = ann["ptot_mm"] - ann["baseline_mean"]
    ann["anomaly_pct"] = 100 * ann["anomaly_mm"] / ann["baseline_mean"]
    ann["baseline"] = f"{BASE0}-{BASE1}"

    # summary per unit
    summ = []
    for k, g in ann.sort_values("year").groupby(key, dropna=False):
        g = g.dropna(subset=["ptot_mm"])
        if len(g) < 10:
            continue
        ts = stats.theilslopes(g["ptot_mm"].values, g["year"].values)
        tau = stats.kendalltau(g["year"].values, g["ptot_mm"].values)
        last5 = g[g.year > end - 5]
        summ.append({**dict(zip(key, k)), "admin0_name": g.admin0_name.iloc[0], "admin1_name": g.admin1_name.iloc[0], "admin2_name": g.admin2_name.iloc[0],
                     "iso3": iso3, "years": f"{int(g.year.min())}-{int(g.year.max())}", "n_years": int(len(g)),
                     "baseline_mean_mm": float(g.baseline_mean.iloc[0]), "baseline_sd_mm": float(g.baseline_sd.iloc[0]),
                     "trend_mm_per_decade": float(ts.slope * 10), "trend_ci_low": float(ts.low_slope * 10), "trend_ci_high": float(ts.high_slope * 10),
                     "mk_tau": float(tau.statistic), "mk_p": float(tau.pvalue),
                     "last5_mean_anomaly_mm": float(last5.anomaly_mm.mean()), "last5_mean_anomaly_pct": float(last5.anomaly_pct.mean()),
                     "wettest_year": int(g.loc[g.ptot_mm.idxmax(), "year"]), "driest_year": int(g.loc[g.ptot_mm.idxmin(), "year"])})
    summ = pd.DataFrame(summ)

    # monthly climatology table
    mrows = []
    for i in range(1, n_units + 1):
        for mi in range(12):
            mrows.append((i, mi + 1, monthly[mi, i]))
    m2 = pd.DataFrame(mrows, columns=["adm_idx", "month", "ptot_mm"]).merge(meta, on="adm_idx"); m2["w"] = m2["adm_idx"].map(lambda i: unit_area[i])
    m2["disputed"] = m2["gaul0_code"] != main_g0
    m2 = m2.rename(columns={"month": "year"})
    mparts = [agg(m2, [], 0), agg(m2, ["admin1_name", "gaul1_code"], 1), agg(m2, ["admin1_name", "gaul1_code", "admin2_name", "gaul2_code"], 2)]
    mclim = pd.concat(mparts, ignore_index=True).rename(columns={"year": "month"})
    mclim["baseline"] = f"{BASE0}-{BASE1}"

    order = ["iso3", "admin_level", "admin0_name", "gaul0_code", "admin1_name", "gaul1_code", "admin2_name", "gaul2_code"]
    out.mkdir(parents=True, exist_ok=True)
    ann[order + ["disputed", "year", "ptot_mm", "baseline", "baseline_mean", "baseline_sd", "anomaly_mm", "anomaly_pct"]].to_parquet(out / f"chirps_admin_annual_{iso3}.parquet", index=False)
    summ.to_parquet(out / f"chirps_admin_summary_{iso3}.parquet", index=False)
    mclim.to_parquet(out / f"chirps_admin_monthly_clim_{iso3}.parquet", index=False)
    for name, df in (("annual", ann), ("summary", summ), ("monthly_clim", mclim)):
        df.to_csv(out / f"chirps_admin_{name}_{iso3}.csv", index=False)
    side = {"id": f"chirps-admin-{iso3.lower()}", "title": f"CHIRPS v3 daily (rnl) → admin rainfall baseline, anomalies, trend — {iso3}",
            "run_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
            "inputs": {"zarr": ZARR_URL, "boundaries": BOUNDARIES_URL if boundaries is None else str(boundaries)},
            "method": (f"daily precip summed to annual totals per 0.05° pixel for {start}–{end}; adm2 = area-weighted mean of pixels whose centre "
                       f"falls in the polygon (centroid pixel if none); adm1/adm0 = area-weighted means of adm2; baseline {BASE0}–{BASE1}; "
                       "anomaly = year − baseline mean; trend = Theil–Sen slope ×10 with 95% CI; Mann–Kendall via Kendall's tau p-value; "
                       f"monthly climatology = mean {BASE0}–{BASE1} monthly totals."),
            "licence": LICENCE,
            "caveats": ["CHIRPS 'rnl' daily = pentad totals disaggregated with ERA5; do not mix with the 'sat' flavour.",
                        "Values stored as int16 × 0.1 mm in the source cube (±0.05 mm).",
                        "Station density varies through time and between countries; trends may reflect input changes (CHC caveat).",
                        "0.05° pixels (~5.5 km): adm2 units smaller than a pixel use the centroid pixel.",
                        f"{end} is the last complete year requested; partial years are skipped.",
                        f"GAUL 2024 lists {n_disputed} disputed-territory unit(s) under {iso3} with their own gaul0 code; adm0 uses the main code "
                        f"({main_g0}) only, disputed units are flagged `disputed=true` at adm1/adm2 (Atlas convention CR-115 still open)."],
            "stats": {"adm2_units": n_units, "disputed_units": n_disputed, "main_gaul0_code": main_g0, "grid": [int(len(lats)), int(len(lons))],
                      "years": years, "seconds": round(time.time() - t0, 1)}}
    (out / f"chirps_admin_{iso3}.json").write_text(json.dumps(side, indent=2, ensure_ascii=False))
    log.info("wrote %s (%.0fs)", out, time.time() - t0)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("iso3")
    ap.add_argument("--out", default="out")
    ap.add_argument("--boundaries", default=None)
    ap.add_argument("--start", type=int, default=1981)
    ap.add_argument("--end", type=int, default=dt.date.today().year - 1)
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if a.verbose else logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    run(a.iso3.upper(), Path(a.out), Path(a.boundaries) if a.boundaries else None, a.start, a.end)


if __name__ == "__main__":
    sys.exit(main())
