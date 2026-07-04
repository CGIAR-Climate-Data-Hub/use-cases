## Current CRI Formulation

This note summarizes current B4T Climate and Environmental Crop Risk Index (CRI) formulation from source documents currently held in OneDrive. It is intended as public-safe working documentation, not as a replacement for underlying source files.

## Scope

Sources used for this note:

- `Crop Risk Index-documentation v1.pdf`
- `HII-scoring matrix.pdf`
- `Crop x region priority- 2025.xlsx`
- 2026-04-29 to 2026-05-08 email context already summarized in [BRIEF.md](../BRIEF.md)

## Core formulation

Current methods note describes CRI as four linked components:

1. Hazard data
2. Hazard intensity and interactions (HII)
3. Crop coping capacity (CCC)
4. Empirical yield changes

### Hazard set

Five hazards are modeled:

- Drought (`D`)
- Flooding (`F`)
- High temperature (`T`)
- Changed rainfall (`R`)
- Salinity (`S`)

Two additional moderating / vulnerability factors are used in interaction scoring:

- Soil water (`W`)
- Irrigation potential (`I`)

### Hazard preprocessing

Current documentation says hazard layers are processed as follows:

1. Standardize map projection to `EPSG:4326`
2. Set full global extent `(-180, 180, -90, 90)`
3. Mask non-crop areas using `1%` of physical pixel area in crop production from CROPGRIDS
4. Downscale to `3 arc-minute (0.05 degree)` resolution
5. Convert each hazard indicator to pseudoprobabilities on a `0-100` scale
6. Calculate weighted average across selected indicators for each hazard type
7. Apply `50-50` weighting between present and future hazard indicators
8. Convert averaged pseudoprobabilities to dummy values using `90th percentile` cutoff

### Exposure and vulnerability

- Exposure proxy: harvested area from CROPGRIDS
- Vulnerability / moderating layers: soil water and irrigation potential
- Documentation says `50` crops were used from CROPGRIDS-based crop list
- Hazard-vulnerability combinations are summarized as area in hectares

### HII scoring

Current HII process:

1. Assign each hazard-vulnerability combination score from `1` to `5`
2. Use LLM-generated draft matrix as first pass
3. Adjust scores through literature review and expert consultation
4. Use single-hazard scores as base values
5. Derive triple-or-higher combinations from lower-order interactions

Current methods note explicitly says LLMs were used to set initial interaction understanding, then cross-validated using literature and expert review. Public implication: matrix provenance is mixed, not purely empirical.

### CCC scoring

CCC uses FAO Ecocrop-derived tolerance proxies:

- Drought: `ROPMN`, `RMIN`
- High temperature: `TOPMN`, `TMAX`
- Flooding: `ROPMX`, `RMAX`
- Changed rainfall: `ROPMN`, `RMIN`, `GMIN`
- Salinity: `SALR`

Documentation groups crop coping capacity into `low`, `medium`, or `high`.

### Final CRI

Current note states CRI is derived by combining:

- hazard intensity and interaction score (`HII`)
- crop coping capacity score (`CCC`)

Illustrative example in source note:

- hazard context `F + S` gives `HII = 3`
- crop with medium tolerance gives `CCC = 2`
- resulting CRI is `2`

### Yield-response step

Current note says projected yield changes are estimated using:

- expert review estimates
- LLM-generated estimates

These are averaged across scenarios described as:

- business-as-usual (`BAU`)
- conservative
- optimistic

## Current methodological weaknesses flagged so far

- Mixed time horizons: some hazard inputs are historic, some `2030`, some `2050`
- Mixed lineage: inherited CCAFS / Thornton-style layers, Aqueduct layers, high-temperature layers, salinity products
- Incomplete reproducibility: narrative note exists, but working pipeline and exact implementation files still need confirmation
- Uneven evidence quality in HII matrix: some entries literature-backed, some expert-adjusted, some marked as extrapolation
- CCC is crop-level, not variety-level
- Yield-response step relies partly on LLM estimates

## Role in B4T prioritization

`Crop x region priority- 2025.xlsx` shows climate risk already appears in B4T prioritization context:

- impact indicator: `Population affected by Climate change`
- value proposition field: `Farmer - Less Loss & Risk - CC relevant stress`

This means CRI revisions can affect more than background analysis. They may influence crop-country prioritization and breeding-segmentation logic.

## What stays outside git

These files remain canonical background sources in OneDrive:

- raw PDFs
- raw workbook
- meeting notes
- internal drafts
- email chains

Repo should carry distilled, publish-safe derivatives only.
