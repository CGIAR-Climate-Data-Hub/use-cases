"""Run every federated client for one country and write tidy tables.

    python -m cdh_federated TGO --out ./out            # all sources
    python -m cdh_federated TGO --only inform,dhs      # a subset

Writes ``<out>/<source>_<ISO3>.parquet`` (+ .csv) per source, a combined
``federated_<ISO3>.parquet`` and a ``manifest_<ISO3>.json`` with row counts, retrieval
timestamps, request URLs and licences — the manifest is the citation record.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
import time
from pathlib import Path

import pandas as pd

from . import SOURCES
from .common import now_iso


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="cdh_federated")
    ap.add_argument("iso3", help="ISO 3166-1 alpha-3, e.g. TGO")
    ap.add_argument("--out", default="out", help="output directory")
    ap.add_argument("--only", help="comma-separated source keys to run", default=None)
    ap.add_argument("--no-csv", action="store_true", help="skip the CSV twins")
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if a.verbose else logging.INFO,
                        format="%(levelname)s %(name)s: %(message)s")
    log = logging.getLogger("cdh_federated")

    iso3 = a.iso3.upper()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    keys = [k.strip() for k in a.only.split(",")] if a.only else list(SOURCES)
    manifest = {"iso3": iso3, "run_at": now_iso(), "sources": {}}
    frames = []
    for k in keys:
        if k not in SOURCES:
            log.error("unknown source %s (choose from %s)", k, ", ".join(SOURCES))
            return 2
        t0 = time.time()
        try:
            df = SOURCES[k](iso3)
            status = "ok" if not df.empty else "empty"
        except Exception as e:  # noqa: BLE001 — one failing provider must not stop the others
            log.error("%s failed: %s", k, e)
            df, status = pd.DataFrame(), f"error: {e.__class__.__name__}: {e}"
        dt_s = round(time.time() - t0, 1)
        entry = {"status": status, "rows": int(len(df)), "seconds": dt_s}
        if not df.empty:
            entry.update({
                "admin_levels": sorted(int(x) for x in df["admin_level"].dropna().unique()),
                "indicators": int(df["indicator_id"].nunique()),
                "periods": (lambda p: [p.min(), p.max()] if len(p) else [])(df["period"].dropna().astype(str)),
                "retrieved_at": str(df["retrieved_at"].iloc[0]),
                "source_url": str(df["source_url"].iloc[0]),
                "licence": str(df["licence"].iloc[0]),
            })
            df.to_parquet(out / f"{k}_{iso3}.parquet", index=False)
            if not a.no_csv:
                df.to_csv(out / f"{k}_{iso3}.csv", index=False)
            frames.append(df)
        manifest["sources"][k] = entry
        log.info("%-18s %-6s %6d rows %5.1fs", k, status.split(":")[0], len(df), dt_s)
    if frames:
        allf = pd.concat(frames, ignore_index=True)
        allf.to_parquet(out / f"federated_{iso3}.parquet", index=False)
        manifest["combined_rows"] = int(len(allf))
    (out / f"manifest_{iso3}.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    log.info("wrote %s", out / f"manifest_{iso3}.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
