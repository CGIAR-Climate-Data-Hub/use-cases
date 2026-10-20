# Human review — `dhs-indicator-api`

The fields below are **authored** fields (CDH standard §4: a person, always). They were drafted by an AI agent from the evidence in the record header; tick each one only after checking it against the source. Edit the YAML, not this sheet.

| ✓ | Field | Draft value | Check |
|---|---|---|---|
| [ ] | title | `DHS Program Indicator Data API - national and subnational survey indicators` | Is this what the producer calls it? Would a user searching for it find it? |
| [ ] | description | `Published population, health and nutrition indicators from Demographic and Health Surveys (DHS) and related surveys (MIS, AIS), as point estimates by survey, country and survey region, with denominators and, for some in…` | Every claim true and sourced (coverage, counts, years, units)? Anything overstated? |
| [ ] | note — limitations | `Subnational rows are survey regions (CharacteristicCategory Region), whose boundaries change between surveys. Join on RegionId with the matching boundaries from the DHS Spatial Data Repository, not on names: labels carr…` | Does it state the main limitations: coverage gaps, resolution or aggregation level, known artefacts, revisions, licence traps? What would bite a first-time user that is not here? |
| [ ] | note / processing — assumptions | `Indicators tabulated by The DHS Program from its survey microdata and published through the Indicator Data API.` | Are the method assumptions behind the values stated (modelled vs observed, thresholds, weighting, projections)? |
| [ ] | license / attribution | `LicenseRef-DHS-Indicator-API-Terms — The DHS Program Indicator Data API, The Demographic and Health Surveys (DHS) Program. ICF. Originally funded by the United States Agency for International Development (USAID). Availa…` | Checked against the producer's own terms page, not a mirror? |
| [ ] | cdh.domain | `["socioeconomic"]` | Right domain(s) for how CDH users will look for it? |
| [ ] | intended_uses[0] | `subnational vulnerability context (nutrition, wealth, water, mortality) for climate finance proposals` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | intended_uses[1] | `targeting regions by published survey indicators` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | not_recommended_for[0] | `Comparing regions or countries as if values shared a year. — because Each value is from one survey; survey years differ by country and region boundaries change. — instead: Report the survey id and year with every value.` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[1] | `Joining regional rows to an admin boundary set by name. — because DHS survey regions are survey-specific and do not always match administrative units. — instead: Join on RegionId with the DHS Spatial Data Repository bou…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | missing misuse? | *(empty)* | What is the misuse you would worry about most? If it is not listed above, add it. |

When done: change the YAML header to `reviewed by <name> <date>` and rerun the verifier.

## AI usage disclosure (paste at the top of the catalog PR)

```text
AI usage: AI-drafted — record drafted by an AI agent from the sources listed; verified with cdh-metadata-verify.
Human review: <name>, <date> — authored fields checked against the sources (REVIEW.md).
```
