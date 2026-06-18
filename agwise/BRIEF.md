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
updated: 2026-06-17
---

> Integrate CDH-facilitated historical and forecasted climate data into the AgWise fertilization module, enabling process-based crop model simulations at scale across Africa via the ag-cube-cm package and associated AI-assisted workflows.

## Brief

### Background & rationale

AgWise is a CGIAR innovation designed to provide tailored agronomic recommendations based on specific demands from partners to improve farmer productivity and/or profitability. Its modular framework offers data-driven advice on fertilizer requirements, optimal planting dates, suitable cultivars, and other agricultural practices. By leveraging extensive datasets, including field trials, market trends, topography, climate, and soil information, AgWise delivers accurate and context-specific guidance to support informed decision-making and enhance farming outcomes.

Specifically, its fertilization module generates actionable recommendations for Decision Support Tools (DSTs) across Africa. These recommendations depend on process-based crop models, which require high-resolution climate, soil, and management data.

To address this data access need, the ag-cube-cm Python package was developed — a tool for spatial NetCDF and Zarr datacube processing and crop model orchestration. It integrates climate data (AgERA5, CHIRPS), soil data (SoilGrids), and management inputs to run pixel-level agricultural simulations at scale, either programmatically or via an AI assistant using the `/spatial-crop-modeler` MCP skill. An initial yield prediction test was conducted for a small area in Malawi, and a Ghana pilot that integrates forecasted and historical climate data to link the crop modeling components (yield prediction and fertilization) is proposed.

The CDH team will support storage and data integration.

### Objectives

- Fully integrate forecast and historical data for use in Process-Based Models, managed through the CDH for storage and AI skill performance assessment.
- Optimise yield prediction process time by integrating the climate API developed by Jemal into the model.
- Run an end-to-end pilot in Ghana to demonstrate the integrated historical + forecast data pipeline.
- Manage climate data storage and skill performance assessment through CDH.
- Define documentation, update frequency, and long-term data access model for the forecast API.
- Plan expansion of coverage and scalability beyond local machine runs.

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
| TBD | Jemal deploys AWS endpoint; documentation shared |
| TBD | CDH metadata v1 shared with Jemal |
| TBD | End-to-end Ghana pilot completed using integrated pipeline |

### Background materials

- [ag-cube-cm GitHub repository](https://github.com/anaguilarar/ag-cube-cm) — Python package for spatial crop model orchestration
- [spatial-crop-modeler skill](https://github.com/anaguilarar/ag-cube-cm/blob/master/.claude/commands/spatial-crop-modeler.md) — MCP skill for AI-assisted crop modelling workflows

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

### Data assets for the hub

| Dataset | Hub status | Hub catalog | Feasibility (1=easy, 5=hard) | Serves | Notes |
| ------- | ---------- | ----------- | ---------------------------- | ------ | ----- |
| ERA5 | scoped | _pending_ | 2 | Weather inputs for DSSAT | Historical climate timeseries |
| CHIRPS | scoped | _pending_ | 1 | Rainfall inputs for DSSAT | Daily precipitation; already cloud-hosted |
| SoilGrids |  |  |  | Soil inputs for DSSAT |  |
| Climate API |  |  |  |  | Developed by Jemal |

### Methodological guidance needed

- [ ]

### Skills & tools

- ag-cube-cm Python package (NetCDF/Zarr processing, DSSAT orchestration)
- `/spatial-crop-modeler` MCP skill (AI-assisted workflow orchestration)
- Climate API

### Delivery mechanism

CDH-managed data storage; integrated data pipeline and MCP/skill.

## Meetings & decisions

| Date | Attendees | Summary | Decisions | Recording / transcript |
| ---- | --------- | ------- | --------- | ---------------------- |
| 2026-05-21 | Andres Aguilar Ariza, Diego Agudelo, Jemal Seid Ahmed | Jemal presented forecast API; discussed AWS migration, data access model, and Ghana pilot | Ghana pilot agreed; CDH metadata v1 to be shared; follow-up meeting to be scheduled | OneNote (CDH SharePoint) |

## Risks & open questions

-

## Outputs

> _Section fills in once status reaches `piloting` or beyond._

- **Deliverables:** _TBD_
- **Adoption signals:** _TBD_
- **Lessons learned:** _TBD_
