---
# === Identity ===
title: S4I Zambia Mechanization - Climate Risk Inputs for Credit Scoring
description: Admin2 climate-hazard indicators (observed year-by-year and projected) for Zambia's maize season, feeding a climate credit scoring model and service-provider risk profiles for financial institutions under CGIAR Scaling for Impact.
science_program: Scaling for Impact (S4I)

# === Lifecycle ===
type: new                            # new | existing
origin: ongoing-project              # ongoing-project | funding-pipeline | data-gap
status: brief                        # idea | brief | active-development | piloting | handover | complete | on-hold | no-go

# === Go / No Go ===
go_no_go:
  decision: pending                  # pending | go | no-go | on-hold
  date:                              # YYYY-MM-DD when decided
  decided_by:                        # e.g. "CDH Core Team"
  notes:

# === People ===
champion: "Shalika Vyas"             # Single named person (display name); domain owner
coordinator: "Peter Steward"         # Single named person (display name); connector / facilitator
task_group: ["Pedro Chilambe"]

# === CA-OS linkage ===
primary_aow:                         # AoW0-Orchestrate | AoW1-Accelerate | AoW2-Adapt | AoW3-Empower | AoW4-Transition | AoW5-Finance
related_aows: []
ca_os_packages: []

# === Metadata ===
tags: [s4i, zambia, mechanization, credit-scoring, hazards, maize, admin2, financial-institutions]
updated: 2026-10-28
---

> Cut admin2 (GAUL) climate-hazard indicators for Zambia's maize season — observed year-by-year and projected — from the Adaptation Atlas hazards pipeline, so the S4I Zambia mechanization team can estimate how often bad seasons occur and feed a climate credit scoring model and service-provider risk profiles for financial institutions.

## Brief

### Background & rationale

On 2026-10-26 Shalika Vyas asked where to download "admin 2 or gridded files for climate indicators heat stress etc for zambia" for "some zambia analysis im doing with pedro", noting the Adaptation Atlas "doesnt allow beyond admin 1". The Atlas climate view is built at admin0/admin1 only; admin2 hazard × exposure tables and 0.25° gridded indices exist on the public `digital-atlas` S3 bucket. Pete sent a handover note the same day ([HANDOVER_2026-10-26_zambia-admin2-gridded-access.md](https://github.com/AdaptationAtlas/hazards_prototype/blob/develop/HANDOVER_2026-10-26_zambia-admin2-gridded-access.md)) and Shalika pulled the admin2 hazard × exposure and raw-index tables from it.

On 2026-10-28 she specified what is still needed. For the log: "this is for the CGIAR Scaling for Impact (S4I) Zambia mechanization work. The end product feeds into a climate credit scoring model and service provider risk profiles for financial institutions."

The request (quoted from the 2026-10-28 message):

- **Indicators:** "maize heat stress (NTxM), NDWS (dry), PTOT-L (low rainfall), PTOT-G (wet) and NDWL0 (waterlogging)", "clipped to Zambia at admin2 (GAUL)".
- **Historical:** "ideally observed **year-by-year** values (e.g. 2000–2025, CHIRPS/CHIRTS-based) rather than a period mean. We want to estimate how often bad seasons occur and compare against survey-reported losses over the last five seasons. If NTxM or NDWS can't be produced from observed data at admin2, let me know which ones can."
- **Season window:** "the maize growing season (Nov–Apr) rather than calendar years, if possible."
- **Projections:** "SSP2-4.5 and SSP5-8.5, 2021–2040, at admin2."
- **Also helpful:** "the .json definitions/thresholds for each indicator, and the risk layers (share of years above threshold) if available."

This is a CDH data-delivery use-case: the hazards pipeline already produces most of these products Africa-wide; the gap is observed year-by-year seasonal indices at admin2, which are not published.

### Objectives

- Deliver the five indicators for Zambia at GAUL admin2 for SSP2-4.5 and SSP5-8.5, 2021–2040, with the `.json` indicator definitions/thresholds and the share-of-years-above-threshold risk layers.
- Establish which of the five can be produced as observed year-by-year (2000–2025) Nov–Apr season values at admin2 from CHIRPS/CHIRTS, produce those, and state clearly which cannot.
- Publish the cut as a documented, re-usable Hub product (S3 keys + sidecar metadata) rather than a one-off file transfer, so other Zambia and credit-scoring work can reuse it.
- Record the S4I Zambia mechanization climate credit scoring model as a CDH downstream use, including how survey-reported losses are compared against the hazard series.

### People involved

| Name | Organisation | Role |
| ---- | ------------ | ---- |
| Shalika Vyas | Alliance Bioversity-CIAT | Champion; S4I Zambia mechanization analysis |
| Pedro Chilambe | Alliance Bioversity-CIAT | Zambia analysis with Shalika |
| Peter Steward | Alliance Bioversity-CIAT | Coordinator; Atlas hazards pipeline / CDH |
| _TBC_ | _TBC_ | Financial-institution partners consuming the credit scoring model |

### Key dates

| Date | Milestone |
| ---- | --------- |
| 2026-10-26 | Shalika asks for admin2 / gridded Zambia climate indicators; Pete sends the S3 handover note (admin2 hazard × exposure parquet, 0.25° rasters, observed monthly COGs) |
| 2026-10-28 | Shalika pulls admin2 hazard × exposure and raw-index tables; specifies the cut (5 indicators, admin2 GAUL, observed year-by-year Nov–Apr 2000–2025, SSP2-4.5 / SSP5-8.5 2021–2040, thresholds, risk layers); names the project |
| _TBC_ | Feasibility answer on observed year-by-year NTxM / NDWS at admin2 |
| _TBC_ | Cut delivered and logged on the Hub |

### Background materials

- [Zambia admin2 + gridded access handover](https://github.com/AdaptationAtlas/hazards_prototype/blob/develop/HANDOVER_2026-10-26_zambia-admin2-gridded-access.md) — S3 keys, caveats, DuckDB / R snippets (Pete, 2026-10-26)
- [Teams chat Pete ↔ Shalika](https://teams.microsoft.com/l/chat/19:1dd1721f-d6b3-4cc1-95c4-e4379b8bc388_b79973a1-2c9c-4c98-a9fe-229ee0f9f780@unq.gbl.spaces/conversations?context=%7B%22contextType%22%3A%22chat%22%7D) — request and specification, 2026-10-26 / 2026-10-28
- [Adaptation Atlas hazards pipeline](https://github.com/AdaptationAtlas/hazards_prototype) — source of the admin2 tables and gridded indices
- S4I Zambia mechanization project documents — _TBC_ (OneDrive `Climate_data_hub/use_cases/s4i-zambia-mechanization/`)

## Go / No Go

> _Filled in by the CDH Core Team after the brief is developed._

- **Decision:** _pending_
- **Date:** _TBC_
- **Decided by:** _TBC_
- **Notes:** Low-cost data-delivery case on an existing pipeline; the only new processing is observed seasonal year-by-year indices at admin2.

## Action plan

> _Required once status reaches `active-development`._

### Actions

- [ ] Confirm which of NTxM, NDWS, PTOT-L, PTOT-G, NDWL0 can be computed observed year-by-year (2000–2025) at admin2 for a Nov–Apr season from CHIRPS v3 / CHIRTS-ERA5; reply to Shalika — Pete / hazards pipeline
- [ ] Cut the projected indicators (SSP2-4.5, SSP5-8.5, 2021–2040) at GAUL admin2 for Zambia, raw index not exposure-weighted, plus share-of-years-above-threshold risk layers — Pete / hazards pipeline
- [ ] Share the `.json` indicator definitions / thresholds (the parquet sidecars) — Pete
- [ ] Shalika to share the survey admin units, the five survey seasons, and the loss variables so the hazard series can be aligned — Shalika
- [ ] Publish the cut under a documented S3 prefix with sidecar metadata and log it in the ingestion matrix — CDH Technical Team
- [ ] CDH Core Team Go / No-Go — CDH Core Team

### Data assets for the hub

| Dataset | Hub status | Hub catalog | Feasibility (1=easy, 5=hard) | Serves | Notes |
| ------- | ---------- | ----------- | ---------------------------- | ------ | ----- |
| Atlas admin2 hazard × exposure (NEX-GDDP-CMIP6, GAUL 2024 admin2, Oct 2026 bake) | published (S3) | _pending_ | 1 | Projected hazard frequency by admin2 × crop | Already pulled by Shalika. Exposure-weighted (USD / ha / t / head), not raw index; `severe` / `moderate` / `extreme` tiers; ENSEMBLEmean of 18 GCMs; `.json` sidecar per file |
| Atlas admin2 raw-index means (`haz_means_adm2.parquet`, 2024 bake) | published (S3) | _pending_ | 1 | Projected raw-index means, SSP2-4.5 / SSP5-8.5, 2021–2040 | 2024 bake: indicative, will not reconcile exactly with the Oct 2026 admin2 tables; current-vintage rasters not yet published |
| Zambia admin2 projected indicator cut (NTxM, NDWS, PTOT-L, PTOT-G, NDWL0; SSP2-4.5 / SSP5-8.5; 2021–2040; raw index + risk layers) | scoped | _pending_ | 2 | Credit scoring model inputs (projected) | New cut from the processing server; season window Nov–Apr vs annual / Jägermeyr calendar _TBC_ |
| Zambia admin2 observed year-by-year season indices (2000–2025, Nov–Apr, CHIRPS v3 / CHIRTS-ERA5) | scoped | _pending_ | 3 | Bad-season frequency vs survey-reported losses | No observed admin2 product is published; needs new processing. Which of the five indicators are feasible from observed data is _TBC_ |
| CHIRPS v3 daily precipitation | published | [catalog](https://cgiar-climate-data-hub.github.io/catalog/chirps-v3-daily/) | 1 | Observed PTOT-L, PTOT-G, NDWS, NDWL0 | Africa-wide monthly PTOT / SPEI COGs also on S3 |
| CHIRTS-ERA5 daily Tmax / Tmin | published | [catalog](https://cgiar-climate-data-hub.github.io/catalog/chirts-era5-daily/) | 1 | Observed NTxM (maize heat stress) | Temporal coverage to 2025 _TBC_ |

_Hub status: `scoped → planned → in-progress → published`._

### Methodological guidance needed

- [ ] Season definition — Pete / Shalika — Nov–Apr fixed window vs crop-calendar (Jägermeyr) window; the published projections use annual or Jägermeyr windows, not Nov–Apr
- [ ] Observed NTxM threshold — Pete — maize-specific NTxM thresholds come from the projection pipeline's `.json`; confirm they apply unchanged to observed CHIRTS Tmax
- [ ] Bake consistency — Pete — projected admin2 values from the Oct 2026 tables vs 2024 rasters differ; state which vintage the cut uses
- [ ] Credit-scoring use — Shalika — how hazard frequency enters the scoring model, so the delivered variables match (e.g. share of years above threshold vs mean index)

### Skills & tools

- Adaptation Atlas hazards pipeline (`hazards_prototype`) — admin2 hazard × exposure, gridded indices, observed CHIRPS / CHIRTS products
- Public `digital-atlas` S3 bucket — anonymous HTTPS reads; DuckDB (`httpfs`) and R `terra` / `vsicurl` snippets in the handover note
- GAUL 2024 admin2 boundaries (Atlas analysis-ready parquet) — the join target; survey units _TBC_

### Delivery mechanism

Documented S3 prefix on the `digital-atlas` bucket (parquet + `.json` sidecar), referenced from the handover note; Hub catalog record _TBC_.

## Meetings & decisions

| Date | Attendees | Summary | Decisions | Recording / transcript |
| ---- | --------- | ------- | --------- | ---------------------- |
| 2026-10-26 | Shalika Vyas, Peter Steward (Teams chat) | Shalika asks for admin2 / gridded Zambia indicators; Pete explains the Atlas admin1 limit and sends S3 handover | Use the public S3 products; Pete to cut current layers on request | Teams chat (link above) |
| 2026-10-28 | Shalika Vyas, Peter Steward (Teams chat) | Shalika confirms the tables pulled and specifies the cut; names the S4I Zambia mechanization project and the credit-scoring end use | Log as CDH use-case | Teams chat (link above) |

## Risks & open questions

- **Risk / open question:** Observed year-by-year NTxM and NDWS at admin2 may not be producible from the current observed products (no observed admin2 product published). **Owner:** Pete **Status:** Open
- **Risk / open question:** Two vintages in play — Oct 2026 admin2 tables vs 2024 gridded rasters — give non-reconciling admin2 values. **Owner:** Pete **Status:** Open
- **Risk / open question:** Nov–Apr season window is not a published window (annual / Jägermeyr only); custom window needs a new run. **Owner:** Pete **Status:** Open
- **Risk / open question:** Survey admin units vs GAUL 2024 admin2 may not match; the Hub boundary standard (World Bank / GAUL) decision is pending across use-cases. **Owner:** Shalika / CDH **Status:** Open
- **Risk / open question:** Financial-institution partners and the credit scoring model's owner are not yet named; adoption pathway _TBC_. **Owner:** Shalika **Status:** Open

## Outputs

> _Section fills in once status reaches `piloting` or beyond. Empty until then._

- **Deliverables:** _TBC_
- **Adoption signals:** _TBC_
- **Lessons learned:** _TBC_
