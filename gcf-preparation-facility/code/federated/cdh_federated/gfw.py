"""Global Forest Watch Data API — tree-cover-loss summaries by GADM admin unit.

Verified 2026-10-07: dataset listing is open, but every ``/query`` call needs an API key
(``x-api-key`` header; ``403 "Request is missing valid API key"`` otherwise). Keys are free:
POST ``/auth/sign-up`` → POST ``/auth/token`` → POST ``/auth/apikey`` (see
https://data-api.globalforestwatch.org/#tag/Authentication). Set ``GFW_API_KEY`` in the
environment; without it this client returns an empty frame and logs a warning.

Tabular datasets used (pre-aggregated, no raster work):
``gadm__tcl__iso_summary`` / ``gadm__tcl__adm1_summary`` (latest version), queried with SQL.

Licence: CC BY 4.0 (UMD/GLAD tree cover loss, as stated in the dataset metadata).
"""
from __future__ import annotations

import logging
import os

import pandas as pd

from .common import empty, get, session, tidy, to_float

log = logging.getLogger("cdh_federated")
BASE = "https://data-api.globalforestwatch.org"
LICENCE = "CC BY 4.0 (UMD tree cover loss via GFW Data API)"


def fetch(iso3: str, *, api_key: str | None = None, levels: tuple[int, ...] = (0, 1), s=None) -> pd.DataFrame:
    key = api_key or os.environ.get("GFW_API_KEY")
    if not key:
        log.warning("GFW: no GFW_API_KEY set — skipping (create one at %s/#tag/Authentication)", BASE)
        return empty()
    s = s or session()
    s.headers["x-api-key"] = key
    rows, url0 = [], None
    for level in levels:
        ds = "gadm__tcl__iso_summary" if level == 0 else f"gadm__tcl__adm{level}_summary"
        sql = f"SELECT * FROM results WHERE iso = '{iso3}'"
        r = get(s, f"{BASE}/dataset/{ds}/latest/query/json", params={"sql": sql}, timeout=180)
        url0 = url0 or r.url
        for x in r.json().get("data", []):
            name = iso3 if level == 0 else str(x.get(f"adm{level}", ""))
            for col, val in x.items():
                if not isinstance(val, (int, float)) or col in ("adm1", "adm2"):
                    continue
                rows.append({
                    "iso3": iso3, "admin_level": level, "admin_name": name, "admin_code": name,
                    "indicator_id": col, "indicator": col.replace("__", " ").replace("_", " "),
                    "value": to_float(val), "unit": "ha" if "__ha" in col or col.endswith("_ha") else "",
                    "period": str(x.get("umd_tree_cover_loss__year", "")),
                    "qualifiers": {k: v for k, v in x.items() if not isinstance(v, (int, float))},
                    "source_url": r.url,
                })
    return tidy(rows, source="gfw", dataset="GFW tree cover loss admin summaries", licence=LICENCE,
                source_url=url0 or BASE)
