# Verification — `oecd-rio-markers` (v1.7, schema v0.5.0)

File `oecd-rio-markers.yaml` · 10 URLs probed · 0 assets opened · HIGH 0 · MED 2 · LOW 7 · INFO 2

| Sev | Path | Check | Finding | Record says | Observed | Hint |
|---|---|---|---|---|---|---|
| MED | `/` | authored | authored fields were machine-drafted and no person has reviewed them yet | # yaml-language-server: $schema=https://cgiar-climate-data-hub.github.io/cdh-metadata-standard/v0.5.0/schemas/profiles/… |  | a person must confirm title, description, note, usage and every cdh field (REVIEW.md) |
| MED | `/data/0/locations/0` | asset-prefix | prefix location without href_template or file_index — cannot verify contents | https://sdmx.oecd.org/dcd-public/rest/data/OECD.DCD.FSD,DSD_RIOMRKR@DF_RIOMARKERS/ |  |  |
| LOW | `/additional_links/0/url` | link | URL unreachable (403) | https://www.oecd.org/en/about/terms-conditions.html |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| LOW | `/additional_links/2/url` | link | URL unreachable (403) | https://one.oecd.org/document/DCD/DAC/STAT(2025)50/REV2/en/pdf |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| LOW | `/additional_links/4/url` | link | URL unreachable (403) | https://www.oecd.org/en/data/insights/data-explainers/2024/07/frequently-asked-questions-on-official-development-assistance-oda.html |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| LOW | `/additional_links/5/url` | link | URL unreachable (403) | https://www.oecd.org/content/oecd/en/data/insights/data-explainers/2024/10/resources-for-reporting-development-finance-statistics.html |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| LOW | `/additional_links/6/url` | link | URL unreachable (403) | https://www.oecd.org/en/topics/oda-eligibility-and-conditions/dac-list-of-oda-recipients.html |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| LOW | `/contact/0/url` | link | URL unreachable (403) | https://www.oecd.org/en/about/directorates/development-co-operation-directorate.html |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| LOW | `/processing/0/derived_from/0/version` | provenance | source version not pinned | CRS: Creditor Reporting System (flows) |  |  |
| INFO | `/` | schema | validate-yaml.js (v0.5.0): ok |  |  |  |
| INFO | `/data/0` | inspect | no inspector for media_type 'application/vnd.sdmx.genericdata+xml' — contents not verified | https://sdmx.oecd.org/dcd-public/rest/data/OECD.DCD.FSD,DSD_RIOMRKR@DF_RIOMARKERS/ |  |  |

Rule (standard §4.6): nothing above is auto-fixed; an authored value wins until a person decides which side is wrong.

## Triage (2026-10-19, before human review)

- **asset-prefix (MED)**: expected for a federated API record — the location is an API base, not a file prefix; the verifier cannot list it. Contents checked instead by running `example.py` against the live API (2026-10-19).
- **oecd.org 403**: bot-blocked; DCD page live in a browser.
- **Fixed after the first verify run**: dead citation URL replaced; `derived_from.id: oecd-dac-crs` (not yet a catalog record) swapped for the CRS Data Explorer URL; marker/score categories checked against CL_CRS_MARKER / CL_CRS_SCORE and the live TGO data (only markers 10-50, scores 0/1/2/99, MD_DIM _T occur); removed advice to deduplicate via MD_DIM DD, which this dataflow does not serve.

## Triage (2026-10-27, before human review)

- **oecd.org 403s (LOW x6)**: oecd.org blocks scripted requests. The terms page, FAQ and resources page were opened in a browser (2026-10-23) and are live. The DAC List of ODA Recipients page is listed by search engines but showed a bot check in the browser on 2026-10-27; its 2024 PDF on webfs.oecd.org returns 200. The Rio markers handbook PDF is linked from the OECD resources page; the server sends it as a download, so it was not read. That is why "does a significant activity count in full?" is _TBC_.
- **asset-prefix (MED)**: expected for a federated API record. Contents checked by running `example.py` for Kenya (2026-10-27).
- **Data checks behind the note**: the dataflow holds DAC members, EU Institutions and some other reporting countries, and no multilaterals (Kenya 2023). MEASURE 100, ALLOCABLE 2 and FLOW_TYPE C are the only values. Adaptation starts in 2007 overall and 2010 for Kenya. 2025 values are near zero (Kenya adaptation principal 0.1 vs 87.9 USD million in 2024). Constant prices have base year 2024 (BASE_PER). Version 1.7 is the latest; 1.6 still answers.
- **Previous version** scored 7/10 in a metadata-only agent test (2026-10-27). Its fixes are folded in.
