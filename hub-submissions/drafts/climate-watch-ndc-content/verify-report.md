# Verification — `climate-watch-ndc-content` (vapi-v1, schema v0.5.0)

File `climate-watch-ndc-content/climate-watch-ndc-content.yaml` · 7 URLs probed · 1 assets opened · **HIGH 1** · MED 3 · LOW 1 · INFO 1

| Sev | Path | Check | Finding | Record says | Observed | Hint |
|---|---|---|---|---|---|---|
| HIGH | `/processing/0/derived_from/0/url` | link | URL unreachable (ConnectionError) | https://unfccc.int/NDCREG |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| MED | `/` | authored | authored fields were machine-drafted and no person has reviewed them yet | # yaml-language-server: $schema=https://cgiar-climate-data-hub.github.io/cdh-metadata-standard/v0.5.0/schemas/profiles/… |  | a person must confirm title, description, note, usage and every cdh field (REVIEW.md) |
| MED | `/additional_links/0/url` | link | URL unreachable (404) | https://www.climatewatchdata.org/about/permissions |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| MED | `/additional_links/1/url` | link | URL unreachable (404) | https://www.climatewatchdata.org/data-explorer/ndc-content |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| LOW | `/processing/0/derived_from/0/version` | provenance | source version not pinned | UNFCCC NDC Registry |  |  |
| INFO | `/` | schema | validate-yaml.js (v0.5.0): ok |  |  |  |

Rule (standard §4.6): nothing above is auto-fixed; an authored value wins until a person decides which side is wrong.

## Triage (2026-10-20, before human review)

- **climatewatchdata.org 404s (MED x2)**: it is a JS single-page app, so scripted requests get 404. Both /about/permissions and /data-explorer/ndc-content were opened in a browser and are live (2026-10-20).
- **Mixed licence**: CC BY 4.0 covers only rows with source = Climate Watch. For Togo, 73% of rows are source WB. Hence the LicenseRef and the usage warning.
- **source version not pinned (LOW)**: the NDC Registry has no version; left unpinned.
- **unfccc.int ConnectionError (HIGH)**: transient; the same URL returned 200 to curl on 2026-10-20 before and after the run.
