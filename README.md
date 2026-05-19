# CGIAR Climate Data Hub — Use Cases

This repository tracks the CGIAR Climate Data Hub (CDH) use-case portfolio. Each use-case has its own folder containing a canonical **`BRIEF.md`** — what it is, who's involved, current status, action plan, and the materials behind it.

Briefs render to a static site at https://cgiar-climate-data-hub.github.io/use-cases/ (planned), built with [Astro](https://astro.build).

## Master list

| Use-case | Champion | Status | One-line description |
| --- | --- | --- | --- |
| [GCF Preparation Facility](./gcf-preparation-facility/BRIEF.md) | Cesare Scartozzi | Active development | Climate Rationale notebook auto-generating evidence-based climate risk narratives and hazard-exposure tables for GCF proposal writers |
| [B4T — Crop Risk Index](./b4t/BRIEF.md) | Bert Lenaerts | Active development | Climate × environmental Crop Risk Index quantifying yield change for prioritising adaptation and breeding interventions |
| [Livestock Emissions (AoW4 – T2)](./livestock-emissions/BRIEF.md) | Aimable Uwizeye (FAO) | Active development | R-based Tier 2 IPCC GHG inventory tooling for Rwanda's livestock subsector |
| [User Needs Assessment](./user-needs-assessment/BRIEF.md) | _TBC_ | Brief | Cross-cutting user research informing CDH scoping and prioritisation |

## How to use this repo

- **Read a use-case** — open the relevant `<slug>/BRIEF.md`.
- **Add a new use-case** — see [`GUIDELINES.md`](./GUIDELINES.md) for the 8-step process, then copy [`BRIEF_TEMPLATE.md`](./BRIEF_TEMPLATE.md) into a new kebab-case folder.
- **Update an existing brief** — open a PR; use issue templates in `.github/ISSUE_TEMPLATE/` for change proposals.
- **Working with Claude Code** — start with [`CLAUDE.md`](./CLAUDE.md); it loads automatically when this repo is opened.

## Local dev

This repo ships an Astro site that renders the briefs.

```bash
npm install
npm run dev      # live preview at http://localhost:4321
npm run build    # static output to ./dist
npm run check    # type + content schema validation
```

## Lifecycle vocabulary

Use one of these values in the `status:` frontmatter field of each brief:

| Status | Meaning |
| --- | --- |
| `idea` | Concept identified, champion not yet assigned |
| `brief` | Champion assigned, brief in draft, awaiting Go / No-Go |
| `active-development` | Go granted, work in flight, deliverables being produced |
| `piloting` | Early users testing real outputs |
| `handover` | Transitioning to a sustained owner |
| `complete` | Delivered and retired from the active list |
| `on-hold` | Paused, with reason captured |
| `no-go` | Declined at the Go / No-Go gate |

## Conventions

- **Folder names**: lowercase kebab-case (`gcf-preparation-facility`, `b4t`, `livestock-emissions`).
- **Canonical entry point per use-case**: `<slug>/BRIEF.md`. Use-case-specific code, notebooks, or sub-briefs may live alongside in the same folder.
- **Background materials, transcripts, working drafts**: live in the OneDrive working store at `Climate_data_hub/use_cases/<slug>/`. Briefs link out by relative path; this repo stays public-readable.
- **Meeting notes**: not duplicated here. Canonical source is `Climate_data_hub/meetings/` in OneDrive.

## License

MIT — see [LICENSE](./LICENSE).
