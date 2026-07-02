---
# === Identity ===
title: B4T - Climate and Environmental Crop Risk Index (CRI)
description: Clarify, audit, and update the B4T Climate and Environmental Crop Risk Index so its hazard inputs, scoring logic, and prioritization role are methodologically defensible and use current climate data where feasible.
science_program: Breeding for Tomorrow

# === Lifecycle ===
type: existing                       # new | existing
origin: ongoing-project              # ongoing-project | funding-pipeline | data-gap
status: brief                        # idea | brief | active-development | piloting | handover | complete | on-hold | no-go

# === Go / No Go ===
go_no_go:
  decision: pending                  # pending | go | no-go | on-hold
  date:                              # YYYY-MM-DD when decided
  decided_by:                        # e.g. "CDH Core Team"
  notes:

# === People ===
champion: "Bert Lenaerts (IRRI)"     # Single named person (display name); domain owner
coordinator: "Peter Steward (Alliance)" # Single named person (display name); connector / facilitator
task_group: ["Peter Steward", "Bert Lenaerts", "Gerdino Badayos"]

# === CA-OS linkage ===
primary_aow:                         # AoW0-Orchestrate | AoW1-Accelerate | AoW2-Adapt | AoW3-Empower | AoW4-Transition | AoW5-Finance
related_aows: []
ca_os_packages: []

# === Metadata ===
tags: [crop-risk-index, climate-hazard, breeding]
updated: 2026-06-30
---

> Review and support refinement of the Climate and Environmental Crop Risk Index (CRI), including its current hazard formulation, source datasets, and role in B4T crop-country-market prioritization.

## Brief

### Background & rationale

Current CRI documentation describes a hazard-risk workflow intended to "enable the quantification of expected yield changes in the future, facilitating benefit modelling." The formulation combines five hazards: drought (D), flooding (F), high temperature (T), changed rainfall (R), and salinity (S), alongside two vulnerability / moderating factors: soil water (W) and irrigation potential (I).

The present workflow is more explicit than current repo brief text suggested. Source documents state that hazard layers are:

- standardized to `EPSG:4326`
- forced to global extent
- masked using a `1%` crop-area cutoff from CROPGRIDS
- downscaled to `3 arc-minute (0.05 degree)` resolution
- converted to pseudoprobabilities on a `0-100` scale
- averaged within hazard type using a `50-50` present/future weighting
- binarized using a `90th percentile` cutoff

The downstream method then:

- scores hazard intensity and interactions (HII) from `1-5`
- scores crop coping capacity (CCC) from Ecocrop-derived crop tolerances
- combines HII and CCC into the final CRI
- uses CRI in a later step to estimate yield-change scenarios

Supplied documents also clarify where CDH review should focus. Current input stack mixes vintages, methods, and time horizons:

- legacy CCAFS / Thornton-style hazard layers from [Ericksen 2011 CCAFS report (SharePoint)](https://cgiar.sharepoint.com/:b:/r/sites/CGIARClimate_data_hub/Shared%20Documents/use_cases/B4T/ccafsreport5-climate_hotspots_final.pdf?csf=1&web=1&e=KVBdit), including historic drought/flood proxies and 2050 threshold-flip layers for changed rainfall and temperature
- Aqueduct 4.0 and Aqueduct Floods layers centred on `2030`
- high-temperature layers from Tuholske et al. covering `1983-2016`
- salinity layers with `1970-2005` and `1986-2016` reference periods

This means CRI currently mixes historic proxies, 2030 water-risk layers, and 2050 climate-threshold layers in one score. Email notes from 2026-04-29 and 2026-04-30 explicitly flag pre-CMIP5 / CMIP5 lineage, inconsistent horizons, and uncertainty about exact provenance of some inherited layers.

HII methodology also needs careful handling. Current methods note says LLMs were used first to draft hazard-interaction scores, then literature review and expert consultation were used to adjust them. The supplied HII matrix still contains many entries marked `Extrapolation from literatures` or expert opinion, so provenance and validation depth remain central questions.

The `Crop x region priority- 2025.xlsx` workbook shows why this matters operationally. Climate risk is already one of three country prioritization indicators (`Population affected by Climate change`), and value propositions include `Farmer - Less Loss & Risk - CC relevant stress`. CRI therefore sits not only as background analysis, but as potential input to B4T prioritization and breeding-segmentation decisions.

CDH role for now is not to redesign CRI from scratch. Near-term job is to reconstruct current formulation precisely, identify what is defensible, isolate what is outdated or weakly evidenced, and propose practical upgrade options.

### Objectives

- Reconstruct exact current CRI formulation from B4T source documents, including hazard preprocessing, HII scoring, CCC scoring, and yield-response assumptions.
- Audit current CRI hazard, exposure, and vulnerability inputs by source year, model lineage, spatial resolution, and time horizon.
- Identify priority dataset upgrades, especially where legacy CCAFS / CMIP5-era inputs can be replaced by more current alternatives.
- Propose harmonization rules for future horizons and scenario logic before swapping datasets piecemeal.
- Review HII matrix provenance, distinguishing literature-backed, expert-adjusted, and extrapolated entries.
- Clarify how CRI outputs are meant to feed B4T crop-country-market prioritization and breeding value propositions.
- Co-produce updated CRI methods documentation once scope and update path are agreed.

### People involved

| Name | Organisation | Role |
| ---- | ------------ | ---- |
| Bert Lenaerts | IRRI | Champion; domain owner |
| Peter Steward | Alliance | Use case lead; coordinator |
| Gerdino Badayos | IRRI | Consultant |

### Key dates

| Date | Milestone |
| ---- | --------- |
| 2026-04-29 | Bert shares hazard data sources, current weighting logic, and known concerns about outdated inputs. |
| 2026-04-30 | Bert relays Philip Thornton notes on inherited drought, flood, and future hazard definitions. |
| 2026-05-08 | CDH outreach email circulated to reviewers with request for critique of CRI method and data choices. |
| 2026-05-15 | Expert review feedback deadline (Peter Steward outreach round) |
| TBD | CDH and B4T confirm current CRI processing chain against working files / scripts. |
| TBD | CDH proposes hazard-by-hazard update and harmonization options. |
| TBD | CDH and B4T agree whether to revise only inputs, or also selected scoring / aggregation rules. |
| TBD | Updated methods note and implementation plan completed. |

### Background materials

- [CRI draft paper (CGSpace)](https://cgspace.cgiar.org/items/2a1d0acb-2e0c-48fc-8b39-56e5899ba16c) — Climate and Environmental Crop Risk Index, draft publication
- [Crop Risk Index documentation v1 (SharePoint)](https://cgiar.sharepoint.com/:b:/r/sites/CGIARClimate_data_hub/Shared%20Documents/use_cases/B4T/Crop%20Risk%20Index-documentation%20v1.pdf?csf=1&web=1&e=JQkPsr) — Full methodology documentation
- [Ericksen 2011 CCAFS report (SharePoint)](https://cgiar.sharepoint.com/:b:/r/sites/CGIARClimate_data_hub/Shared%20Documents/use_cases/B4T/ccafsreport5-climate_hotspots_final.pdf?csf=1&web=1&e=KVBdit) — Mapping hotspots of climate change and food insecurity in the global tropics
- [HII scoring matrix (SharePoint)](https://cgiar.sharepoint.com/:b:/r/sites/CGIARClimate_data_hub/Shared%20Documents/use_cases/B4T/HII-scoring%20matrix.pdf?csf=1&web=1&e=rGr7fr) — Hazard Intensity and Interactions scoring matrix
- Crop x region priority- 2025.xlsx — B4T working prioritization workbook linking country, crop, and value-proposition relevance; shareable link _TBC_
- [Current CRI formulation note](./methods/current-cri-formulation.md) — Public-safe summary of current CRI workflow reconstructed from source documents
- [Dataset inventory](./methods/dataset-inventory.csv) — Hazard, soil-water, and irrigation input inventory with time horizons and upgrade flags
- [HII evidence audit seed](./methods/hii-evidence-audit.csv) — First-pass structured audit of selected HII rows by evidence type

## Go / No Go

> _Filled in by the CDH Core Team after the brief is developed._

- **Decision:** Pending
- **Date:** _TBD_
- **Decided by:** CDH Core Team
- **Notes:**

## Action plan

> _To be developed once status reaches `active-development`._

### Actions

- [ ] Reconstruct current CRI pipeline step-by-step from working documents, matrices, and any underlying scripts/files — CDH + B4T — establish exact baseline before proposing updates
- [ ] Build hazard-by-hazard inventory with source, reference period, scenario basis, processing method, and replacement options — CDH — focus first on D/F/R/T/S inputs
- [ ] Audit HII matrix entries for literature support, expert adjustment, or unsupported extrapolation — B4T + CDH — prioritize high-impact combinations and entries used in active crop geographies
- [ ] Trace where CRI outputs enter B4T country/crop/market-segment prioritization workflows — B4T — connect CRI revision work to actual decisions
- [ ] Draft update options note covering horizon harmonization, scenario alignment, and minimum viable improvements versus deeper redesign — CDH — frame decision for Go / No-Go discussion
- [ ] Co-develop revised methods note and implementation plan for agreed changes — CDH + B4T — only after baseline and scope are agreed

### Data assets for the hub

| Dataset | Hub status | Hub catalog | Feasibility (1=easy, 5=hard) | Serves | Notes |
| ------- | ---------- | ----------- | ---------------------------- | ------ | ----- |
| Legacy CCAFS / Thornton hazard layers (SPI, flood frequency, LGP / temperature threshold flips) | scoped | _pending_ | 3 | Current CRI hazard stack | Mix of historic proxies and 2050 threshold layers; provenance partly inherited via older CCAFS workflows |
| Aqueduct 4.0 water-risk layers | scoped | _pending_ | 2 | Drought / changed-rainfall replacement candidates | Current methods note cites 2030 blue water, gross demand, water stress, and variability layers |
| Aqueduct Floods river + coastal hazard layers | scoped | _pending_ | 2 | Flood update candidates | Current methods note cites 2030 flood layers forced by `RCP8.5` / ISIMIP-era inputs |
| CROPGRIDS harvested area | scoped | _pending_ | 1 | Exposure masking and crop weighting | Used with 1% physical pixel cutoff to mask non-crop areas |
| Ecocrop tolerance variables | scoped | _pending_ | 2 | Crop Coping Capacity | Crop-level tolerances do not represent within-crop varietal differences |
| HII scoring matrix + supporting references | scoped | _pending_ | 4 | Hazard interaction scoring | Many entries remain extrapolated and need provenance audit |

### Methodological guidance needed

- [ ] Hazard definitions and thresholds — CDH + B4T — confirm exact indicator formulas now in use versus descriptions in narrative documentation
- [ ] Time-horizon and scenario consistency — CDH — decide how to treat mixed historic / 2030 / 2050 inputs
- [ ] Aggregation logic — CDH + B4T — review whether 50-50 present/future weighting and 90th-percentile binarization remain fit for purpose
- [ ] HII evidence standard — B4T + CDH — decide what minimum literature / expert support is required for retaining interaction scores
- [ ] Crop specificity in CCC — B4T — assess whether crop-level Ecocrop tolerances are sufficient for breeding decisions involving distinct market segments or stress traits
- [ ] Link to breeding workflows — B4T + CDH — specify where CRI should inform trial environments, market segmentation, and value-proposition design
- [ ] Yield-response step — B4T + CDH — assess whether current expert + LLM averaging approach is acceptable for operational use

### Skills & tools

- Spatial hazard dataset audit and harmonization
- Literature-backed evidence review for interaction scoring
- Crop suitability / tolerance review using Ecocrop and breeding context
- Reproducible geospatial processing and methods documentation

### Delivery mechanism

Updated methods note, revised source inventory, and reproducible processing guidance for B4T / CDH implementation. Final delivery format beyond brief stage is _TBC_.

## Meetings & decisions

| Date | Attendees | Summary | Decisions | Recording / transcript |
| ---- | --------- | ------- | --------- | ---------------------- |
| 2026-04-29 | Bert Lenaerts, Peter Steward | Bert shares current CRI data sources, weighting logic, and concerns about outdated hazard inputs and mixed time horizons. | Need CDH / Climate Action review of current implementation. | Email thread |
| 2026-04-30 | Bert Lenaerts, Peter Steward | Bert relays Philip Thornton notes on current/past drought and flood proxies plus future hazard thresholds. | Legacy definitions need reconstruction before replacement planning. | Email thread |
| 2026-05-08 | Peter Steward | Email sent to external reviewers | Feedback requested by 2026-05-15 | Email thread |

## Risks & open questions

- **Risk / open question:** Exact provenance and reproducibility of some inherited hazard layers remains unclear. **Owner:** Bert Lenaerts / CDH **Status:** Open
- **Risk / open question:** Current CRI mixes historic, 2030, and 2050 layers in one score, which weakens comparability across hazards. **Owner:** CDH **Status:** Open
- **Risk / open question:** HII matrix contains many extrapolated entries and AI-assisted drafting history, so confidence is uneven across hazard combinations. **Owner:** B4T + CDH **Status:** Open
- **Risk / open question:** Current CCC scoring is crop-level and may be too coarse for varietal or market-segment decisions. **Owner:** B4T **Status:** Open
- **Risk / open question:** Yield-response step currently averages expert and LLM estimates; suitability for operational decision support is not yet established. **Owner:** B4T + CDH **Status:** Open

## Outputs

> _Section fills in once status reaches `piloting` or beyond._

- **Deliverables:** _TBD_
- **Adoption signals:** _TBD_
- **Lessons learned:** _TBD_
