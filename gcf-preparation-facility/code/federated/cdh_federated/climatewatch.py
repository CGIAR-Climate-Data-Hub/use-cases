"""Climate Watch (WRI) — structured NDC content for a country.

Verified 2026-10-07 (no key):
``/api/v1/ndcs/<ISO3>/content_overview`` → sectors covered + headline values per document;
``/api/v1/ndcs/<ISO3>/text`` → the list of NDC documents (type, language, html).
The list endpoint ``/api/v1/ndcs?filter=sectoral`` ignores ``location`` — filter client-side.

Licence: CC BY 4.0 for Climate-Watch-produced data.
"""
from __future__ import annotations

import pandas as pd

from .common import get, session, tidy

BASE = "https://www.climatewatchdata.org/api/v1"
LICENCE = "CC BY 4.0 (Climate Watch data)"


def fetch(iso3: str, *, s=None) -> pd.DataFrame:
    s = s or session()
    r = get(s, f"{BASE}/ndcs/{iso3}/content_overview", timeout=120)
    d = r.json()
    rows = []
    for v in d.get("values", []):
        rows.append({
            "iso3": iso3, "admin_level": 0, "admin_name": iso3, "admin_code": iso3,
            "indicator_id": f"ndc_{v.get('slug')}", "indicator": v.get("name"),
            "value_text": v.get("value"), "period": v.get("document_slug"),
            "qualifiers": {"document": v.get("document_slug")},
        })
    for sec in d.get("sectors", []):
        rows.append({
            "iso3": iso3, "admin_level": 0, "admin_name": iso3, "admin_code": iso3,
            "indicator_id": "ndc_sector_covered", "indicator": "NDC sector covered",
            "value_text": sec, "value": 1.0, "unit": "flag",
        })
    r2 = get(s, f"{BASE}/ndcs/{iso3}/text", timeout=120)
    for doc in r2.json():
        rows.append({
            "iso3": iso3, "admin_level": 0, "admin_name": iso3, "admin_code": iso3,
            "indicator_id": "ndc_document", "indicator": "NDC document available",
            "value_text": f"{doc.get('document_type')} ({doc.get('language')}{', translated' if doc.get('translated') else ''})",
            "period": doc.get("document_type"),
            "qualifiers": {"language": doc.get("language"), "translated": doc.get("translated"),
                           "html_chars": len(doc.get("html") or ""), "self": doc.get("links", {}).get("self")},
            "source_url": r2.url,
        })
    return tidy(rows, source="climate_watch", dataset="Climate Watch NDC content", licence=LICENCE, source_url=r.url)
