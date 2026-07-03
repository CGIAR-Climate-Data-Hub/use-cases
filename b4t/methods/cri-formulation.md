# Current CRI formulation (reconstructed from source)

Public-safe reconstruction of the B4T **Climate and Environmental Crop Risk Index (CRI)**, read directly from the primary source document (Lenaerts & Badayos, *Climate and environmental Crop Risk Index (CRI)*, v1, 2025-12-15) held in OneDrive. This note exists so the repo carries an accurate, citable summary without duplicating the source PDF. Where the source is ambiguous it is flagged, not smoothed over.

## Conceptual frame

The CRI follows an IPCC-style risk framing (Table 1 of the source, citing Rød et al. 2025 for the hazard definition and Dilley 2005 for exposure):

- **Hazard** — gridded historic and future climate/environmental hazards relevant to crop production.
- **Exposure** — spatial crop harvested area (from CROPGRIDS).
- **Vulnerability** — moderating factors: soil water and irrigation potential.
- **Coping capacity** — crop tolerance to hazards, via Ecocrop optimum growing conditions.
- **Risk** — the interaction of the above.

Stated objective: *"develop a crop production risk index that enables the quantification of expected yield changes in the future, facilitating benefit modelling."*

The method has four components: (1) hazard data, (2) hazard intensity and interactions (HII), (3) crop coping capacity (CCC), (4) empirical yield changes.

## 1. Hazard data

Five hazards: **drought (D), flooding (F), high temperature (T), changed rainfall (R), salinity (S)**. Two vulnerability/moderating factors: **soil water (W), irrigation potential (I)**. Sources are inventoried in [appendix-table-1.csv](./appendix-table-1.csv) (23 dataset rows).

**Processing chain (source §2.2):**

1. Standardise projection to `EPSG:4326`.
2. Set full global extent `(-180, 180, -90, 90)`.
3. Mask non-crop areas using a `1%` physical-pixel crop-area cutoff from CROPGRIDS.
4. Downscale to `3 arc-minute (0.05°)` resolution.
5. Convert each hazard indicator to pseudo-probabilities on a `0–100` scale.
6. Weighted average across selected indicators per hazard type (source calls this "ensemble learning," citing Mienye & Sun 2022; in practice this is a weighted average of indicator layers).
7. `50–50` weighting between present and future indicators.
8. Binarise via a `90th-percentile` cutoff (top 10% → `1`).

## 2. Hazard Intensity and Interactions (HII)

Each hazard / hazard-vulnerability combination is scored `1–5` (Table 2: 1 = none/very low loss → 5 = total loss). Approach (source §3):

1. **AI first pass** — a structured schema-based prompt (reproduced in the source as Appendix Text 1, with a defined `net_val = sign × ES × Ew × Fw` rubric) run across **ChatGPT 5.0, Copilot GPT-5, and Gemini**, tested Jul–Oct 2025, to draft interaction scores.
2. **Cross-validation** — literature review (~50 references in the source's Appendix Table 3) plus expert consultation to adjust the AI-drafted scores.

Single-hazard scores are base values (from global yield-impact literature); multi-hazard scores are built up incrementally, with documented exceptions (e.g. flood + salinity treated as coastal flooding; irrigation deductions against soil water). Triple+ combinations are derived from the two-hazard interactions.

> The AI-assisted provenance is more structured than "an LLM guessed" — there is a real rubric and a literature/expert cross-check. But the depth of validation is uneven across the matrix. This is a **Phase-2 methods** question, not a dataset question.

## 3. Crop Coping Capacity (CCC)

Crop tolerance from FAO Ecocrop (Brown et al. 2024), per hazard:

- Drought: `ROPMN`, `RMIN`
- High temperature: `TOPMN`, `TMAX`
- Flooding: `ROPMX`, `RMAX`
- Changed rainfall: `ROPMN`, `RMIN`, `GMIN`
- Salinity: `SALR`

Scored low / medium / high. The source explicitly notes this is **crop-level, not variety-level** — e.g. submergence-tolerant rice or salt-tolerant wheat would shift the rating. `50` crops are used (Appendix Table 2). This crop-vs-variety gap is directly relevant to B4T breeding segmentation.

## 4. Final CRI and yield changes

- **CRI** combines HII and CCC (source Figure 2). Example: flooding + salinity gives `HII = 3`; a crop of medium tolerance gives `CCC = 2`; resulting `CRI = 2`.
- **Yield changes** (source §6): projected yearly yield change under three scenarios — business-as-usual, conservative, optimistic — over a 10-year frame. Estimates are the **simple average of (a) expert review and (b) an LLM** (Copilot "Think Deeper" mode, 11 Nov 2025, 1%/yr baseline yield increase assumed).

## Where CRI feeds B4T decisions

`Crop x region priority- 2025.xlsx` shows climate risk already sits in B4T prioritization (`Population affected by Climate change`; value proposition `Farmer - Less Loss & Risk - CC relevant stress`). Meeting notes (2026-04-16, 2026-04-20) confirm B4T wants climate hazard information linked at market-segment / TPP granularity and projected forward ~20–25 years. So CRI revisions can influence crop-country prioritization and breeding-segment decisions, not just background analysis.

## Corrections from B4T technical emails (supersede the doc)

Bert's emails of 2026-04-29/30 (relaying Philip Thornton's personal communication) describe the *actual* data used and correct the published documentation, which lags:

- **Drought (D-01) is WASP, not SPI.** The drought layer is the Weighted Anomaly of Standardized Precipitation (WASP, IRI), computed on a **2.5°×2.5°** grid from monthly precipitation for **1980–2000** (event = ≤50% of long-term median for 3+ consecutive months), with high-risk areas from the top two deciles of Dilley (2005). The doc's "SPI, 1974–2004, Ericksen" framing conflicts with this. The coarse 2.5° resolution strengthens the modernization case.
- **Future layers are CMIP5, not CMIP3.** The 2050s threshold-flip layers (R-01, R-02, T-02, T-03) used **17 CMIP5 GCMs under RCP8.5** via Jones & Thornton (2009/2013/2015) — a generation newer than the Ericksen-2011 CMIP3/A2 basis. Bert is unsure of exact provenance and the notebook flags "possibly pre-CMIP5", so treat as `conflicted`; still pre-CMIP6/SSP either way.
- **Aqueduct may be older than cited.** Bert flags the CRI "seems [to use] CMIP5" Aqueduct, while the doc cites Aqueduct 4.0 (CMIP6) — verify the version per row.

## Known weaknesses to carry forward

- **Mixed vintage and horizon** in one score: historic layers (WASP drought 1980–2000, Dartmouth 1985–2003), 2030 Aqueduct layers, and 2050s CMIP5/RCP8.5 threshold layers.
- **Everything is pre-CMIP6 / pre-SSP** — the future layers are RCP8.5/CMIP5; Aqueduct is CMIP5–CMIP6 (version to confirm).
- **`T-03` appears to duplicate `R-01`** — identical LGP-flip wording under a different hazard.
- **CCC is crop-level, not variety-level** (Ecocrop + soil water-balance over MapSPAM crops; no changed-rainfall/LGP or salinity in that dataset; perennials awkward).
- **Yield step averages expert + LLM estimates.**
- **"SPI" (D-01) is mislabelled** — the actual index is WASP (a distinct IRI index), not the WMO-standard SPI.

> Not all inputs are outdated. The real problems are *mixed vintage, mixed horizon, unclear reprocessing lineage, and uneven method transparency* — not uniform obsolescence.
