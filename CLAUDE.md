# CLAUDE.md — Working in the CDH use-cases repo

This file orients Claude Code when working inside this repo. Read it once on entry, then refer back as needed.

## What this repo is

Public-facing source for the CGIAR Climate Data Hub (CDH) use-case portfolio. Each use-case is one folder containing a canonical `BRIEF.md`, rendered to a static site by [Astro](https://astro.build).

A private working store lives in OneDrive at `Climate_data_hub/use_cases/` — that's where background materials, meeting transcripts, and drafts sit. This GitHub repo holds only what's safe to publish.

## Conventions

- **Folder names**: lowercase kebab-case. Examples: `gcf-preparation-facility`, `b4t`, `livestock-emissions`, `user-needs-assessment`.
- **Canonical file per use-case**: `<slug>/BRIEF.md`. Use-case-specific code or notebooks may live alongside (in `<slug>/code/`, `<slug>/notebooks/`, etc.).
- **Frontmatter schema**: see [`BRIEF_TEMPLATE.md`](./BRIEF_TEMPLATE.md) for the canonical field list. Formal validation rules live in [`src/content/config.ts`](./src/content/config.ts) (Zod).
- **No meeting note duplicates here** — source of truth is `Climate_data_hub/meetings/` in OneDrive.
- **Status vocabulary**: `idea` → `brief` → `active-development` → `piloting` → `handover` → `complete`. Terminal off-ramps: `on-hold`, `no-go`.

## How a use-case develops

See [`GUIDELINES.md`](./GUIDELINES.md) for the 8-step development process. Summary:

1. Identify the use case
2. Assign a champion
3. Develop the brief + assemble materials
4. CDH Core Team Go / No-Go gate
5. Clarify data requirements (if Go)
6. Agree on a practical plan
7. Coordinate via task group
8. Track progress and document as you go

## Roles

- **Champion** — domain owner; defines the problem and data needs; named in `champion:` frontmatter.
- **Coordinator** — connects people and data; maintains tracking and documentation; named in `coordinator:` frontmatter.
- **CDH Technical Team** — data preparation, ingestion, format standards.
- **Data Providers** — prepare and share datasets.

## Rules for Claude Code in this repo

1. **Ask before creating new files.** Default to extending existing files. Announce intent before writing so it can be redirected.
2. **Never invent facts.** When you don't know — owner, date, dataset link, decision — write `_TBC_` and explain what's missing. Half-correct content is worse than visible gaps.
3. **Use the template.** New use-cases: copy `BRIEF_TEMPLATE.md` into a new kebab-case folder as `BRIEF.md`. Don't freelance the structure.
4. **Frontmatter is load-bearing.** Astro validates against the Zod schema in `src/content/config.ts`. The build fails on invalid frontmatter — keep it clean.
5. **Don't reach into OneDrive from this repo.** Briefs may link to OneDrive paths (relative); reading or writing those paths from this repo's working tree is out of scope.
6. **Quote stakeholders verbatim where possible.** Titles, decisions, and key phrasing from source documents should be reproduced — not paraphrased.
7. **Each PR should reference the use-case it serves** — use the PR template at `.github/PULL_REQUEST_TEMPLATE.md`.

## Local dev

```bash
npm install
npm run dev      # live preview at http://localhost:4321
npm run build    # static output to ./dist
npm run check    # type + content schema validation
```

## When in doubt

Open an issue using the templates in `.github/ISSUE_TEMPLATE/` rather than freelancing a structural change. The repo is small enough that lightweight discussion costs nothing.
