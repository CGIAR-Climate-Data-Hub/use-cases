# Human review — `oecd-rio-markers`

The fields below are **authored** fields (CDH standard §4: a person, always). They were drafted by an AI agent from the evidence in the record header; tick each one only after checking it against the source. Edit the YAML, not this sheet.

| ✓ | Field | Draft value | Check |
|---|---|---|---|
| [ ] | title | `OECD DAC Rio markers - ODA targeting climate adaptation, mitigation and the environment` | Is this what the producer calls it? Would a user searching for it find it? |
| [ ] | description | `Development aid committed by bilateral providers (DAC members, EU Institutions and some other reporting countries) that they have tagged as targeting the Rio Conventions: climate change adaptation, climate change mitiga…` | Every claim true and sourced (coverage, counts, years, units)? Anything overstated? |
| [ ] | note — limitations | `Limitations (assumptions are under processing; incorrect uses under cdh.usage). Which providers. Only bilateral providers that report Rio markers to the OECD: DAC members, EU Institutions and some other reporting countr…` | Does it state the main limitations: coverage gaps, resolution or aggregation level, known artefacts, revisions, licence traps? What would bite a first-time user that is not here? |
| [ ] | note / processing — assumptions | `Bilateral providers report every aid activity to the OECD's Creditor Reporting System and, for each one, score it against each Rio marker: 2 if the objective is principal, 1 if significant, 0 if the activity was screene…` | Are the method assumptions behind the values stated (modelled vs observed, thresholds, weighting, projections)? |
| [ ] | license / attribution | `LicenseRef-OECD-Data-Terms — OECD (2026), RioMarkers: Aid (ODA) activities targeting global environmental objectives, OECD Data Explorer, https://data-explorer.oecd.org/vis?lc=en&df%5Bds%5D=DcdDisseminateFinalDMZ&df%5Bi…` | Checked against the producer's own terms page, not a mirror? |
| [ ] | cdh.domain | `["socioeconomic", "adaptation", "mitigation"]` | Right domain(s) for how CDH users will look for it? |
| [ ] | intended_uses[0] | `Show how much climate-tagged aid a country already receives from bilateral providers, for the climate rationale or baseline of a funding proposal (e.g. a GCF concept note): adaptation and mitigation commitments per year…` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | intended_uses[1] | `Identify which bilateral providers and sectors already fund adaptation in a country, to argue how a proposal complements them (e.g. which donors fund agriculture-related adaptation). The example script lists the top pro…` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | intended_uses[2] | `Compare the weight given to adaptation versus mitigation in a country's bilateral aid over time, using constant prices (PRICE_BASE Q) and multi-year averages to smooth commitment spikes.` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | not_recommended_for[0] | `Adding adaptation and mitigation amounts together to get total climate finance. — because One activity can carry both markers, so the same money is counted twice. — instead: Report adaptation and mitigation separately, …` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[1] | `Reading marked amounts as money spent on, or achieving, climate objectives. — because Markers record the provider's declared objective when the money is committed, not disbursement or results. — instead: Describe them a…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[2] | `Treating the totals as all climate finance a country receives. — because Multilateral organisations (World Bank, development banks, climate funds) and non-reporting providers are not in this dataset. — instead: Add mult…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[3] | `Adding principal and significant amounts without saying so. — because Significant means climate is a secondary objective of the activity; how much of its value relates to climate is not stated here (_TBC_ against the Ri…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[4] | `Reporting the latest year as a full year. — because The latest year is published incomplete (2025 in October 2026) and filled in when detailed data appear in December. — instead: Use the last complete year, and check fo…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[5] | `Adding sector codes from different levels together (e.g. 310 and 311, or 100 and 140). — because Higher-level sector codes already include the codes below them, so the sum counts the same money twice. — instead: Use one…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[6] | `Targeting or reporting climate aid at county or district level (e.g. Homa Bay County). — because Country is the finest geography; there is no sub-national location. — instead: The providers' own project records, or the …` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | missing incorrect use? | *(empty)* | Is there a way people are likely to misuse this data that is not listed above? |
| [ ] | missing limitation? | *(empty)* | Is there a gap or weakness in the data itself (coverage, quality, timing) that the note does not mention? |
| [ ] | missing assumption? | *(empty)* | Is there an assumption behind how the values are produced that the method text does not state? |

When done: change the YAML header to `reviewed by <name> <date>` and rerun the verifier.

## AI usage disclosure (paste at the top of the catalog PR)

```text
AI usage: AI-drafted — record drafted by an AI agent from the sources listed; verified with cdh-metadata-verify.
Human review: <name>, <date> — authored fields checked against the sources (REVIEW.md).
```
