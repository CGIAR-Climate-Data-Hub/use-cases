# Human review — `worldcover-admin`

The fields below are **authored** fields (CDH standard §4: a person, always). They were drafted by an AI agent from the evidence in the record header; tick each one only after checking it against the source. Edit the YAML, not this sheet.

| ✓ | Field | Draft value | Check |
|---|---|---|---|
| [ ] | title | `ESA WorldCover land-cover and cropland area by administrative unit (GAUL 2024, Africa)` | Is this what the producer calls it? Would a user searching for it find it? |
| [ ] | description | `Area in hectares and share of each ESA WorldCover land-cover class, and of cropland, for every GAUL 2024 administrative unit at levels 0, 1 and 2, computed from the 10 m WorldCover maps for 2021 (v200) and 2020 (v100). …` | Every claim true and sourced (coverage, counts, years, units)? Anything overstated? |
| [ ] | note — limitations | `Areas sum to the rasterised unit (centre-pixel rule at 10 m), not to the vector polygon area; differences are small for large units and larger for small or narrow ones. The 2020 (v100) and 2021 (v200) maps were made wit…` | Does it state the main limitations: coverage gaps, resolution or aggregation level, known artefacts, revisions, licence traps? What would bite a first-time user that is not here? |
| [ ] | note / processing — assumptions | `ESA WorldCover 10 m maps for 2020 (v100) and 2021 (v200), read as COGs from the public AWS bucket, and FAO GAUL 2024 level-2 polygons (Africa) from the Adaptation Atlas analysis-ready store. ; Level-2 polygons rasterise…` | Are the method assumptions behind the values stated (modelled vs observed, thresholds, weighting, projections)? |
| [ ] | license / attribution | `CC-BY-4.0 — Contains ESA WorldCover data: Zanaga, D. et al. (2022) ESA WorldCover 10 m 2021 v200, doi:10.5281/zenodo.7254221, and Zanaga, D. et al. (2021) ESA WorldCover 10 m 2020 v100, doi:10.5281/zenodo.5571936, CC BY…` | Checked against the producer's own terms page, not a mirror? |
| [ ] | cdh.domain | `["land", "agricultural-production"]` | Right domain(s) for how CDH users will look for it? |
| [ ] | intended_uses[0] | `land-cover context per district for climate finance proposals (e.g. GCF beneficiary and impact sections)` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | intended_uses[1] | `cropland area per admin unit as activity data for emissions tools such as EX-ACT` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | intended_uses[2] | `district-level cropland share to weight or mask other admin-level indicators` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | not_recommended_for[0] | `Land-cover change from the 2020 and 2021 rows. — because The two maps use different algorithms, so differences mix real and methodological change. — instead: A consistent multi-year land-cover series, or one year only.` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[1] | `Total agricultural or farm area. — because Cropland is annual herbaceous crops only; tree crops and pasture fall in other classes. — instead: Add tree-crop and pasture estimates from crop statistics or MapSPAM / CROPGRI…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[2] | `Areas for small units as exact figures. — because The centre-pixel rule at 10 m assigns boundary pixels to one unit only. — instead: Treat small-unit areas as estimates, or compute with the polygon overlay for the unit.` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | plausibility (Togo test run) | `Admin-1 cropland share 2021: Savanes 0.72, Kara 0.36, Plateaux 0.14, Centrale 0.12, Maritime 0.05` | Does this match what you know of Togo? WorldCover cropland (class 40) accuracy varies in West Africa; if it is off, add a limitation to `note`. |
| [ ] | missing misuse? | *(empty)* | What is the misuse you would worry about most? If it is not listed above, add it. |

When done: change the YAML header to `reviewed by <name> <date>` and rerun the verifier.

## AI usage disclosure (paste at the top of the catalog PR)

```text
AI usage: AI-drafted — record drafted by an AI agent from the sources listed; verified with cdh-metadata-verify.
Human review: <name>, <date> — authored fields checked against the sources (REVIEW.md).
```
