---
# === Identity ===
title: Use Case Name
description: One-sentence summary of what this use case is and who it serves.

# === Lifecycle ===
type: existing                       # new | existing
                                     #   new       = CDH team works with a partner to discover and implement
                                     #   existing  = a CAP bilateral asset showcased in the Hub
origin: ongoing-project              # ongoing-project | funding-pipeline | data-gap
status: brief                        # idea | brief | active-development | piloting | handover | complete | on-hold | no-go

# === Go / No Go ===
go_no_go:
  decision: pending                  # pending | go | no-go | on-hold
  date:                              # YYYY-MM-DD when decided
  decided_by:                        # e.g. "CDH Core Team"
  notes:

# === People ===
champion: ""                         # Single named person (display name); domain owner
coordinator: ""                      # Single named person (display name); connector / facilitator
task_group: []                       # Additional named contributors (display names)

# === CA-OS linkage ===
primary_aow:                         # AoW0-Orchestrate | AoW1-Accelerate | AoW2-Adapt | AoW3-Empower | AoW4-Transition | AoW5-Finance
related_aows: []                     # other AoWs this use case touches
ca_os_packages: []                   # e.g. [M2, CA30] — packages in CA-OS this use case feeds or draws from

# === Metadata ===
tags: []                             # short keywords, kebab-case
updated: 2026-05-19                  # YYYY-MM-DD of last meaningful change
---

> _One-line summary visible at the top of the rendered page. Repeat or expand the `description:` field as prose. The page H1 is rendered from the frontmatter `title` field — do not add an H1 here._

## Brief

### Background & rationale

_Why this use case exists. The problem it addresses, the demand signal that triggered CDH involvement, and how it fits into the broader CDH portfolio._

### Objectives

_Bullet list of concrete objectives. What does success look like?_

- Objective 1
- Objective 2

### People involved

_Champion, coordinator, task group, and external contributors. Roles are explicit._

| Name | Organisation | Role |
| ---- | ------------ | ---- |
|      |              |      |

### Key dates

| Date | Milestone |
| ---- | --------- |
|      |           |

### Background materials

_Links to canonical reference materials in OneDrive (`Climate_data_hub/use_cases/<slug>/`) or external sources._

- [Document title](relative/path/or/url) — one-line description

## Go / No Go

> _Filled in by the CDH Core Team after the brief is developed. Mirror the `go_no_go:` frontmatter here as prose with rationale._

- **Decision:** _pending_ | Go | No-Go | On hold
- **Date:** _YYYY-MM-DD_
- **Decided by:** _e.g. CDH Core Team_
- **Notes:** _short rationale or context_

## Action plan

> _Required once status reaches `active-development`. Empty stub while in `idea` or `brief` stages._

### Actions

_GitHub-flavoured task list. Each item names an owner. Mark `[x]` when done._

- [ ] Action — Owner — context
- [ ] Action — Owner — context

### Data assets for the hub

_Datasets this use case needs in (or federated with) the CDH catalog._

| Dataset | Hub status | Hub catalog | Feasibility (1=easy, 5=hard) | Serves | Notes |
| ------- | ---------- | ----------- | ---------------------------- | ------ | ----- |
|         | scoped     | _pending_   |                              |        |       |

_Hub status: `scoped → planned → in-progress → published`. The Hub catalog column becomes a live link once the STAC entry exists._

### Methodological guidance needed

_Open methodology questions, blocks, or external review needs._

- [ ] Topic — Owner — context

### Skills & tools

_Short bullets — what this use case uses and what downstream users need._

- Tool or method 1
- Tool or method 2

### Delivery mechanism

_Where the output lives and how users get to it (notebook, portal, training, API, etc.)._

## Meetings & decisions

| Date | Attendees | Summary | Decisions | Recording / transcript |
| ---- | --------- | ------- | --------- | ---------------------- |
|      |           |         |           |                        |

_Source of truth for transcripts: `Climate_data_hub/meetings/` in OneDrive. Link out by relative path._

## Risks & open questions

- **Risk / open question:** _…_ **Owner:** _…_ **Status:** _…_

## Outputs

> _Section fills in once status reaches `piloting` or beyond. Empty until then._

- **Deliverables:** _what was produced_
- **Adoption signals:** _who is using it and how_
- **Lessons learned:** _what to carry forward to the next use case_
