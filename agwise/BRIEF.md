---
# === Identity ===
title: AgWise - Climate Data Integration for Process-Based Crop Modelling
description: Integrate historical and forecasted climate data into the AgWise fertilization module to support process-based crop model simulations and Decision Support Tools across Africa.
science_program: Sustainable Farming (SFP)

# === Lifecycle ===
type: existing                       # new | existing
origin: ongoing-project              # ongoing-project | funding-pipeline | data-gap
status: active-development           # idea | brief | active-development | piloting | handover | complete | on-hold | no-go

# === Go / No Go ===
go_no_go:
  decision: go                       # pending | go | no-go | on-hold
  date:                              # YYYY-MM-DD when decided
  decided_by:                        # e.g. "CDH Core Team"
  notes:

# === People ===
champion: ""                         # Single named person (display name); domain owner
coordinator: "Andres Aguilar Ariza"  # Single named person (display name); connector / facilitator
task_group: ["Andres Aguilar Ariza", "Diego Agudelo", "Jemal Seid Ahmed", "Lizeth Llanos-Herrera"]

# === CA-OS linkage ===
primary_aow: AoW2-Adapt              # AoW0-Orchestrate | AoW1-Accelerate | AoW2-Adapt | AoW3-Empower | AoW4-Transition | AoW5-Finance
related_aows: []
ca_os_packages: []

# === Metadata ===
tags: [agwise, crop-modelling, crops, forecasting, agricultural-services, climate-information]
updated: 2026-10-07
---

> Integrate CDH-facilitated historical and forecasted climate data into the AgWise fertilization module, enabling process-based crop model simulations at scale across Africa via the ag-cube-cm package and associated AI-assisted workflows.

## Brief

### Background & rationale

AgWise is a CGIAR innovation designed to provide tailored agronomic recommendations based on specific demands from partners to improve farmer productivity and/or profitability. Its modular framework offers data-driven advice on fertilizer requirements, optimal planting dates, suitable cultivars, and other agricultural practices. By leveraging extensive datasets, including field trials, market trends, topography, climate, and soil information, AgWise delivers accurate and context-specific guidance to support informed decision-making and enhance farming outcomes.

Specifically, its fertilization module generates actionable recommendations for Decision Support Tools (DSTs) across Africa. These recommendations depend on process-based crop models, which require high-resolution climate, soil, and management data.

To address this data access need, the ag-cube-cm Python package was developed — a tool for spatial NetCDF and Zarr datacube processing and crop model orchestration. It integrates climate data (AgERA5, CHIRPS), soil data (SoilGrids), and management inputs to run pixel-level agricultural simulations at scale, either programmatically or via an AI assistant using the `/spatial-crop-modeler` MCP skill. An initial yield prediction test was conducted for a small area in Malawi, and a Ghana pilot that integrates forecasted and historical climate data to link the crop modeling components (yield prediction and fertilization) is proposed.

A second AgWise data layer, the `agwise-data` module ([byliz-ai/data_sourcing](https://github.com/byliz-ai/data_sourcing)), fetches, harmonises and caches climate, soil, terrain and remote-sensing inputs on CGLabs (CHIRPS, AgERA5, SEAS5, SoilGrids, iSDA, Copernicus DEM, MODIS, ESA WorldCover, geoBoundaries) and writes DSSAT/APSIM inputs. Its catalog entries already follow the CDH metadata core fields. How it relates to `ag-cube-cm` and `aggeodata` — supersedes, complements, or separate — is _TBC_ with Andres and Lizeth.

A parallel Alliance stack exists: **PRISM** (Platform-Ready Inputs for Spatial Modeling; Tonle, Segnon, Gouroubera & Zougmoré, CIAT Dakar, _Comput. Electron. Agric._ 254, 2026, AICCRA-funded) and its `prismpy` package formalise retrieval → harmonisation → translation → validation → packaging of crop-model inputs for CRAFT, PYTHIA, ACEA and SARRA-Py, with ICASA/DOME configs and provenance-tracked packages. Its stated roadmap — add SoilGrids and CHIRPS, cache retrieved layers, build a STAC-style package-discovery platform — is what CDH and `agwise-data` already provide. Both stacks retrieve and harmonise source data — that is the duplication. They differ in what sits around that core: `agwise-data` has a shared CGLabs cache, a CDH-aligned catalog and a wider source set (SoilGrids, CHIRPS, SEAS5, Copernicus DEM, MODIS, WorldCover); PRISM has ICASA/DOME standards, per-platform translators and validators, provenance-tracked packaging and the PRISMWEB front end. CDH's role is to be the neutral shared data layer both pull from, so neither team maintains its own retrieval code for the same providers. This use-case now also covers bringing them together. First contact already happened: Pete flagged PRISM to the AgWise team in a "PRISM <> AgWISE?" Teams chat on 2026-08-06 (Jemal: already using PYTHIA for Ethiopia, testing PRISM for multi-country runs); Franck Tonle posted PRISM + PYTHIA (DSSAT) results for two Ethiopian zones on 2026-08-09 and offered a demo with Alcade Segnon; the demo was never scheduled. PRISM also ships as a hosted platform, [PRISMWEB](https://prism.cdecentre.org/).

The CDH team will support storage and data integration.

### Objectives

- Fully integrate forecast and historical data for use in Process-Based Models, managed through the CDH for storage and AI skill performance assessment.
- Optimise yield prediction process time by integrating the climate API developed by Jemal into the model.
- Run an end-to-end pilot in Ghana to demonstrate the integrated historical + forecast data pipeline.
- Manage climate data storage and skill performance assessment through CDH.
- Define documentation, update frequency, and long-term data access model for the forecast API.
- Plan expansion of coverage and scalability beyond local machine runs.
- Position CDH as the shared retrieval + cache layer for both Alliance crop-model data stacks — `agwise-data` and PRISM/`prismpy` (CIAT Dakar) — and offer the CDH STAC catalog as the home for PRISM's planned input-package metadata platform, so the two teams coordinate rather than duplicate.

### People involved

| Name | Organisation | Role |
| ---- | ------------ | ---- |
| Andres Aguilar Ariza | Alliance Bioversity-CIAT | Developer of ag-cube-cm; coordinator |
| Diego Agudelo | Alliance Bioversity-CIAT | CDH team; co-developer |
| Jemal Seid Ahmed | Alliance Bioversity-CIAT | Climate forecast API developer |
| Siyabusa Mkuhlani | IITA | Co-developer |

### Key dates

| Date | Milestone |
| ---- | --------- |
| 2026-04 | ag-cube-cm package developed; initial Malawi yield test completed |
| 2026-05-02 | Approach confirmed: integrate forecast + historical climate data for AgWise; Ghana proposed as pilot |
| 2026-05-21 | CDH meeting — Jemal presents forecast API; Ghana pilot agreed; AWS migration in progress |
| 2026-08-06 | Pete opens "PRISM <> AgWISE?" Teams chat (Franck Tonle, Wuletawu Abera, Jemal Seid Ahmed); Franck posts PRISM + PYTHIA results 2026-08-09; demo proposed for week of 17 Aug, not held |
| 2026-10-07 | Dataset access analysis of `byliz-ai/data_sourcing`; AgWise ingestion queue drafted (11 rows) and rolled into the CDH ingestion tracker's use-case matrix; PRISM coordination added to scope |
| TBD | Jemal deploys AWS endpoint; documentation shared |
| TBD | CDH metadata v1 shared with Jemal |
| TBD | End-to-end Ghana pilot completed using integrated pipeline |

### Background materials

- [ag-cube-cm GitHub repository](https://github.com/CGIAR-Climate-Data-Hub/ag-cube-cm) — Python package for spatial crop model orchestration (NetCDF/Zarr processing, DSSAT pixel-level orchestration)
- [spatial-crop-modeler skill](https://github.com/CGIAR-Climate-Data-Hub/skills/tree/main/.agents/skills/spatial-crop-modeler) — AI agent skill for end-to-end spatial crop model workflows: environment check, parameter collection, YAML config generation, simulation execution, quality gate, and result interpretation
- [agwise-data data-sourcing module](https://github.com/byliz-ai/data_sourcing) — Python package (R wrappers, CLI) that fetches, harmonises and caches climate, soil, terrain and remote-sensing inputs on CGLabs; MIT
- [Dataset access analysis](./data-sourcing-access-analysis.md) — per-dataset review (2026-10-07) of what `agwise-data` can pull and whether each source is reached by regional API/COG request, bulk yearly download, or local staging
- [PRISM paper](https://doi.org/10.1016/j.compag.2026.112223) — Tonle et al. 2026, _Computers and Electronics in Agriculture_ 254, 112223 (open access, CC BY-NC); the [prismpy repository](https://github.com/izuku-franck1555/prismpy) (MIT per paper; LICENSE file not yet in repo); and the hosted [PRISMWEB platform](https://prism.cdecentre.org/)
- [Ingestion queue](./data/ingestion-queue.csv) — the 11 rows queued on 2026-10-07; feeds the cross-use-case `Use-case matrix` sheet of the CDH ingestion tracker (`asset_mapping/CDH_data-ingestion v2.xlsx`, OneDrive) via `hub-submissions/build_matrix.py`; same column set as the GCF queue plus four workflow fields

## Go / No Go

> _Filled in by the CDH Core Team after the brief is developed._

- **Decision:** Go (implicit)
- **Date:** TBC — formal CDH Core Team decision not yet recorded
- **Decided by:** TBC
- **Notes:**

## Action plan

> _To be developed once status reaches `active-development`._

### Actions

- [ ] Deploy AWS endpoint and share API documentation — Jemal
- [ ] Share CDH metadata v1 with Jemal — Andres / Diego
- [ ] Set up pilot pipeline for Ghana using Jemal's forecast API — Andres
- [ ] Reconnect to review AWS endpoint and metadata schema — All
- [ ] Define documentation standards and update frequency for forecast API — TBD
- [ ] Integrate API into full CDH pipeline to make it fully operational — TBD
- [ ] Define long-term data access / open data model — TBD
- [ ] Confirm how `byliz-ai/data_sourcing` relates to `ag-cube-cm` / `aggeodata` (supersedes, complements, separate) — Andres / Lizeth
- [ ] Decide CHIRPS version and staging model (v2 COG/GEE vs staged v3 yearly files) and iSDA staging vs provider API — Andres / CDH Technical Team
- [ ] Decide credential model for CDS and Earth Engine sources in CDH runs (user tokens, service account, or CDH-hosted derived layers) — CDH Technical Team
- [ ] Revive the "PRISM <> AgWISE?" Teams chat (dormant since 2026-08-09): add Alcade Segnon, Andres, Lizeth, Diego; schedule the demo Wuletawu asked for; agree one shared retrieval + cache layer — Pete
- [ ] Offer CDH-federated SoilGrids / CHIRPS / AgERA5 routes as PRISM's next data sources (their stated roadmap) — CDH Technical Team, after intro
- [ ] Propose the CDH STAC catalog as the home for PRISM's planned input-package metadata platform — Pete
- [ ] Adopt PRISM's `provenance.json` + checksummed `manifest.json` convention for `agwise-data` cache outputs — Andres / Lizeth, after intro
- [ ] Confirm the cropland-mask grid spec with Andres (0.00225° vs other multiple of 1/12000°; origin snapped from (0,0), not MODIS-tile aligned; country bbox, unclipped) against what `agwise-data` / `ag-cube-cm` resample to; then run the GCF WorldCover job `--grid` for Ghana (pilot) and host the COGs on CDH — Andres / CDH Technical Team

### Data assets for the hub

Per-dataset detail — access route actually implemented by `agwise-data`, authentication, transfer granularity, licence, live-probe result (2026-10-07) and proposed integration lead — lives in the [ingestion queue](./data/ingestion-queue.csv) (rolled into the tracker's `Use-case matrix` sheet alongside the GCF and B4T queues) and the [dataset access analysis](./data-sourcing-access-analysis.md). Rows already on the tracker's `Priority Data` sheet (AgERA5, CHIRPS v3, CHIRTS, NASA POWER, World Bank Admin Boundaries) are not duplicated; they get `AgWise` added to their Use Case column.

| Dataset | Hub status | Hub catalog | Feasibility (1=easy, 5=hard) | Serves | Notes |
| ------- | ---------- | ----------- | ---------------------------- | ------ | ----- |
| CHIRPS v2.0 (daily COG / GEE) | scoped | _pending_ | 2 | Precipitation (RAIN) for DSSAT | Workflow default; small domains via COG windows or GEE, large domains download ~1.1 GB global yearly NetCDF. No auth for CHC routes; GEE fallback needs credentials. Version decision vs v3 open (see actions) |
| CHIRPS v3 (on Priority Data) | published | [catalog](https://cgiar-climate-data-hub.github.io/catalog/chirps-v3-daily/) | 1 | Precipitation (RAIN) for DSSAT | Staged on CGLabs 1981–2025; workflow has no network path for v3 |
| CHIRTS (on Priority Data) | published | [catalog](https://cgiar-climate-data-hub.github.io/catalog/chirts-era5-daily/) | 1 | Temperature (TMAX, TMIN) for DSSAT | Daily Tmax/Tmin; 0.05° resolution; no auth required; values in K, converted to °C. In the brief but not in `agwise-data`, which takes temperature from AgERA5 |
| AgERA5 (on Priority Data) | scoped | _pending_ | 2 | SRAD, TMAX, TMIN, RHUM, wind for DSSAT | 0.1° resolution; CDS token required; staged yearly NetCDF read first, else CDS API bbox request; CDS licence CC-BY |
| ECMWF SEAS5 (system 51) | scoped | _pending_ | 2 | Seasonal forecast PRCP, TMAX, TMIN, TEMP, SRAD | CDS API, bbox subset; relationship to Jemal's Climate API _TBC_ |
| SoilGrids 2.0 | scoped | _pending_ | 2 | Soil inputs for DSSAT (.SOL) | OGC WCS regional subsets (≤ 2° chunks) or staged depth rasters; CC BY 4.0; "unclaimed common asset" in the CDH integration priorities — AgWise claims it |
| iSDAsoil v0.13 | scoped | _pending_ | 3 | Alternative soil inputs (Africa) | Local staged Africa-wide rasters only; provider API is key-gated and point-based; staging decision open |
| MODIS MOD13Q1 / MYD13Q1 | scoped | _pending_ | 2 | NDVI, EVI | Earth Engine `computePixels` by bbox; GEE credentials + Cloud project |
| ESA WorldCover 2021 (cropland fraction) | scoped | _pending_ | 2 | Cropland mask for pixel selection | Today derived server-side in GEE. The GCF WorldCover job now emits it as a per-country COG (`--grid`: 0.00225° ≈ 250 m and 1 km, class 40 fraction, 2021 v200; Togo verified 2026-10-07) → derive-then-host on CDH, GEE as fallback. Grid origin is not MODIS-tile aligned; confirm resample with Andres. CC BY 4.0 |
| Copernicus DEM GLO-30 | scoped | _pending_ | 1 | Elevation, slope, aspect, TPI, TRI | Public AWS COG tiles, range reads, no auth; Africa tiles also staged on CGLabs |
| geoBoundaries (gbOpen) | scoped | _pending_ | 1 | AOI definition / clipping | Per-country, per-level GeoJSON via API; per-layer licences vary; align with Hub boundary standard (WB / GAUL) |
| Climate API (Jemal) | scoped | _pending_ | _TBC_ | Seasonal forecast inputs | Endpoint, licence, access model and update frequency _TBC_; not wired into `agwise-data` |
| PRISM / `prismpy` (tool) | scoped | _pending_ | 2 | Provenance-tracked input packages for CRAFT, PYTHIA, ACEA, SARRA-Py | Software record, not a dataset. Candidate consumer of CDH-federated SoilGrids / CHIRPS / AgERA5; candidate STAC catalog user for package metadata |

### Methodological guidance needed

- [ ]

### Skills & tools

- **ag-cube-cm** Python package — spatial NetCDF/Zarr datacube processing and pixel-level DSSAT orchestration; supports `full_pipeline` (download → build → simulate) and `with_cubes` (simulate from existing cubes) modes
- **aggeodata** Python package — climate and soil data download and datacube assembly; integrates CHIRPS, CHIRTS, AgERA5, NASA POWER, GEE, and SoilGrids
- **agwise-data** Python package ([byliz-ai/data_sourcing](https://github.com/byliz-ai/data_sourcing), MIT) — catalog → driver → harmonise → shared cache on CGLabs for CHIRPS, AgERA5, SEAS5, SoilGrids, iSDA, Copernicus DEM, MODIS, ESA WorldCover and geoBoundaries; R wrappers, CLI and Claude Code driven; writes DSSAT/APSIM inputs. Relationship to `ag-cube-cm` / `aggeodata` _TBC_
- **`/spatial-crop-modeler`** AI agent skill ([CGIAR CDH skills repo](https://github.com/CGIAR-Climate-Data-Hub/skills/tree/main/.agents/skills/spatial-crop-modeler)) — end-to-end orchestration: environment check, YAML config generation, simulation execution, quality gate (ok/failed/no-data pixel audit), and HWAM result interpretation
- Climate API (Jemal) — seasonal forecast inputs; to be integrated into the pipeline

### Delivery mechanism

CDH-managed data storage; integrated data pipeline and MCP/skill.

## Meetings & decisions

| Date | Attendees | Summary | Decisions | Recording / transcript |
| ---- | --------- | ------- | --------- | ---------------------- |
| 2026-05-21 | Andres Aguilar Ariza, Diego Agudelo, Jemal Seid Ahmed | Jemal presented forecast API; discussed AWS migration, data access model, and Ghana pilot | Ghana pilot agreed; CDH metadata v1 to be shared; follow-up meeting to be scheduled | OneNote (CDH SharePoint) |

## Risks & open questions

- **Two overlapping data layers.** The brief describes `ag-cube-cm` + `aggeodata`; the live CGLabs workflow is `agwise-data` (`byliz-ai/data_sourcing`). Whether one supersedes the other is _TBC_; the inventories differ (CHIRTS and NASA POWER only in the former; SEAS5, iSDA, MODIS, WorldCover, DEM, geoBoundaries only in the latter).
- **Bulk-download paths.** CHIRPS v2 large-domain/fallback route downloads ~1.1 GB global yearly NetCDF then crops; CHIRPS v3 and iSDA require Africa-wide or global files staged locally with no network path. CDH must decide host vs federate vs subsetting service for each.
- **Credential dependencies.** AgERA5 and SEAS5 need a CDS token; MODIS, WorldCover and the CHIRPS GEE fallback need Earth Engine credentials and a Google Cloud project. The brief's "no auth" for CHIRPS holds only for the CHC COG/NetCDF routes.
- **Boundaries.** AgWise uses geoBoundaries; the Hub is standardising on World Bank boundaries / GAUL. Mixed boundary sets will break joins with other use-cases.
- **Climate API scope.** Until Jemal's endpoint and docs are shared, it is unclear whether it duplicates the SEAS5 CDS route.
- **Parallel Alliance stacks.** `agwise-data` (AgWise) and `prismpy` (PRISM, CIAT Dakar) both implement retrieve → harmonise for crop-model inputs, with overlapping providers (AgERA5, iSDA), different source sets otherwise, and no shared cache. Without coordination the Alliance maintains two pipelines and CDH federates the same datasets twice. `prismpy` repo currently carries no LICENSE file despite the paper's MIT statement.

## Outputs

> _Section fills in once status reaches `piloting` or beyond._

- **Deliverables:** _TBD_
- **Adoption signals:** _TBD_
- **Lessons learned:** _TBD_
