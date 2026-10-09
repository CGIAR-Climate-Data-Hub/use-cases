"""Shared plumbing for the federated-source clients.

Every client returns a pandas DataFrame in one tidy schema (``TIDY_COLUMNS``) so the per-source
tables can be concatenated and fed to a notebook or the planned ``climate-rationale`` skill.
"""
from __future__ import annotations

import datetime as dt
import json
import logging
import time
from typing import Any, Iterable

import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

log = logging.getLogger("cdh_federated")

USER_AGENT = "CGIAR-Climate-Data-Hub federated-client/0.1 (+https://cgiar-climate-data-hub.github.io/)"
DEFAULT_TIMEOUT = 90

# One row = one observation for one admin unit.
TIDY_COLUMNS = [
    "iso3",          # ISO 3166-1 alpha-3 of the country
    "admin_level",   # 0 = national, 1 = first subnational, 2 = second
    "admin_name",    # unit name as the provider gives it (country name at level 0)
    "admin_code",    # provider's own unit code (ISO3 at level 0; INFORM/DHS/FEWS codes below)
    "source",        # short provider key, e.g. "inform", "fews_net"
    "dataset",       # provider dataset / dataflow name
    "indicator_id",  # provider indicator code
    "indicator",     # human label
    "value",         # numeric value (float) — text values go to `value_text`
    "value_text",    # categorical / text observation (e.g. IPC phase label)
    "unit",
    "period",        # year, date or period label as the provider reports it
    "scenario",      # projection / scenario label where relevant, else None
    "qualifiers",    # JSON string of extra dimensions (donor, sector, marker …)
    "retrieved_at",  # UTC ISO timestamp of the pull
    "source_url",    # the exact request URL (deterministic query = citation)
    "licence",       # licence as logged in the evidence log
]


def session(total_retries: int = 4, backoff: float = 1.5) -> requests.Session:
    """A requests session with retries on connection resets and 5xx (several of these APIs reset)."""
    s = requests.Session()
    retry = Retry(
        total=total_retries,
        connect=total_retries,
        read=total_retries,
        backoff_factor=backoff,
        status_forcelist=(500, 502, 503, 504, 429),
        allowed_methods=("GET",),
        raise_on_status=False,
    )
    s.mount("https://", HTTPAdapter(max_retries=retry))
    s.headers.update({"User-Agent": USER_AGENT, "Accept": "application/json, text/csv;q=0.9, */*;q=0.8"})
    return s


def get(s: requests.Session, url: str, *, params: dict | None = None, timeout: int = DEFAULT_TIMEOUT,
        attempts: int = 3, **kw) -> requests.Response:
    """GET with an extra manual retry loop for providers that drop connections mid-response."""
    last: Exception | None = None
    for i in range(attempts):
        try:
            r = s.get(url, params=params, timeout=timeout, **kw)
            r.raise_for_status()
            return r
        except (requests.ConnectionError, requests.Timeout, requests.HTTPError) as e:  # noqa: PERF203
            last = e
            log.warning("GET %s failed (%s), attempt %d/%d", url, e.__class__.__name__, i + 1, attempts)
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"GET failed after {attempts} attempts: {url}") from last


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def to_float(x: Any) -> float | None:
    try:
        if x is None or x == "":
            return None
        return float(x)
    except (TypeError, ValueError):
        return None


def tidy(rows: Iterable[dict], *, source: str, dataset: str, licence: str, source_url: str) -> pd.DataFrame:
    """Fill the constant columns and order everything to ``TIDY_COLUMNS``."""
    ts = now_iso()
    out = []
    for r in rows:
        rec = {c: None for c in TIDY_COLUMNS}
        rec.update(r)
        rec.update({"source": source, "dataset": dataset, "licence": licence, "retrieved_at": ts})
        rec.setdefault("source_url", source_url)
        if rec.get("source_url") is None:
            rec["source_url"] = source_url
        q = rec.get("qualifiers")
        if isinstance(q, dict):
            rec["qualifiers"] = json.dumps(q, ensure_ascii=False, sort_keys=True)
        out.append(rec)
    df = pd.DataFrame(out, columns=TIDY_COLUMNS)
    if not df.empty:
        df["value"] = pd.to_numeric(df["value"], errors="coerce")
        df["admin_level"] = df["admin_level"].astype("Int64")
    return df


def empty() -> pd.DataFrame:
    return pd.DataFrame(columns=TIDY_COLUMNS)
