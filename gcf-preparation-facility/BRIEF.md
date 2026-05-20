---
title: GCF Preparation Facility
description: Climate Rationale notebook auto-generating evidence-based climate risk narratives, hazard-exposure tables, and statistical summaries for Green Climate Fund proposal writers.

type: existing
origin: ongoing-project
status: active-development

go_no_go:
  decision: go
  date:
  decided_by: _TBC_
  notes: >-
    Implicit Go — this is an existing CAP bilateral asset (Atlas Climate Rationale v2) being showcased
    in the CGIAR Climate Data Hub; the formal CDH Core Team Go / No-Go decision has not yet been recorded.

champion: Cesare Scartozzi
coordinator: Peter Steward
task_group:
  - Peter Steward
  - Brayden Youngberg
  - Cesare Scartozzi
  - Majambo Gamoyo

primary_aow: AoW5-Finance
related_aows:
  - AoW1-Accelerate
  - AoW2-Adapt
ca_os_packages:
  - CA30
  - M2

tags:
  - gcf
  - climate-rationale
  - quarto
  - hazard-exposure

updated: 2026-05-19
---

# GCF Preparation Facility

> A Climate Rationale notebook that auto-generates evidence-based climate risk narratives, hazard-exposure tables, and statistical summaries to support Green Climate Fund (GCF) proposal writers. Existing CAP bilateral asset being showcased through the CGIAR Climate Data Hub.

## Brief

### Background & rationale

GCF proposals require a defensible climate rationale grounded in subnational climate and agricultural data — currently a slow, manual, and inconsistent process. CDH is building the **Atlas Climate Rationale v2** notebook (Quarto + Observable JS) on top of CDH data infrastructure to compress this work from weeks to hours while maintaining methodological transparency. The Togo SAT climate rationale (April 2025) is the reference gold standard.

### Objectives

- Enable GCF proposal writers to produce evidence-based climate rationales with minimal manual effort.
- Provide transparent methodological attribution (sources, baselines, ensemble methods).
- Generate publication-ready tables and figures — particularly the hazard-exposure matrix in the Togo SAT style.
- Support both non-technical users (proposal writers) and technical users (climate scientists).
- Integrate with the broader CGIAR Climate Data Hub architecture for long-term scaling.

### People involved

| Name | Organisation | Role |
| --- | --- | --- |
| Cesare Scartozzi | CGIAR / Alliance Bioversity-CIAT (CACC1) | Champion — sets GCF data requirements |
| Peter Steward | CGIAR / Alliance Bioversity-CIAT | Coordinator — climate adaptation analyst; driving handover |
| Brayden Youngberg | CGIAR / Alliance Bioversity-CIAT | Engineering co-author — selector architecture and data pipeline |
| Majambo Gamoyo | CGIAR / Alliance Bioversity-CIAT | End-user / partner — feedback on spatial mapping, admin-2 support, multi-region geometries |
| Harold | External consultant | Trend statistics (Mann-Kendall, Sen's slope) — deferred from current sprint |

### Key dates

| Date | Milestone |
| --- | --- |
| 2023-04 | Majambo CR Needs assessment (early user feedback) |
| 2025-04 | Togo SAT climate rationale published — reference gold standard |
| 2026-03 | Cesare Scartozzi GCF data-requirements memo |
| 2026-05-13 | Pete's code review + decision log finalised; handover materials published |

### Background materials

Canonical materials live in OneDrive at `Climate_data_hub/use_cases/gcf-preparation-facility/`. Not linkable from this public repo; reference paths below.

- **Claude Climate Rational Project README** — project handover brief, folder structure, PR workflow. `Claude Climate Rational Project/README.md`
- **DECISIONS.md** — seven resolved Q1–Q7 design decisions (selector design, temperature filters, SSP labelling, GCF links, French review, ensemble size). `Claude Climate Rational Project/DECISIONS.md`
- **ISSUES.md** — 45-issue backlog grouped into 11 PRs (A–K) with landing order. `Claude Climate Rational Project/ISSUES.md`
- **Pete's walkthrough notes** — spoken observations from the live notebook; why behind each issue. `Claude Climate Rational Project/context/03_petes_walkthrough_notes.md`
- **GCF Data Notebook Memo (Cesare Scartozzi, 2026.03)** — GCF data requirements and use-case framing. `Background Materials/2026.03 - GCF_Data_Notebook_Memo - Cesare Scartozzi.docx`
- **Togo SAT climate risk analysis (2025-04)** — visual reference for target outputs (Table 5, Figure 5). `Background Materials/Togo_SAT_climate risk_risk_analysis_Updated_24042025.pdf`
- **Majambo CR Needs (2023-04)** — user feedback on spatial mapping and admin-2 polygons. `Background Materials/2023.04 - Majambo CR Needs.docx`

## Go / No Go

- **Decision:** Go (implicit)
- **Date:** _TBC_ — formal CDH Core Team decision not yet recorded
- **Decided by:** _TBC_
- **Notes:** This is an existing CAP bilateral asset already in active development. Formal Go / No-Go is being treated as a retroactive bookkeeping step rather than a real gate.

## Action plan

### Actions

- [x] Code review + decision log finalised — Peter Steward — completed 2026-05-13
- [ ] Lock selector architecture — Brayden Youngberg — blocks 3 PRs
- [ ] Dispatch 8 unblocked PRs via Claude Code — Peter Steward — ready
- [ ] Resolve HSH-max interpretation — Brayden Youngberg — open question
- [ ] Audit parquet inventory (canonical inputs vs legacy artefacts) — Brayden Youngberg — open question
- [ ] Review AI-drafted French translations — Peter Steward — pending
- [ ] Finalise methods appendix — Peter Steward — in draft
- [ ] Re-scope admin-2 support post-MVP — _TBC_ — deferred
- [ ] Slot Mann-Kendall / Sen's slope into a future sprint — _TBC_ — Harold engagement deferred

### Data assets for the hub

Datasets needed in (or federated with) the CDH catalog. Sources and section mapping derived from Cesare's GCF Data Notebook Memo (2026.03). Memo status column: **IN CR** = already in Atlas Climate Rationale notebook; **PARTIAL** = partially present, needs additions; **NEW** = not in CR.

| Dataset | Memo status | Hub status | Hub catalog | Feasibility (1=easy, 5=hard) | Serves | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| NEX-GDDP-CMIP6 (or CMIP6 / CORDEX) | IN CR | scoped | _pending_ | 2 | CN C.1 · FP B.1 — climate trends & projections | Bias-corrected daily downscaled, 0.25°, multi-GCM |
| ERA5 reanalysis | IN CR | scoped | _pending_ | 2 | CN C.1 · FP B.1 | Historical climate timeseries |
| CHIRPS | IN CR | scoped | _pending_ | 1 | CN C.1 · FP B.1 | Daily precipitation; already cloud-hosted |
| CHIRTS | IN CR | scoped | _pending_ | 1 | CN C.1 · FP B.1 | Daily temperature pair to CHIRPS |
| Section-1-derived z-score extremes | IN CR | scoped | _pending_ | 2 | CN C.1 · FP B.1, D.1 — extreme events | Derived in-notebook from Section 1 |
| MapSPAM 2020 | PARTIAL | scoped | _pending_ | 2 | CN C.1, C.2 · FP B.1, D.1 — crop hazard exposure | Crop production value layers |
| FAOSTAT | PARTIAL | scoped | _pending_ | 1 | CN C.1, C.2 · FP B.1 | National agricultural statistics |
| FAO GLEAM | PARTIAL | scoped | _pending_ | 3 | CN C.1, C.2 · FP B.1 — livestock exposure | New for this use-case |
| WRI Aqueduct | PARTIAL | scoped | _pending_ | 2 | CN C.1, C.2 · FP B.1 | Water-demand stress on irrigated systems |
| World Bank development indicators | PARTIAL | scoped | _pending_ | 1 | CN Exec Summary · FP D.4 | Poverty, GDP by sector, land use |
| ND-GAIN | PARTIAL | scoped | _pending_ | 1 | CN Exec Summary · FP D.4 | Composite vulnerability index |
| INFORM Risk | PARTIAL | scoped | _pending_ | 1 | CN Exec Summary · FP D.4 | Composite risk index |
| IPC / CH food insecurity | PARTIAL | scoped | _pending_ | 2 | CN Exec Summary · FP D.4 | Food insecurity prevalence |
| WHO / UNICEF JMP | PARTIAL | scoped | _pending_ | 1 | CN Exec Summary · FP D.4 | Water and WASH access |
| WorldPop | PARTIAL | scoped | _pending_ | 2 | CN Exec Summary · FP D.4 + A.6–A.7 | Population, gender-disaggregated |
| DHS / MICS | PARTIAL | scoped | _pending_ | 2 | CN Exec Summary · FP D.4 | Household surveys |
| UNFCCC NDC Registry | NEW | scoped | _pending_ | 3 | CN A.16 · FP D.5 — NDC / NAP alignment | NDC text extraction needed (Section 5 of memo) |
| NAP Central | NEW | scoped | _pending_ | 3 | CN A.16 · FP D.5 | NAP priority actions extraction |
| Climate Watch | NEW | scoped | _pending_ | 2 | CN A.16 · FP D.5 | Country climate commitments |
| GCF country programmes | NEW | scoped | _pending_ | 2 | CN A.16 · FP D.5 | Country programme priorities |
| IPCC default emission factors | NEW | scoped | _pending_ | 2 | CN A.6–A.7 · FP D.1, E.3 — beneficiary estimates | Tier 1 mitigation accounting |
| EX-ACT | NEW | scoped | _pending_ | 3 | CN A.6–A.7 · FP D.1, E.3 | Ex-ante carbon balance tool |
| Atlas yield gaps | NEW | scoped | _pending_ | 2 | CN A.6–A.7 · FP D.1, E.3 | Yield-gap layer for impact estimates |
| WOCAT | NEW | scoped | _pending_ | 2 | CN A.6–A.7 · FP D.1, E.3 | Sustainable land management practices |
| National census data | NEW | scoped | _pending_ | 4 | CN A.6–A.7 · FP D.1, E.3 | Per-country acquisition needed |
| GCF approved-project database | NEW | scoped | _pending_ | 2 | FP B.2, D.2 — theory of change / portfolio evidence | Filter to food / land / water result areas (T4, T5, T6) |
| CGIAR evidence maps | NEW | scoped | _pending_ | 3 | FP B.2, D.2 | Adaptation/mitigation evidence base |
| World Bank IEG evaluations | NEW | scoped | _pending_ | 2 | FP B.2, D.2 | Adjacent project evaluations |
| IFAD evaluations | NEW | scoped | _pending_ | 2 | FP B.2, D.2 | Smallholder finance evaluations |
| Cesare's MCF project dataset | NEW | scoped | _pending_ | 3 | FP B.2, D.2 + CN D.1–D.4 | Project-level multilateral climate finance |
| WDPA (protected areas) | NEW | scoped | _pending_ | 2 | CN C.4 · FP G.1–G.2 — safeguards | Project-zone overlay |
| IUCN Red List | NEW | scoped | _pending_ | 2 | CN C.4 · FP G.1–G.2 | Biodiversity hotspots |
| FAO Gender & Land Rights | NEW | scoped | _pending_ | 2 | CN C.4 · FP G.1–G.2 | Land tenure |
| OECD SIGI | NEW | scoped | _pending_ | 2 | CN C.4 · FP G.1–G.2 | Gender inequality index |
| World Bank CPIA | NEW | scoped | _pending_ | 2 | CN C.4 · FP G.1–G.2 | Country policy assessment |
| Climate Security Programming Dashboard (CSO) | NEW | scoped | _pending_ | 3 | CN C.4 | Climate security context |
| OECD DAC CRS | NEW | scoped | _pending_ | 2 | CN D.1–D.4 · FP B.5, C.1 — financial context | Climate finance flows |
| CPI landscape (Climate Policy Initiative) | NEW | scoped | _pending_ | 2 | CN D.1–D.4 | Adaptation finance gap |
| IMF fiscal data | NEW | scoped | _pending_ | 2 | CN D.1–D.4 | Fiscal space indicators |
| GAUL admin boundaries (2024) | IN CR | scoped | _pending_ | 1 | All sections | Admin-0 / admin-1 (admin-2 deferred) |

_Hub status vocabulary: `scoped → planned → in-progress → published`. The Hub catalog column becomes a live link once Brayden's STAC entry exists for each dataset._

### Methodological guidance needed

- [ ] **Mann-Kendall / Sen's slope trend statistics** — Harold (external) — deferred from current sprint; risk of methodological drift if not slotted into a future sprint
- [ ] **HSH-max interpretation** — Brayden Youngberg — open: what does the current implementation actually compute vs what was intended?
- [ ] **Parquet inventory** — Brayden Youngberg — which derived parquet files are canonical inputs vs legacy artefacts?
- [ ] **Admin-2 support** — _TBC_ — deferred post-MVP; known user ask from Majambo
- [ ] **HII matrix validation** — cross-link to B4T (Bert Lenaerts) — external peer review may be needed before publication

### Skills & tools

- Quarto + Observable JS notebooks
- Z-score classification of extreme temperature and precipitation events
- Warming stripes; multi-scenario projection visualisation
- Hazard × crop / livestock exposure intersection valued in USD
- French translation review workflow (AI-drafted → human review)
- STAC-aware dataset access (planned)

### Delivery mechanism

Quarto + Observable JS notebook served at <https://notebooks-climaterationale.adaptation-atlas-nb.pages.dev/>. Six analytical sections: Key Facts · Recent Changes · Future Projections · Extreme Events · Crop & Livestock Exposure · Summary. English / French toggle.

## Meetings & decisions

| Date | Attendees | Summary | Decisions | Recording / transcript |
| --- | --- | --- | --- | --- |
| 2026-04-29 | Peter Steward, Cesare Scartozzi, Brayden Youngberg | Implementation scope: get a usable v1 by August; federated S3 + STAC catalog + use-case wiki as MVP | Federate rather than mirror NEX-GDDP-CMIP6; Brayden owns the metadata standard | `Climate_data_hub/meetings/2026.04.29 - CDH GCF Use-case.docx` |
| 2026-03-17 | Peter Steward, Cesare Scartozzi, Bia Carneiro, Brayden Youngberg | CACC1 × CACC2 integration — repurpose the Atlas Climate Rationale notebook for the GCF pipeline | Short concept memo to follow from Cesare | `Climate_data_hub/meetings/2026.03.17 - GCF Use-case - CACC1 & CACC2 integration.docx` |

_Source of truth for transcripts: `Climate_data_hub/meetings/` in OneDrive._

## Risks & open questions

- **Selector architecture decision** — Brayden Youngberg — blocking 3 PRs
- **HSH-max interpretation** — Brayden Youngberg — what does the current implementation actually compute vs what was intended?
- **Parquet inventory** — Brayden Youngberg — which derived parquet files are canonical inputs vs legacy artefacts?
- **Admin-2 support** — deferred from current scope but a known user ask (Majambo); re-open after MVP
- **Trend statistics drift** — Mann-Kendall / Sen's slope work paused; Harold engagement deferred; risk of methodological drift if not slotted into a future sprint
- **NDC / NAP text extraction** — Section 5 of Cesare's memo is the highest-priority NEW data ingestion; non-trivial NLP work

## Outputs

> Status is `active-development`. The notebook is live and in use, but formal piloting / handover metrics have not yet been captured. This section fills in as the use-case progresses.

- **Deliverables in flight:** Climate Rationale v2 notebook (live), Key Facts and hazard-exposure exportable tables, methods appendix (in draft), French translations (AI-drafted, Pete-reviewed)
- **Adoption signals:** _TBC_ — track usage of the notebook for live GCF concept notes
- **Lessons learned:** _TBC_ — fill in at handover
