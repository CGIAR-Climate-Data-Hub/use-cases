"""INFORM Risk (JRC) — national composite risk scores via the public JSON API.

Endpoint verified 2026-10-07: ``Countries/Scores/?WorkflowId=<id>&Iso3=<ISO3>&IndicatorId=<ids>``
returns rows ``{Iso3, IndicatorId, IndicatorScore, …}``. The server duplicates each score many
times (one copy per related unit), so rows are de-duplicated here. The parameter spelling
``CountryIso3Codes=`` is ignored by the server and returns every country — don't use it.

``workflow_id`` identifies the INFORM release. 528 is the workflow the GCF review used; the
``Workflows`` listing endpoint is not public (404), so confirm the current-year id on
https://drmkc.jrc.ec.europa.eu/inform-index before relying on a release label.

**Open semantics (2026-10-07).** For one workflow and one indicator the server returns ~72
distinct scores for a country (e.g. CC for TGO ranges 6.0–8.1), all with ``ValidityYear = 0`` and
``nodelevel = 0``; a different ``WorkflowId`` changes the set, an unknown one returns nothing. The
rows are therefore real per-workflow data whose extra dimension (year? sub-workflow? node?) the
API does not label. This client keeps every distinct row and sets ``qualifiers.semantics =
"unresolved"``; do **not** average them. Until the INFORM team confirms the shape, the annual
INFORM Risk results file (HDX / INFORM site) is the citable headline number.

Licence: CC BY 4.0 under the EC reuse policy (Decision 2011/833/EU); not printed on the INFORM site.
"""
from __future__ import annotations

import pandas as pd

from .common import get, session, tidy, to_float

BASE = "https://drmkc.jrc.ec.europa.eu/Inform-Index/API/InformAPI"
LICENCE = "CC BY 4.0 (EC reuse policy, Decision 2011/833/EU)"

# Composite + the three dimensions + a handful of the most-cited components.
DEFAULT_INDICATORS = ["INFORM", "HA", "VU", "CC", "HA.NAT", "HA.HUM", "VU.SEV", "VU.VGR", "CC.INS", "CC.INF"]
LABELS = {
    "INFORM": "INFORM Risk index", "HA": "Hazard & exposure", "VU": "Vulnerability",
    "CC": "Lack of coping capacity", "HA.NAT": "Natural hazard", "HA.HUM": "Human hazard",
    "VU.SEV": "Socio-economic vulnerability", "VU.VGR": "Vulnerable groups",
    "CC.INS": "Institutional coping capacity", "CC.INF": "Infrastructure coping capacity",
}


def fetch(iso3: str, *, workflow_id: int = 528, indicators: list[str] | None = None,
          s=None) -> pd.DataFrame:
    s = s or session()
    inds = indicators or DEFAULT_INDICATORS
    url = f"{BASE}/Countries/Scores/"
    params = {"WorkflowId": workflow_id, "Iso3": iso3, "IndicatorId": ",".join(inds)}
    r = get(s, url, params=params, timeout=120)
    data = r.json()
    seen = set()
    rows = []
    for x in data:
        key = (x.get("Iso3"), x.get("IndicatorId"), x.get("IndicatorScore"))
        if key in seen or x.get("Iso3") != iso3:
            continue
        seen.add(key)
        rows.append({
            "iso3": iso3, "admin_level": 0, "admin_name": iso3, "admin_code": iso3,
            "indicator_id": x["IndicatorId"],
            "indicator": LABELS.get(x["IndicatorId"], x.get("IndicatorName") or x["IndicatorId"]),
            "value": to_float(x.get("IndicatorScore")), "unit": "score 0-10",
            "period": str(x.get("ValidityYear") or f"workflow {workflow_id}"),
            "qualifiers": {"workflow_id": workflow_id, "nodelevel": x.get("nodelevel"),
                           "semantics": "unresolved — multiple distinct scores per indicator per workflow; see module docstring"},
        })
    return tidy(rows, source="inform", dataset=f"INFORM Risk (workflow {workflow_id})",
                licence=LICENCE, source_url=r.url)
