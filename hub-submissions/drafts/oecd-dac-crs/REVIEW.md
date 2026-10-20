# Human review — `oecd-dac-crs`

The fields below are **authored** fields (CDH standard §4: a person, always). They were drafted by an AI agent from the evidence in the record header; tick each one only after checking it against the source. Edit the YAML, not this sheet.

| ✓ | Field | Draft value | Check |
|---|---|---|---|
| [ ] | title | `OECD DAC Creditor Reporting System (CRS) - development finance flows` | Is this what the producer calls it? Would a user searching for it find it? |
| [ ] | description | `Activity-level official development assistance (ODA) and other official flows reported by OECD Development Assistance Committee (DAC) members and other providers, aggregated by provider, recipient country, sector (CRS p…` | Every claim true and sourced (coverage, counts, years, units)? Anything overstated? |
| [ ] | note — limitations | `The dataflow is an external reference on sdmx.oecd.org/public; data and structures must be requested from https://sdmx.oecd.org/dcd-public/rest/. SDMX 3.0 component filters (c[RECIPIENT]=) are ignored by the server and …` | Does it state the main limitations: coverage gaps, resolution or aggregation level, known artefacts, revisions, licence traps? What would bite a first-time user that is not here? |
| [ ] | note / processing — assumptions | `Provider reporting compiled by the OECD Development Co-operation Directorate.` | Are the method assumptions behind the values stated (modelled vs observed, thresholds, weighting, projections)? |
| [ ] | license / attribution | `CC-BY-4.0 — Source: OECD Creditor Reporting System (CRS), licensed under CC BY 4.0.` | Checked against the producer's own terms page, not a mirror? |
| [ ] | cdh.domain | `["socioeconomic", "adaptation"]` | Right domain(s) for how CDH users will look for it? |
| [ ] | intended_uses[0] | `development and climate finance context for a country (e.g. GCF concept note section D)` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | intended_uses[1] | `identifying which providers and sectors already fund a country or theme` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | not_recommended_for[0] | `Summing 3-4 digit sector aggregates together with 5-digit purpose codes. — because Aggregates already contain their purpose codes, so the total double-counts. — instead: One sector level at a time (5-digit purpose codes…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[1] | `Treating OBS_VALUE as US dollars. — because Values are in millions of US dollars (UNIT_MULT 6). — instead: Multiply by 1e6 or label the unit as USD millions.` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | missing misuse? | *(empty)* | What is the misuse you would worry about most? If it is not listed above, add it. |

When done: change the YAML header to `reviewed by <name> <date>` and rerun the verifier.

## AI usage disclosure (paste at the top of the catalog PR)

```text
AI usage: AI-drafted — record drafted by an AI agent from the sources listed; verified with cdh-metadata-verify.
Human review: <name>, <date> — authored fields checked against the sources (REVIEW.md).
```
