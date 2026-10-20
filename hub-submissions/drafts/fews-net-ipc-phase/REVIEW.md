# Human review — `fews-net-ipc-phase`

The fields below are **authored** fields (CDH standard §4: a person, always). They were drafted by an AI agent from the evidence in the record header; tick each one only after checking it against the source. Edit the YAML, not this sheet.

| ✓ | Field | Draft value | Check |
|---|---|---|---|
| [ ] | title | `FEWS NET acute food insecurity classifications (IPC-compatible)` | Is this what the producer calls it? Would a user searching for it find it? |
| [ ] | description | `Acute food insecurity classifications from the Famine Early Warning Systems Network (FEWS NET): the IPC-compatible phase (1 Minimal to 5 Famine) for each country and each sub-national classification unit (administrative…` | Every claim true and sourced (coverage, counts, years, units)? Anything overstated? |
| [ ] | note — limitations | `Rows are classification episodes: one per unit, scenario (Current Situation, Near Term Projection, Medium Term Projection, Most Likely) and projection window. Some scenario names carry a trailing space in the API. Sub-n…` | Does it state the main limitations: coverage gaps, resolution or aggregation level, known artefacts, revisions, licence traps? What would bite a first-time user that is not here? |
| [ ] | note / processing — assumptions | `FEWS NET analysts' IPC-compatible classifications, published through the FEWS NET Data Warehouse.` | Are the method assumptions behind the values stated (modelled vs observed, thresholds, weighting, projections)? |
| [ ] | license / attribution | `LicenseRef-US-Government-FEWS-NET — Source: Famine Early Warning Systems Network (FEWS NET).` | Checked against the producer's own terms page, not a mirror? |
| [ ] | cdh.domain | `["socioeconomic"]` | Right domain(s) for how CDH users will look for it? |
| [ ] | intended_uses[0] | `food-security context for a country or sub-national area (e.g. GCF vulnerability section)` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | intended_uses[1] | `identifying areas in IPC phase 3 or worse for targeting` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | not_recommended_for[0] | `Joining sub-national rows to an admin boundary set by name. — because Most sub-national units are admin x livelihood-zone units with FEWS NET's own ids. — instead: Join on fnid with the FEWS NET geographic boundaries.` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[1] | `Treating the country list as global coverage. — because FEWS NET monitors a fixed set of food-insecure countries. — instead: IPC / Cadre Harmonise for countries FEWS NET does not cover.` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | missing misuse? | *(empty)* | What is the misuse you would worry about most? If it is not listed above, add it. |

When done: change the YAML header to `reviewed by <name> <date>` and rerun the verifier.

## AI usage disclosure (paste at the top of the catalog PR)

```text
AI usage: AI-drafted — record drafted by an AI agent from the sources listed; verified with cdh-metadata-verify.
Human review: <name>, <date> — authored fields checked against the sources (REVIEW.md).
```
