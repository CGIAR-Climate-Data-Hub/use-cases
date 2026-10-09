"""WHO/UNICEF JMP — WASH household coverage via the UNICEF SDMX API.

Verified 2026-10-07 (no key):
``https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/UNICEF,WASH_HOUSEHOLDS,1.0/<ISO3>...?format=csv``
Key = REF_AREA.INDICATOR.SERVICE_TYPE.WEALTH_QUINTILE.RESIDENCE (wildcards allowed). Columns:
``REF_AREA, INDICATOR, SERVICE_TYPE, WEALTH_QUINTILE, RESIDENCE, UNIT_MEASURE, TIME_PERIOD, OBS_VALUE``.
RESIDENCE: _T total, U urban, R rural. National only (admin0).

Licence: JMP reports are CC BY-NC-SA 3.0 IGO; the data licence is not stated on washdata.org —
treat as non-commercial, attribute WHO/UNICEF JMP.
"""
from __future__ import annotations

import csv
import io

import pandas as pd

from .common import get, session, tidy, to_float

BASE = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/UNICEF,WASH_HOUSEHOLDS,1.0"
LICENCE = "CC BY-NC-SA 3.0 IGO (reports); data licence unstated — attribute WHO/UNICEF JMP"

LABELS = {  # the headline ladder indicators; everything else keeps its code
    "WS_PPL_W-ALB": "Population using at least basic drinking water services",
    "WS_PPL_W-SM": "Population using safely managed drinking water services",
    "WS_PPL_S-ALB": "Population using at least basic sanitation services",
    "WS_PPL_S-SM": "Population using safely managed sanitation services",
    "WS_PPL_S-OD": "Population practising open defecation",
    "WS_PPL_H-B": "Population with basic hygiene (handwashing) facilities",
}


def fetch(iso3: str, *, last_n: int | None = None, start: int | None = 2010, s=None) -> pd.DataFrame:
    s = s or session()
    params = {"format": "csv"}
    if last_n:
        params["lastNObservations"] = last_n
    elif start:
        params["startPeriod"] = start
    r = get(s, f"{BASE}/{iso3}....", params=params, timeout=120)
    rows = []
    for x in csv.DictReader(io.StringIO(r.text)):
        rows.append({
            "iso3": iso3, "admin_level": 0, "admin_name": iso3, "admin_code": iso3,
            "indicator_id": x["INDICATOR"], "indicator": LABELS.get(x["INDICATOR"], x["INDICATOR"]),
            "value": to_float(x.get("OBS_VALUE")), "unit": x.get("UNIT_MEASURE"), "period": x.get("TIME_PERIOD"),
            "qualifiers": {"service_type": x.get("SERVICE_TYPE"), "residence": x.get("RESIDENCE"),
                           "wealth_quintile": x.get("WEALTH_QUINTILE"), "data_source": x.get("DATA_SOURCE")},
        })
    return tidy(rows, source="unicef_jmp", dataset="WHO/UNICEF JMP WASH_HOUSEHOLDS (UNICEF SDMX)",
                licence=LICENCE, source_url=r.url)
