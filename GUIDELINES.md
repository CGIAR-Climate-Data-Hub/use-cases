# CDH Use Case Development Guidelines

These guidelines support the efficient development of CGIAR Climate Data Hub (CDH) use cases. The aim is to move quickly from ideas to delivery, while keeping work coordinated, visible, and reusable across the team.

## Core working principle

All use-case work must be shared, visible, and centrally documented.

| Surface | Purpose |
| --- | --- |
| **SharePoint** (mirrored to OneDrive at `Climate_data_hub/use_cases/<slug>/`) | Working files: proposals, slides, datasets, working drafts |
| **OneNote (CDH Notebook)** | Narrative documentation, meeting summaries, decisions |
| **MS Planner** | Task tracking, owners, dates |
| **This repo** | Public-facing briefs and the rendered Astro site |

If others can't see it, it effectively doesn't exist.

## The development process

### Step 1 — Identify the use case

Use cases emerge from:

- Ongoing projects
- Funding or proposal pipelines
- Known data gaps

Capture the idea briefly. **Output:** short description of the problem and intended outcome.

### Step 2 — Assign a Use Case Champion

Each use case should have a champion who:

- Understands the domain
- Can define what is needed
- Remains engaged through delivery

### Step 3 — Develop the brief and assemble materials

The champion and coordinator work together to produce a structured brief using [`BRIEF_TEMPLATE.md`](./BRIEF_TEMPLATE.md).

| Section | Content |
| --- | --- |
| **A. Narrative** | What is the use case? Who will use it? Why is it needed now? |
| **B. Data needs (initial)** | What data is required? At what scale? What exists vs what is missing? |
| **C. Expected outcome** | What this will enable (decision, analysis, proposal, etc.) |
| **D. Background materials (required)** | All relevant materials gathered and organised in SharePoint |

Requirements for materials:

- Store files in the shared CDH SharePoint structure
- Organise them clearly (folders or naming conventions)
- Record links and notes in the CDH Notebook page for the use case

**Output:** Use Case Brief v1 (committed to this repo) + organised supporting materials (SharePoint + OneNote links).

### Go / No-Go gate

Before proceeding past the brief, the CDH Core Team reviews and decides:

- **Go** — proceed to data requirements clarification
- **No Go** — declined, with rationale captured in `go_no_go:` frontmatter
- **On hold** — paused, with reason captured

Record the decision in the brief's `go_no_go:` frontmatter block and in the Go / No-Go section of the rendered page.

### Step 4 — Clarify data requirements [if Go]

The champion (with support) refines data needs into:

- Variables
- Datasets
- Sources
- Required transformations

The coordinator may connect to relevant experts or help locate datasets across the program.

**Output:** clear, actionable data requirements — captured in the **Data assets for the hub** table inside the brief's Action Plan section.

### Step 5 — Agree on a practical plan

Define how the use case will move forward.

- **Activities** — data identification, preparation/cleaning, metadata creation, ingestion into CDH
- **Roles** — Champion, named Data Providers, CDH Technical Support, Coordinator
- **Timeline** — simple milestones, realistic expectations

**Output:** short implementation plan in the brief's Action Plan section.

### Step 6 — Coordinate through the use case task group

Each active use case has a small task group, typically:

- The champion
- CDH team members
- The coordinator
- Relevant contributors (as needed)

**Meetings:**

- Short and focused
- Action-oriented
- Scheduled as needed (not excessive)
- Recorded where possible; transcripts summarised and stored in `Climate_data_hub/meetings/`
- Key decisions and actions captured in the brief's **Meetings & decisions** table and in OneNote

### Step 7 — Track progress

All use cases must be tracked using shared tools.

- **MS Planner** — each use case has tasks, each task has an owner, progress visible
- **OneNote (CDH Notebook)** — each use case has a dedicated page: description, progress updates, meeting notes, links to datasets and materials
- **This repo** — brief reflects current status, lifecycle stage, dataset status, and risks

### Step 8 — Document as you go

Keep documentation simple but consistent. Capture:

- What was agreed
- What data was used
- What challenges were encountered
- How issues were resolved

This ensures the use case can later be reused as a Hub catalogue entry, case study, or internal guidance.

## Roles and responsibilities

### Use Case Champion

- Defines the problem and need
- Leads on data requirements
- Contributes content and expertise

### Use Case Coordinator

- Supports structure and clarity
- Connects people and data
- Maintains oversight across use cases
- Ensures tracking and documentation are in place
- Facilitates task group coordination

### CDH Technical Team

- Supports data preparation and ingestion
- Advises on formats and standards
- Helps translate requirements into implementation

### Data Providers / Contributors

- Prepare and share datasets
- Support data quality and documentation
- Respond to requests in a timely manner

## Working principles

- **Work in shared spaces** — SharePoint, OneNote, Planner, and this repo are the default; avoid duplication and private storage.
- **Keep it action-oriented** — focus on next steps; avoid over-discussion.
- **Be clear on ownership** — every task has a named person.
- **Maintain momentum** — small, regular progress is expected.
- **Raise issues early** — flag data gaps, delays, or constraints early so they can be addressed.

## Where things live

| Content | Location |
| --- | --- |
| Use-case briefs (public, version-controlled) | This repo: `<slug>/BRIEF.md` |
| Rendered briefs (Astro site) | <https://cgiar-climate-data-hub.github.io/use-cases/> (planned) |
| Background materials (PDFs, slides, proposals) | OneDrive: `Climate_data_hub/use_cases/<slug>/` |
| Meeting transcripts (canonical) | OneDrive: `Climate_data_hub/meetings/` |
| Meeting transcripts (use-case-specific duplicates, optional) | OneDrive: `Climate_data_hub/use_cases/<slug>/meetings/` |
| Task tracking | MS Planner |
| Working notes & decisions | OneNote (CDH Notebook) |

## Final note

These guidelines are intended to support efficient, coordinated delivery. They remain lightweight and evolve as the team gains experience.
