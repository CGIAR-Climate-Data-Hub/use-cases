# Human review — `imf-fiscal-monitor`

The fields below are **authored** fields (CDH standard §4: a person, always). They were drafted by an AI agent from the evidence in the record header; tick each one only after checking it against the source. Edit the YAML, not this sheet.

| ✓ | Field | Draft value | Check |
|---|---|---|---|
| [ ] | title | `IMF Fiscal Monitor - general government fiscal indicators (via World Bank Data360)` | Is this what the producer calls it? Would a user searching for it find it? |
| [ ] | description | `General government gross debt, revenue, expenditure, net lending/borrowing and primary balance as a percentage of GDP, by country and year, including IMF projections five years ahead, from the IMF Fiscal Monitor as redi…` | Every claim true and sourced (coverage, counts, years, units)? Anything overstated? |
| [ ] | note — limitations | `Years after the latest actual are IMF projections: each April and October Fiscal Monitor revises them, so record the retrieval date. Data360 serves the IMF series under its own indicator ids (e.g. IMF_FM_G_XWDG_G01_GDP_…` | Does it state the main limitations: coverage gaps, resolution or aggregation level, known artefacts, revisions, licence traps? What would bite a first-time user that is not here? |
| [ ] | note / processing — assumptions | `IMF Fiscal Monitor series redistributed by the World Bank Data360 platform.` | Are the method assumptions behind the values stated (modelled vs observed, thresholds, weighting, projections)? |
| [ ] | license / attribution | `CC-BY-4.0 — Source: IMF Fiscal Monitor, via World Bank Data360.` | Checked against the producer's own terms page, not a mirror? |
| [ ] | cdh.domain | `["socioeconomic"]` | Right domain(s) for how CDH users will look for it? |
| [ ] | intended_uses[0] | `fiscal-space context for climate finance proposals (e.g. GCF concept note section D)` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | not_recommended_for[0] | `Quoting a projected year as an observed value. — because Years after the latest actual are IMF projections and are revised twice a year. — instead: State the vintage (Fiscal Monitor month and year) and mark projections.` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | missing misuse? | *(empty)* | What is the misuse you would worry about most? If it is not listed above, add it. |

When done: change the YAML header to `reviewed by <name> <date>` and rerun the verifier.

## AI usage disclosure (paste at the top of the catalog PR)

```text
AI usage: AI-drafted — record drafted by an AI agent from the sources listed; verified with cdh-metadata-verify.
Human review: <name>, <date> — authored fields checked against the sources (REVIEW.md).
```
