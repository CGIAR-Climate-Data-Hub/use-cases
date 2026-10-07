# `cdh_rationale` — climate-rationale fragments prototype

The first end-to-end pass of the generic, fund-neutral **climate-rationale** capability the review
page's Skills tab specifies: Hub-catalogued (or queued) data in, **labelled, citable fragments** out,
one list per proposal section, gaps stated explicitly, no narrative authored.

```bash
# inputs: cdh_federated outputs + worldcover_admin outputs for the same country
python -m cdh_rationale TGO --federated ../federated/out --worldcover ../worldcover/out --out out --subnational
```

Outputs: `rationale_<ISO3>.json` (every fragment with `values` and `source_citation`),
`rationale_<ISO3>.md` (grouped by section with numbered sources), `rationale_<ISO3>_coverage.csv`
(section × fragment type counts and gaps — what the rationale can and cannot say yet).

## How it works

1. Reads [`data/rationale-map.yaml`](../../data/rationale-map.yaml) for the section structure
   (theme, question, GCF CN/FP codes, datasets and their status).
2. Loads whatever inputs exist: `cdh_federated` parquets (INFORM, FEWS NET, DHS, OECD CRS + Rio
   markers, Data360 IMF/IDS, Climate Watch, UNICEF JMP, GFW), the WorldCover admin products, and
   the Atlas `haz_freq.parquet` straight from S3 (DuckDB, `hive_partitioning=false`).
3. One builder per section (`fragments.py`) turns rows into fragments: `{section, theme, serves,
   fragment_type, admin_level, admin_name, text, values, source_citation, caveats}`. The citation
   is the row's own request URL — a deterministic query is the citation.
4. Guardrails: a number is emitted only if a row carries it; a section with no input emits a
   `gap` fragment naming what is missing and where it is queued; known data problems become
   caveats, never silent omissions (e.g. INFORM's unlabelled score sets; the saturated historic
   NDWS baseline in `haz_freq`, see below).

## Togo, 2026-10-07

9 federated sources + WorldCover + `haz_freq` → 60-ish fragments with `--subnational`, 6 gaps
(observed climate baseline not wired; exposure matrix not wired; tCO₂e engine; comparable
projects list; GFW key; protected-area overlays). Sections 4, 5, 7 and 9 are fully data-backed.

**Data defect found while building this.** In `haz_freq.parquet` the historic (1995–2014)
frequency of NDWS exceedance is **1.0 for every GCM and every African adm0** (both severities;
`frequency_n = 19 = n_years`), while NDWL0 historic values are normal and NDWS projections are
plausible (median 0.17–0.87). The historic NDWS baseline is saturated and cannot be compared with
the projections. The Section 2 builder detects this and emits the projection with an explicit
`DATA DEFECT` caveat instead of a historical-vs-projected comparison. Raised as ask #6 in the
Theme 2 request ([`methods/ingestion-notes.md` §2](../../methods/ingestion-notes.md)).

## What this is not (yet)

- Not a Claude Code skill — it is the deterministic data layer a skill would call; the skill
  spec (`outputs/skills-issue-climate-rationale.md`) adds the LLM composition step on top, with
  the same guardrails.
- Not a template for any one funder — GCF codes come from the map; an IFI/MDB template would
  only re-map `serves`.
- Evals to add: reproduce Togo SAT Table 5 / Figure 5 values once the exposure tiers are wired;
  assert every `source_citation.url` resolves.
