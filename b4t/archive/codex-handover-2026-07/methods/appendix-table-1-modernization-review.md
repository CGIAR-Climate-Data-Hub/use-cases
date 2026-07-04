## Appendix Table 1 Modernization Review

## 0) Introduction

This document supports modernization of Appendix Table 1 in `Crop Risk Index-documentation v1.pdf` for the B4T use-case and links directly to the public-facing [B4T brief](../BRIEF.md). The wider problem is not only dataset age. It is also lineage ambiguity, mixed time horizons, inconsistent climate-scenario framing, unclear model provenance, and weak reproducibility across parts of the current CRI stack. Those issues can reduce technical credibility, make ingestion into the Climate Data Hub harder, and weaken confidence in downstream risk interpretation.

The Climate Data Hub is trying to help by turning inherited CRI inputs into documented, reviewable, and ingestible dataset choices. That means identifying better-supported open datasets, recording where evidence is still incomplete, and separating dataset problems from methodological problems. If done well, this work enables cleaner ingestion decisions, more credible communication with B4T and reviewers, and a later old-versus-new comparison once replacement candidates are implemented.

This document is for B4T domain leads, the CDH technical team, methods reviewers, and data providers. It is designed to support practical decisions:

- which current inputs are acceptable to retain for now
- which current inputs need clarification before any recommendation
- which modern dataset families should be prepared for CDH ingestion
- which questions should be routed back to B4T methods owners before deeper implementation

Use this document in five passes:

1. scan current-state table for what B4T appears to use today
2. scan improved-options table for up to three viable replacements where relevant
3. route unresolved current-state gaps through Bert clarification queue
4. use detailed row reviews to judge evidence for each variable
5. translate agreed recommendations into CDH ingestion and comparison tasks

Do not use this file as field-level source-of-truth. The compact Annex 1 table is rendered from explicit registry fields in:

- [dataset-inventory.csv](./dataset-inventory.csv)

Candidate-review notes and challenge findings remain in:

- [modern-open-dataset-review-template.csv](./modern-open-dataset-review-template.csv)

Canonical Appendix row order and row wording now live in:

- [appendix-table-1-canonical-extract.csv](./appendix-table-1-canonical-extract.csv)

### 0.1 Workflow review and restart protocol

First pass showed three structural failure points:

- Appendix order was inferred instead of extracted
- current-lineage and improved-option evidence could drift into each other
- shared blockers were not grouped cleanly enough for follow-up

Current workflow now assumes:

1. start from canonical Appendix extract
2. audit current lineage first
3. log exact shared or row-level blocker for Bert where needed
4. assess improved options only after current function is pinned down
5. verify claims
6. run adversarial challenge
7. promote only challenged outputs into tables and row notes

Iterative loop should therefore be one Appendix row at a time, not one broad hazard at a time.

## 1) Dataset Modernization and Harmonization

This section focuses on dataset choice, dataset lineage, and dataset harmonization. The specific problem is that Appendix Table 1 currently mixes historic and future inputs with uneven documentation for baseline datasets, future datasets, CMIP generation, SSP framing, GCM ensemble choice, downscaling, and bias correction. In practice, that can create avoidable uncertainty about whether the CRI is technically up to date, whether different hazards are comparable, and whether the resulting indicators are credible enough for Hub publication and external scrutiny.

The goal of this section is concrete: produce recommendations for which dataset families should be retained, clarified, or prepared for inclusion in the Climate Data Hub so B4T can run the CRI on a better-documented and more defensible footing. Two linked investigations are needed. One asks what B4T is using now. The other asks what open improved options should replace or complement those inputs. Where resources allow later, this section should also support an old-versus-new comparison so inherited inputs and proposed replacements can be tested side by side.

### 1.1 Current dataset investigation

Canonical Appendix 1 extract for ordering and source-grounding: [appendix-table-1-canonical-extract.csv](/Users/pstewarda/Documents/rprojects/use-cases/b4t/methods/appendix-table-1-canonical-extract.csv)

Caption: Compact overview of Annex 1 Table 1 variables rendered from current-state registry fields. Order should follow the canonical Appendix 1 extract above, not inferred hazard grouping. Unknown fields are shown as `To do`, `Unclear`, or `Blocked` on purpose rather than inferred from partial evidence. Use this table to audit what B4T appears to use now and where Bert clarification is still needed.

[[CURRENT_DATASET_TABLE]]

### 1.2 Improved dataset options investigation

Caption: Compact overview of improved open dataset options under review. Use one row per option and keep up to `3` options for any current CRI row when no single option is clearly superior. Shared methods bundles should be reused rather than duplicated.

[[IMPROVED_DATASET_TABLE]]

### 1.3 Outstanding questions for Bert

These questions should be resolved early because they affect credibility, comparability, and whether CDH can ingest replacement-ready datasets with confidence. Until a B4T-specific clarification issue form exists, use the repository `Add a dataset to a use-case` issue form with `slug = b4t` and an item-specific title so responses can still be captured in a structured way.

| Clarification item | Why it matters | Issue capture | Current action |
| --- | --- | --- | --- |
| High-temperature row `LGP-linked temperature stress` | Appendix wording appears to duplicate the changed-rainfall LGP proxy, so the actual CRI variable may not be distinct. | [Open issue form](https://github.com/CGIAR-Climate-Data-Hub/use-cases/issues/new?template=add-dataset.yml&title=%5BDataset%5D%20b4t%3A%20Clarify%20LGP-linked%20temperature%20stress%20row) | Resolve methods meaning before dataset recommendation |
| Exact climate inputs for Aqueduct rows | Saying `Aqueduct 4.0` is not enough; CRI review needs the named baseline and future climate inputs behind the selected layers. | [Open issue form](https://github.com/CGIAR-Climate-Data-Hub/use-cases/issues/new?template=add-dataset.yml&title=%5BDataset%5D%20b4t%3A%20Clarify%20Aqueduct%20climate%20inputs) | Hold climate-lineage fields at `To do` or `Blocked` until source lineage is extracted |
| Exact GAEZ future LGP threshold assets | Both changed-rainfall rows depend on proof that threshold-specific future LGP layers are openly accessible and like-for-like enough. | [Open issue form](https://github.com/CGIAR-Climate-Data-Hub/use-cases/issues/new?template=add-dataset.yml&title=%5BDataset%5D%20b4t%3A%20Clarify%20GAEZ%20future%20LGP%20threshold%20assets) | Keep GAEZ v5 under review, hold rows at `Clarify` |
| Exact GCM lists and named downscaling / bias-correction methods for all future rows | CRI review cannot treat `CMIP6`, `ISIMIP3b`, or a portal name as a substitute for the exact model list or the actual method name. | [Open issue form](https://github.com/CGIAR-Climate-Data-Hub/use-cases/issues/new?template=add-dataset.yml&title=%5BDataset%5D%20b4t%3A%20Clarify%20future-row%20GCMs%20and%20methods) | Keep these fields at `Blocked` unless the exact names are extracted from source evidence |
| Growing-season derivation for heat threshold row | WorldClim provides open CMIP6 `tmax`, but not CRI-ready growing-season threshold layers. | [Open issue form](https://github.com/CGIAR-Climate-Data-Hub/use-cases/issues/new?template=add-dataset.yml&title=%5BDataset%5D%20b4t%3A%20Clarify%20growing-season%20heat%20derivation) | Document derivation need explicitly |
| Global fit of CHIRPS v3 for drought row | Reviewed official coverage is `60N` to `60S`, so global CRI fit is not yet proven. | [Open issue form](https://github.com/CGIAR-Climate-Data-Hub/use-cases/issues/new?template=add-dataset.yml&title=%5BDataset%5D%20b4t%3A%20Clarify%20CHIRPS%20global%20fit%20for%20drought) | Keep as lead drought-input family, do not recommend replacement yet |
| Aqueduct horizon mismatch | Several rows already use modern Aqueduct families, but current CRI slices still mix `2030` with `2050` hazard framing. | [Open issue form](https://github.com/CGIAR-Climate-Data-Hub/use-cases/issues/new?template=add-dataset.yml&title=%5BDataset%5D%20b4t%3A%20Clarify%20Aqueduct%20horizon%20mismatch) | Treat as harmonization issue, not immediate source replacement |
| Thin public evidence for some soil-water and irrigation rows | Several cited modern sources still lack verified open access paths in this review pass. | [Open issue form](https://github.com/CGIAR-Climate-Data-Hub/use-cases/issues/new?template=add-dataset.yml&title=%5BDataset%5D%20b4t%3A%20Clarify%20soil-water%20and%20irrigation%20source%20access) | Keep affected rows at `Clarify` or `No open replacement confirmed` |

Structured queue file:

- [bert-clarification-queue.csv](./bert-clarification-queue.csv)

Shared evidence index:

- [evidence-index.csv](./evidence-index.csv)

Evidence storage rules:

- store public methods paper when available
- otherwise store screengrab of official page
- reuse shared bundles for shared dataset families such as `Aqueduct 4.0`

### 1.4 Detailed Dataset Review and Recommendations

This section is the deep-dive layer for each Annex 1 Table 1 variable. Use it when the compact table is not enough and a row needs closer scrutiny. Each entry records what the current CRI function is trying to do, what is known or unknown about the current dataset lineage, what modern open candidate family was reviewed, what evidence supports or weakens that candidate, and whether CDH should move toward ingestion, hold for clarification, or avoid making a replacement claim.

### Drought

#### `D-01` `Drought` `Standardized Precipitation Index (SPI)`

**Current CRI function**

Estimate average number of drought events per year per pixel using three consecutive months with less than `50 percent` of average precipitation.

**Current dataset**

- Dataset name / version: `Legacy CCAFS / Thornton drought proxy layer`; exact file name and version unverified
- Underlying climate datasets used if any - Baseline / Future (if any): baseline precipitation source unverified from reviewed public-safe materials; no future climate dataset used in current historic row
- Baseline period: `1974-2004` analysis window for current CRI row; exact SPI climatology baseline unverified
- Future period: `N/A`
- SSPs used: `N/A`
- Ensemble used + GCMs: `N/A`
- Downscaling method: `N/A`
- Bias correction method: `N/A`
- Resolution: `Unverified`
- Reference period / horizon: `1974-2004`
- Production-specific: `No`
- Main concern: legacy historic drought proxy from older CCAFS lineage with unclear reproducibility and no direct path to CRI-wide future horizon alignment

**Best candidate**

- Dataset: `CHIRPS v3 3-monthly precipitation for SPI-style drought derivation`
- Official page: `https://www.chc.ucsb.edu/data/chirps3`
- Direct access: `https://data.chc.ucsb.edu/products/CHIRPS/v3.0/3-monthly/global/`
- Citation: `Funk et al. 2026 Scientific Data paper; CHIRPS v3 official steward page`
- Spatial resolution: `0.05 degree (~5 km)`
- Temporal coverage: `1981` to `near-present`
- Climate era / scenarios: `Historical / monitoring product`, not a future scenario dataset

**Traceability**

- Canonical Appendix row: `appendix-table-1-canonical-extract.csv#annex_sequence=1`
- Current-state inventory row: `dataset-inventory.csv#code=D-01`
- Bert clarification request: `bert-clarification-queue.csv#request_id=bert-b4t-001`
- Shared evidence bundle: `evidence-index.csv#evidence_bundle_id=chirps-v3-shared-methods`
- Saved evidence manifest: `b4t/methods/evidence/shared/chirps-v3/MANIFEST.md`
- Saved official README: `b4t/methods/evidence/shared/chirps-v3/README-CHIRPSv3.0.txt`
- Saved open methods paper: `b4t/methods/evidence/shared/chirps-v3/chirps-v3-scientific-data-2026.pdf`

**Method provenance**

- GCMs / models: `N/A`
- Baseline data / baseline period: `CHIRPS v3 precipitation time series`; `1981` to `near-present`; exact SPI baseline definition not verified
- Bias correction / downscaling: `N/A` from reviewed source page
- Exact method / algorithm: saved README and open methods paper state CHIRPS v3 combines climatology, thermal infrared satellite observations, and station observations; candidate is still not a precomputed SPI event-frequency layer, so CRI-equivalent derivation would need explicit implementation of three consecutive months below `50 percent` of average precipitation
- Season onset / growing-season logic relevance: current row is drought-event logic, not onset-of-season logic; reviewed source does not provide CRI-ready failed-season or event-frequency algorithm

**Decision**

- Status: `Clarify`
- Confidence: `Low`

**Why this decision**

CHIRPS v3 is strongest drought-input candidate reviewed so far because the official steward page states it is a public-domain, `0.05` degree precipitation product spanning more than `40` years, with improved station density and better variance trends than `CHIRPS v2`, and the official data service exposes direct open `3-monthly` products that align more closely with the current CRI drought-event logic than the legacy inherited layer. But current evidence still does not prove that CHIRPS v3 is a direct like-for-like replacement for the existing CRI SPI event-frequency layer. It is a precipitation input family, not a precomputed hazard layer, and the reviewed official page states coverage from `60N` to `60S`, which may not fully match the global CRI footprint.

**Evidence-backed superiority statement**

CHIRPS v3 is better than the legacy Ericksen et al. 2011 SPI lineage for modernization review because the official steward page states it is a public-domain, `0.05` degree, `40+` year precipitation product with improved station density and variance performance relative to `CHIRPS v2`, and the official data directory exposes direct open `3-month` products that are closer to the current drought-event logic; exact CRI-equivalent drought-event derivation remains unverified.

**Limitations**

- candidate is precipitation input family, not precomputed SPI event-frequency layer
- current CRI row uses specific three-month drought-event logic rather than standard SPI alone
- reviewed official coverage is `60N` to `60S`, not confirmed as fully global
- candidate remains historical / near-present and does not solve future-horizon alignment by itself
- no separate authority-level endorsement beyond steward documentation was confirmed in this pass

**Verification**

- Verification status: `partially-verified`
- Primary sources checked:
  - `https://www.chc.ucsb.edu/data/chirps3`
  - `https://data.chc.ucsb.edu/products/CHIRPS/v3.0/3-monthly/global/`
  - `https://data.chc.ucsb.edu/products/CHIRPS/v3.0/README-CHIRPSv3.0.txt`
  - `https://www.nature.com/articles/s41597-026-07096-4.pdf`

**Adversarial challenge**

- Challenge summary: CHIRPS v3 is clearly open and modern as a precipitation input family, but it is not a direct like-for-like replacement for the CRI SPI event-frequency layer. It also does not cover poleward areas outside `60N` to `60S` and does not by itself address future hazard alignment.
- Challenge status: `major unresolved issue`
- Disposition: `Do not replace yet. Keep CHIRPS v3 as lead drought-input candidate family for follow-up and leave row at Clarify.`

#### `D-02` `Drought` `Failed season`

_Expanded row block not yet written. Use the Drought summary table and audited CSV for the current review disposition._

#### `D-03` `Drought` `Available blue water`

_Expanded row block not yet written. Use the Drought summary table and audited CSV for the current review disposition._

#### `D-04` `Drought` `Gross water demand and net consumption`

_Expanded row block not yet written. Use the Drought summary table and audited CSV for the current review disposition._

#### `D-05` `Drought` `Baseline water stress`

_Expanded row block not yet written. Use the Drought summary table and audited CSV for the current review disposition._

### Flooding

#### `F-01` `Flooding` `Dartmouth flood frequency`

_Expanded row block not yet written. Use the Flooding summary table and audited CSV for the current review disposition._

#### `F-02` `Flooding` `River flood hazard`

_Expanded row block not yet written. Use the Flooding summary table and audited CSV for the current review disposition._

#### `F-03` `Flooding` `Coastal flood hazard`

_Expanded row block not yet written. Use the Flooding summary table and audited CSV for the current review disposition._

### Changed rainfall

#### `R-01` `Changed rainfall` `LGP flip over 120 days`

**Current CRI function**

Identify areas where length of growing period shifts from greater than `120` days per year to less than `120` days by `2050` as a changed-rainfall hazard threshold.

**Current dataset**

- Dataset name / version: `Legacy CCAFS / Thornton LGP threshold-flip layer`; exact file name and version unverified
- Underlying climate datasets used if any - Baseline / Future (if any): exact baseline and future climate inputs unverified from reviewed public-safe materials; climate-model lineage for operational B4T layer remains unclear
- Baseline period: `Unverified`
- Future period: `2050`
- SSPs used: `Unverified`
- Ensemble used + GCMs: `Unverified`
- Downscaling method: `Unverified`
- Bias correction method: `Unverified`
- Resolution: `Unverified`
- Reference period / horizon: `2050`
- Production-specific: `No`
- Main concern: legacy future threshold layer from Ericksen 2011 lineage; modernization need is driven by older climate-model lineage and CRI-wide horizon inconsistency

**Best candidate**

- Dataset: `GAEZ v5 agro-climatic resource / future climate layers`
- Official page: `https://www.fao.org/gaez/en/`
- Direct access: `https://data.apps.fao.org/gaez/`
- Citation: `FAO & IIASA. 2025. Global Agro-ecological Zoning version 5 (GAEZ v5) Model Documentation.`
- Spatial resolution: `30 arc-seconds (~1 km) for key outputs`, but model documentation also refers to `5 arc-minutes` for large spatial data holdings
- Temporal coverage: `2021-2040`, `2041-2060`, `2061-2080`, `2081-2100`
- Climate era / scenarios: `CMIP6`; `SSP1-2.6`, `SSP3-7.0`, `SSP5-8.5`

**Method provenance**

- GCMs / models: `Blocked`; exact GCM list for the reviewed future asset was not extracted in this pass
- Baseline data / baseline period: `Unclear`; reviewed notes suggest `AgERA5` may be involved in the broader candidate family, but the exact baseline linkage for this row was not proven from the source pack used here
- Downscaling method: `Blocked`; exact named downscaling method for the reviewed threshold-flip asset was not extracted
- Bias correction method: `Blocked`; reviewed notes indicate updated future forcing, but they do not yet give a trustworthy method name for this row-level asset
- Exact method / algorithm: reviewed public sources confirm GAEZ v5 agro-climatic analysis framework and future LGP-related indicators at system level, but exact public algorithm for CRI-style `LGP >120 -> <120` threshold-flip layer was not extracted in this pass
- Season onset / growing-season logic relevance: `Blocked`; reviewed public sources did not yet confirm exact onset-of-season, perhumid, or arid-region handling used to derive this specific threshold-flip construct

**Decision**

- Status: `Clarify`
- Confidence: `Low`

**Why this decision**

GAEZ v5 remains the strongest candidate family reviewed so far because FAO and IIASA present it as an updated open-access agro-climatic platform tied to a more modern future-climate workflow than the legacy Ericksen 2011 lineage. But this review pass did not extract the exact GCM list, exact named bias-correction method, exact named downscaling method, or the exact open threshold-flip asset for this row. Replacement therefore cannot yet be recommended.

**Evidence-backed superiority statement**

Proposed dataset family appears better than the current legacy lineage for modernization review because FAO and IIASA present GAEZ v5 as a newer open-access platform with future-climate support and finer published output options; exact replacement equivalence for the CRI LGP threshold layer remains unverified.

**Limitations**

- exact future LGP threshold-flip layer not yet verified
- exact file-level ungated download URL not yet verified
- reviewed sources do not yet confirm exact variable naming for this row
- resolution evidence is internally mixed between `30 arc-seconds` and `5 arc-minutes`
- license not yet confirmed from reviewed sources

**Verification**

- Verification status: `partially-verified`
- Primary sources checked:
  - `https://www.fao.org/gaez/en/`
  - `https://github.com/un-fao/gaezv5/wiki`

**Adversarial challenge**

- Challenge summary: modern CMIP6-based platform status is supported, but like-for-like row replacement is not yet proven; direct open access to exact future LGP threshold-flip asset remains unresolved
- Challenge status: `major unresolved issue`
- Disposition: `Do not replace yet. Keep GAEZ v5 as lead candidate family for follow-up and leave row at Clarify.`

#### `R-02` `Changed rainfall` `LGP flip over 90 days`

**Current CRI function**

Identify areas where length of growing period shifts from greater than `90` days per year to less than `90` days by `2050` as a changed-rainfall hazard threshold.

**Current dataset**

- Dataset name / version: `Legacy CCAFS / Thornton LGP threshold-flip layer`; exact file name and version unverified
- Underlying climate datasets used if any - Baseline / Future (if any): exact baseline and future climate inputs unverified from reviewed public-safe materials; climate-model lineage for operational B4T layer remains unclear
- Baseline period: `Unverified`
- Future period: `2050`
- SSPs used: `Unverified`
- Ensemble used + GCMs: `Unverified`
- Downscaling method: `Unverified`
- Bias correction method: `Unverified`
- Resolution: `Unverified`
- Reference period / horizon: `2050`
- Production-specific: `No`
- Main concern: legacy future threshold layer from Ericksen 2011 lineage; modernization need is driven by older climate-model lineage and CRI-wide horizon inconsistency

**Best candidate**

- Dataset: `GAEZ v5 agro-climatic resource / future climate layers`
- Official page: `https://www.fao.org/gaez/en/`
- Direct access: `https://data.apps.fao.org/gaez/`
- Citation: `FAO & IIASA. 2025. Global Agro-ecological Zoning version 5 (GAEZ v5) Model Documentation.`
- Spatial resolution: `30 arc-seconds (~1 km) for key outputs`, but model documentation also refers to `5 arc-minutes` for large spatial data holdings
- Temporal coverage: `2021-2040`, `2041-2060`, `2061-2080`, `2081-2100`
- Climate era / scenarios: `CMIP6`; `SSP1-2.6`, `SSP3-7.0`, `SSP5-8.5`

**Method provenance**

- GCMs / models: `Blocked`; exact GCM list for the reviewed future asset was not extracted in this pass
- Baseline data / baseline period: `Unclear`; reviewed notes suggest `AgERA5` may be involved in the broader candidate family, but the exact baseline linkage for this row was not proven from the source pack used here
- Downscaling method: `Blocked`; exact named downscaling method for the reviewed threshold-flip asset was not extracted
- Bias correction method: `Blocked`; reviewed notes indicate updated future forcing, but they do not yet give a trustworthy method name for this row-level asset
- Exact method / algorithm: reviewed public sources confirm GAEZ v5 agro-climatic analysis framework and future LGP-related indicators at system level, but exact public algorithm for CRI-style `LGP >90 -> <90` threshold-flip layer was not extracted in this pass
- Season onset / growing-season logic relevance: `Blocked`; reviewed public sources did not yet confirm exact onset-of-season, perhumid, or arid-region handling used to derive this specific threshold-flip construct

**Decision**

- Status: `Clarify`
- Confidence: `Low`

**Why this decision**

GAEZ v5 is again the strongest candidate family reviewed so far because FAO and IIASA present it as an updated open-access agro-climatic platform tied to a more modern future-climate workflow than the legacy Ericksen 2011 lineage. But this review pass did not extract the exact GCM list, exact named bias-correction method, exact named downscaling method, or the exact open threshold-flip asset for this row. Replacement therefore cannot yet be recommended.

**Evidence-backed superiority statement**

Proposed dataset family appears better than the current legacy lineage for modernization review because FAO and IIASA present GAEZ v5 as a newer open-access platform with future-climate support and finer published output options; exact replacement equivalence for the CRI `90`-day LGP threshold layer remains unverified.

**Limitations**

- exact future LGP threshold-flip layer not yet verified
- exact file-level ungated download URL not yet verified
- reviewed sources do not yet confirm exact variable naming for this row
- resolution evidence is internally mixed between `30 arc-seconds` and `5 arc-minutes`
- license not yet confirmed from reviewed sources

**Verification**

- Verification status: `partially-verified`
- Primary sources checked:
  - `https://www.fao.org/gaez/en/`
  - `https://github.com/un-fao/gaezv5/wiki`

**Adversarial challenge**

- Challenge summary: modern CMIP6-based platform status is supported, but like-for-like row replacement is not yet proven; direct open access to exact future LGP threshold-flip asset remains unresolved
- Challenge status: `major unresolved issue`
- Disposition: `Do not replace yet. Keep GAEZ v5 as lead candidate family for follow-up and leave row at Clarify.`

#### `R-03` `Changed rainfall` `Annual rainfall coefficient of variation`

_Expanded row block not yet written. Use the Changed rainfall summary table and audited CSV for the current review disposition._

#### `R-04` `Changed rainfall` `Intra-annual variability`

_Expanded row block not yet written. Use the Changed rainfall summary table and audited CSV for the current review disposition._

#### `R-05` `Changed rainfall` `Seasonal variability`

_Expanded row block not yet written. Use the Changed rainfall summary table and audited CSV for the current review disposition._

### High temperature

#### `T-01` `High temperature` `Extreme humid heat days`

_Expanded row block not yet written. Use the High temperature summary table and audited CSV for the current review disposition._

#### `T-03` `High temperature` `LGP-linked temperature stress`

_Expanded row block not yet written. Use the High temperature summary table and audited CSV for the current review disposition._

#### `T-02` `High temperature` `Growing-season Tmax flip over 30C`

**Current CRI function**

Identify areas where average maximum daily temperature shifts from less than `30 C` to greater than `30 C` during the primary growing season, masked where length of growing period is greater than `40` days.

**Current dataset**

- Dataset name / version: `Legacy CCAFS / Thornton growing-season heat threshold layer`; exact file name and version unverified
- Underlying climate datasets used if any - Baseline / Future (if any): exact baseline and future climate inputs unverified from reviewed public-safe materials; no confirmed evidence yet for exact model family used in operational B4T layer
- Baseline period: `Unverified`
- Future period: `2050`
- SSPs used: `Unverified`
- Ensemble used + GCMs: `Unverified`
- Downscaling method: `Unverified`
- Bias correction method: `Unverified`
- Resolution: `Unverified`
- Reference period / horizon: `2050`
- Production-specific: `No`
- Main concern: legacy threshold layer from older CCAFS / Thornton lineage; modernization need is driven by older climate-model basis and weak direct reproducibility

**Best candidate**

- Dataset: `WorldClim CMIP6 future climate monthly maximum temperature`
- Official page: `https://www.worldclim.org/data/cmip6/cmip6climate.html`
- Direct access: `https://geodata.ucdavis.edu/cmip6/30s/ACCESS-CM2/ssp245/wc2.1_30s_tmax_ACCESS-CM2_ssp245_2041-2060.tif`
- Citation: `WorldClim future climate data page; WCRP CMIP6 overview page`
- Spatial resolution: `30 arc-seconds (~1 km)` for reviewed direct-download example
- Temporal coverage: `2021-2040`, `2041-2060`, `2061-2080`, `2081-2100`
- Climate era / scenarios: `CMIP6`; `SSP1-2.6`, `SSP2-4.5`, `SSP3-7.0`, `SSP5-8.5`

**Method provenance**

- GCMs / models: `Blocked`; reviewed source pages indicate multiple GCMs, but the exact list relevant to the intended B4T use was not extracted in this pass
- Baseline data / baseline period: `WorldClim v2.1 baseline climate`; exact baseline-year range for the reviewed use path was not separately captured in this pass
- Downscaling method: `Unclear`; the official page states the data are downscaled, but the named method was not extracted into the current evidence pack
- Bias correction method: `Unclear`; the official page links the product to `WorldClim v2.1` baseline climate, but the exact method name used for correction / calibration was not extracted in this pass
- Exact method / algorithm: official product provides monthly `tmax` climatologies, not precomputed CRI growing-season threshold-flip layer
- Season onset / growing-season logic relevance: `Blocked`; primary growing-season logic and `LGP > 40` mask would need separate derivation

**Decision**

- Status: `Clarify`
- Confidence: `Low`

**Why this decision**

WorldClim is a strong modernization candidate family because its official page presents an open `CMIP6` future-climate product at multiple resolutions and explicitly positions the older downscaled `CMIP5` product as obsolete. That clearly improves the climate-model era and openness relative to the legacy CRI layer. But the current CRI row is not simply monthly maximum temperature. It is a growing-season threshold-flip indicator using primary growing season logic and an `LGP > 40` mask. Current evidence does not yet show that WorldClim directly provides that indicator, and this pass did not extract the exact GCM list or exact named methods needed for a stronger provenance claim.

**Evidence-backed superiority statement**

WorldClim CMIP6 monthly maximum temperature appears better than the legacy Ericksen et al. 2011 growing-season heat threshold layer for modernization review because the official WorldClim page presents a newer open `CMIP6` climate product with direct file links and explicitly notes the older downscaled `CMIP5` product is obsolete; exact CRI-equivalent growing-season threshold derivation remains unverified.

**Limitations**

- candidate is monthly `tx`, not precomputed growing-season threshold-flip layer
- primary growing season logic is not embedded in reviewed product page
- `LGP > 40` masking would need separate derivation or companion layer
- direct file URL is exposed, but file retrieval was not independently completed in this pass
- dataset-specific license not separately captured in this pass

**Verification**

- Verification status: `partially-verified`
- Primary sources checked:
  - `https://www.worldclim.org/data/cmip6/cmip6climate.html`
  - `https://wcrp-cmip.org/cmip-phases/cmip6/`

**Adversarial challenge**

- Challenge summary: modern CMIP6 and direct open access are supported, but candidate is not direct like-for-like replacement because CRI row requires growing-season threshold logic rather than raw monthly `tx`
- Challenge status: `major unresolved issue`
- Disposition: `Do not replace yet. Keep WorldClim CMIP6 as strong candidate family for derived heat indicator work and leave row at Clarify.`

### Salinity

#### `S-01` `Salinity` `Global map of salt-affected soils`

_Expanded row block not yet written. Use the Salinity summary table and audited CSV for the current review disposition._

#### `S-02` `Salinity` `Global soil salinity`

_Expanded row block not yet written. Use the Salinity summary table and audited CSV for the current review disposition._

### Soil water

#### `W-01` `Soil water` `Water retention volume at 1500 kPa and 30 to 60 cm depth`

_Expanded row block not yet written. Use the Soil water summary table and audited CSV for the current review disposition._

#### `W-02` `Soil water` `Available water capacity at 30 to 60 cm depth`

_Expanded row block not yet written. Use the Soil water summary table and audited CSV for the current review disposition._

#### `W-03` `Soil water` `Rooting zone water storage capacity`

_Expanded row block not yet written. Use the Soil water summary table and audited CSV for the current review disposition._

#### `W-04` `Soil water` `Plant-available soil water`

_Expanded row block not yet written. Use the Soil water summary table and audited CSV for the current review disposition._

### Irrigation

#### `I-01` `Irrigation` `Area equipped with irrigation`

_Expanded row block not yet written. Use the Irrigation summary table and audited CSV for the current review disposition._

#### `[Row ID]` `[Hazard group]` `[Current dataset name]`

**Current CRI function**

_TBC_

**Current dataset**

- Dataset name / version: `_TBC_`
- Underlying climate datasets used if any - Baseline / Future (if any): `_TBC_`
- Baseline period: `_TBC_`
- Future period: `_TBC_`
- SSPs used: `_TBC_`
- Ensemble used + GCMs: `_TBC_`
- Downscaling method: `_TBC_`
- Bias correction method: `_TBC_`
- Resolution: `_TBC_`
- Reference period / horizon: `_TBC_`
- Production-specific: `_TBC_`
- Main concern: `_TBC_`

**Best candidate**

- Dataset: `_TBC_`
- Official page: `_TBC_`
- Direct access: `_TBC_`
- Citation: `_TBC_`
- Spatial resolution: `_TBC_`
- Temporal coverage: `_TBC_`
- Climate era / scenarios: `_TBC_`

**Method provenance**

- GCMs / models: `_TBC_`
- Baseline data / baseline period: `_TBC_`
- Bias correction / downscaling: `_TBC_`
- Exact method / algorithm: `_TBC_`
- Season onset / growing-season logic relevance: `_TBC_`

**Decision**

- Status: `_TBC_`
- Confidence: `_TBC_`

**Why this decision**

_One short paragraph. Must state whether candidate is better, not better, or still unclear, and why._

**Evidence-backed superiority statement**

_Template: Proposed dataset is better than current dataset for [specific reason], supported by [source]._  
If not possible: `_Insufficient evidence to claim superiority._`

**Limitations**

- `_TBC_`

**Verification**

- Verification status: `_TBC_`
- Primary sources checked:
  - `_TBC_`
  - `_TBC_`

**Adversarial challenge**

- Challenge summary: `_TBC_`
- Challenge status: `_TBC_`
- Disposition: `_TBC_`

### 1.5 Priority shortlist

_Placeholder. This section should be completed after the detailed row reviews mature and should highlight the dataset families most ready for CDH ingestion, harmonization, and any later old-versus-new comparison work._

### Hazard summaries

These sections help non-technical readers scan results by theme.

### Drought

| Current dataset / indicator | Candidate | Status | Plain-language reason |
| --- | --- | --- | --- |
| Standardized Precipitation Index (SPI) | CHIRPS v3 3-monthly precipitation for SPI-style drought derivation | Clarify | Strong open precipitation candidate exists, but it is not a ready-made CRI drought-event layer and official coverage is not fully global |
| Failed season | N/A | Clarify | Current source access and active CRI use were not verified, so replacement review is premature |
| Available blue water | Aqueduct 4.0 available blue water / water supply indicators | Keep | Current source already sits in latest open WRI water-risk family; main issue is horizon harmonization |
| Gross water demand and net consumption | Aqueduct 4.0 monthly gross water demand and net consumption | Keep | Current source already sits in latest open WRI water-risk family; main issue is horizon harmonization |
| Baseline water stress | Aqueduct 4.0 baseline water stress | Keep | Current source already sits in latest open WRI water-risk family; main issue is horizon harmonization |

### Flooding

| Current dataset / indicator | Candidate | Status | Plain-language reason |
| --- | --- | --- | --- |
| Dartmouth flood frequency | Aqueduct Floods hazard maps | Clarify | Stronger future-oriented flood family exists, but exact equivalence to legacy event-frequency construct is not yet proven |
| River flood hazard | Aqueduct Floods river flood hazard maps | Keep | Current source is already open WRI flood-hazard family; main gap is horizon and scenario documentation |
| Coastal flood hazard | Aqueduct Floods coastal flood hazard maps | Keep | Current source is already open WRI flood-hazard family; main gap is horizon and assumption documentation |

### Changed rainfall

| Current dataset / indicator | Candidate | Status | Plain-language reason |
| --- | --- | --- | --- |
| LGP flip over 120 days | GAEZ v5 agro-climatic resource / future climate layers | Clarify | Stronger and more modern FAO/IIASA candidate family exists, but exact open future threshold-flip layer still needs proof before replacement |
| LGP flip over 90 days | GAEZ v5 agro-climatic resource / future climate layers | Clarify | Same FAO/IIASA modernization candidate as the 120-day row, but threshold-specific open layer access still is not proven |
| Annual rainfall coefficient of variation | CHIRPS v3 precipitation for annual rainfall variability derivation | Clarify | Strong open precipitation family exists, but direct annual-CV hazard derivation and full global fit were not verified |
| Intra-annual variability | Aqueduct 4.0 water-supply variability indicators | Keep | Current source already sits in latest open WRI variability family; main issue is 2030 versus 2050 harmonization |
| Seasonal variability | Aqueduct 4.0 water-supply variability indicators | Keep | Current source already sits in latest open WRI variability family; main issue is 2030 versus 2050 harmonization |

### High temperature

| Current dataset / indicator | Candidate | Status | Plain-language reason |
| --- | --- | --- | --- |
| Extreme humid heat days | ERA5 hourly single-level data for humid-heat derivation | Clarify | Stronger authoritative open climate backbone exists, but dangerous-WBGT-day derivation was not verified |
| Growing-season Tmax flip over 30C | WorldClim CMIP6 future climate monthly maximum temperature | Clarify | Strong modern open CMIP6 temperature product exists, but it is not yet the same thing as the CRI growing-season threshold-flip hazard layer |
| LGP-linked temperature stress | GAEZ v5 agro-climatic resource / future climate layers | Clarify | Current Appendix wording looks duplicated, so row meaning needs methods clarification before replacement work |

### Salinity

| Current dataset / indicator | Candidate | Status | Plain-language reason |
| --- | --- | --- | --- |
| Global map of salt-affected soils | Global map of salt-affected soils (GSASmap) | Keep | Current source already sits in authoritative FAO salinity framework; main limitation is static future representation |
| Global soil salinity | Global map of salt-affected soils (GSASmap) | Clarify | FAO stewardship appears stronger, but exact like-for-like variable equivalence is not yet proven |

### Soil water

| Current dataset / indicator | Candidate | Status | Plain-language reason |
| --- | --- | --- | --- |
| Water retention volume at 1500 kPa and 30 to 60 cm depth | WoSIS-derived soil property framework | Keep | Current source already sits in authoritative ISRIC soil-profile ecosystem; main limitation is long heterogeneous observation window |
| Available water capacity at 30 to 60 cm depth | SoilGrids250m 2.0 / current SoilGrids framework | Clarify | Maintained ISRIC framework is clearly newer than legacy 2017 citation, but exact AWC variable mapping was not verified |
| Rooting zone water storage capacity | N/A | No open replacement confirmed | Current cited source looks promising, but open dataset access and better replacement candidate were not verified |
| Plant-available soil water | N/A | No open replacement confirmed | Current cited source looks promising, but open dataset access and better replacement candidate were not verified |

### Irrigation

| Current dataset / indicator | Candidate | Status | Plain-language reason |
| --- | --- | --- | --- |
| Area equipped with irrigation | N/A | No open replacement confirmed | Current cited source looks promising, but open dataset access and better replacement candidate were not verified |

### Decision rules

Write `Replace` only when all are true:

- candidate is open and ungated
- direct access verified
- variable meaning is fit for CRI use
- superiority statement is supported
- no major unresolved blocker remains

Write `Clarify` when:

- candidate looks promising
- but one or more important fields remain partial, conflicted, or not verified

Write `No open replacement confirmed` when:

- no verified candidate passes hard filters
- or adversarial review finds unresolved blocker

### Notes for presentation

When this file starts filling up, most users should be able to read:

1. Annex 1 dataset overview table
2. Outstanding questions for Bert
3. Priority shortlist
4. One hazard section

and avoid opening the CSV unless they need audit detail.

## 2) Methodological review / recommendations

_Placeholder. This section should review Sections 2, 3, 4, 5, and 6 of the CRI methods document once the dataset modernization work is stable enough to separate data problems from method problems._

Initial topics to cover later:

- whether the CRI hazard formulation remains fit for purpose once dataset lineage is modernized
- how season onset, failed season, and growing-period logic are implemented and whether they are reproducible
- how threshold choices affect accuracy, interpretability, and cross-hazard comparability
- how any future old-versus-new comparison should be designed and evaluated
- whether AI use in the HII is technically defensible, transparent, and appropriate for a Hub-published workflow
