# hub-submissions — pre-submission staging for Climate Data Hub records

Where draft metadata records sit **before** they go through the Hub's submission route, and the
one table that shows which use-cases need which dataset and how far each is from being in the Hub.

```text
hub-submissions/
  matrix.csv                     dataset × use-case × route × Hub status (+ links) — generated
  build_matrix.py                generator; also writes the tracker's 'Use-case matrix' tab
  drafts/<record-id>/
    <record-id>.yaml             the CDH v0.5.x record (drafted by a person or an agent)
    example.py                   runnable example against the live source (federated records)
    verify-report.md             output of the cdh-metadata-verify skill (+ a hand-written '## Triage' section, kept on rerun)
    REVIEW.md                    human checklist for the authored fields (written once by the skill; the reviewer ticks it)
    SUBMISSION.md                written when submitted: `issue: <url>` of the cdh-catalog issue, then the PR / record URL
```

## Lifecycle

| status | meaning | who moves it |
| --- | --- | --- |
| `queued` | in a use-case queue (`<slug>/data/ingestion-queue.csv`), no record yet | use-case coordinator |
| `draft` | `drafts/<id>/<id>.yaml` exists; header comment says who/what drafted it and from which evidence | author (person or agent) |
| `verified` | `verify-report.md` with **HIGH 0** (or each HIGH triaged), every MED fixed or accepted with a reason, `REVIEW.md` ticked, and the YAML header says `reviewed by <name> <date>` | reviewer (Pete / Brayden / Andrés) |
| `submitted` | `SUBMISSION.md` carries the cdh-catalog issue URL; the bot opens the PR | author |
| `published` | record is live in `cdh-catalog` → the matrix links the catalog page | CDH review |
| `in data lake, no record` | data under `s3://digital-atlas/cdh/data/<id>/` but no catalog record yet | CDH team |

A draft is a draft: nothing here is authoritative for the Hub. The catalog is. AI-drafted records
say so in the first comment line of the YAML (`# drafted by <agent> on <date> from <inputs>; reviewed by <person> <date>`).
That header only lives here: the catalog keeps no AI marker in the metadata (agreed in
[cdh-catalog#74](https://github.com/CGIAR-Climate-Data-Hub/cdh-catalog/issues/74)). Instead, **every catalog PR
starts with an AI usage disclosure**: the level of AI help (AI-drafted / AI-assisted / none) and whether the
human author has reviewed it. `REVIEW.md` ends with a block to paste.

### Authored fields need a person

The standard lists some fields as *authored* — "a person, always": `title`, `description`, `note`,
`keywords`, `license`, `contact`, `citation`, units, caveats and every `cdh` field. A verifier can check
links, schema and data against the record, but not whether these are *right*. The ones that most need
a human with domain knowledge:

- **`cdh.usage.intended_uses`** — specific tasks at a stated scale, not "research" or "decision-making".
- **`cdh.usage.not_recommended_for`** — the misuses that would actually happen, each with a true `reason`
  and a `use_instead` that exists.
- **Limitations** — record-level `note`: coverage gaps, resolution or aggregation, artefacts, revisions,
  licence traps. The standard has no separate limitations field.
- **Assumptions** — `processing[].description` and `note`: modelled vs observed, thresholds, weighting,
  projections.

`REVIEW.md` lists each of these with the question to answer. The verifier's `authored` check flags an
AI-drafted record that nobody has reviewed, vague intended uses, not-recommended uses with no reason
or alternative, and a missing `note`.

## The matrix

`matrix.csv` is generated — edit the use-case queues, not the matrix:

```bash
python hub-submissions/build_matrix.py                                   # refresh matrix.csv
python hub-submissions/build_matrix.py --tracker "<CDH_data-ingestion v2.xlsx>" --write-tracker   # + tracker tab
```

Rows are **source datasets**, joined across the use-case queues, the tracker's *Priority Data*
sheet, `catalog.json` and the data-lake listing on a canonical key (`ALIASES` in the script —
add a spelling there when a new one appears). One dataset that two use-cases derive different
products from is one row with both flags and both products listed (e.g. ESA WorldCover: GCF
admin summaries + AgWise cropland-fraction grid). Columns: `GCF | AgWise | B4T | other`,
`products`, `route`, `hub_status`, `hub_record_url`, `lake_prefix`, `draft_record`,
`verify_report`, `submission_issue`, per-use-case `queue_status` and `priority`, licence, lead,
locations.

`priority-matrix.csv` (tracker tab **Priority matrix**) is the prioritised view: datasets rated P1/P2 by GCF or
AgWise, needed by the B4T CRI rebuild (verdicts from `public/b4t/cri-review.html`), or already held by the Hub;
columns `GCF | AgWise | B4T | PRISM` carry each use-case's rating, colour-coded, plus an overall priority and the
Hub link. PRISM (CIAT Dakar `prismpy`) needs are read from its code — `PRISM_NEEDS` in the script, 13 inputs across its CRAFT, PYTHIA, ACEA and SARRA-Py pipelines.

The tracker's **Use-case matrix** tab is the full table with hyperlinks; it replaced the per-use-case
tabs on 2026-10-08. Per-use-case detail (rescreen verdicts, serves codes, workflow columns) stays
in each `<slug>/data/ingestion-queue.csv`.

## Submission route (Hub side)

CDH Metadata Generator (or the `cdh-metadata` skill) → `cdh-catalog` "Submit metadata record"
issue → bot validates and opens the PR → CODEOWNER review → published. Run the
`cdh-metadata-verify` skill on the draft first; the bot only checks the schema.
