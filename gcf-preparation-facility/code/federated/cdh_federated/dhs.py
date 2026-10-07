"""DHS Program Indicator API — subnational aggregate indicators (never microdata).

Endpoint verified 2026-10-07 (no key): ``https://api.dhsprogram.com/rest/dhs/data`` with
``countryIds=<DHS 2-letter code>&indicatorIds=…&breakdown=subnational&f=json``. Rows carry
``CharacteristicLabel`` (region name), ``RegionId``, ``SurveyYear``, ``Value``, CI bounds.
DHS also publishes an MCP server (see api.dhsprogram.com) — the same data for agents.

Licence: aggregate indicators via the API are open (attribution); microdata/GPS are restricted
and not touched here.
"""
from __future__ import annotations

import pandas as pd

from .common import get, session, tidy, to_float

BASE = "https://api.dhsprogram.com/rest/dhs/data"
LICENCE = "open aggregate Indicator API (attribution: The DHS Program)"
_ISO3_TO_DHS = {"TGO": "TG", "BEN": "BJ", "NGA": "NG", "KEN": "KE", "ZMB": "ZM", "EGY": "EG", "ETH": "ET",
                "MWI": "MW", "SEN": "SN", "NER": "NI", "GHA": "GH", "MLI": "ML", "BFA": "BF", "TZA": "TZ",
                "UGA": "UG", "MOZ": "MZ", "ZWE": "ZW", "RWA": "RW", "BDI": "BU", "MDG": "MD", "CMR": "CM",
                "COD": "CD", "LBR": "LB", "SLE": "SL", "GIN": "GN", "TCD": "TD", "HTI": "HT"}

# Vulnerability indicators the GCF Theme 4 narrative leans on (all verified present for TG).
DEFAULT_INDICATORS = [
    "CN_NUTS_C_HA2",   # children stunted (%)
    "HC_WIXQ_P_LOW",   # population in lowest wealth quintile (%)
    "HC_ELEC_H_ELC",   # households with electricity (%)
    "WS_SRCE_P_IMP",   # population using an improved water source (%)
    "ED_LITR_W_LIT",   # women who are literate (%)
    "CM_ECMR_C_U5M",   # under-five mortality rate (per 1,000)
    "HC_HEFF_H_MPH",   # households possessing a mobile telephone (%)
    "FP_CUSA_W_MOD",   # modern contraceptive use, all women (%)
]


def fetch(iso3: str, *, dhs_code: str | None = None, indicators: list[str] | None = None,
          survey_year_start: int = 2005, latest_only: bool = True, s=None) -> pd.DataFrame:
    s = s or session()
    cc = dhs_code or _ISO3_TO_DHS.get(iso3)
    if not cc:
        raise ValueError(f"need the DHS country code for {iso3} (pass dhs_code=)")
    inds = indicators or DEFAULT_INDICATORS
    rows, urls = [], []
    for level, breakdown in ((0, "national"), (1, "subnational")):
        params = {"countryIds": cc, "indicatorIds": ",".join(inds), "breakdown": breakdown,
                  "surveyYearStart": survey_year_start, "f": "json", "perpage": 5000}
        r = get(s, BASE, params=params, timeout=120)
        urls.append(r.url)
        data = r.json().get("Data", [])
        if latest_only:
            latest = {}
            for x in data:
                k = (x["IndicatorId"], x.get("RegionId") or "national")
                if k not in latest or x["SurveyYear"] > latest[k]["SurveyYear"]:
                    latest[k] = x
            data = list(latest.values())
        for x in data:
            if level == 1 and x.get("IsTotal") in (1, "1", True):
                continue
            rows.append({
                "iso3": iso3, "admin_level": level,
                "admin_name": x.get("CountryName") if level == 0 else x.get("CharacteristicLabel"),
                "admin_code": iso3 if level == 0 else x.get("RegionId"),
                "indicator_id": x["IndicatorId"], "indicator": x.get("Indicator"),
                "value": to_float(x.get("Value")), "unit": "percent" if x.get("Precision") in (1, "1") else "",
                "period": str(x.get("SurveyYear")),
                "qualifiers": {"survey_id": x.get("SurveyId"), "survey_type": x.get("SurveyType"),
                               "ci_low": x.get("CILow"), "ci_high": x.get("CIHigh"),
                               "denominator_weighted": x.get("DenominatorWeighted"), "sdrid": x.get("SDRID")},
                "source_url": r.url,
            })
    return tidy(rows, source="dhs", dataset="DHS Program Indicator API", licence=LICENCE, source_url=urls[0])
