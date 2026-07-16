# Review-page playbook

How to build an interactive, public-safe **review page** for a use-case — a single hosted
HTML page that reviews a project's datasets and/or method, carries reviewer feedback inline,
and is safe to share outside CGIAR.

Reference implementation: [`public/b4t/cri-review.html`](./public/b4t/cri-review.html) (B4T Crop
Risk Index review). Copy its patterns; this file records the generalizable conventions,
styling, and tooling so the next use-case doesn't start from scratch.

> This is an **optional** deliverable, not part of the standard brief. Build one when a
> use-case needs external stakeholders to scrutinise datasets or a method and comment in place.

---

## 1. When to build one

- A use-case has a **dataset audit** (current inputs vs recommended alternatives) or a
  **method reconstruction** that domain experts / a review panel need to check.
- You want structured, attributable feedback (per section) without emailing documents around.
- The content is **public-safe** (confirm with the champion). Sensitive material stays in
  OneDrive and is only linked, never embedded.

## 2. File & deploy setup

- One standalone HTML file at `public/<slug>/<name>.html` (e.g. `public/b4t/cri-review.html`).
  `public/` is served at the site root, so it lands at
  `https://cgiar-climate-data-hub.github.io/use-cases/<slug>/<name>.html`.
- It is a **wrapped standalone document** (own `<style>`/`<script>`), not an Astro page — so it
  does **not** go through the content schema and does **not** trigger markdown-lint / link-check
  CI (those run on `*.md` only). Fast to iterate.
- Deploy: `deploy.yml` runs on push to `main` (Astro build → GitHub Pages). Site `base` is
  `/use-cases`.
- Supporting assets (source PDFs, rendered page images) live under `public/<slug>/docs/` and
  `public/<slug>/docs/img/`, referenced with **relative** paths (`docs/…`, `docs/img/…`).
- Link to the **rendered** brief, not the raw `.md`: `…/use-cases/use-cases/<slug>/` (the
  double `use-cases` is the base + the Astro route — verify with a 200 before shipping).

## 3. Single-surface workflow

Iterate on the **hosted HTML only**. Do not maintain parallel copies (a claude.ai artifact, a
markdown mirror) in lockstep — that multiplies the work per change. The repo markdown/CSVs stay
as the data-of-record but are allowed to drift; reconcile only if the page is later ported to
Astro (the real single-source fix). Batch several edits, then open **one** PR per round.

## 4. Page structure

- **Tabs** for distinct audiences/topics (e.g. *Data* / *Methods*), toggled by a `.tabbar`;
  each tab is a `.shell[data-tab]` panel, one visible at a time.
- **Sidebar TOC** (`.toc`) per tab. **The TOC numbers must match the section headings** — if the
  body uses its own numbering (e.g. a source doc's component numbers), strip it so the sequential
  TOC numbers are the only ones. Cross-tab links use a `data-jump="tab:anchor"` handler that
  switches tab then scrolls.
- **Lead with the decision.** Open with an "at a glance" summary/verdict table before the detail.
- **Per-item detail cards** (one per dataset): verbatim source definition (see §5), a
  current-vs-recommended comparison on identical axes (`.spec` panels: `Present` | `Recommended`),
  a verdict, open questions, provenance.
- **Honesty box** near the top — state where facts come from, that conflicts are flagged, and
  that unconfirmed items are marked, never guessed.

## 5. Content conventions

- **Quote the source verbatim** where it's load-bearing (e.g. each dataset's definition from the
  source document's appendix, reproduced exactly incl. any typos, in a `blockquote.srcquote`).
  Don't paraphrase decisions, titles, or key phrasing.
- **Never invent.** Mark unknowns `pending` / `_TBC_` and say what's missing. Half-correct is
  worse than a visible gap.
- **Chips/pills** encode state at a glance: a *verdict* (keep / replace / clarify / legacy) and,
  where useful, a neutral "how used" category. Keep semantic colour separate from the accent.
- **De-personalise open questions** to the team, not an individual — but keep a person's name
  where it's a genuine source citation (their emails, their attributed statement).
- **Hyperlink datasets where named** (recommended panel + text mentions), to the dataset's
  official page — using only URLs **verified in the evidence log**. Leave plain where there is no
  clean verified URL rather than guessing one.

## 6. Evidence discipline

- Keep an **evidence log** (`<slug>/methods/evidence/sources.md`): one entry per external source,
  what it verified, the date, and the official URL. Every claim about an alternative traces to an
  entry.
- Verify **live** (WebFetch) and **re-check adversarially** — a second pass that tries to refute
  the first. Record licences explicitly (matters for CDH hosting; note non-commercial / share-alike).
- Where the source document and a stakeholder's correction disagree, the **correction describes
  the actual data and takes precedence** — flag the conflict, don't silently pick one.

## 7. Feedback system

Two channels, so anyone can respond:

**(a) Per-section comments — GitHub Discussions via giscus.** One collapsible comment box per
section (and per open question). Requires the giscus GitHub App installed on the repo + Discussions
enabled + a category.

> **Critical gotcha:** do **not** lazy-load giscus by injecting `<script src=giscus.app/client.js>`
> per box. `client.js` reads `document.currentScript`, which is **`null` for the 2nd+
> dynamically-injected script** — so only the first box a user opens ever renders. **Build the
> giscus `…/widget?` iframe directly** per box (params: `origin, session, theme, reactionsEnabled,
> emitMetadata, inputPosition, repo, repoId, category, categoryId, strict, backLink, term`), add a
> `message` listener that reads **`giscus.resizeHeight`** (not `resize.height`) to size each iframe,
> and persist the GitHub session from the `?giscus=<token>` sign-in callback. See the loader in the
> reference page. Works for unlimited instances.

- One thread per section (`data-term` = a stable, unique title). Changing a `data-term` orphans
  its existing discussion.
- Merge an open-question callout and its answer box into **one** block rather than two separate
  elements.
- Add a standing note in every box: *no GitHub account, and don't want one? use the Feedback
  button* — inject it once in the loader so it's consistent everywhere.

**(b) No-account form.** A Microsoft Form → Power Automate → GitHub issue flow, opened from a
floating action button (`.fab`, bottom-right) and a sidebar link. Lets reviewers without a GitHub
account still submit feedback (becomes a tracked issue the coordinator triages).

## 8. Styling tokens

Pulled from the reference page — reuse for visual consistency across use-cases:

- **Neutrals with a slight blue bias**, a single accent (`--brand`, a considered blue), a muted
  ink, and hazard/semantic accents kept separate from the accent.
- **Type:** a serif display for headings, a clean sans for body, a mono for codes/IDs. Set a scale
  and stay on it.
- **Components:** `.note` (soft callout), `.callout` (accented), `.pill`/chips (state), `.spec` +
  `.spec-col present|rec` (comparison panels), `.src`/`.srcbody`/`.srcquote` (collapsible source
  folds + verbatim quotes), `.cmts` (comment boxes), `.tabbar`, `.toc`.
- Wide content (tables, page images) scrolls inside its own container; the body never scrolls
  sideways. Give collapsed `<details>` a clear, brand-coloured summary.

## 9. Tooling

- **Highlighted source-PDF images** (show the exact passage a claim rests on): render the page
  with `pdftoppm -png -r 150 -f N -l N -singlefile in.pdf out` (crop with `-x/-y/-W/-H`), get word
  boxes with `pdftotext -bbox`, match the passage's start/end phrases, convert the line boxes to
  **percentages of the page** and drop translucent `.pdfhl` overlay divs over an `<img>` — the
  overlay then scales with the responsive image. No image-editing library needed. Keep the verbatim
  text as a collapsible transcript alongside.
- **Verbatim appendix definitions** come from a canonical extract CSV, not re-typed.

## 10. Process rules (learned the hard way)

- **Check a PR's state before pushing more to its branch** (`gh pr view <n> --json state,mergedAt`).
  PRs here merge fast; pushing onto a merged branch orphans the commit. Branch fresh off
  `origin/main` for each change.
- **GitHub Pages deploy flake:** `Deployment failed, try again later` (build green, deploy job red)
  is a Pages backend flake, not your code. A `--failed` rerun retries the same stuck deploy and
  fails again — trigger a **fresh full run** (`gh run rerun <id>` without `--failed`, or
  `gh workflow run deploy.yml`). Confirm the change is live by `curl`-ing the page for a known
  string; hard-refresh (Cmd-Shift-R) to beat the CDN cache.
- **Don't reach into OneDrive** from the repo. Link sensitive material; host only what the champion
  confirms is public.
- Commit/PR style follows the repo (`.github/PULL_REQUEST_TEMPLATE.md`); reference the use-case.

## 11. Patterns & gotchas (from the GCF Preparation Facility build + B4T v1.1, 2026-07)

Reusable structure and hard-won gotchas beyond the B4T reference page:

### Page structure

- **Tabs per audience/topic**, and a cross-cutting **"alignment" tab** to a sibling use-case (GCF page has a *GCA alignment* tab: the parallel IFI/MDB use-case + an overlap table — build once, serve both).
- **Three-source dataset model**: tag every dataset **Present** (already in the Hub/notebook) · **requested** (the champion's / memo's list) · **additional** (this review's own deep research). Show it as a three-box summary panel per theme **and** a `Source` column in the detail table. Keeps "what they asked for" vs "what we found" legible.
- **Per-dataset unpacking for the ingestion/tech team** — one detail table per theme, columns: dataset · what it is · native format & resolution/geometry · transformation to admin0/1/2 · IP/licence · **CDH integration route**. The route is one of **mirror-host** (open raw) / **federate** (live API) / **derive-then-host** (compute a product — for bulk-only or non-commercial data).
- **Priority rubric** per recommended dataset (`P1/P2/P3` = value to proposals × ease of integration [open + API = easiest] × coverage × non-redundancy), rendered as a pill. Then a **consolidated "ingestion shortlist"** near the top — every P1 across themes in one do-first list, quick-wins (open + API/cloud) split from resolve-first (NC / unclear licence / derive step). The scattered per-theme priorities aren't actionable for the data team on their own.
- **Framing lead per section**: one plain sub-paragraph stating the proposal need the theme serves + the question the datasets must answer. Fold it into the "Serves …" line — **not everything needs a box.** Number every table (`Table N —`) with a caption that carries the source + priority key. Give cryptic status chips (`IN CR`, etc.) `title` tooltips.

### Licence gate (decides what the Hub can host)

- **Open** → mirror-host the raw data. **Non-commercial** → federate/link the raw data, *don't copy it* — but for non-commercial research use you can nearly always **compute and publish derived admin-level products** (that's the whole notebook). **Unclear** → resolve before cataloguing.
- Three catches on derived products: **ShareAlike cascade** (CC BY-NC-SA derivatives inherit the licence; a combined export can conflict), **transformative rule** (e.g. ACLED — aggregates must not be reverse-engineerable), and **publish-stats-not-raw** (WDPA/IUCN/DHS/MICS: expose the computed number, keep the raw with the provider). Verify each licence **live + adversarially**; log in the evidence file.

### Feedback loop & versioning

- When reviewers answer the open questions (giscus), fold each answer inline as an **"✅ Answered — <name>, <date>"** note in the relevant card (so the resolution shows without opening the thread), update the evidence log, and **version**: a page footer stamp + a foldable *version history* (`v1.1 = feedback incorporated …`), and bump the brief's `updated:` + a progress note. (B4T went to v1.1 this way after Bert's answers.)

### giscus image gotcha (corrects a wrong assumption)

- The giscus comment box is a **plain Markdown textarea — it does NOT support drag-and-drop image upload** (GitHub's uploader isn't wired into the embed; see giscus issue #197). For a screenshot, tell reviewers to **paste a hosted image URL**, attach on github.com directly, or use the **no-account form** (which takes file uploads). Don't claim drag-drop works.

### Internal source docs

- Linking **CDH SharePoint** originals is fine for public-safe pages (SharePoint is CGIAR-auth-gated). Use a foldable **"Source documents"** annex; use the **real share links** the coordinator supplies (right-click → Share) — don't fabricate URLs. `cgiar.sharepoint.com` is already in the lychee exclude list.

### Repo CI traps for use-case markdown

- A use-case **`.md`** (brief, evidence log) triggers **markdownlint** and **lychee link-check**; standalone HTML in `public/` is exempt. markdownlint fires **MD034 (no-bare-urls)** on URL-dense evidence logs — either a file-scoped `<!-- markdownlint-disable MD034 -->` or wrap URLs in code-spans / `[text](url)`. lychee 403s on WAF/bot-blocked or cert-flaky hosts (IUCN, OECD, IMF, IPC, MICS, IFAD, ACLED, Climate Watch, …) — add them to the `--exclude` list in `linkcheck.yml` (same pattern as the existing entries).

### Branch discipline (this repo merges fast + auto-deletes branches)

- Cut a **fresh branch off `origin/main` before each push**, and **check the PR's merge state first** — pushing a follow-up commit after a PR merged (its branch auto-deleted) lands the commit orphaned on a re-created branch. Verified the hard way several times this session.
