# Human review — `who-unicef-jmp-wash`

The fields below are **authored** fields (CDH standard §4: a person, always). They were drafted by an AI agent from the evidence in the record header; tick each one only after checking it against the source. Edit the YAML, not this sheet.

| ✓ | Field | Draft value | Check |
|---|---|---|---|
| [ ] | title | `WHO/UNICEF JMP household drinking water, sanitation and hygiene estimates` | Is this what the producer calls it? Would a user searching for it find it? |
| [ ] | description | `National estimates from the WHO/UNICEF Joint Monitoring Programme (JMP) of the share of the population using each rung of the drinking water, sanitation and hygiene service ladders (safely managed, at least basic, limit…` | Every claim true and sourced (coverage, counts, years, units)? Anything overstated? |
| [ ] | note — limitations | `National level only (admin0); REF_AREA also holds regional and income-group aggregates (about 290 areas in total). Positional key REF_AREA.INDICATOR.SERVICE_TYPE.WEALTH_QUINTILE.RESIDENCE, empty positions are wildcards,…` | Does it state the main limitations: coverage gaps, resolution or aggregation level, known artefacts, revisions, licence traps? What would bite a first-time user that is not here? |
| [ ] | note / processing — assumptions | `JMP national estimates modelled from household surveys and censuses, distributed through the UNICEF SDMX data warehouse.` | Are the method assumptions behind the values stated (modelled vs observed, thresholds, weighting, projections)? |
| [ ] | license / attribution | `LicenseRef-UNICEF-Terms-of-Use — Source: WHO/UNICEF Joint Monitoring Programme for Water Supply, Sanitation and Hygiene (JMP).` | Checked against the producer's own terms page, not a mirror? |
| [ ] | cdh.domain | `["socioeconomic"]` | Right domain(s) for how CDH users will look for it? |
| [ ] | intended_uses[0] | `national water and sanitation access as vulnerability context for climate finance proposals` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | intended_uses[1] | `urban/rural gaps in basic services` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | not_recommended_for[0] | `Re-hosting the table or publishing a derived layer in the Hub. — because UNICEF asks for permission before republishing; the data licence is unstated and JMP reports are NC-SA. — instead: Query the API at use time and c…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[1] | `Subnational analysis. — because Estimates are national (with urban/rural splits) only. — instead: DHS survey indicators (record dhs-indicator-api) for regional water and sanitation figures.` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | missing misuse? | *(empty)* | What is the misuse you would worry about most? If it is not listed above, add it. |

When done: change the YAML header to `reviewed by <name> <date>` and rerun the verifier.

## AI usage disclosure (paste at the top of the catalog PR)

```text
AI usage: AI-drafted — record drafted by an AI agent from the sources listed; verified with cdh-metadata-verify.
Human review: <name>, <date> — authored fields checked against the sources (REVIEW.md).
```
