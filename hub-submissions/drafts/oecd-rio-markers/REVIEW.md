# Human review — `oecd-rio-markers`

The fields below are **authored** fields (CDH standard §4: a person, always). They were drafted by an AI agent from the evidence in the record header; tick each one only after checking it against the source. Edit the YAML, not this sheet.

| ✓ | Field | Draft value | Check |
|---|---|---|---|
| [ ] | title | `OECD DAC Rio markers - ODA targeting climate adaptation, mitigation and the environment` | Is this what the producer calls it? Would a user searching for it find it? |
| [ ] | description | `Bilateral allocable official development assistance (ODA) commitments from DAC members, tagged with the Rio markers for climate change adaptation, climate change mitigation, biodiversity, desertification and environment…` | Every claim true and sourced (coverage, counts, years, units)? Anything overstated? |
| [ ] | note — limitations | `Only commitments (FLOW_TYPE C) and bilateral allocable ODA (ALLOCABLE 2) are published. A marker score of 2 (principal) or 1 (significant) records the provider's stated intent, not climate outcomes; the same activity ca…` | Does it state the main limitations: coverage gaps, resolution or aggregation level, known artefacts, revisions, licence traps? What would bite a first-time user that is not here? |
| [ ] | note / processing — assumptions | `Provider reporting of Rio markers in the CRS, compiled by the OECD Development Co-operation Directorate.` | Are the method assumptions behind the values stated (modelled vs observed, thresholds, weighting, projections)? |
| [ ] | license / attribution | `CC-BY-4.0 — Source: OECD DAC Rio markers (CRS), licensed under CC BY 4.0.` | Checked against the producer's own terms page, not a mirror? |
| [ ] | cdh.domain | `["socioeconomic", "adaptation", "mitigation"]` | Right domain(s) for how CDH users will look for it? |
| [ ] | intended_uses[0] | `adaptation and mitigation finance a country already receives (e.g. GCF financing justification)` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | intended_uses[1] | `comparing providers' climate-tagged portfolios by sector` | Specific task and scale? Would the producer endorse it? Is the data fit for it at its resolution? |
| [ ] | not_recommended_for[0] | `Adding adaptation and mitigation amounts to get total climate finance. — because One activity can carry both markers, so the sum double-counts. — instead: Report each marker separately; this dataflow serves aggregates o…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | not_recommended_for[1] | `Reading a marked amount as money spent on climate outcomes. — because Markers record the provider's declared objective at commitment, not disbursement or impact. — instead: State "ODA committed with a climate objective"…` | Is the reason true for this dataset? Is the alternative really better, and available? |
| [ ] | missing misuse? | *(empty)* | What is the misuse you would worry about most? If it is not listed above, add it. |

When done: change the YAML header to `reviewed by <name> <date>` and rerun the verifier.

## AI usage disclosure (paste at the top of the catalog PR)

```text
AI usage: AI-drafted — record drafted by an AI agent from the sources listed; verified with cdh-metadata-verify.
Human review: <name>, <date> — authored fields checked against the sources (REVIEW.md).
```
