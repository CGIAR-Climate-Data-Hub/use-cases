"""World Bank Data360 — IMF Fiscal Monitor (IMF_FM) and International Debt Statistics (WB_IDS).

Verified 2026-10-07 (no key): ``https://data360api.worldbank.org/data360/data?DATABASE_ID=…&REF_AREA=TGO``
returns ``{count, value: [{INDICATOR, REF_AREA, TIME_PERIOD, OBS_VALUE, UNIT_MEASURE, …}]}`` paged
by ``skip``. ``…/indicators?datasetId=IMF_FM`` lists indicator ids. Routing IMF through Data360
keeps us inside IMF's terms (their own bulk endpoint bans automated download).

Licence: CC BY 4.0 (World Bank Data360).
"""
from __future__ import annotations

import pandas as pd

from .common import get, session, tidy, to_float

BASE = "https://data360api.worldbank.org/data360"
LICENCE = "CC BY 4.0 (World Bank Data360)"

IMF_FM_LABELS = {
    "IMF_FM_G_XWDG_G01_GDP_PT": "General government gross debt (% of GDP)",
    "IMF_FM_G_X_G01_GDP_PT": "General government expenditure (% of GDP)",
    "IMF_FM_GGR_G01_GDP_PT": "General government revenue (% of GDP)",
    "IMF_FM_GGXCNL_G01_GDP_PT": "General government net lending/borrowing (% of GDP)",
    "IMF_FM_GGXONLB_G01_GDP_PT": "General government primary net lending/borrowing (% of GDP)",
}
# A compact debt-sustainability set from WB_IDS; others are available via /indicators?datasetId=WB_IDS
WB_IDS_DEFAULT = ["WB_IDS_DT_DOD_DECT_CD", "WB_IDS_DT_TDS_DECT_EX", "WB_IDS_DT_DOD_DECT_GN_ZS", "WB_IDS_DT_DOD_DECT_PC"]


def _pull(s, database: str, iso3: str, indicator: str | None = None) -> tuple[list[dict], str]:
    rows, skip, url0 = [], 0, None
    while True:
        params = {"DATABASE_ID": database, "REF_AREA": iso3, "skip": skip}
        if indicator:
            params["INDICATOR"] = indicator
        r = get(s, f"{BASE}/data", params=params, timeout=120)
        url0 = url0 or r.url
        d = r.json()
        vals = d.get("value", [])
        rows.extend(vals)
        skip += len(vals)
        if not vals or skip >= int(d.get("count", 0)):
            break
    return rows, url0


def fetch_imf_fm(iso3: str, *, s=None) -> pd.DataFrame:
    s = s or session()
    vals, url = _pull(s, "IMF_FM", iso3)
    rows = [{
        "iso3": iso3, "admin_level": 0, "admin_name": iso3, "admin_code": iso3,
        "indicator_id": x["INDICATOR"], "indicator": IMF_FM_LABELS.get(x["INDICATOR"], x["INDICATOR"]),
        "value": to_float(x.get("OBS_VALUE")), "unit": x.get("UNIT_MEASURE"), "period": x.get("TIME_PERIOD"),
        "qualifiers": {"obs_status": x.get("OBS_STATUS"), "freq": x.get("FREQ")},
    } for x in vals]
    return tidy(rows, source="data360_imf_fm", dataset="IMF Fiscal Monitor via World Bank Data360",
                licence=LICENCE, source_url=url)


def fetch_wb_ids(iso3: str, *, indicators: list[str] | None = None, s=None) -> pd.DataFrame:
    s = s or session()
    inds = indicators or WB_IDS_DEFAULT
    rows, url0 = [], None
    for ind in inds:
        vals, url = _pull(s, "WB_IDS", iso3, ind)
        url0 = url0 or url
        for x in vals:
            rows.append({
                "iso3": iso3, "admin_level": 0, "admin_name": iso3, "admin_code": iso3,
                "indicator_id": x["INDICATOR"], "indicator": x["INDICATOR"],
                "value": to_float(x.get("OBS_VALUE")), "unit": x.get("UNIT_MEASURE"), "period": x.get("TIME_PERIOD"),
                "qualifiers": {k: x.get(k) for k in ("COMP_BREAKDOWN_1", "COMP_BREAKDOWN_2", "COMP_BREAKDOWN_3",
                                                      "UNIT_MULT", "OBS_STATUS")},
                "source_url": url,
            })
    return tidy(rows, source="data360_wb_ids", dataset="World Bank International Debt Statistics via Data360",
                licence=LICENCE, source_url=url0 or BASE)
