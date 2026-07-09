---
title: GCF Preparation Facility
description: Climate Rationale notebook auto-generating evidence-based climate risk narratives, hazard-exposure tables, and statistical summaries for Green Climate Fund proposal writers.
science_program: Critical Capacity (CACC2) — Climate Data & Innovations Hub

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
  - climate-finance

updated: 2026-07-09
---

> A Climate Rationale notebook that auto-generates evidence-based climate risk narratives, hazard-exposure tables, and statistical summaries to support Green Climate Fund (GCF) proposal writers. Existing CAP bilateral asset being showcased through the CGIAR Climate Data Hub.

## Brief

### Background & rationale

This use-case is a deliverable of **CACC2** — the CGIAR Climate Data & Innovations Hub, the Climate Action capability that builds shared, quality-assured climate-data infrastructure. It is designed to support **CACC1** — "Support the development of CGIAR's GCF portfolio", the capability that gives CGIAR Centers technical backstopping on climate rationale and proposal design (current engagements: Togo, Benin/Nigeria, Egypt, Zambia, Kenya). In short: CACC2 provides the shared data and tools; CACC1 puts them to work in GCF proposals.

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
| Cesare Scartozzi | CGIAR / Alliance Bioversity-CIAT — CACC1 (GCF portfolio) | Champion — sets GCF data requirements; first user |
| Peter Steward | CGIAR / Alliance Bioversity-CIAT — CACC2 (Climate Data Hub) | Coordinator — CDH Hub focal point; climate adaptation analyst |
| Brayden Youngberg | CGIAR / Alliance Bioversity-CIAT | Engineering co-author — selector architecture and data pipeline |
| Majambo Gamoyo | CGIAR / Alliance Bioversity-CIAT | End-user / partner — feedback on spatial mapping, admin-2 support, multi-region geometries |
| Harold | External consultant | Trend statistics (Mann-Kendall, Sen's slope) — deferred from current sprint |

### Key dates

| Date | Milestone |
| --- | --- |
| 2023-04 | Majambo CR Needs assessment (early user feedback; file dated 2023.04 but content cites NAP Expo 2025 — date _TBC_) |
| 2025-04 | Togo SAT climate rationale published — reference gold standard |
| 2026-01-31 | Cesare Scartozzi GCF data-requirements memo (document header date; filed in OneDrive as 2026.03) |
| 2026-05-13 | Pete's code review + decision log finalised; handover materials published |
| 2026-06-17 | Cesare delivers partial multilateral-climate-funds dataset (CSV, 5,115 projects: GEF 3,524 / GCF 936 / AF 250) + notebook concept |
| 2026-08 | Target: usable v1 — federated S3 datasets + metadata standard + catalog front end ("really optimistically", 2026-04-29 meeting) |

### Background materials

Canonical materials live in OneDrive at `Climate_data_hub/use_cases/gcf-preparation-facility/`. Not linkable from this public repo; reference paths below.

- **Claude Climate Rational Project README** — project handover brief, folder structure, PR workflow. `Claude Climate Rational Project/README.md`
- **DECISIONS.md** — seven resolved Q1–Q7 design decisions (selector design, temperature filters, SSP labelling, GCF links, French review, ensemble size). `Claude Climate Rational Project/DECISIONS.md`
- **ISSUES.md** — 45-issue backlog grouped into 11 PRs (A–K) with landing order. `Claude Climate Rational Project/ISSUES.md`
- **Pete's walkthrough notes** — spoken observations from the live notebook; why behind each issue. `Claude Climate Rational Project/context/03_petes_walkthrough_notes.md`
- **GCF Data Notebook Memo (Cesare Scartozzi, 2026.03)** — GCF data requirements and use-case framing. `Background Materials/2026.03 - GCF_Data_Notebook_Memo - Cesare Scartozzi.docx`
- **Togo SAT climate risk analysis (2025-04)** — visual reference for target outputs (Table 5, Figure 5). `Background Materials/Togo_SAT_climate risk_risk_analysis_Updated_24042025.pdf`
- **Majambo CR Needs (2023-04)** — user feedback on spatial mapping and admin-2 polygons. `Background Materials/2023.04 - Majambo CR Needs.docx`
- **Sample multilateral-climate-funds dataset (Cesare Scartozzi, 2026-06-17)** — partial CSV of the health/food/water-security investment pipeline across GEF, GCF, and Adaptation Fund; sector/theme/implementing-entity-type harmonised; final sub-classifiers to follow. `example dataset/projects_dis_by_country_fund.csv` + covering email.
- **GCF/B.33/05 "Steps to enhance the climate rationale of GCF-supported activities" (2022-06-24)** — GCF Board paper defining climate rationale and the four adaptation principles (Identification, Response, Alignment, M&E); policy basis for the notebook's outputs. `Background Materials/gcf-b33-05.pdf`
- **GCF Concept Note template v3.1** — section codes (A.1–A.17, C.1–C.5, D.1–D.4) that the memo's nine notebook sections map onto. `GCF_Concept note template_V.3.1.docx`
- **Data-in-GCF-Proposal database + synthesis deck** — indicators extracted from 10 real GCF proposals (Niger, Ghana, Mali, Malawi, Senegal ×2, Ethiopia, Kenya ×2, Zambia) classified Hazards / Vulnerability / Exposure / Solutions, mapped to decision-support tools. `Background Materials/2. Data-in-GCF-Proposal- CLEAN.xlsx`, `Background Materials/GCF data synthesis.pptx`

## Go / No Go

- **Decision:** Go (implicit)
- **Date:** _TBC_ — formal CDH Core Team decision not yet recorded
- **Decided by:** _TBC_
- **Notes:** This is an existing CAP bilateral asset already in active development. Formal Go / No-Go is being treated as a retroactive bookkeeping step rather than a real gate.

## Action plan

### Actions

- [x] Code review + decision log finalised — Peter Steward — completed 2026-05-13
- [x] Selector architecture (notebook side) — Peter Steward — resolved: one global sticky selector (DECISIONS.md Q1); cross-notebook adoption still with Brayden Youngberg
- [x] Fix-sweep sessions on Climate Rationale v2 — Peter Steward + Claude — 20+ cowork sessions 2026-05-14 → 2026-06-16; CR backlog worked through CR-122 (perf, baselines, extreme-event tails, exposure controls)
- [x] Review AI-drafted French translations — Peter Steward — production FR gaps zero as of 2026-06-16
- [ ] Resolve HSH-max interpretation — Brayden Youngberg — open question
- [ ] Audit parquet inventory (canonical inputs vs legacy artefacts) — Brayden Youngberg — open question
- [ ] Finalise methods appendix — Peter Steward — in draft
- [ ] Re-scope admin-2 support post-MVP — _TBC_ — deferred
- [ ] Slot Mann-Kendall / Sen's slope into a future sprint — _TBC_ — Harold engagement deferred
- [ ] Build interactive multilateral-climate-funds notebook — Cesare Scartozzi (Jupyter mock-up) → Brayden Youngberg (Quarto port, est. "a couple of days… a week maximum") — agreed 2026-04-29; partial dataset delivered 2026-06-17
- [ ] Finalise dataset sub-classifiers (project-intervention types) — Cesare Scartozzi — promised end June 2026; status _TBC_
- [ ] Upload original dataset to CGSpace / Harvard Dataverse for a DOI — Cesare Scartozzi — agreed 2026-04-29
- [ ] Use Cesare's dataset as first non-geospatial pilot of the CDH metadata standard — Brayden Youngberg — agreed 2026-04-29
- [ ] Mitigation data needs: engage L2 focal point (Augusto Castro — name garbled in transcript, _TBC_) — Cesare Scartozzi — from 2026-04-29 meeting
- [ ] Connect with Adaptation Insights on hazard ↔ solutions mapping — Peter Steward — from 2026-04-29 meeting
- [ ] Meet Cesare on notebook next steps — Peter Steward — Cesare requested "first half of July" (2026-06-17 email); due now

### Data assets for the hub

The full per-dataset audit — all ~40 datasets behind the nine notebook sections, with verified source URLs, **licences** (open → mirror-hostable vs non-commercial → federate/link only), and how each can be **summarised under a geoselector** or **reached by an AI skill** (federate vs rehost) — lives in the review page and evidence log, not here:

- **[Review page — Data tab](https://cgiar-climate-data-hub.github.io/use-cases/gcf-preparation-facility/gcf-prep-review.html)** — dataset detail per notebook section + the "Delivering the data" delivery-route analysis.
- **[Evidence log](./methods/evidence/sources.md)** — one entry per dataset: URL, licence, verification date, derived-products guidance.

Section-level summary (memo status: **IN CR** = already in the Climate Rationale notebook; **PARTIAL** = partly present, needs additions; **NEW** = not yet built; **DEPRIORITISED** = in the memo but since parked). All sections are currently at Hub status `scoped`.

| # | Notebook section | Serves (CN · FP) | Memo status | Feasibility (1=easy, 5=hard) |
| --- | --- | --- | --- | --- |
| 1 | Climate trends & projections | CN C.1 · FP B.1 | IN CR | 2 |
| 2 | Extreme events | CN C.1 · FP B.1, D.1 | IN CR | 2 |
| 3 | Crop & livestock hazard exposure | CN C.1, C.2 · FP B.1, D.1 | PARTIAL | 2–3 |
| 4 | Vulnerability & socioeconomic context | CN Exec Summary · FP D.4 | PARTIAL | 1–2 |
| 5 | NDC & NAP alignment | CN A.16 · FP D.5 | DEPRIORITISED | 3 |
| 6 | Impact potential & beneficiaries | CN A.6–A.7 · FP D.1, E.3 | NEW | 2–4 |
| 7 | Theory of change & GCF portfolio | FP B.2, D.2 | NEW | 2–3 |
| 8 | Safeguards & gender screening | CN C.4 · FP G.1–G.2 | NEW | 2 |
| 9 | Financial context & justification | CN D.1–D.4 · FP B.5, C.1 | NEW | 2 |
| — | Admin boundaries (GAUL 2024) | all sections | IN CR | 1 |

_Hub status vocabulary: `scoped → planned → in-progress → published`. Per-dataset hub status and the eventual STAC catalog links are tracked in the evidence log._

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
| 2026-06-17 | Cesare Scartozzi → Peter Steward, Brayden Youngberg (email) | Partial multilateral-climate-funds dataset delivered (CSV, 5,115 projects); notebook concept: "allow users to select one or multiple countries to see past and ongoing investment pipelines, so that they can identify gaps, complementary projects, or examples for project development" | Share incomplete dataset now, final sub-classifiers end June; meet first half of July | `use_cases/gcf-preparation-facility/example dataset/` |
| 2026-04-29 | Peter Steward, Cesare Scartozzi, Brayden Youngberg | Implementation scope: get a usable v1 by August; federated S3 + STAC catalog + use-case wiki as MVP. Cesare demoed the MCF SQL dataset (~2,100 projects, 15k documents); agreed to turn it into an Atlas-style interactive notebook (Cesare Jupyter → Brayden Quarto). NAP/NDC automation withdrawn by Cesare | Federate rather than mirror NEX-GDDP-CMIP6; Brayden owns the metadata standard; dataset = first non-geospatial metadata pilot; DOI via CGSpace/Dataverse | `Climate_data_hub/meetings/2026.04.29 - CDH GCF Use-case.docx` |
| 2026-03-17 | Peter Steward, Cesare Scartozzi, Bia Carneiro, Brayden Youngberg | CACC1 × CACC2 integration — repurpose the Atlas Climate Rationale notebook for the GCF pipeline | Short concept memo to follow from Cesare | `Climate_data_hub/meetings/2026.03.17 - GCF Use-case - CACC1 & CACC2 integration.docx` |

_Source of truth for transcripts: `Climate_data_hub/meetings/` in OneDrive._

## Risks & open questions

- **Geographic coverage** — crop-exposure pipeline is Sub-Saharan Africa only (MapSPAM SSA); Cesare calls this "the biggest limitation" — target is all non-Annex-I countries; active GCF pipeline includes Syria, Iraq, Sri Lanka, Egypt. **Owner:** _TBC_ **Status:** open
- **Hazard ↔ solutions mapping gap** — Cesare: what would be "super useful… that we don't have" is a mapping of CGIAR-deliverable climate solutions to hazards/vulnerability; a prior GPT-generated attempt fabricated references. Route via Adaptation Insights. **Owner:** Peter Steward **Status:** open
- **HSH-max interpretation** — Brayden Youngberg — what does the current implementation actually compute vs what was intended?
- **Parquet inventory** — Brayden Youngberg — which derived parquet files are canonical inputs vs legacy artefacts?
- **Admin-2 support** — deferred from current scope but a known user ask (Majambo); re-open after MVP
- **Trend statistics drift** — Mann-Kendall / Sen's slope work paused; Harold engagement deferred; risk of methodological drift if not slotted into a future sprint
- **NDC / NAP text extraction** — was the memo's highest-priority NEW ingestion, but deprioritised 2026-04-29: Cesare withdrew the ask (corpus too small to justify automation); revisit only if demand recurs
- **Overlapping external products** — climateprojectexplorer.org (the funds' own explorer) and data.unfccc.int launched while the dataset was in preparation; CDH offer must stay differentiated (harmonised metadata, FLW focus, notebook analytics). **Owner:** Cesare Scartozzi **Status:** watching

## Outputs

> Status is `active-development`. The notebook is live and in use, but formal piloting / handover metrics have not yet been captured. This section fills in as the use-case progresses.

- **Deliverables in flight:** Climate Rationale v2 notebook (live; 20+ fix-sweep sessions to 2026-06-16), Key Facts and hazard-exposure exportable tables, methods appendix (in draft), French translations (complete — zero production FR gaps as of 2026-06-16), multilateral-climate-funds pipeline notebook (partial dataset in hand; notebook not started)
- **Use-case review page (DRAFT):** [GCF Preparation Facility — data, skills & notebook review](https://cgiar-climate-data-hub.github.io/use-cases/gcf-preparation-facility/gcf-prep-review.html) — three tabs (Data / Skills / Notebook): the nine notebook sections mapped to GCF Concept Note / Funding Proposal codes with present-vs-recommended datasets and the Togo SAT Table 5 target output; the CDH skills library vs this use-case plus a proposed GCF-proposal skill; and Cesare's multilateral-climate-funds notebook concept. Per-section giscus comment boxes + a no-account feedback form. Backed by the [evidence log](./methods/evidence/sources.md) (per-dataset URLs, licences, delivery routes). Not for external circulation until the champion confirms it is public-safe.
- **Adoption signals:** _TBC_ — track usage of the notebook for live GCF concept notes
- **Lessons learned:** _TBC_ — fill in at handover
