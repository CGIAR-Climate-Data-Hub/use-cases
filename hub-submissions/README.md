# hub-submissions — pre-submission staging for Climate Data Hub records

Where draft metadata records sit **before** they go through the Hub's submission route, and the
one table that shows which use-cases need which dataset and how far each is from being in the Hub.

```text
hub-submissions/
  matrix.csv                     dataset × use-case × route × Hub status (+ links) — generated
  build_matrix.py                generator; also writes the tracker's 'Use-case matrix' tab
  drafts/<record-id>/
    <record-id>.yaml             the CDH v0.4.x record (drafted by a person or an agent)
    verify-report.md             output of the cdh-metadata-verify skill — must show HIGH 0 before submission
    SUBMISSION.md                written when submitted: `issue: <url>` of the cdh-catalog issue, then the PR / record URL
```

## Lifecycle

| status | meaning | who moves it |
| --- | --- | --- |
| `queued` | in a use-case queue (`<slug>/data/ingestion-queue.csv`), no record yet | use-case coordinator |
| `draft` | `drafts/<id>/<id>.yaml` exists; header comment says who/what drafted it and from which evidence | author (person or agent) |
| `verified` | `verify-report.md` present with **HIGH 0** and every MED either fixed or accepted with a reason | reviewer (Pete / Brayden / Andrés) |
| `submitted` | `SUBMISSION.md` carries the cdh-catalog issue URL; the bot opens the PR | author |
| `published` | record is live in `cdh-catalog` → the matrix links the catalog page | CDH review |
| `in data lake, no record` | data under `s3://digital-atlas/cdh/data/<id>/` but no catalog record yet | CDH team |

A draft is a draft: nothing here is authoritative for the Hub. The catalog is. AI-drafted records
say so in the first comment line of the YAML (`# drafted by <agent> on <date> from <inputs>; reviewed by <person> <date>`).

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

The tracker's **Use-case matrix** tab is this table with hyperlinks; it replaced the per-use-case
tabs on 2026-10-08. Per-use-case detail (rescreen verdicts, serves codes, workflow columns) stays
in each `<slug>/data/ingestion-queue.csv`.

## Submission route (Hub side)

CDH Metadata Generator (or the `cdh-metadata` skill) → `cdh-catalog` "Submit metadata record"
issue → bot validates and opens the PR → CODEOWNER review → published. Run the
`cdh-metadata-verify` skill on the draft first; the bot only checks the schema.
