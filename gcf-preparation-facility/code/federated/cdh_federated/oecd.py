"""OECD DAC — CRS (Creditor Reporting System) and Rio markers via SDMX-REST.

Verified 2026-10-07. The CRS / Rio-marker dataflows are *external references* on
``sdmx.oecd.org/public`` — data and structures must be requested from
``https://sdmx.oecd.org/dcd-public/rest/``. SDMX 3.0 ``c[RECIPIENT]=`` filters are ignored
(the server returns the whole cube, >1 GB), so keys are positional:

CRS  ``OECD.DCD.FSD,DSD_CRS@DF_CRS,1.6``
     DONOR.RECIPIENT.SECTOR.MEASURE.CHANNEL.MODALITY.FLOW_TYPE.PRICE_BASE.MD_DIM.MD_ID.UNIT_MEASURE
Rio  ``OECD.DCD.FSD,DSD_RIOMRKR@DF_RIOMARKERS,1.6``
     DONOR.RECIPIENT.SECTOR.MEASURE.ALLOCABLE.MARKER.SCORE.FLOW_TYPE.PRICE_BASE.MD_DIM.MD_ID.UNIT_MEASURE

Codes used: MEASURE 100 = ODA; FLOW_TYPE D disbursements (CRS) / C commitments (Rio only offers C);
PRICE_BASE V current USD; MD_DIM _T aggregate; MD_ID 0; UNIT_MEASURE USD; SECTOR 1000 = all;
Rio MARKER 30 = climate adaptation, 20 = mitigation; SCORE 1 significant, 2 principal;
ALLOCABLE 2 = bilateral allocable. The all-DAC donor aggregate is ``DAC`` in CRS and
``DAC_EC`` in Rio markers. OBS_VALUE is in USD millions (UNIT_MULT 6).

Licence: CC BY 4.0 for OECD content published from 1 July 2024.
"""
from __future__ import annotations

import csv
import io

import pandas as pd

from .common import get, session, tidy, to_float

BASE = "https://sdmx.oecd.org/dcd-public/rest/data"
CRS = "OECD.DCD.FSD,DSD_CRS@DF_CRS,1.6"
RIO = "OECD.DCD.FSD,DSD_RIOMRKR@DF_RIOMARKERS,1.6"
LICENCE = "CC BY 4.0 (OECD Open Access, from 1 Jul 2024)"


def _csv(r) -> list[dict]:
    return list(csv.DictReader(io.StringIO(r.text)))


def fetch_crs(iso3: str, *, start: int = 2015, end: int | None = None, donor: str = "DAC",
              by_sector: bool = True, s=None) -> pd.DataFrame:
    """ODA disbursements to `iso3` from all DAC donors, total and (optionally) by CRS sector."""
    s = s or session()
    sector = "" if by_sector else "1000"
    key = f"{donor}.{iso3}.{sector}.100._T._T.D.V._T.0.USD"
    params = {"startPeriod": start, "format": "csvfilewithlabels"}
    if end:
        params["endPeriod"] = end
    r = get(s, f"{BASE}/{CRS}/{key}", params=params, timeout=180)
    rows = []
    for x in _csv(r):
        rows.append({
            "iso3": iso3, "admin_level": 0, "admin_name": x.get("Recipient"), "admin_code": iso3,
            "indicator_id": f"crs_oda_disb_{x['SECTOR']}",
            "indicator": f"ODA disbursements — {x.get('Sector')}",
            "value": to_float(x.get("OBS_VALUE")), "unit": "USD million, current prices",
            "period": x.get("TIME_PERIOD"),
            "qualifiers": {"donor": x.get("DONOR"), "donor_name": x.get("Donor"), "sector_code": x.get("SECTOR"),
                           "measure": x.get("MEASURE"), "flow_type": x.get("FLOW_TYPE"),
                           "price_base": x.get("PRICE_BASE"), "unit_mult": x.get("UNIT_MULT")},
        })
    return tidy(rows, source="oecd_crs", dataset="OECD DAC CRS (DF_CRS 1.6)", licence=LICENCE, source_url=r.url)


def fetch_rio_markers(iso3: str, *, start: int = 2015, end: int | None = None, donor: str = "DAC_EC",
                      markers: tuple[str, ...] = ("30", "20"), s=None) -> pd.DataFrame:
    """Climate-marked ODA commitments to `iso3` (adaptation 30, mitigation 20) by score, all sectors."""
    s = s or session()
    key = f"{donor}.{iso3}.1000.100.2.{'+'.join(markers)}..C.V._T.0.USD"
    params = {"startPeriod": start, "format": "csvfilewithlabels"}
    if end:
        params["endPeriod"] = end
    r = get(s, f"{BASE}/{RIO}/{key}", params=params, timeout=180)
    rows = []
    for x in _csv(r):
        rows.append({
            "iso3": iso3, "admin_level": 0, "admin_name": x.get("Recipient"), "admin_code": iso3,
            "indicator_id": f"rio_{x['MARKER']}_score{x['SCORE']}",
            "indicator": f"ODA commitments — {x.get('Marker')}, {x.get('Score')}",
            "value": to_float(x.get("OBS_VALUE")), "unit": "USD million, current prices",
            "period": x.get("TIME_PERIOD"),
            "qualifiers": {"donor": x.get("DONOR"), "donor_name": x.get("Donor"), "marker": x.get("MARKER"),
                           "score": x.get("SCORE"), "allocable": x.get("ALLOCABLE"),
                           "flow_type": x.get("FLOW_TYPE"), "unit_mult": x.get("UNIT_MULT")},
        })
    return tidy(rows, source="oecd_rio_markers", dataset="OECD DAC Rio markers (DF_RIOMARKERS 1.6)",
                licence=LICENCE, source_url=r.url)
