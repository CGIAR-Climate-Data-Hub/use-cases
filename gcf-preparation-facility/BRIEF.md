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

updated: 2026-10-07
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
- [ ] Meet Cesare on notebook next steps — Peter Steward — Cesare requested "first half of July" (2026-06-17 email); chased 2026-09-23 ("i can look into it tomorrow/friday"), no reply since
- [x] Queue the recommended datasets in the CDH ingestion tracker — Peter Steward + Claude — `GCF use-case` sheet added to `asset_mapping/CDH_data-ingestion v2.xlsx` (31 rows) and mirrored in [`data/ingestion-queue.csv`](./data/ingestion-queue.csv), 2026-10-07
- [x] Adversarial rescreen of every queued dataset (live endpoint, licence, alternatives) — Claude — results in the [evidence log](./methods/evidence/sources.md#rescreen-2026-10-07--queued-datasets-adversarial-re-check); GMIA v5 → GMIA-NEXT swap, EX-ACT route change, 2026-10-07
- [ ] Theme 2 extreme-events request to the Atlas hazards pipeline — Peter Steward — questions block in [`methods/ingestion-notes.md` §2](./methods/ingestion-notes.md); relay to the hazards session, then finalise the request
- [ ] Message Cesare (review comments, final dataset, extraction method, DOI, champion role) and MFL/Mosaic (host/federate Theme 8 layers) — Peter Steward — drafts in `outputs/` (not committed)
- [ ] Author CDH metadata records for the P1 rows — Brayden Youngberg + Peter Steward — **after `cdh-metadata-standard` v0.4.0 lands** (open PR #35); order in `ingestion-notes.md` → Follow-ons
- [ ] `climate-rationale` skill — _TBC_ — issue text drafted (`outputs/skills-issue-climate-rationale.md`); build after ≥1 theme is catalogued

### Data assets for the hub

The full per-dataset audit — all ~40 datasets behind the nine notebook sections, with verified source URLs, **licences** (open → mirror-hostable vs non-commercial → federate/link only), and how each can be **summarised under a geoselector** or **reached by an AI skill** (federate vs rehost) — lives in the review page and evidence log, not here:

- **[Review page — Data tab](https://cgiar-climate-data-hub.github.io/use-cases/gcf-preparation-facility/gcf-prep-review.html)** — dataset detail per notebook section + the "Delivering the data" delivery-route analysis.
- **[Evidence log](./methods/evidence/sources.md)** — one entry per dataset: URL, licence, verification date, derived-products guidance; **Rescreen 2026-10-07** table at the end.
- **[Ingestion queue](./data/ingestion-queue.csv)** — the 31 rows queued on 2026-10-07 (Pete's per-theme P1/P2 calls), mirrored as the `GCF use-case` sheet of the CDH ingestion tracker; route, licence, complexity, rescreen verdict, proposed lead per row.
- **[Ingestion notes](./methods/ingestion-notes.md)** — the decision record and per-theme working notes: Theme 2 hazards request, spatial-vs-method split, Theme 5 document-registry spec, EX-ACT / WorldCover designs, the OECD/Data360 client, the safeguards licence split.
- **[Rationale map](./data/rationale-map.yaml)** — machine-readable GCF section → theme → dataset → Hub route/status index for AI agents and the planned `climate-rationale` skill.
- **[Rationale prototype](./code/rationale/README.md)** — `python -m cdh_rationale TGO` turns the federated pulls, WorldCover products and Atlas `haz_freq` into labelled, citable fragments per GCF section (JSON + Markdown + coverage table), gaps explicit; surfaced a saturated historic-NDWS defect in `haz_freq` (Theme 2 request ask #6).
- **[Federated clients](./code/federated/README.md)** — `python -m cdh_federated TGO` pulls the open-API P1 datasets (INFORM, FEWS NET, DHS, OECD CRS + Rio markers, Data360 IMF/IDS, Climate Watch, UNICEF JMP, GFW with key) into one tidy admin0/1 schema with per-row request URLs; verified for TGO and KEN on 2026-10-07.

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
| 2026-10-07 | Peter Steward (coordinator decision; champion unresponsive) | Proceed on the review's recommended datasets without further champion input. Per theme: 1 in hand · 2 technical note + request to the Atlas hazards pipeline · 3 split spatial data vs method notes (GLEAM-X, iCLEANED) · 4 P1 + P2, not P3 · 5 test Climate Watch, spec a document-registry parquet, chase Cesare's extraction dataset · 6 EX-ACT as engine, WorldCover derived product, EDGAR P1, P2s parked · 7 with 5, P1 only · 8 P1 + promote LandMark, KBA, FAO SDG 5.a.x; ask MFL/Mosaic · 9 P1 | Queue 31 rows in the ingestion tracker; rescreen each; metadata after v0.4.0; `climate-rationale` skill spec'd not built | [`methods/ingestion-notes.md`](./methods/ingestion-notes.md) |
| 2026-09-17 | Cesare Scartozzi, Peter Steward, Bia Carneiro | "Climate Data Hub (input from CACC1)" — resume CACC1 contributions to the Hub (30 min, Cesare's invite) | _TBC_ — no transcript available | Teams meeting; Cesare posted the CR notebook link in the meeting chat |
| 2026-06-17 | Cesare Scartozzi → Peter Steward, Brayden Youngberg (email) | Partial multilateral-climate-funds dataset delivered (CSV, 5,115 projects); notebook concept: "allow users to select one or multiple countries to see past and ongoing investment pipelines, so that they can identify gaps, complementary projects, or examples for project development" | Share incomplete dataset now, final sub-classifiers end June; meet first half of July | `use_cases/gcf-preparation-facility/example dataset/` |
| 2026-04-29 | Peter Steward, Cesare Scartozzi, Brayden Youngberg | Implementation scope: get a usable v1 by August; federated S3 + STAC catalog + use-case wiki as MVP. Cesare demoed the MCF SQL dataset (~2,100 projects, 15k documents); agreed to turn it into an Atlas-style interactive notebook (Cesare Jupyter → Brayden Quarto). NAP/NDC automation withdrawn by Cesare | Federate rather than mirror NEX-GDDP-CMIP6; Brayden owns the metadata standard; dataset = first non-geospatial metadata pilot; DOI via CGSpace/Dataverse | `Climate_data_hub/meetings/2026.04.29 - CDH GCF Use-case.docx` |
| 2026-03-17 | Peter Steward, Cesare Scartozzi, Bia Carneiro, Brayden Youngberg | CACC1 × CACC2 integration — repurpose the Atlas Climate Rationale notebook for the GCF pipeline | Short concept memo to follow from Cesare | `Climate_data_hub/meetings/2026.03.17 - GCF Use-case - CACC1 & CACC2 integration.docx` |

_Source of truth for transcripts: `Climate_data_hub/meetings/` in OneDrive._

## Risks & open questions

- **Champion responsiveness** — no comments on the review page (shared 2026-07-14, chased 2026-09-23); MCF dataset sub-classifiers, extraction method and DOI outstanding since June; Cesare moved from the climate-security team to ImpactSF (2026-09-09) — confirm he remains champion or add a CACC1 co-champion. **Owner:** Peter Steward **Status:** open — message drafted 2026-10-07
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
- **Use-case review page (DRAFT):** [GCF Preparation Facility — data, skills, notebook & GCA-alignment review](https://cgiar-climate-data-hub.github.io/use-cases/gcf-preparation-facility/gcf-prep-review.html) — four tabs:
  - **Data** — the nine notebook themes mapped to GCF Concept Note / Funding Proposal codes, each with a three-source panel (Present in Hub/Atlas · CACC1-requested · additional researched), a per-theme detail table (native format → admin transform → IP/licence → CDH integration route) with `P1/P2/P3` priority pills, and a consolidated **ingestion shortlist** (every P1 in one do-first list) for the CDH data team. Togo SAT Table 5 shown as an illustrative target, not a gold standard.
  - **Skills** — the CDH skills library vs this use-case, scoped to a **generic climate-rationale + orchestration** skill (pull evidence into a proposal-dev pipeline); GCF-specific skills deferred to Cesare + AoW1.
  - **Notebook** — Cesare's multilateral-climate-funds notebook concept.
  - **GCA alignment** — the AAA Atlas GCA use-case, GCA feedback, and an overlap table; foldable **Source documents** annex with internal CDH SharePoint links.
  - Per-section giscus comment boxes (with a comment-type dropdown incl. "suggest a resource") + a no-account feedback form. Backed by the [evidence log](./methods/evidence/sources.md) (per-dataset URLs, licences, delivery routes). Follows [`REVIEW_PAGE_PLAYBOOK.md`](../REVIEW_PAGE_PLAYBOOK.md). Not for external circulation until the champion confirms it is public-safe.
- **Open items (handover):**
  - **Theme 3 hazard-exposure S3 mismatch — resolved 2026-10-07 (the July audit had it backwards).** Both prefixes are live. Canonical = `domain=hazard_exposure/source=nex-gddp-cmip6/region=ssa/…/variable=vop_nominal-usd21/period=jagermeyr/model=ENSEMBLEmean/…` (written 2026-10-06 by `scripts/r3_publish_tiers.R`, 18-GCM ensemble, `.parquet.json` sidecar) — the path the notebook reads. `source=atlas_cmip6/…` is the stale 2025-06 tree (5-GCM pin). Verified with `aws s3 ls`. Still open: only `period=jagermeyr` is published canonically; per-GCM exposure exists only in the legacy tree.
  - **Theme 2 extreme-events data** — `haz_freq.parquet` (per-GCM frequency of NDWS/NDWL0 exceedance, 18 GCMs, adm0/1/2, 17 scenario-periods) is already public; request to extend SEC4 to NTx35 / TAVG / PTOT / HSH_max / THI_max + Moderate drafted in [`methods/ingestion-notes.md` §2](./methods/ingestion-notes.md) — Peter Steward to send.
  - **GCA scope undecided** — GCA alignment is a tab here; whether GCA becomes its own CDH use-case brief or stays a workstream of this facility is open.
  - **Adoption signals:** _TBC_ — track usage of the notebook for live GCF concept notes
  - **Lessons learned:** _TBC_ — fill in at handover
