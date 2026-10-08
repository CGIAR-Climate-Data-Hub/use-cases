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

## §1 — Climate trends: observed rainfall for any country (built 2026-10-07)

Theme 1 was "in hand" for Africa only — the CR notebook's observed rainfall is the Africa CHIRPS
parquet. The GCF pipeline includes Syria, Iraq, Sri Lanka and Egypt, so the coverage gap was real.
Andrés Aguilar's **CHIRPS v3.0 daily (`rnl`) Zarr v3 cube on Hugging Face** (global 60°S–60°N,
0.05°, 1981 → 2026-08, CC0, CDH v0.3.0 record beside it) closes it:
[`code/rainfall/chirps_admin.py`](../code/rainfall/README.md) reads only the chunks under a
country's bbox (one year at a time, no dask), rasterises GAUL 2024 adm2 on the 0.05° grid and
writes adm0/1/2 **annual totals 1981–2025, 1991–2020 baseline and anomalies, Theil–Sen trend with
Mann–Kendall p, last-5-year anomaly, wettest/driest year, and the monthly climatology**. Boundaries
for non-African countries come from the Atlas **global** raw GAUL 2024 file (725 MB; filter by
`iso3_code`). GAUL's disputed territories (e.g. Bir Tawil, Hala'ib for EGY) carry their own
gaul0 code — adm0 uses the main code, disputed units are flagged.

**Runs 2026-10-07** (1981–2025, 1991–2020 baseline, ~4–5 s per country-year over HTTP):

| Country | adm2 units | Mean annual rainfall 1991–2020 | Theil–Sen trend (95 % CI), MK p | Last 5 yrs vs baseline | adm1 range |
| --- | --- | --- | --- | --- | --- |
| Egypt (EGY) | 366 (+2 disputed) | 19 ± 5 mm | −0.1 mm/decade (−1.4 … +1.3), p = 0.89 | −21 % | Luxor 0 → Alexandria 148 mm |
| Syria (SYR) | 62 | 278 ± 63 mm | **−17.0 mm/decade** (−29.5 … −1.2), p = 0.04 | −21 % | Deir-Ez-Zor 174 → Lattakia 1,217 mm |
| Sri Lanka (LKA) | 25 | 1,962 ± 223 mm | **+91 mm/decade** (+36 … +150), p < 0.01 | +16 % | Northern 1,288 → Sabaragamuwa 3,259 mm |

Syria and Sri Lanka are outside the Africa product — the first observed-climate numbers the
rationale can cite for them. `cdh_rationale --rainfall <dir>` now emits Section 1 fragments
(baseline, trend with significance, last-5-year anomaly, wettest/driest year, seasonality peak
months) from these tables; Egypt test: 33 fragments, 7 gaps (temperature/CHIRTS and projections
still gaps outside Africa). Outputs are regenerated, not committed.

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

### Part A — answered (hazards session, 2026-10-07)

The hazards session answered with a verified inventory
(`hazards_prototype/HANDOVER_2026-10-07_gcf-theme2-extremes-inventory.md`, untracked there).
Headline: **a per-GCM frequency-of-extremes table already exists and is public.** The
re-verification below was run from this machine on 2026-10-07 with `aws s3 ls --no-sign-request`
and DuckDB over the public HTTPS endpoint, always with `read_parquet(…, hive_partitioning=false)`
(the `key=value/` path segments otherwise override the stored `timeframe` column and hide the
period dimension).

| Claim | Verified |
| --- | --- |
| `s3://digital-atlas/domain=climate/type=hazard-indices/source=nex-gddp-cmip6/region=africa/processing=hazard-change/timeframe=annual/variable=haz_freq.parquet` — 5.4 MB, dated 2026-06-24 | ✅ listed (5,439,142 B); companions `haz_freq_ensemble`, `ntx_perc_area_by_model`, `thi_perc_area_by_model`, `ptot_change_by_model`, `ptot_diff_by_model` (+ `_ensemble` twins) present |
| Schema `iso3, admin0_name, admin1_name, admin2_name, variable, value, scenario, model, timeframe, severity, hazard, crop, hazard_user` | ✅ |
| 12,467,664 rows; 4,292 distinct adm2; **18 GCMs** | ✅ (ACCESS-CM2 … TaiESM1, list matches the briefing) |
| `historic/1995-2014` + 4 SSPs × 4 periods = 17 scenario × period combinations, 733,392 rows each | ✅ |
| `hazard ∈ {NDWS (drought), NDWL0 (wet)}` only; `severity ∈ {severe, extreme}` only; `variable ∈ {frequency (0–1), frequency_n (0–19 years)}` | ✅ |
| `haz_freq_ensemble.parquet` = `mean, min, max, sd` across GCMs (no `model` column) | ✅ |
| Defect: `ntx_perc_area_by_model.variable` holds the raw layer name (e.g. `ssp126_EC-Earth3_2041-2060_NTx35-mean-G21_extreme`) instead of `perc_area`; `thi_perc_area_by_model.variable = perc_area` is clean | ✅ |
| Thresholds (`metadata/haz_classes.csv`): NDWS severe > 20 d, extreme > 25 d; NDWL0 severe > 5 d, extreme > 8 d; every other hazard (NTx35, NTx40, TAVG, PTOT, HSH_max, THI_max, NDD, TAI) already has Moderate / Severe / Extreme thresholds | ✅ |
| SEC4 (`R/2.2_haz_change.R:633-637`) is `haz_choices <- c("NDWS","NDWL0")`, `sev_classes <- c("Severe","Extreme")` | ✅ |
| **Prefix discrepancy — the July audit had it backwards.** Canonical hazard-exposure tiers are `domain=hazard_exposure/source=nex-gddp-cmip6/region=ssa/…/variable=vop_nominal-usd21/period=jagermeyr/model=ENSEMBLEmean/severity={severe,moderate,extreme}/int=multi-hazard.parquet` (~63 MB each + `.parquet.json` sidecar), written 2026-10-06 — the path the CR notebook reads. `source=atlas_cmip6/…` is the stale 2025-06 tree | ✅ both prefixes listed |
| No stored z-score / percentile-class product exists, per GCM or ensemble; only threshold classes | not re-checked here (repo grep by the hazards session) |

Two consequences for Theme 2: the notebook can read `haz_freq.parquet` today for drought and
waterlogging frequency with full per-GCM spread; and the request is an **extension of SEC4**, not
a new product. The NEX-GDDP historical run ends 2014, so a WMO 1991–2020 baseline is an
observational-pipeline question, not part of this ask.

### Part B — the data request (ready to send; paste-ready copy in `outputs/request-hazards-theme2-2026-10-07.md`)

> **Request to the hazards pipeline — extend SEC4 `haz_freq` for GCF Prep Facility Theme 2**
>
> **Context.** `haz_freq.parquet` (`processing=hazard-change/timeframe=annual`, 2026-06-24)
> already gives per-GCM frequency of NDWS / NDWL0 exceedance (severe, extreme) at adm0/1/2 for
> `historic 1995-2014` and 4 SSPs × 4 periods, 18 GCMs. GCF Theme 2 ("Extreme events", CN C.1 /
> FP B.1, D.1) needs the same statistic for the other hazards the Climate Rationale notebook
> reports. All of them already have thresholds in `metadata/haz_classes.csv` and per-GCM frequency
> COGs on disk from R/2, so this is a SEC4 re-run with a wider choice set — no R/2 re-bake, no
> NEX-GDDP re-ingest.
>
> **Ask.**
>
> 1. In `R/2.2_haz_change.R` SEC4, extend `haz_choices` from `c("NDWS","NDWL0")` to add
>    **NTx35, TAVG, PTOT, HSH_max, THI_max** (and NDD, TAI if cheap — they are in the same table).
>    PTOT is a *below*-threshold hazard (`direction <`) — keep its class semantics as in
>    `haz_classes.csv`.
> 2. Extend `sev_classes` from `c("Severe","Extreme")` to add **"Moderate"**.
> 3. Fix `ntx_perc_area_by_model.variable` to the constant `perc_area` (currently the raw layer
>    name); `thi_perc_area_by_model` is already correct and is the pattern.
> 4. Before launching, read the `SEC4 (haz_freq) — DONE in Xs` line from the last R/2.2 log on the
>    node and report it, so the extended run can be scoped.
> 5. Run SEC4 for **both** timeframe axes: `annual` (as now) **and `jagermeyr`** (crop-calendar
>    season) — the GCF rationale needs growing-season extremes more than calendar-year ones.
>    `R/2.2_haz_change.R:178` already exposes this as `R22_TIMEFRAME` (default `annual`; the
>    parent dirs carry a `jagermeyr` axis from R/2), so it is a second invocation with
>    `R22_TIMEFRAME=jagermeyr`, publishing under `processing=hazard-change/timeframe=jagermeyr/`.
>    Expectation as an invariant: the jagermeyr run yields the same row count per
>    `(hazard, severity, scenario, period, model)` as the annual run. Note the stored `timeframe`
>    column holds the *period* (e.g. `2021-2040`) while the path segment `timeframe=jagermeyr` holds
>    the season axis — consumers must read with `hive_partitioning=false` or the path value
>    overrides the column. Worth stating in the `.parquet.json` sidecar.
> 6. **Defect — historic NDWS frequency is saturated.** In the published `haz_freq.parquet`,
>    `scenario='historic'` rows for **NDWS** (both `severe` and `extreme`) have `frequency = 1.0`
>    and `frequency_n = 19` for **every GCM and every African adm0** (1,062 rows each, verified
>    2026-10-07 with DuckDB, `hive_partitioning=false`); NDWL0 historic values are normal (mean
>    0.13 severe / 0.04 extreme) and NDWS projections are plausible (ssp245 2021–2040 median 0.87
>    severe / 0.17 extreme). So the historic NDWS baseline is unusable for a historical-vs-projected
>    comparison. Suspects: the historic NDWS raster stack read by SEC4 is on a different scale/units
>    than the projection stacks, or the `>` threshold is applied to a cumulative rather than annual
>    layer. Please check the historic NDWS inputs to `R/2.2_haz_change.R` SEC4 and re-publish; the
>    extended run (asks 1–5) should not inherit this.
>
> **Keep.** Same output path and schema (`variable ∈ {frequency, frequency_n}`, `severity`,
> `hazard`, `hazard_user`, `crop`, `model`, `scenario`, `timeframe`), same GAUL 2024 adm0/1/2, same
> 1995–2014 baseline with identical thresholds applied to historic and projected, and the
> `_ensemble` twin (`mean, min, max, sd`). Add `hazard_user` labels for the new hazards (heat /
> rainfall-deficit / human-heat / livestock-heat) consistent with the existing `drought` / `wet`.
> `crop` stays `generic` except THI (`cattle` as in `thi_perc_area_by_model`).
>
> **Expectations, stated as invariants (not figures).** Row count scales linearly with
> `n_hazards × n_severities × 17 × 18 × n_admin_units`; each scenario × period slice has the
> same row count as every other; `frequency ∈ [0,1]`; `frequency_n ≤ n_years` (19 for 1995–2014,
> 20 for future periods); every `(hazard, severity)` pair present for all 18 GCMs. SEC4 zonal
> extraction scales ~linearly with layer count. The s3 uploader has no verify and always
> overwrites — diff local vs S3 after publish; do not use `s3fs::s3_file_delete()` on this bucket
> (permanent, all versions).
>
> **Not in this request.** Any z-score / σ-based classification. The notebook's "unusual ≥1σ /
> extreme ≥2σ" statistic is a notebook-method question handled separately.
>
> **Consumer.** The GCF review page Theme 2
> (https://cgiar-climate-data-hub.github.io/use-cases/gcf-preparation-facility/gcf-prep-review.html#s2)
> and the CR notebook's extreme-events section, which will read `haz_freq.parquet` in place of the
> client-side classification. A CDH catalog record for `haz_freq` will be authored after the
> metadata-standard v0.4.0 release.

Parked, outside the request: whether the CR notebook divides anomalies by the published
across-GCM `sd` (`timeseries_mean_month` → `sd`, "Standard deviation of hazard values across
GCMs") rather than the interannual baseline SD — inferred by the hazards session from column
semantics, **not confirmed against notebook source**. Resolve in the notebook repo before
asserting anything about the z-score method. (The `jagermeyr` question is closed — Pete,
2026-10-07: crop-calendar framing is preferred, so it is ask #5 above.)

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

**Sibling product (AgWise use-case, 2026-10-07).** The AgWise queue carries "ESA WorldCover 2021
v200 (cropland-fraction grid)" — same source, a second derivative. One zonal job now emits both:
see below.

**Built 2026-10-07 — [`code/worldcover/worldcover_admin.py`](../code/worldcover/README.md).**
Reads the 10 m COGs from `s3://esa-worldcover` (anonymous, windowed), rasterises the Atlas GAUL
2024 adm2 polygons on the WorldCover grid, and writes `worldcover_admin_area` (year × class →
ha, share), `worldcover_admin_change` (2020→2021 transition matrix) and
`worldcover_admin_cropland` (class 40 ha + share, the AgWise product) at adm0/1/2 plus a
provenance sidecar. Togo run: 4 tiles, 213 windows, 148 s; national 2021 total 5.705 Mha
(Togo ≈ 5.68 Mha land + water — reconciles); cropland 25.7 %, shrubland 27.2 %, tree cover
24.8 %, grassland 20.4 %; adm1 cropland share from 4.7 % (Maritime) to 72.4 % (Savanes). The
change table demonstrates the v100→v200 caveat: 334 kha "shrubland → tree cover" and 234 kha
"shrubland → grassland" in one year are algorithm change, not land-use change — hence
`not_recommended_for: trend claims` in the sidecar. Any country in the GAUL Africa set runs with
one command; outputs are not committed (regenerate), only the code is.

**Boundaries — a Hub standardisation decision is pending.** This use-case and the Atlas hazards
products use GAUL 2024; *Priority Data* lists World Bank Admin Boundaries (in progress); the
AgWise brief uses geoBoundaries. Every admin-indexed record's `joins.target` depends on this — the
AgWise brief flags it; resolve it with Brayden before the first metadata records are authored.

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

- **Metadata YAMLs** — **unblocked 2026-10-07/08:** `cdh-metadata-standard` **v0.4.0 and v0.4.1**
  released (PR #35/#36), the `cdh-metadata` skill bumped to 0.4.1 overnight. What changed for us:
  `structures[]` replaces record-level dimensions/variables (datacube extension folded into core);
  `joins` → `foreign_keys` (Frictionless shape, `reference.resource` = catalog record id);
  `spatial.resolution` removed (grid spacing is an `xy` dimension; tables declare a
  `type: location` dimension + `foreign_keys` to a boundary record); `version`, `created`,
  `updated` and a `maintainer` contact are required; `citation.authors` are objects;
  `data[].nodata` → `variables[].nodata`; API-served data is a `data[]` entry with
  `service-desc`/`service-doc` links; `file_index` (`cdh-inventory` CSV) for file sets;
  `attribution`, `update_frequency`, `parent`, `derived_from[].id`. Templates dir is gone — use
  `examples/kitchen-sink/admin2/` as the shape for admin-indexed tables and
  `scripts/validate-yaml.js` to validate. Catalog records themselves are still v0.3.0.
  Submission route: the [CDH Metadata Generator](https://anaguilarar.github.io/CDH-metadata-app/)
  → `cdh-catalog` "Submit metadata record" issue → bot opens the PR → CDH review. Order for us:
  derived products first (WorldCover admin + cropfrac grid, CHIRPS admin rainfall, `haz_freq`
  extension when fixed) as children/derivations with `processing[].derived_from`; then the
  federated API sources (INFORM, FEWS NET, DHS, OECD CRS/CRDF, Data360, Climate Watch, UNICEF JMP)
  as API-endpoint records; then tool/method records (EX-ACT, GLEAM, iCLEANED).
- **Hosting route is now explicit** — `cdh-data-pipeline` (pushed 2026-10-07): one recipe per
  dataset (`recipes/<id>.py` calling `write_parquet` / `write_cog` / `write_zarr`), outputs under
  `s3://digital-atlas/cdh/data/<dataset-id>/` (lowercase kebab ids, `cog/` inside the prefix,
  upstream version in the id, no `latest/`). Our WorldCover and CHIRPS-admin jobs should become
  recipes there rather than ad-hoc uploads.
- **Boundaries decision — effectively made by the pipeline:** `recipes/wb_boundaries.py` publishes
  World Bank GAD v2 (adm0/1/2 GeoParquet + attribute tables carrying HASC / **GAUL** / P-code
  crosswalks) to `cdh/data/wb-boundaries-gad/`. Our products are on GAUL 2024; the crosswalk makes
  a `foreign_keys` join possible without re-running, but new products should be cut on WB GAD once
  its catalog record exists. Confirm with Brayden; AgWise (geoBoundaries) is affected more.
- **`climate-rationale` skill** — spec on the review page's Skills tab; issue text drafted in
  `outputs/skills-issue-climate-rationale.md`. **Prototype of the data layer built 2026-10-07:**
  [`code/rationale/`](../code/rationale/README.md) (`python -m cdh_rationale TGO …`) reads the
  rationale map + the federated pulls + WorldCover + `haz_freq` and emits labelled, citable
  fragments per section with explicit gaps; Togo: sections 4, 5, 7, 9 fully data-backed, 6 gaps.
  The LLM composition step (the skill proper) sits on top of this.
- **Adaptation Insights** (Njuguna / Muller / Nowak) may hold assets for Themes 5–7 — not contacted
  this round.
