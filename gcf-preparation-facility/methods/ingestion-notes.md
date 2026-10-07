<!-- markdownlint-disable MD034 -->
# Ingestion notes — GCF Preparation Facility datasets (decisions of 2026-10-07)

Working notes for moving the review page's recommended datasets into the Climate Data Hub
without waiting on the champion. Companion to the queue in
[`../data/ingestion-queue.csv`](../data/ingestion-queue.csv) (mirrored as the `GCF use-case`
sheet of the CDH ingestion tracker, `asset_mapping/CDH_data-ingestion v2.xlsx` in OneDrive) and to
the per-dataset [evidence log](./evidence/sources.md). Theme numbers follow the review page
(Themes 1–9, Tables 2–10).

**Decision record.** On 2026-10-07 the coordinator (Peter Steward) decided to proceed on the
review's P1 recommendations without further champion input: the champion has not commented on the
review page (shared 2026-07-14, chased 2026-09-23 — "i can look into it tomorrow/friday", nothing
since) and the multilateral-climate-funds dataset, its sub-classifiers and the extraction method
remain undelivered. Per-theme calls below. Metadata records are authored only after the
`cdh-metadata-standard` v0.4.0 release lands (open PR #35, 63 commits, 100 files) — re-pull the
templates, authoring guide and the `cdh-metadata` skill first.

---

## Rescreen method (applied to every row in the queue)

Each queued dataset was re-tested on 2026-10-07 against five questions, with the live endpoint
hit from this machine (`curl`, browser UA, 25 s timeout):

1. **Best-in-class?** Is there a stronger, equally open alternative — including anything logged in
   the `climate-assets` "What's New" catalogue since July?
2. **Route live?** Does the API / cloud endpoint answer, and with what (JSON / SDMX / COG / bulk)?
3. **Licence still as logged** on 2026-07-07?
4. **Cloud-optimised?** COG / Zarr / Parquet / SDMX / JSON vs bulk-only.
5. **Route + complexity** (1 = federate an open JSON API … 5 = per-country acquisition).

Results are in the queue (`Rescreen status`, `Rescreen verdict / alternative`) and in the
evidence log's *Rescreen 2026-10-07* table. Swaps that came out of it:

| Was | Now | Why |
| --- | --- | --- |
| AQUASTAT GMIA v5 (5 arc-min, 2005) | **GMIA-NEXT** (30 m, 2023/24 season, CC BY 4.0, Zenodo 17627111) — keep v5 only as the legacy "% equipped" layer | 20 years newer, 1000× finer, open licence; 5.2 GB binary + continental probability GeoTIFFs → derive admin irrigated-area shares, don't mirror the 30 m |
| GLEAM data treated as restricted | **GLEAM 3 dashboard** (https://foodandagricultureorganization.shinyapps.io/GLEAMV3_Public/) Terms of Use: data licensed **CC BY 4.0** + FAO Statistical Database Terms of Use — verified in a browser by Pete, 2026-10-07 | GLEAM moves from "licence-blocked" to "federate the dashboard data (animal population, products, emissions, emission intensities), cite"; model code `un-fao/GLEAM` is AGPL-3 |
| INFORM vs ND-GAIN both P1/P2 | **INFORM Risk P1, ND-GAIN P2** stays | INFORM has a live JSON API and an EC open-reuse basis; ND-GAIN download page carries no licence text at all |
| LandMark "FPIC conditions" | **CC BY-SA 4.0** (June 2026 update) + LandMark ToS, form-gated download | Clearer than logged: ShareAlike, not FPIC-blocked — derived flags are publishable under BY-SA |
| KBA "request-gated, NC" | Confirmed: non-commercial via request form (5–10 working days); commercial via IBAT | Unchanged; budget the lead time |
| IATI "open API" | API Gateway **subscription key required** (free Trial → Full Access) | Still federate; register a Hub key |
| Protected Planet "API" | **Token required** via request form | Same |
| FAO EX-ACT "online tool" | Hosted app does **not** expose `/api/*` (SPA catch-all); the API exists only in the AGPL codebase | Integration must self-host or vendor the math layer — see §6 |

---

## §2 — Extreme events: technical note and request for the Atlas hazards session

**Where this sits.** Theme 2 is `IN CR` — the Climate Rationale notebook already classifies
unusual / extreme temperature and precipitation events by z-score against 1995–2014, computed
client-side from the Section 1 projections parquet, **ensemble-mean only**. The memo asks for
"historical vs. projected frequency by scenario"; the Atlas data audit (2026-07-09) flagged that
without per-GCM classification the tail models are masked, so no uncertainty band can be shown.

The hazards pipeline (Atlas `hazards_prototype`, the `hazards-prototype-*` Claude sessions) is the
only place these products can be built. Before specifying anything, ask it what already exists.

### Part A — questions for the hazards session (paste as-is)

> **Context.** GCF Preparation Facility use-case, Theme 2 "Extreme events" (review page
> https://cgiar-climate-data-hub.github.io/use-cases/gcf-preparation-facility/gcf-prep-review.html#d-s2).
> The CR notebook today does an ensemble-mean z-score classification of TAVG / PTOT / TMAX
> anomalies vs 1995–2014. I need to know what the hazards pipeline already produces that speaks to
> *frequency of extremes, historical vs projected, with per-GCM spread*, before I write a request.
>
> 1. Which hazard indices are currently baked per GCM (not just ENSEMBLEmean) — NTx35, NDWS,
>    NDWL0, HSH, PTOT/TAVG anomalies, others? For which SSPs and periods, and which of the 18
>    NEX-GDDP-CMIP6 GCMs?
> 2. Do any outputs already express **frequency** (e.g. % of years above a threshold, return-period
>    style counts) for a historical window and for each future window? If so: variable names, units,
>    thresholds, baseline, S3 prefixes.
> 3. Are there z-score or percentile-class products (e.g. "unusual ≥1σ / extreme ≥2σ") stored per
>    GCM anywhere, or only computed in the notebook?
> 4. Admin coverage of the hazard parquets: adm0 / adm1 / adm2? Africa only or any global tiles?
>    Which boundary set (GAUL 2024)?
> 5. The data audit found the CR notebook reads `nex-gddp-cmip6/…/vop_nominal-usd21/ENSEMBLEmean`
>    while the pipeline writes `atlas_cmip6/…/vop_intld15/ENSEMBLE`. Has that been S3-verified,
>    and which prefix is canonical now?
> 6. What would it cost (compute / wall-clock) to add a per-GCM extreme-event classification table
>    at adm0/adm1 for 4 SSPs × 4 periods, if it doesn't exist?
>
> Please answer with paths and variable names rather than prose where you can.

### Part B — request skeleton (finalise after Part A is answered)

| Field | Draft |
| --- | --- |
| Product | `extreme_events_frequency` — per admin unit × hazard × scenario × period: share of years classified *unusual* (≥1σ) and *extreme* (≥2σ) vs the 1995–2014 baseline; one row per GCM plus ensemble median and 17–83 % range |
| Hazards | PTOT (both tails), TAVG, TMAX, NTx35, NDWS, NDWL0, HSH (match the CR notebook's threshold rows) |
| Scenarios × periods | SSP1-2.6, 2-4.5, 3-7.0, 5-8.5 × 2021–40, 2041–60, 2061–80, 2081–2100 + historical 1981–2020 observed (CHIRPS v3 / CHIRTS-ERA5) |
| Admin | adm0 + adm1 (adm2 later), GAUL 2024 codes |
| Schema | Parquet; columns `adm0_code, adm1_code, hazard, scenario, period, gcm, p_unusual, p_extreme, n_years, baseline, threshold_sd`; keyed so it joins the existing CR projections parquet |
| Known fix to fold in | Togo SAT labels Z = 1 / Z = 2 inconsistently with its annex — set the threshold labels explicitly in the product metadata so the template cannot inherit the ambiguity |
| Delivery | S3 under the canonical prefix from Part A Q5; CDH record via the `datacube` extension; notebook reads it in place of the client-side classification |

---

## §3 — Theme 3 & 6 recommendations: spatial data vs method / tool notes

Pete's call: separate what is **spatial data the Hub can host or federate** from what is a
**method or tool** that needs a metadata note (and maybe a worked example), not a raster.

| Recommendation | Kind | What the Hub does | Queue row |
| --- | --- | --- | --- |
| WRI Aqueduct 4.0 (bws / bwd) | spatial — vector polygons | already on *Priority Data* for B4T; add GCF; derive admin-joined bws/bwd parquet | note row |
| AQUASTAT GMIA v5 → **GMIA-NEXT** | spatial — raster | derive admin irrigated-area share (ha, %) from the 30 m binary; federate the Zenodo source | GMIA |
| FAO FishStat aquaculture value | tabular, admin0 | derive-then-host ISO3 × year parquet (NC-SA) | FishStat |
| FAO GLW4 | spatial — raster | **held** (published record `glw4-2020`) | — |
| Annual gridded livestock 1961–2021 (ESSD 2025, 5 km) | spatial — raster time-series | complement to GLW4 for trend/baseline; log as candidate, not P1 | evidence log |
| FAO GLEAM / GLEAM-X | **method / model + federated data** | record as `resource_type: software` (GLEAM R package `un-fao/GLEAM`, **AGPL-3**, pushed 2026-09-17) and federate the **GLEAM 3 dashboard** data (CC BY 4.0; https://foodandagricultureorganization.shinyapps.io/GLEAMV3_Public/); GLW4 supplies animal numbers so GLEAM is only the emission-intensity layer | GLEAM (method) |
| iCLEANED / CLEANED | **method / tool** | metadata case study (`resource_type` software or document); model package `CIAT/cleaned` (MIT, v0.6.0) + Shiny app `CIAT/icleaned` (MIT) served at https://icleaned.alliance.cgiar.org/; CDH support still at *idea* — see [`../../icleaned/BRIEF.md`](../../icleaned/BRIEF.md) | iCLEANED (method) |
| FAO EX-ACT | **tool / engine** | computation engine, see §6 | EX-ACT (tool) |
| IPCC EFDB | **lookup / method** | curated Tier-1 emission-factor lookup (licence check first) | EFDB |
| ESA WorldCover | spatial — raster | derived admin product, see §6 | WorldCover |
| EDGAR / FAOSTAT emissions | spatial grid + tabular | federate FAOSTAT country totals; mirror EDGAR grid only if zonal stats are needed | EDGAR |
| GYGA, WOCAT, national census | — | **parked** (P2/P3) | — |

Design consequence: the Hub's metadata standard needs the `software` / `document` resource types
exercised with real examples. EX-ACT, GLEAM-X and iCLEANED are the three case studies for that —
coordinate with Brayden once v0.4.0 is in.

---

## §4 — Theme 4: P1 + P2, MICS dropped

All ten remaining Theme 4 datasets are queued. Live-check results: INFORM JSON API answers (all
countries in one ~2 MB payload; country filter parameters still to be confirmed), FEWS NET FDW
`ipcphase` answers without a key (admin0…admin2 + livelihood zones, `pct_phase3/4/5`), DHS
Indicator API answers for TGO (and now ships an **MCP server** — "Connect with Claude" — worth a
look for the AI route), UNICEF SDMX serves JMP WASH as CSV, HDX serves the RWI package metadata.
GDL and INFORM-Subnational pages live. UNICEF MICS is out (P3, restricted microdata, no API).

---

## §5 — Theme 5: Climate Watch test + document-registry parquet (spec only)

### Climate Watch API — tested 2026-10-07

- `GET /api/v1/ndcs/TGO/text` → the revised first NDC as HTML (French), with document type and
  linkages. Works.
- `GET /api/v1/ndcs/TGO/content_overview` → sector list (Agriculture, Water, LULUCF/Forestry…) +
  headline values (adaptation included, GHG target type, …) per document. Works.
- `GET /api/v1/ndcs?filter=sectoral` → the sectoral-indicator catalogue (Agriculture → Food
  security → indicator ids …). Works; the `location` parameter is ignored on the list endpoint, so
  filter client-side.
- Verdict: **good enough to federate for CN A.16 / FP D.5 headline alignment** (which sectors a
  country's NDC covers, adaptation/mitigation targets). Not a substitute for reading the NAP.

### Document-registry parquet — specification (build later)

Purpose: one table that *describes* the policy PDFs an LLM pipeline needs to open, with a primary
link and a backup so the citation survives a registry redesign. No text extraction.

| Column | Type | Note |
| --- | --- | --- |
| `doc_id` | string | `{registry}-{iso3}-{slug}-{version}` |
| `country_iso3` | string | ISO 3166-1 alpha-3 |
| `registry` | enum | `NDC` (UNFCCC NDC Registry) · `NAP` (NAP Central) · `GCF-CP` (GCF country programme) |
| `title` | string | as published |
| `party` / `publisher` | string | |
| `document_type` | string | e.g. first NDC, updated NDC, NAP, country programme |
| `version` | string | registry's own versioning where present |
| `submission_date` | date | |
| `language` | string | BCP-47 |
| `primary_url` | string | registry URL at harvest |
| `backup_url` | string | Wayback Machine snapshot URL (`web.archive.org/save/` at harvest) |
| `sha256` | string | of the fetched PDF |
| `pages` | int | |
| `fetched_at` | datetime | |
| `licence_terms` | string | UNFCCC Terms of Use / GCF terms — link and cite, no redistribution of the PDF |

Harvest: NDC Registry and NAP Central have no structured API — scrape the listing pages;
GCF country programmes are a filtered operational-documents view. Climate Watch's `ndcs/{iso}/text`
gives the NDC document list per country and can seed the NDC rows. Hub record:
`spatial-indexed` template, `dimensions: [{name: country_iso3, type: location}]`, `joins` to the
admin0 boundary record.

**Dependency on CACC1.** Cesare's SQL store held project documents and (per the 2026-04-29 demo)
an extraction pipeline over them. Before building, ask for the extraction dataset and the
method/code so this registry can be made repeatable and updatable rather than rebuilt — see the
Teams message drafted for him (`outputs/msg-cesare-2026-10.md`, not committed).

---

## §6 — Theme 6: EX-ACT as an engine; WorldCover as a derived product; EDGAR; EFDB

### EX-ACT — can an AI run it or read what it needs?

Facts (repo `un-fao/exact-django-webapp`, read 2026-10-07): AGPL-3.0-or-later; Python 3.11,
Django 5.2 + Django REST Framework; `djangoexact/api/urls.py` registers REST routers for projects,
activities and every module (annual-croplands, perennial-croplands, grasslands, flooded-rices,
land-use-changes, livestock, inputs, irrigation, fisheries, aquaculture, coastal/inland wetlands…),
with Swagger/ReDoc at `/api/swagger/` and `/api/docs/` and a shipped Postman collection;
`djangoexact/math_model/` is a **pure-Python calculation layer independent of Django**; IPCC
default factors ship as versioned fixtures (`api/fixtures/*.json`, incl. `gleamregion.json`,
`handinhandcountry.json`, `emissionfactorsource.json`); `docs/faostat-integration.md` documents a
FAOSTAT lookup; last push 2026-10-06. The hosted app (exact.apps.fao.org) returns the SPA shell for
`/api/*`, i.e. no public API.

| Option | How | Pros | Cons |
| --- | --- | --- | --- |
| A. Call the hosted instance | authenticate (Firebase/JWT) and use its REST API | zero hosting | API not exposed publicly; account-bound; FAO ToS |
| B. **Self-host the AGPL app** (Docker: `deploy/Dockerfile.web_service`) behind a Hub endpoint | REST + Swagger out of the box; module-by-module activity data in, tCO₂e out | reproducible, versioned factors, citable; an MCP/skill can drive it | AGPL network copyleft (fine — we don't modify or we publish changes); PostgreSQL + WeasyPrint deps |
| C. Vendor `math_model` + fixtures as a Python library | import the calculators directly in the pipeline | lightest; no web stack | must track upstream factor updates; module wiring (phases, scenarios) lives in Django models, not the math layer |

**Recommendation:** B for the engine (one container, documented API, FAO's own code),
C only for notebook-side quick estimates. Either way the Hub's job is to emit the **activity data
per admin unit** EX-ACT consumes: land-cover class areas (WorldCover admin product), livestock head
(GLW4), irrigated area (GMIA-NEXT), cropland area (MapSPAM / CROPGRIDS), plus climate zone and
soil type (EX-ACT's own `climate` / `soiltype` tables, which key to FAO HiH regions). Record EX-ACT
in the Hub as `resource_type: software` with the activity-data contract in `cdh.usage`.

### ESA WorldCover — derived admin product

Source: `s3://esa-worldcover/` (eu-central-1, no-sign-request, STAC endpoint), v100 (2020) and
v200 (2021), 11 classes, CC BY 4.0. Hosting 10 m globally is out of scope; the Hub hosts:

- `worldcover_admin_area` — adm0/1/2 × year (2020, 2021) × class → area (ha) and share (%);
- `worldcover_admin_change` — adm0/1/2 × class-from × class-to → ha (transition matrix) and net
  change per class, 2020→2021, **with the caveat ESA itself gives**: v100→v200 differ in algorithm,
  so change contains method artefacts — publish, but flag `not_recommended_for: trend claims`;
- 10 m access stays **federated** (AWS COG / STAC; GEE `ESA/WorldCover/v200`; Terrascope WMS —
  the WMS timed out from here, prefer AWS).

GAUL 2024 / World Bank boundaries as the zonal units (the `World Bank Admin Boundaries` row on
*Priority Data* is the join target). Complexity 3 (a one-off global zonal-stats job).

### EDGAR / FAOSTAT

FAOSTAT bulk `Emissions_Totals_E_All_Data.zip` (14 MB) downloads cleanly; the FAOSTAT REST
endpoint was flaky from here (401 / timeout) — use bulk for the Hub copy, API for live lookups.
EDGAR 2024 dataset page live; grids are 0.1° NetCDF per sector — mirror only the AFOLU sectors if
zonal stats are needed, otherwise country tables suffice. Avoid the IEA-EDGAR CO₂ subset (separate
terms).

### IPCC EFDB

Site states the EFDB "is undergoing a renewal and renovation" with "a more user-friendly EF
database … for use in early 2026" — recheck before building a lookup. No licence text; IPCC
copyright. Treat as *link + cite* until the new platform states terms; EX-ACT's fixtures already
carry the Tier-1 factors we need, which is the practical route.

---

## §7 & §9 — Portfolio and finance: one SDMX / Data360 client

- **OECD** — `sdmx.oecd.org/public/rest/dataflow/OECD.DCD.FSD/DSD_CRS@DF_CRS/` answers (SDMX 2.1
  structure). CRDF is a dataflow on the same endpoint → one client, two dataflows. CC BY 4.0 for
  content published from July 2024.
- **World Bank Data360** — `data360api.worldbank.org/data360/indicators?datasetId=IMF_FM` lists
  the IMF Fiscal Monitor series (`IMF_FM_GGXWDG_…`, `IMF_FM_GGR_…`); `data?DATABASE_ID=WB_IDS&REF_AREA=TGO`
  returns the debt series. Both answer without a key. Use Data360 for IMF, never IMF bulk.
- **IATI Datastore** — needs an API Gateway subscription (free Trial, then Full Access). Register
  one Hub key; one query pulls AF, IFAD, WB, UNDP activities for a recipient country.
- **World Bank IEG** — site and `/data` 403 to automated fetch (as in July); the DDH API rate-limited
  (429) on a cold call. Verify in a browser; federate via DDH once the dataset id is pinned.
- The CACC1 MCF dataset (5,115 projects) remains the comparables spine for Theme 7 — pending the
  champion's final version (see the Cesare message).

---

## §8 — Safeguards: licence split and the MFL / Mosaic ask

| Dataset | Licence (rescreened) | Hub route |
| --- | --- | --- |
| Global Forest Watch tree-cover loss | CC BY 4.0 (GFW Data API `umd_tree_cover_loss`, v1.9.1) | federate API / mirror zonal stats |
| FAO SDG 5.a.1 / 5.a.2 + Land Portal | FAO open terms (portal live; Land Portal API 403 to bots) | federate |
| CSPD / CSPDxCF | CC BY-NC 4.0 (CGIAR CSO) | federate link + derive country tier — coordinate with Bia Carneiro |
| WDPA / Protected Planet | NC, no-redistribute; API token via request form | derive overlay stat only |
| Key Biodiversity Areas | non-commercial via request form (5–10 working days); commercial via IBAT | derive overlay %; request a copy |
| LandMark | **CC BY-SA 4.0** + LandMark ToS (June 2026 update); form-gated download | derive Indigenous-land flag / area; ShareAlike on the derivative |

Pete's call: promote LandMark, KBA and FAO SDG 5.a.x to P1, and ask the Multifunctional Landscapes
programme ("Mosaic") whether they will host or federate the biodiversity / tenure layers — they are
closer to WDPA/KBA/LandMark than the Hub's climate team is. Draft message:
`outputs/msg-mfl-mosaic-2026-10.md` (not committed).

---

## Follow-ons not done in this round

- **Metadata YAMLs** for every federated/hosted row — after v0.4.0; order: open tabular P1s
  (INFORM, FEWS NET, DHS, OECD CRS/CRDF, Data360/IMF, IDS, Climate Watch) with the
  `spatial-indexed` template + `joins` to the boundary record → derived products (RWI admin, SHDI,
  WorldCover admin, WDPA/KBA/LandMark overlays, GMIA-NEXT admin) → tool/method records (EX-ACT,
  GLEAM, iCLEANED).
- **`climate-rationale` skill** — spec on the review page's Skills tab; issue text drafted in
  `outputs/skills-issue-climate-rationale.md`; build after one theme's data is in the Hub.
- **Adaptation Insights** (Njuguna / Muller / Nowak) may hold assets for Themes 5–7 — not contacted
  this round.
