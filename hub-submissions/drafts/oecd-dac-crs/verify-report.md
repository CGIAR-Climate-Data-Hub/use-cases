# Verification — `oecd-dac-crs` (v1.6, schema v0.5.0)

File `oecd-dac-crs.yaml` · 9 URLs probed · 0 assets opened · **HIGH 1** · MED 2 · LOW 7 · INFO 2

| Sev | Path | Check | Finding | Record says | Observed | Hint |
|---|---|---|---|---|---|---|
| HIGH | `/processing/0/derived_from/0/url` | link | URL unreachable (403) | https://www.oecd.org/content/oecd/en/data/insights/data-explainers/2024/10/resources-for-reporting-development-finance-statistics.html |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| MED | `/` | authored | authored fields were machine-drafted and no person has reviewed them yet | # yaml-language-server: $schema=https://cgiar-climate-data-hub.github.io/cdh-metadata-standard/v0.5.0/schemas/profiles/… |  | a person must confirm title, description, note, usage and every cdh field (REVIEW.md) |
| MED | `/data/0/locations/0` | asset-prefix | prefix location without href_template or file_index — cannot verify contents | https://sdmx.oecd.org/dcd-public/rest/data/OECD.DCD.FSD,DSD_CRS@DF_CRS,1.6/ |  |  |
| LOW | `/additional_links/0/url` | link | URL unreachable (403) | https://www.oecd.org/en/about/terms-conditions.html |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| LOW | `/additional_links/2/url` | link | URL unreachable (403) | https://www.oecd.org/en/data/insights/data-explainers/2024/07/frequently-asked-questions-on-official-development-assistance-oda.html |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| LOW | `/additional_links/3/url` | link | URL unreachable (403) | https://www.oecd.org/content/oecd/en/data/insights/data-explainers/2024/10/resources-for-reporting-development-finance-statistics.html |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| LOW | `/additional_links/4/url` | link | URL unreachable (403) | https://one.oecd.org/document/DCD/DAC(2026)14/FINAL/en/pdf |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| LOW | `/additional_links/5/url` | link | URL unreachable (403) | https://www.oecd.org/en/topics/sub-issues/oda-standards/glossary-of-statistical-terms-and-concepts-of-development-finance.html |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| LOW | `/contact/0/url` | link | URL unreachable (403) | https://www.oecd.org/en/about/directorates/development-co-operation-directorate.html |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| LOW | `/processing/0/derived_from/0/version` | provenance | source version not pinned | Provider activity reports to the OECD (DAC Converged Statistical Reporting Directives) |  |  |
| INFO | `/` | schema | validate-yaml.js (v0.5.0): ok |  |  |  |
| INFO | `/data/0` | inspect | no inspector for media_type 'application/vnd.sdmx.genericdata+xml' — contents not verified | https://sdmx.oecd.org/dcd-public/rest/data/OECD.DCD.FSD,DSD_CRS@DF_CRS,1.6/ |  |  |

Rule (standard §4.6): nothing above is auto-fixed; an authored value wins until a person decides which side is wrong.

## Triage (2026-10-19, before human review)

- **asset-prefix (MED)**: expected for a federated API record — the location is an API base, not a file prefix; the verifier cannot list it. Contents checked instead by running `example.py` against the live API (2026-10-19).
- **oecd.org 403s**: Cloudflare blocks scripted requests; the DCD page was opened in a browser and is live (2026-10-19).
- **Fixed after the first verify run**: three oecd.org URLs drafted from memory were dead (404 in a browser) and were replaced with Data Explorer / SDMX codelist URLs; media_type corrected to SDMX-ML (the bare endpoint's default).
- **source version not pinned (LOW)**: provider reporting has no version; left unpinned.

## Triage (2026-10-23, round 2, before human review)

- **oecd.org / one.oecd.org 403s (HIGH x1, LOW x7)**: oecd.org blocks scripted requests. The terms page, FAQ, reporting-resources page, glossary and DCD page were each opened in a browser and are live (2026-10-23). The reporting-directives link is a PDF the server sends as a download.
- **asset-prefix (MED)**: expected for a federated API record. Contents checked by running `example.py` for Kenya (2026-10-23).
- **Round 2 changes** (from Peter Steward's round-1 review and a metadata-only test agent): licence corrected to the OECD data terms (the CC BY 4.0 grant covers OECD written content, not data); note rewritten as practical limitations; processing describes how the OECD compiles the data; intended uses expanded with worked examples; ALLD replaces DAC as the recipient total (DAC is member countries only, under half of Kenya's total); provider groups, the remaining key dimensions and the empty project/climate columns documented; disbursement gross/net left _TBC_.
