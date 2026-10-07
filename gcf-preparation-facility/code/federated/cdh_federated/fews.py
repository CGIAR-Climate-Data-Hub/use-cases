"""FEWS NET Data Warehouse — acute food-insecurity (IPC-compatible) classifications.

Endpoint verified 2026-10-07 (no key): ``https://fdw.fews.net/api/ipcphase/?format=json&country_code=TG``
returns one row per geographic unit × classification scenario × projection window, with
``unit_type`` in {admin0, admin1, admin2, livelihood zone …}, ``fnid`` as the FEWS unit code,
``value`` = IPC phase (1–5) and ``description`` = phase label.

Licence: open — US Government work (USAID); attribute FEWS NET.
"""
from __future__ import annotations

import pandas as pd

from .common import get, session, tidy, to_float

BASE = "https://fdw.fews.net/api/ipcphase/"
LICENCE = "open (US Government / USAID; attribution)"
_ISO3_TO_ISO2 = {"TGO": "TG", "BEN": "BJ", "NGA": "NG", "KEN": "KE", "ZMB": "ZM", "EGY": "EG", "ETH": "ET",
                 "MWI": "MW", "SEN": "SN", "NER": "NE", "GHA": "GH", "MLI": "ML", "BFA": "BF", "TZA": "TZ",
                 "UGA": "UG", "MOZ": "MZ", "ZWE": "ZW", "SDN": "SD", "SSD": "SS", "SOM": "SO", "TCD": "TD",
                 "CMR": "CM", "RWA": "RW", "BDI": "BI", "MDG": "MG", "AGO": "AO", "COD": "CD", "LBR": "LR",
                 "SLE": "SL", "GIN": "GN", "MRT": "MR", "HTI": "HT", "AFG": "AF", "YEM": "YE"}
# FEWS unit types: admin0/1/2 are GAUL-like admin units; `fsc_admin_lhz` is the food-security
# classification unit (admin × livelihood zone) and `fsc_rm_admin` a remote-monitoring admin unit —
# both subnational, reported here as admin_level 1 with the unit_type kept in `qualifiers`.
_LEVEL = {"admin0": 0, "admin1": 1, "admin2": 2, "fsc_admin_lhz": 1, "fsc_rm_admin": 1}


def fetch(iso3: str, *, iso2: str | None = None,
          unit_types: tuple[str, ...] = ("admin0", "admin1", "admin2", "fsc_admin_lhz", "fsc_rm_admin"),
          s=None) -> pd.DataFrame:
    s = s or session()
    cc = iso2 or _ISO3_TO_ISO2.get(iso3)
    if not cc:
        raise ValueError(f"need the ISO2 code for {iso3} (pass iso2=)")
    params = {"format": "json", "country_code": cc}
    r = get(s, BASE, params=params, timeout=120)
    data = r.json()
    data = data if isinstance(data, list) else data.get("results", [])
    rows = []
    for x in data:
        ut = x.get("unit_type")
        if ut not in unit_types:
            continue
        rows.append({
            "iso3": iso3, "admin_level": _LEVEL[ut], "admin_name": x.get("geographic_unit_full_name"),
            "admin_code": x.get("fnid"),
            "indicator_id": "ipc_phase", "indicator": f"Acute food insecurity phase ({x.get('classification_scale')})",
            "value": to_float(x.get("value")), "value_text": x.get("description"), "unit": "IPC phase 1-5",
            "period": f"{x.get('projection_start')}/{x.get('projection_end')}",
            "scenario": x.get("scenario_name"),
            "qualifiers": {**{k: x.get(k) for k in ("source_document", "pct_phase3", "pct_phase4", "pct_phase5",
                                                     "is_allowing_for_assistance", "status", "id")},
                           "unit_type": ut, "admin0_fnid": x.get("fnid", "")[:2]},
        })
    return tidy(rows, source="fews_net", dataset="FEWS NET FDW ipcphase", licence=LICENCE, source_url=r.url)
