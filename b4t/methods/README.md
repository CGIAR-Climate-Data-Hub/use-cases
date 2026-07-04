# B4T CRI review — working folder

Supports the B4T use-case brief ([../BRIEF.md](../BRIEF.md)): review the Climate and Environmental Crop Risk Index (CRI), recommend modern open datasets feasible for CDH integration, and (Phase 2) review the CRI methodology.

## Approach

Rebuilt from scratch (July 2026). An earlier first pass by Codex is archived under [../archive/codex-handover-2026-07/](../archive/codex-handover-2026-07/) — kept for reference, not treated as source of truth. Its canonical Appendix Table 1 extraction was independently re-verified against the source PDF and found faithful; everything downstream was rebuilt.

Principles: accuracy over coverage; current-dataset facts only from B4T source documents, candidate facts only from steward pages verified live; unknowns written as unknowns, never inferred; one row worked and agreed before fanning out.

## Files

| File | What it is |
| --- | --- |
| [dataset-review.md](./dataset-review.md) | The deliverable: exec summary, decisions, lineage tables, recommendations, per-row detail (later → Astro page) |
| [current-datasets.csv](./current-datasets.csv) | Current-state lineage interrogation (12 axes) — backs §3 of the report |
| [improved-options.csv](./improved-options.csv) | Recommended open alternatives on the same 12 axes — backs §4 |
| [appendix-table-1.csv](./appendix-table-1.csv) | The 23 hazard/vulnerability datasets (verified against source) |
| [cri-formulation.md](./cri-formulation.md) | Accurate public-safe reconstruction of the current CRI method |
| [evidence/sources.md](./evidence/sources.md) | Log of every external source, what it verified, when |

## Project notes

- **Bert's technical emails (2026-04-29/30) supersede the CRI documentation** on what data is actually used. Key corrections now folded in: drought = WASP (2.5°, 1980–2000), not "SPI"; future layers = 17 CMIP5 GCMs / RCP8.5 (Jones & Thornton), not CMIP3; Aqueduct version uncertain (may be CMIP5-era, not the CMIP6 4.0 the doc cites). Conflicts flagged as `conflicted` in the registries.
- **Eventual deliverable (per Todd):** a rebuilt CRI pipeline in code producing current vs modernized index side-by-side, to show whether the data change is meaningful for breeding. This review scopes it.
- **Build on existing CDH assets (steers recommendations):** recommendations prioritise the strong datasets the Hub already produces, so they are ready to adopt. Internal tracks to draw on first: **CHIRPS-CHIRTS-ERA5 SPEI** (observational, Africa — used for D-01), **NASA NEX-GDDP-CMIP6 v2** (projections, CMIP6/SSP source for future rows), **water-balance v2** (NDWS/NDWL, FAO-56 Penman-Monteith). New datasets can follow as later enhancements. D-01 therefore recommends extending the existing CDH SPEI pipeline to global 0.05° (a re-run, not a new indicator; CHIRPS bounds 60°N–60°S), with FAO ASI as a complementary agriculture-specific layer — open issue: SPEI≠SPI/WASP (adds PET, construct needs B4T sign-off).
- **Use-case coordination:** Bia.

## Status (2026-07-02)

- Phase 1 (datasets): **all 23 rows scoped (draft)** — verdict + recommended direction (off-the-shelf vs CDH-derived) + Bert questions per row. Pending: consolidate Bert questions, confirm lineage gaps, then the old-vs-new pipeline rebuild (per Todd).
- Phase 2 (methodology — HII provenance, CCC crop-vs-variety, yield step, horizon harmonization): not started; intended as the shared PoD input for 2026/27 planning.

## Roadmap

1. Agree the D-01 row shape with the champion.
2. Fan out the remaining 22 rows (drought → flooding → changed rainfall → high temperature, then salinity/soil water/irrigation).
3. Consolidate genuine unknowns into a short clarification list for Bert.
4. Render `dataset-review.md` as a CDH-styled Astro page for shared review.
5. Phase 2 methodology review.
