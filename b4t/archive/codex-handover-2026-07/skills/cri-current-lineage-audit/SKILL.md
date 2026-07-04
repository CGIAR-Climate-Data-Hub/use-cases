---
name: cri-current-lineage-audit
version: 0.2.1
description: Audit what is currently used in B4T CRI Appendix Table 1. Use this skill when task is to identify exact current datasets, methods, baseline and future inputs, scenarios, GCMs, and unresolved gaps for inherited CRI rows, and to save short clarification requests for Bert Laenarts.
---

# CRI Current Lineage Audit

Use for current-state investigation only.

Primary outputs:

- use `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/appendix-table-1-canonical-extract.csv` as row-order and row-name source of truth
- update `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/dataset-inventory.csv`
- update `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/bert-clarification-queue.csv`
- update `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/evidence-index.csv`

Evidence capture:

- download public methods paper when stable public file exists
- else save screengrab of official source page
- save shared lineage docs once for shared families such as `Aqueduct 4.0`, `Aqueduct Floods`, `GAEZ v5`, `WorldClim CMIP6`, `CHIRPS v3`
- index every artifact in `evidence-index.csv`
- keep a `MANIFEST.md` inside each evidence bundle with source URLs, saved files, supported claims, and unresolved gaps

Rules:

- never start from current table display order; start from canonical Appendix extract
- do not infer current lineage from candidate review
- if exact current source, method, or model list is unknown, write `To do`, `Unclear`, or `Blocked`
- every blocked row must produce short Bert request in `bert-clarification-queue.csv`
- request must be short, specific, and answerable
- request should name the exact missing method fields rather than asking for general clarification
- use `request_scope = shared` and shared key when blocker clearly spans multiple rows

Current-state row minimum:

- `code`
- `review_agent_version`
- `resolution`
- `baseline_dataset`
- `baseline_period`
- `future_dataset`
- `future_period`
- `future_scenario`
- `cmip_version`
- `downscaling_method`
- `bias_correction_method`
- `gcm_ensemble_used`
- `evidence_status`
- `evidence_notes`

If shared methods doc applies:

- reuse shared bundle id
- do not create row-specific duplicate
