## Modern Open Dataset Research Strategy for B4T CRI

This note defines a guarded research process for replacing or retaining datasets listed in Appendix Table 1 of `Crop Risk Index-documentation v1.pdf`.

Goal: identify modern, open, usable datasets that are objectively better than current CRI inputs, or conclude that no such replacement is currently justified.

`N/A` is valid. No field should be filled from memory or guesswork.

## What workflow audit taught us

Main lessons from first pass:

- Appendix Table 1 itself must be extracted and stored as repo artifact before review work starts
- canonical row order cannot be inferred from hazard grouping or code family assumptions
- current-lineage audit and improved-option review need separate evidence tracks
- shared blockers such as `Aqueduct 4.0` or `Aqueduct Floods` should use shared request keys, not loosely duplicated row notes
- markdown section order, table order, and CSV order must all reconcile back to canonical Appendix extract

Current source-of-truth file:

- `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/appendix-table-1-canonical-extract.csv`

That file controls:

- row existence
- row naming
- row sequence
- source page reference

## Scope

Research unit is each dataset row in Appendix Table 1, not each broad hazard label. Some current CRI hazard groups mix multiple dataset types and time horizons. Review must therefore happen row by row.

Initial review scope:

- Drought
- Flooding
- Changed rainfall
- High temperature
- Salinity
- Soil water
- Irrigation

## Non-negotiables

Any proposed replacement must satisfy all hard filters below unless explicitly marked `candidate-but-ineligible`.

### Hard filters

- accessible without paywall
- accessible without mandatory account / login / request workflow
- stable download or API access URL exists
- documentation exists from official steward or repository
- citation exists from literature or formal technical documentation
- variable / indicator meaning is documented clearly enough to map to CRI use
- spatial and temporal characteristics can be verified from source

If any hard filter fails:

- do not recommend
- record reason
- keep current dataset under review or mark `no open replacement confirmed`

## Authority hierarchy

Preference order for evidence and stewardship:

1. IPCC-aligned or WCRP CMIP6-consistent datasets and official documentation
2. official intergovernmental or quasi-official stewards with open portals
   Examples: Copernicus, ECMWF, FAO, WMO, ISRIC, WRI
3. peer-reviewed datasets with clear public download and versioning
4. project pages or lab pages only when they expose methods and access clearly

Do not treat popularity or citation count alone as authority.

## Objective superiority tests

A replacement is only "better" when claim is tied to explicit evidence. At least one of these must be true, and none may be asserted without source support:

1. newer climate-model era
   Example target logic: `CMIP6` is better than pre-CMIP5 / CMIP5 for future-climate consistency when CRI objective is future breeding risk
2. closer alignment to authoritative practice
   Example target logic: dataset or workflow explicitly aligned with AR6 / CMIP6 or stewarded by bodies widely used in global climate assessments
3. better horizon consistency
   Example target logic: same scenario framework and comparable future periods across hazards
4. better spatial or temporal resolution
5. clearer methods and versioning
6. open and reproducible access
7. better variable fit to CRI construct
   Example: direct heat threshold metric better than indirect proxy when CRI hazard is heat stress

Every superiority statement must be written as:

`Proposed dataset is better than current dataset for [specific reason], supported by [source].`

Not allowed:

- `better overall`
- `more modern`
- `best available`

unless reasons and source-backed criteria are listed.

## Research workflow

### Pre-phase. Anchor row in canonical Appendix extract

Before any review:

- identify `annex_sequence`
- confirm row name against canonical Appendix extract
- confirm hazard group against canonical Appendix extract
- preserve Appendix order in all downstream outputs

If canonical extract and working registry disagree:

- fix working registry
- do not continue from conflicted row state

### Phase 1. Define current function

For each Appendix Table 1 row, capture:

- current hazard group
- current dataset / indicator
- current intended CRI function
- current variable or threshold logic
- current reference period / future horizon
- whether it is production-specific

Question to answer first:

`What exact CRI function must replacement preserve or improve?`

Do not search alternatives before this is written.

### Phase 2. Candidate discovery

Search only primary sources first:

- official dataset portal
- steward technical documentation
- peer-reviewed source paper
- repository or data catalog from steward

Secondary summaries can help locate sources, but cannot support final claims.

### Phase 3. Hard-filter screen

For each candidate, confirm:

- open ungated access
- direct data location
- license or terms
- GCMs / model set
- baseline data source
- baseline period
- spatial resolution
- temporal coverage
- exact method / algorithm
- season-onset, growing-season, or threshold logic if relevant
- bias correction / downscaling
- update / version information
- variable definitions

If unknown, enter `N/A`.

### Phase 4. CRI fit assessment

Assess whether candidate can replace current CRI function:

- same construct
- proximate construct
- weaker proxy
- not fit

Examples:

- replacing historic rainfall coefficient of variation with future CMIP6 variability product may improve future consistency
- replacing flood-event frequency with water-stress indicator is not a like-for-like flood replacement

### Phase 5. Superiority statement

Write one short statement per candidate:

- why it is better
- why it is not better
- or why evidence insufficient

### Phase 6. Verification pass

No row is accepted until second-pass review is complete.

### Phase 7. Adversarial challenge pass

After extractor and verifier finish, a separate AI review pass must actively try to break the recommendation.

Adversarial agent tasks:

- look for unsupported claims
- look for fields that were inferred rather than sourced
- check whether official source contradicts literature source
- challenge whether candidate is truly like-for-like for CRI function
- challenge whether "better" means objectively better, or only different
- challenge whether access is really ungated in practice
- challenge whether cited source actually says what summary claims it says

Adversarial prompt should be framed negatively, for example:

`Assume this recommendation may be wrong. Identify every claim that is unsupported, overstated, ambiguous, or contradicted by source evidence. Prefer rejection over acceptance when evidence is thin.`

No recommendation is final until adversarial comments are addressed.

## Guardrails against hallucination

### Field-level truth policy

Every factual field must have:

- source URL
- evidence type
- verification status

Allowed verification statuses:

- `verified`
- `partially-verified`
- `conflicted`
- `not-verified`
- `N/A`

### Claim policy

Allowed claim labels:

- `supported`
- `unsupported`
- `insufficient-evidence`
- `disputed`

If claim is unsupported or disputed, recommendation must not rely on it.

### Source policy

- prefer official steward page plus literature
- if official page lacks key metadata, add source paper or technical documentation
- if literature exists but no open access path exists, mark candidate ineligible
- if dataset is open but variable definition is unclear, mark `needs clarification`

### Review roles

Use three passes, even if all are AI-assisted:

1. extractor
   Fills candidate row strictly from source text

## Minimum artifact set per review cycle

Before calling row materially reviewed, repo should contain:

- canonical Appendix anchor row in `appendix-table-1-canonical-extract.csv`
- current-state row in `dataset-inventory.csv`
- improved-option row or explicit `No open replacement confirmed` in `modern-open-dataset-review-template.csv`
- evidence bundle entry in `evidence-index.csv`
- Bert blocker entry in `bert-clarification-queue.csv` when needed
- human-facing note in `appendix-table-1-modernization-review.md`

Improved-option row should also carry direct trace fields back to:

- canonical extract
- current inventory
- Bert queue
- evidence index

## Iterative restart loop

Recommended loop for restarting row review:

1. pick one canonical Appendix row
2. confirm current CRI function from canonical extract and methods text
3. audit current lineage only
4. save blockers and evidence artifacts
5. only then assess improved options
6. verify
7. adversarially challenge
8. promote to markdown
9. move to next row

Do not batch many unresolved rows into recommendation language first.
2. verifier
   Re-checks every filled field against linked source and flags unsupported claims
3. adversarial reviewer
   Attempts to falsify recommendation, find contradictory evidence, and detect hidden assumptions

Optional fourth pass:

4. decision auditor
   Confirms that recommendation uses only `verified` or `partially-verified` fields, that adversarial findings were resolved or left open visibly, and that any superiority statement is explicitly evidenced

### Failure conditions

Automatic `do not recommend` if:

- no direct public access path
- no steward documentation
- no clear variable definition
- future-scenario dataset but scenario / horizon unspecified
- only AI-generated or tertiary summaries available
- adversarial reviewer finds unsupported core claim that remains unresolved

## Minimum metadata to capture

Use CDH metadata standard as backbone. Relevant fields are drawn from:

- `templates/full-standard.yaml`
- `spec/authoring-guide.md`
- `spec/standard.md`

Practical subset for CRI review:

- `id`
- `title`
- `description`
- `resource_type`
- `license`
- `access`
- `citation`
- `doi`
- `keywords`
- `spatial.bbox`
- `spatial.crs`
- `spatial.resolution`
- `temporal.start_date`
- `temporal.end_date`
- `temporal.resolution`
- `variables`
- `dimensions`
- `climate.mip_era`
- `climate.scenarios`
- `climate.models`
- `climate.baseline`
- `climate.bias_adjustment`
- `climate.downscaling`
- `processing`
- `data.locations`
- `additional_links`

Additional B4T review fields needed beyond core CDH metadata:

- `current_cri_row`
- `hazard_group`
- `current_dataset_name`
- `candidate_fit`
- `production_specific`
- `authoritative_alignment`
- `open_ungated`
- `direct_download_url`
- `objective_better_statement`
- `objective_better_criteria`
- `verification_status`
- `adversarial_findings`
- `adversarial_status`
- `challenge_disposition`
- `reviewer_notes`

## Seed candidate families already justified for investigation

These are not final recommendations. They are starting points because evidence already supports at least part of their relevance.

### Multi-hazard future climate baselines and projections

- `WorldClim CMIP6`
 Why investigate:
  - official page states data are `CMIP6 downscaled future climate projections`
  - page states bias correction / calibration done against WorldClim v2.1 baseline
  - page lists `23` GCMs, `SSP1-2.6`, `SSP2-4.5`, `SSP3-7.0`, `SSP5-8.5`
  - page lists multiple spatial resolutions from `10 minutes` to `30 seconds`
  - page notes older downscaled `CMIP5` data are obsolete
  Use-case fit:
  - strong starting candidate for changed-rainfall and temperature replacements
  - possible climate backbone for harmonized future hazard derivation
  Caveat:
  - still need to test whether monthly climatologies are sufficient for each CRI hazard construct

### Official soil information

- `ISRIC / SoilGrids family`
  Why investigate:
  - official ISRIC stewardship
  - clearly global soil information platform
  Use-case fit:
  - likely candidate family for soil-water background layers
  Caveat:
  - exact variable match, open asset path, and resolution details still need row-level verification

### Flood products

- `Copernicus / GloFAS family`
  Why investigate:
  - official Copernicus emergency management stewardship
  Use-case fit:
  - possible modern open source for historical flood characterization
  Caveat:
  - accessibility, downloadable assets, and fit to CRI future flood function still need verification
  - do not assume eligibility yet

## Recommended work order

1. Review all Appendix Table 1 rows and map exact CRI function.
2. Build candidate register using template CSV.
3. Prioritize hazard groups with clearest replacement upside:
   - changed rainfall
   - high temperature
   - drought
   - flooding
4. Treat salinity, soil water, and irrigation separately because best open modern replacement may be weaker or `N/A`.
5. Only after row-level review, propose harmonized CRI v2 stack.

## Deliverables

Minimum outputs for this research stream:

1. candidate register CSV
2. source-evidence log
3. adversarial findings log
4. short recommendation memo per hazard group
5. explicit `keep / replace / clarify / no-open-replacement` decision for every Appendix Table 1 row

## Sources for this strategy

- CDH metadata standard README: <https://github.com/CGIAR-Climate-Data-Hub/cdh-metadata-standard>
- CDH full template: <https://raw.githubusercontent.com/CGIAR-Climate-Data-Hub/cdh-metadata-standard/main/templates/full-standard.yaml>
- CDH authoring guide: <https://raw.githubusercontent.com/CGIAR-Climate-Data-Hub/cdh-metadata-standard/main/spec/authoring-guide.md>
- CDH standard: <https://raw.githubusercontent.com/CGIAR-Climate-Data-Hub/cdh-metadata-standard/main/spec/standard.md>
- WorldClim CMIP6 page: <https://www.worldclim.org/data/cmip6/cmip6climate.html>
- WCRP CMIP6 overview: <https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6>
- IPCC AR6 Atlas landing page: <https://www.ipcc.ch/report/ar6/wg1/chapter/atlas/>
- ISRIC SoilGrids landing page: <https://www.isric.org/explore/soilgrids>
- Copernicus global flood portal: <https://global-flood.emergency.copernicus.eu/>

## Handover state as of 2026-07-02

This section is project-memory for restart and handover.

### Files that now act as source of truth

- canonical Appendix row list and order:
  - `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/appendix-table-1-canonical-extract.csv`
- current-lineage registry:
  - `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/dataset-inventory.csv`
- improved-option registry:
  - `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/modern-open-dataset-review-template.csv`
- blocker / clarification queue for Bert:
  - `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/bert-clarification-queue.csv`
- evidence bundle index:
  - `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/evidence-index.csv`
- human-facing synthesis:
  - `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/appendix-table-1-modernization-review.md`
- current CRI formulation note:
  - `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/current-cri-formulation.md`

### Exact status snapshot

- canonical Appendix rows captured: `23`
- current-lineage inventory rows captured: `23`
- improved-option rows captured: `23`
- Bert clarification requests logged: `23`
- evidence bundles indexed: `5`

Current-lineage status counts in `dataset-inventory.csv`:

- `Unclear`: `14`
- `Blocked`: `5`
- `To do`: `4`

Improved-option decision counts in `modern-open-dataset-review-template.csv`:

- `Clarify`: `11`
- `Keep`: `9`
- `No open replacement confirmed`: `3`

### What has materially advanced

- canonical Appendix Table 1 extraction is now stored in repo and should control all downstream ordering
- current-lineage registry and improved-option registry are split; they should not overwrite each other
- Bert queue is populated row by row, with shared request keys for repeated blockers such as `aqueduct-4-current-lineage`, `aqueduct-floods-current-lineage`, `legacy-ccafs-lgp-current-lineage`, and `legacy-ccafs-heat-current-lineage`
- evidence store structure exists and shared bundle pattern is defined in `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/evidence/README.md`
- `CHIRPS v3` bundle is only bundle currently beyond placeholder state:
  - `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/evidence/shared/chirps-v3/MANIFEST.md`
  - `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/evidence/shared/chirps-v3/README-CHIRPSv3.0.txt`
  - `/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/evidence/shared/chirps-v3/chirps-v3-scientific-data-2026.pdf`
- D-01 has deepest row-level improved-option review so far and is linked through evidence, queue, and markdown narrative

### Important cautions for next person

- do not infer row order from hazard family or code pattern; use canonical extract only
- do not let candidate-review evidence populate current-lineage fields unless source explicitly proves current operational lineage
- in compact tables, `Unclear`, `Blocked`, and `To do` are preferable to plausible but unproven dataset names
- keep period, scenario, CMIP generation, baseline dataset, future dataset, downscaling, bias correction, and GCM list as separate fields
- naming `Aqueduct 4.0`, `Aqueduct Floods`, `GAEZ v5`, `WorldClim CMIP6`, or `CHIRPS v3` alone is not enough; exact climate inputs, exact methods, and exact model lists still need extraction where those fields matter
- D-01 remains candidate-review progress, not proof of current CRI lineage; exact current drought formula, exact precipitation input, and exact SPI climatology baseline remain unresolved

### Preview / rendering state

Local review preview currently depends on temporary files outside repo:

- renderer:
  - `/private/tmp/render_b4t_review.mjs`
- rendered HTML:
  - `/tmp/b4t-review.html`

That preview work is useful for review, but it is not yet durable repo infrastructure.
Before long-term continuation, move renderer logic into versioned repo location so handover does not depend on temp paths.

### Recommended restart point

If work resumes:

1. keep current two-stream split:
   - current lineage
   - improved options
2. treat D-01 as worked example, not as proof that workflow is complete
3. next best row to deepen is `D-02` or another row with contained scope before returning to broad shared families
4. build missing shared evidence bundles for:
   - `Aqueduct 4.0`
   - `Aqueduct Floods`
   - `GAEZ v5`
   - `WorldClim CMIP6`
5. wait for Bert clarifications before upgrading current-lineage fields from `Unclear` or `Blocked`
6. only promote `Replace` when verification and adversarial challenge are complete and exact CRI-fit is demonstrated

### Minimal handover message

If someone needs one short brief:

`B4T CRI dataset modernization now has canonical Appendix control, split current-versus-candidate registries, full Bert blocker queue, and early evidence-store structure. Workflow is sounder than first pass, but row-level evidence remains thin. D-01 is strongest worked example. Most rows remain at Clarify, Unclear, Blocked, or seeded state pending exact lineage, methods, and model-list extraction.`
