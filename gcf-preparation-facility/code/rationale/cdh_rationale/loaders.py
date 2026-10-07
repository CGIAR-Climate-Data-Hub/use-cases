"""Load the inputs the rationale prototype reads: the rationale map, the federated pulls, the
WorldCover admin products and the Atlas `haz_freq` table. Everything is optional — a missing
input becomes a gap fragment downstream, never a fabricated value."""
from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd
import yaml

log = logging.getLogger("cdh_rationale")

HERE = Path(__file__).resolve().parent
DEFAULT_MAP = HERE.parents[2] / "data" / "rationale-map.yaml"   # gcf-preparation-facility/data/
HAZ_FREQ_URL = ("https://digital-atlas.s3.amazonaws.com/domain=climate/type=hazard-indices/source=nex-gddp-cmip6/"
                "region=africa/processing=hazard-change/timeframe=annual/variable=haz_freq.parquet")
HAZ_FREQ_LICENCE = "CC0 (derived from NEX-GDDP-CMIP6; Atlas hazard-change product, 2026-06-24)"


def load_map(path: Path | None = None) -> dict:
    p = Path(path) if path else DEFAULT_MAP
    with open(p) as f:
        return yaml.safe_load(f)


def load_federated(fed_dir: Path | None, iso3: str) -> pd.DataFrame:
    if not fed_dir:
        return pd.DataFrame()
    fed_dir = Path(fed_dir)
    frames = []
    for p in sorted(fed_dir.glob(f"*_{iso3}.parquet")):
        if p.name.startswith("federated_"):
            continue
        frames.append(pd.read_parquet(p))
    if not frames:
        log.warning("no federated parquet files for %s in %s", iso3, fed_dir)
        return pd.DataFrame()
    df = pd.concat(frames, ignore_index=True)
    log.info("federated: %d rows from %d sources", len(df), df["source"].nunique())
    return df


def load_worldcover(wc_dir: Path | None, iso3: str) -> dict[str, pd.DataFrame]:
    out = {}
    if not wc_dir:
        return out
    wc_dir = Path(wc_dir)
    for key in ("area", "change", "cropland"):
        p = wc_dir / f"worldcover_admin_{key}_{iso3}.parquet"
        if p.exists():
            out[key] = pd.read_parquet(p)
    if out:
        log.info("worldcover: %s", ", ".join(f"{k}={len(v)}" for k, v in out.items()))
    return out


def load_haz_freq(iso3: str, *, remote: bool = True, local: Path | None = None) -> pd.DataFrame:
    """Per-GCM hazard frequency at adm0 and adm1 for one country (Atlas S3, anonymous)."""
    src = str(local) if local else HAZ_FREQ_URL
    if not remote and not local:
        return pd.DataFrame()
    try:
        import duckdb
    except ImportError:
        log.warning("duckdb not installed — haz_freq skipped")
        return pd.DataFrame()
    con = duckdb.connect()
    if src.startswith("http"):
        con.execute("INSTALL httpfs; LOAD httpfs;")
    q = f"""
        SELECT iso3, admin0_name, admin1_name, admin2_name, variable, value, scenario, model, timeframe,
               severity, hazard, hazard_user
        FROM read_parquet('{src}', hive_partitioning=false)
        WHERE iso3 = '{iso3}' AND variable = 'frequency' AND admin2_name IS NULL
    """
    try:
        df = con.execute(q).df()
    except Exception as e:  # noqa: BLE001
        log.warning("haz_freq query failed: %s", e)
        return pd.DataFrame()
    df["admin_level"] = df["admin1_name"].isna().map({True: 0, False: 1})
    df["source_url"] = src
    log.info("haz_freq: %d rows (%d GCMs)", len(df), df["model"].nunique())
    return df
