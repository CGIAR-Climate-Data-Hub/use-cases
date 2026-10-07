"""Small federated-source clients for the GCF Preparation Facility P1 datasets.

Each module exposes ``fetch(iso3, ...)`` (or ``fetch_<flow>``) returning a DataFrame in the
common tidy schema (`common.TIDY_COLUMNS`). See README.md for the source list and `__main__`
for the one-command runner.
"""
from . import climatewatch, data360, dhs, fews, gfw, inform, oecd, unicef_jmp  # noqa: F401
from .common import TIDY_COLUMNS  # noqa: F401

SOURCES = {
    "inform": lambda iso3, **kw: inform.fetch(iso3, **kw),
    "fews_net": lambda iso3, **kw: fews.fetch(iso3, **kw),
    "dhs": lambda iso3, **kw: dhs.fetch(iso3, **kw),
    "oecd_crs": lambda iso3, **kw: oecd.fetch_crs(iso3, **kw),
    "oecd_rio_markers": lambda iso3, **kw: oecd.fetch_rio_markers(iso3, **kw),
    "data360_imf_fm": lambda iso3, **kw: data360.fetch_imf_fm(iso3, **kw),
    "data360_wb_ids": lambda iso3, **kw: data360.fetch_wb_ids(iso3, **kw),
    "climate_watch": lambda iso3, **kw: climatewatch.fetch(iso3, **kw),
    "unicef_jmp": lambda iso3, **kw: unicef_jmp.fetch(iso3, **kw),
    "gfw": lambda iso3, **kw: gfw.fetch(iso3, **kw),
}
