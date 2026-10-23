# Human review — `oecd-dac-crs`

The fields below are **authored** fields (CDH standard §4: a person, always). They were drafted by an AI agent from the evidence in the record header; tick each one only after checking it against the source. Edit the YAML, not this sheet.

| ✓ | Field | Draft value | Check |
|---|---|---|---|
| [ ] | title | `OECD DAC Creditor Reporting System (CRS) - development finance flows` | Is this what the producer calls it? Would a user searching for it find it? |
| [ ] | description | `Official development assistance (ODA) and other development finance reported to the OECD by its Development Assistance Committee (DAC) members, other reporting countries, multilateral organisations and the largest priva…` | Every claim true and sourced (coverage, counts, years, units)? Anything overstated? |
| [ ] | note — limitations | `What the data cover and miss. Only providers that report to the OECD are included: DAC members, other countries that choose to report, multilateral organisations and some large foundations. Finance from providers that d…` | Does it state the main limitations: coverage gaps, resolution or aggregation level, known artefacts, revisions, licence traps? What would bite a first-time user that is not here? |
| [ ] | note / processing — assumptions | `Providers report every activity (project, programme or contribution) to the OECD in a single Creditor Reporting System format, following the DAC Converged Statistical Reporting Directives: what was funded, where, for wh…` | Are the method assumptions behind the values stated (modelled vs observed, thresholds, weighting, projections)? |
| [ ] | license / attribution | `LicenseRef-OECD-Data-Terms — OECD (2026), CRS: Creditor Reporting System (flows), OECD Data Explorer, https://data-explorer.oecd.org/vis?lc=en&df%5Bds%5D=DcdDisseminateFinalDMZ&df%5Bid%5D=DSD_CRS@DF_CRS&df%5Bag%5D=OECD.…` | Checked against the producer's own terms page, not a mirror? |
| [ ] | cdh.domain | `["socioeconomic", "adaptation"]` | Right domain(s) for how CDH users will look for it? |
| [ ] | intended_uses[0] | `Describe the development finance a country already receives, for the context or baseline section of a funding proposal (e.g. a GCF concept note): total ODA disbursed per year over the last 5-10 years from all official p…` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | intended_uses[1] | `Show where a proposed project fits among existing funders: list which providers already fund a sector in the country (e.g. agriculture, purpose codes 311xx) and how much, so the proposal can argue complementarity rather…` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | intended_uses[2] | `Track trends in support to a sector over time, using disbursements at constant prices (PRICE_BASE Q) so that years are comparable after inflation and exchange-rate changes.` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | not_recommended_for[0] | `Treating the totals as all the external finance a country receives. — because Only providers that report to the OECD are included; private investment, remittances and non-reporting providers are missing.  — instead: Say…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[1] | `Reading commitments as money spent, or comparing one year's commitments with the same year's disbursements. — because A multi-year commitment is recorded in full in the year it is signed, while disbursements in any year…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[2] | `Targeting or reporting finance at county or district level (e.g. Homa Bay County). — because Country is the finest geography; there is no sub-national location, and project text is not served by this API. — instead: The…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[3] | `Adding up providers that include each other (e.g. DAC + United States, or World Bank Group + IDA). — because Provider codes include groups that already contain their members, so sums count the same money twice. — instea…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[4] | `Climate-tagged finance (adaptation or mitigation) from this dataflow. — because The climate marker columns are empty in this API dataflow. — instead: The oecd-rio-markers record, which serves the Rio marker tables.` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[5] | `Adding sector aggregates (3- or 4-digit codes) to 5-digit purpose codes. — because Aggregates already include their purpose codes, so the sum counts the same money twice. — instead: Use one sector level at a time (5-dig…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[6] | `Quoting values as US dollars. — because Values are in millions of US dollars. — instead: Multiply by 1,000,000, or label the unit as "USD million".` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | missing misuse? | *(empty)* | What is the misuse you would worry about most? If it is not listed above, add it. |

When done: change the YAML header to `reviewed by <name> <date>` and rerun the verifier.

## AI usage disclosure (paste at the top of the catalog PR)

```text
AI usage: AI-drafted — record drafted by an AI agent from the sources listed; verified with cdh-metadata-verify.
Human review: <name>, <date> — authored fields checked against the sources (REVIEW.md).
```
