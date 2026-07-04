---
name: cri-modernization-review
version: 0.4.0
description: Review and modernize B4T Climate and Environmental Crop Risk Index (CRI) Appendix Table 1 datasets. Use this skill whenever the user asks to evaluate current CRI hazard datasets, identify open modern replacements, compare candidate climate datasets, verify whether a proposed dataset is objectively better, or update the B4T Appendix Table 1 modernization review. Always use this skill for row-by-row CRI dataset replacement work, especially when open access, authoritative alignment, citation quality, and hallucination-resistant verification matter.
---

# CRI Modernization Review

Use this skill for repeatable, guarded review of Appendix Table 1 in `Crop Risk Index-documentation v1.pdf`.

Primary goal:

- decide whether each current CRI dataset row should be `Replace`, `Keep`, `Clarify`, or `No open replacement confirmed`

Secondary goal:

- produce outputs that are both machine-auditable and easy for humans to review
- keep unknowns visible instead of inferred

## Files this skill uses

Read these first:

- `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/appendix-table-1-canonical-extract.csv`
- `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/dataset-inventory.csv`
- `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/bert-clarification-queue.csv`
- `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/evidence-index.csv`
- `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/modern-open-dataset-research-strategy.md`
- `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/modern-open-dataset-review-template.csv`
- `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/appendix-table-1-modernization-review.md`

Use these as current-state context:

- `/Users/pstewarda/Documents/rprojects/use-cases/b4t/BRIEF.md`
- `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/current-cri-formulation.md`

## Non-negotiable rules

Follow all of these:

- canonical Appendix extract is source of truth for row existence, row naming, row order, and source page
- treat each Appendix Table 1 row as separate review unit
- use primary sources first
- do not fill any field from memory
- never infer current-lineage metadata from a candidate dataset review
- keep period, scenario, CMIP generation, climate inputs, downscaling method, bias-correction method, and GCM list as separate fields
- if exact climate inputs are not evidenced, write `To do` or `Unclear`
- if an exact method or model list is required but not extracted, write `Blocked`
- write `N/A` only when the field truly does not apply
- do not recommend gated or paywalled datasets as replacement candidates
- do not call a dataset "better" unless reason is explicit and source-backed
- do not collapse uncertainty; surface it visibly
- do not derive row order from hazard grouping or code assumptions
- if markdown section order, table order, or CSV order conflicts with canonical Appendix extract, canonical extract wins

## Minimum pipeline

Every row review must move through this order:

1. `Appendix anchor`
2. `Current lineage audit`
3. `Bert blocker capture` if needed
4. `Improved option search`
5. `Verification`
6. `Adversarial challenge`
7. `Human-facing promotion`

If any upstream step is incomplete, downstream decision must stay at `Clarify`, `Blocked`, or `To do`.

## Required workflow

### Agent split

Use two agents / roles:

- `Current lineage audit`
- `Improved dataset options`

Current-lineage work updates current-state registry and Bert queue.
Improved-options work updates candidate-option registry.
Do not let improved-option evidence overwrite current-lineage evidence.

### Step 1. Define current CRI function

For current Appendix Table 1 row, capture:

- hazard group
- current dataset name
- current variable or proxy
- current reference period or horizon
- production-specific flag
- exact CRI function being served

Before any row work:

- match row to `annex_sequence` in `appendix-table-1-canonical-extract.csv`
- preserve canonical hazard label and row title
- preserve canonical Appendix order in all outputs

If exact function is unclear, stop recommendation work and mark `Clarify`.

### Step 2. Find candidate datasets

Search candidate datasets using:

- official steward pages
- steward technical documentation
- peer-reviewed source papers
- official repository or catalog entries

Prefer sources aligned with:

- WCRP / CMIP6
- IPCC assessment practice
- Copernicus / ECMWF
- FAO / WMO
- ISRIC
- WRI

Do not use tertiary summaries as final evidence.

### Step 3. Fill review template row

Populate one or more candidate rows in:

- `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/modern-open-dataset-review-template.csv`

Use one row per candidate option.
Keep at most `3` live options per current row unless user explicitly asks for more.

Minimum fields to fill when evidence exists:

- `current_cri_row`
- `hazard_group`
- `current_dataset_name`
- `current_function_in_cri`
- `candidate_dataset_name`
- `candidate_steward`
- `candidate_official_page_url`
- `candidate_direct_download_url`
- `candidate_access_open_ungated`
- `candidate_citation`
- `candidate_spatial_resolution_*`
- `candidate_temporal_*`
- `candidate_mip_era`
- `candidate_scenarios`
- `candidate_models`
- `candidate_baseline_period`
- `candidate_bias_adjustment`
- `candidate_processing_summary`
- `candidate_fit_to_cri_function`
- `objective_better_statement`
- `verification_status`

If field is unknown:

- enter `N/A`

For the compact Annex 1 registry in:

- `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/dataset-inventory.csv`

populate only explicit current-row evidence for:

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

Registry status rules:

- `Reviewed` means row-level lineage fields are materially evidenced
- `Unclear` means some evidence exists, but exact lineage or methods remain unresolved
- `Blocked` means exact method, GCM list, or access path is required and still missing
- `To do` means the row has not yet been investigated deeply enough

For missing current-state facts:

- save one short request in `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/bert-clarification-queue.csv`
- request must target exact missing item, not broad narrative

For source artifacts:

- if public methods paper or technical PDF exists, save local copy in repo evidence store
- else save screengrab of official source page
- index each artifact in `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/evidence-index.csv`
- reuse shared bundle ids for shared families such as `Aqueduct 4.0`, `Aqueduct Floods`, `GAEZ v5`, `WorldClim CMIP6`, `CHIRPS v3`
- set `request_scope` and `shared_request_key` in Bert queue when blocker applies to multiple rows

### Step 4. Verification pass

Run a verifier pass against filled row.

Verifier must:

- re-check important claims against source URLs
- confirm no field was inferred without evidence
- downgrade doubtful fields to `partially-verified`, `conflicted`, or `not-verified`

Important claims include:

- GCMs / model set
- exact GCM list, not just count
- baseline dataset and baseline period
- named baseline climate input, not just portal name
- climate model era
- scenario set
- spatial resolution
- temporal coverage
- bias adjustment / downscaling
- named bias-correction method, not just forcing family
- named downscaling method, not just platform family
- exact method / algorithm
- growing-season, onset-of-season, or threshold logic
- license / access
- direct download existence
- variable meaning

### Step 5. Adversarial challenge pass

Run an adversarial pass after verification.

Adversarial reviewer must assume recommendation may be wrong and try to break it.

Challenge questions:

- Is candidate actually like-for-like for CRI function?
- Is "better" evidenced or only implied?
- Does official source contradict paper or vice versa?
- Is access truly ungated?
- Did summary overstate steward authority?
- Did summary confuse baseline climatology with hazard-ready indicator?
- Did summary confuse data product with portal or service?

Record outcome in CSV fields:

- `adversarial_findings`
- `adversarial_status`
- `challenge_disposition`

If adversarial reviewer finds unresolved core problem:

- do not mark `Replace`
- downgrade compact-registry fields to `Blocked`, `Unclear`, or `To do` as needed

### Step 6. Promote into human-facing review

Once row is verified and challenged, update:

- `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/appendix-table-1-modernization-review.md`

Update all relevant sections:

- executive summary
- priority shortlist if appropriate
- row-level review block
- relevant hazard summary table

## What changed after workflow audit

These failure modes already happened once and must not recur:

- inferred Appendix order was used instead of exact Appendix extraction
- table order and markdown order drifted apart
- shared blockers were duplicated without shared keys
- candidate-method statements were sometimes stronger than current evidence justified

Workflow now assumes:

- canonical extract controls sequence
- row names in review outputs should trace back to canonical extract
- current-lineage and improved-option evidence remain separate
- shared family blockers should be grouped, not rewritten ad hoc

Every row-level review block must include explicit standardized sections for:

- `GCMs / models`
- `Baseline data / baseline period`
- `Downscaling method`
- `Bias correction method`
- `Exact method / algorithm`
- `Season onset / growing-season logic relevance`

If evidence is missing:

- write `To do`, `Unclear`, or `Blocked` as appropriate

### Step 7. Final recommendation rule

Use only these statuses:

- `Replace`
- `Keep`
- `Clarify`
- `No open replacement confirmed`

Decision rules:

- `Replace` only if candidate is open, ungated, like-for-like enough, and superiority statement is supported
- `Keep` if current dataset remains best-supported option
- `Clarify` if candidate looks promising but unresolved issue remains
- `No open replacement confirmed` if no verified candidate passes hard filters

## Output style

When reporting results to user:

- lead with decision
- name current dataset
- name best candidate if any
- state why candidate is better or why no replacement is justified
- state confidence
- state unresolved blocker if present

Do not dump raw CSV unless asked.

## Reusable prompt pattern

When invoked on a row, use this framing internally:

1. What exact CRI function does current row serve?
2. What open ungated candidate datasets could plausibly replace it?
3. What are exact GCMs, baseline data, baseline period, bias correction, and method details?
4. What evidence proves or disproves superiority?
5. What does adversarial review say?
6. What is final disposition?

## When to refuse recommendation

Refuse to recommend replacement when:

- evidence is too thin
- dataset access is gated
- variable meaning cannot be confirmed
- official and literature sources conflict materially
- candidate is not sufficiently like-for-like

In those cases, write:

- `Insufficient evidence to recommend replacement.`

If a blocker depends on information not accessible from current public-safe materials:

- state the blocker explicitly
- ask the user for assistance or for a source document pointer
