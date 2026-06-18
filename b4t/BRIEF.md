---
# === Identity ===
title: B4T - Climate and Environmental Crop Risk Index (CRI)
description: Review, harmonize, and update the Climate and Environmental Crop Risk Index to use current climate model inputs and consistent future time horizons across all hazard indicators.
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
updated: 2026-06-17
---

> Review and provide support to update climate data for the Climate and Environmental Crop Risk Index (CRI), a tool based on a hazard-risk framework that utilises spatial data on climate and environmental factors to support crop breeding prioritization under climate change.

## Brief

### Background & rationale

The Climate and Environmental Crop Risk Index (CRI) is a CGIAR tool that quantifies climate-related risks to crop production by combining multiple hazard indicators (e.g. drought, flooding, rainfall variability, heat, and salinity) into a composite score. The methodology converts each hazard indicator into pseudoprobabilities (0–100), then calculates a weighted average across indicators per hazard type. A 50-50 weighting is applied between present and future (2050) hazard indicators to reflect uncertainty in future projections.

A second-phase will aim to use hazard scores to predict yield responses to breeding under climate change scenarios (see [CRI draft on CGSpace](https://cgspace.cgiar.org/items/2a1d0acb-2e0c-48fc-8b39-56e5899ba16c)).

CDH support was triggered through outreach by the team to B4T colleagues in April 2026. A discussion and subsequent interactions identified several data quality concerns:

- The primary hazard input data is based on pre-CMIP5 projections; CMIP6 data is now available.
- The Aqueduct flood/water risk data in use predates Aqueduct v4.0 (which uses CMIP6).
- Different hazard indicators use inconsistent future time horizons (some 2030, some 2050), undermining comparability.
- The Hazard Intensity and Interactions (HII) scoring matrix was partly generated using AI (LLMs), which raised concerns about hallucination and insufficient literature validation.

The CDH team has proposed to work with the CRI team not to redesign the system, but rather understand the current methodology, identify strengths and weaknesses, explore improvement opportunities, and think about where climate data could add value to breeding and market segmentation workflows.

### Objectives

- Audit current CRI climate hazard input datasets.
- Identify priority updates: e.g. where feasible, replace CMIP5 (and prior) inputs with CMIP6 equivalents.
- Harmonize future time horizons across indicators.
- Support review of HII scoring matrix, flagging AI-generated entries not supported by literature.
- Co-produce an updated CRI documentation describing revised methodology and data sources.

### People involved

| Name | Organisation | Role |
| ---- | ------------ | ---- |
| Bert Lenaerts | IRRI | Champion; domain owner |
| Peter Steward | Alliance | Use case lead; coordinator |
| Gerdino Badayos | IRRI | Consultant |

### Key dates

| Date | Milestone |
| ---- | --------- |
| 2026-04 | Contact initiated, IRRI shares CRI data sources and methodologies, identifies needs. |
| 2026-05-15 | Expert review feedback deadline (Peter Steward outreach round) |
| TBD | CDH team reviews data/methods |
| TBD | CDH team proposes update/harmonization plan |
| TBD | CDH and CRI team co-produce updated methods note and CDH data pipeline incorporated into CRI model. |

### Background materials

- [CRI draft paper (CGSpace)](https://cgspace.cgiar.org/items/2a1d0acb-2e0c-48fc-8b39-56e5899ba16c) — Climate and Environmental Crop Risk Index, draft publication
- [Crop Risk Index documentation v1 (SharePoint)](https://cgiar.sharepoint.com/:b:/r/sites/CGIARClimate_data_hub/Shared%20Documents/use_cases/B4T/Crop%20Risk%20Index-documentation%20v1.pdf?csf=1&web=1&e=JQkPsr) — Full methodology documentation
- [Ericksen 2011 CCAFS report (SharePoint)](https://cgiar.sharepoint.com/:b:/r/sites/CGIARClimate_data_hub/Shared%20Documents/use_cases/B4T/ccafsreport5-climate_hotspots_final.pdf?csf=1&web=1&e=KVBdit) — Mapping hotspots of climate change and food insecurity in the global tropics
- [HII scoring matrix (SharePoint)](https://cgiar.sharepoint.com/:b:/r/sites/CGIARClimate_data_hub/Shared%20Documents/use_cases/B4T/HII-scoring%20matrix.pdf?csf=1&web=1&e=rGr7fr) — Hazard Intensity and Interactions scoring matrix

## Go / No Go

> _Filled in by the CDH Core Team after the brief is developed._

- **Decision:** Pending
- **Date:** _TBD_
- **Decided by:** CDH Core Team
- **Notes:**

## Action plan

> _To be developed once status reaches `active-development`._

### Actions

- [ ] Compile full inventory of current CRI input datasets — CRI and CDH teams
- [ ] Identify CMIP6 replacements for each outdated input — CDH
- [ ] Draft data update/harmonization plan (datasets, time horizons, bias-correction approach) — CRI and CDH teams
- [ ] Co-develop updated CRI documentation to reflect revised inputs and methodology — CRI and CDH teams

### Data assets for the hub

| Dataset | Hub status | Hub catalog | Feasibility (1=easy, 5=hard) | Serves | Notes |
| ------- | ---------- | ----------- | ---------------------------- | ------ | ----- |
|  |  |  |  |  |  |

### Methodological guidance needed

- [ ] Climate hazard indicators and thresholds currently used
- [ ] Balance between climatological simplicity vs decision relevance
- [ ] Use of historical vs projected hazard indicators
- [ ] Whether current indicators are sufficiently crop- or system-specific
- [ ] How climate risk and adaptation potential could be represented more robustly
- [ ] Linking climate information to trial environments, market segments, or varietal performance
- [ ] Envirotyping / analogue approaches
- [ ] Probabilistic vs threshold-based hazard framing
- [ ] Adaptation metrics beyond simple exposure mapping

### Skills & tools

-

### Delivery mechanism

TBD

## Meetings & decisions

| Date | Attendees | Summary | Decisions | Recording / transcript |
| ---- | --------- | ------- | --------- | ---------------------- |
| 2026-05-08 | Peter Steward | Email sent to external reviewers | Feedback requested by 2026-05-15 |  |

## Risks & open questions

-

## Outputs

> _Section fills in once status reaches `piloting` or beyond._

- **Deliverables:** _TBD_
- **Adoption signals:** _TBD_
- **Lessons learned:** _TBD_
