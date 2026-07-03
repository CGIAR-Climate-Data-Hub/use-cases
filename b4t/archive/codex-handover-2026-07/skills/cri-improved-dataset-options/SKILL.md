---
name: cri-improved-dataset-options
version: 0.2.1
description: Investigate improved open dataset options for B4T CRI Appendix Table 1. Use this skill when task is to identify, compare, and rank up to three candidate replacement options for each CRI row, with evidence links, methods documentation, and adversarial verification.
---

# CRI Improved Dataset Options

Use for improved-option investigation only.

Primary outputs:

- use `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/appendix-table-1-canonical-extract.csv` for canonical row names and sequence
- update `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/modern-open-dataset-review-template.csv`
- update `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/evidence-index.csv`

Option rules:

- capture up to `3` options per current row when no single option is clearly superior
- use one CSV row per option
- keep options ranked
- if only one option survives review, keep only ranked option `1`

Evidence capture:

- prefer public methods paper or official technical document download
- if no stable public document exists, save screengrab of official page
- reuse shared lineage docs once for shared families
- index every artifact in `evidence-index.csv`
- keep a `MANIFEST.md` inside each evidence bundle with source URLs, saved files, verified claims, and unresolved gaps

Verification rules:

- no recommendation from memory
- exact GCM list required when claimed
- exact named downscaling method required when claimed
- exact named bias-correction method required when claimed
- if claim cannot be evidenced, downgrade field or row
- if current CRI function itself is unclear, do not promote candidate above `Clarify`

Improved-option row should record:

- canonical Appendix anchor ref
- current inventory ref
- Bert blocker ref when current-lineage uncertainty exists
- evidence-index ref
- local evidence manifest path
- candidate rank
- candidate dataset name
- steward
- official page
- direct download
- methods / evidence bundle
- scenarios
- CMIP generation
- GCM list
- baseline period
- fit to CRI function
- decision status

If multiple options remain live:

- explain why no single option is clearly superior
- keep all live options within top `3`
