# Human review — `climate-watch-ndc-content`

The fields below are **authored** fields (CDH standard §4: a person, always). They were drafted by an AI agent from the evidence in the record header; tick each one only after checking it against the source. Edit the YAML, not this sheet.

| ✓ | Field | Draft value | Check |
|---|---|---|---|
| [ ] | title | `Climate Watch NDC Content - coded content of national climate pledges` | Is this what the producer calls it? Would a user searching for it find it? |
| [ ] | description | `Structured content of countries' Nationally Determined Contributions (NDCs) and related UNFCCC submissions, coded by Climate Watch (WRI) and partners into about 650 indicators: Paris Agreement status, mitigation targets…` | Every claim true and sourced (coverage, counts, years, units)? Anything overstated? |
| [ ] | note — limitations | `Mixed sources: each row's 'source' says who coded it. For Togo (2026-10-20) 1,786 of 2,434 rows are from the World Bank NDC database ("WB"), 584 from Climate Watch, 46 from UNICEF and 18 from Pledges. Climate Watch's CC…` | Does it state the main limitations: coverage gaps, resolution or aggregation level, known artefacts, revisions, licence traps? What would bite a first-time user that is not here? |
| [ ] | note / processing — assumptions | `NDC and UNFCCC submissions coded into indicators by Climate Watch (WRI) and partner organisations.` | Are the method assumptions behind the values stated (modelled vs observed, thresholds, weighting, projections)? |
| [ ] | license / attribution | `LicenseRef-Climate-Watch-Mixed — Climate Watch. 2026. Washington, DC: World Resources Institute. Available online at: https://www.climatewatchdata.org. Cite the original source of rows not produced by Climate Watch.` | Checked against the producer's own terms page, not a mirror? |
| [ ] | cdh.domain | `["adaptation", "mitigation"]` | Right domain(s) for how CDH users will look for it? |
| [ ] | intended_uses[0] | `what a country has committed to in its NDC (adaptation priorities, sectors, targets) for a climate rationale` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | intended_uses[1] | `checking alignment of a proposal with national commitments (e.g. GCF country ownership)` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | not_recommended_for[0] | `Republishing all rows under CC BY 4.0. — because Most rows for many countries come from other coders (e.g. World Bank) with their own terms. — instead: Filter on source, or cite and license each source separately.` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[1] | `Quoting a row as the content of the latest NDC. — because Rows carry no document id and several NDC versions can coexist for one indicator. — instead: Check the document with content_overview (document_slug) or the NDC …` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | missing misuse? | *(empty)* | What is the misuse you would worry about most? If it is not listed above, add it. |

When done: change the YAML header to `reviewed by <name> <date>` and rerun the verifier.

## AI usage disclosure (paste at the top of the catalog PR)

```text
AI usage: AI-drafted — record drafted by an AI agent from the sources listed; verified with cdh-metadata-verify.
Human review: <name>, <date> — authored fields checked against the sources (REVIEW.md).
```
