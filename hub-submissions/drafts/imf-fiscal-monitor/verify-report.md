# Verification — `imf-fiscal-monitor` (vdata360-IMF_FM, schema v0.5.0)

File `imf-fiscal-monitor/imf-fiscal-monitor.yaml` · 6 URLs probed · 0 assets opened · **HIGH 3** · MED 3 · LOW 1 · INFO 1

| Sev | Path | Check | Finding | Record says | Observed | Hint |
|---|---|---|---|---|---|---|
| HIGH | `/data/0/locations/0` | asset-url | primary data location unreachable (404) | https://data360api.worldbank.org/data360/data |  |  |
| HIGH | `/data/0/locations/0/url` | link | URL unreachable (404) | https://data360api.worldbank.org/data360/data |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| HIGH | `/processing/0/derived_from/0/url` | link | URL unreachable (404) | https://www.imf.org/en/Publications/FM |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| MED | `/` | authored | authored fields were machine-drafted and no person has reviewed them yet | # yaml-language-server: $schema=https://cgiar-climate-data-hub.github.io/cdh-metadata-standard/v0.5.0/schemas/profiles/… |  | a person must confirm title, description, note, usage and every cdh field (REVIEW.md) |
| MED | `/additional_links/2/url` | link | URL unreachable (404) | https://www.imf.org/en/Publications/FM |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| MED | `/contact/0/url` | link | URL unreachable (404) | https://www.imf.org/en/Publications/FM |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| LOW | `/processing/0/derived_from/0/version` | provenance | source version not pinned | IMF Fiscal Monitor |  |  |
| INFO | `/` | schema | validate-yaml.js (v0.5.0): ok |  |  |  |

Rule (standard §4.6): nothing above is auto-fixed; an authored value wins until a person decides which side is wrong.

## Triage (2026-10-19, before human review)

- **asset-prefix (MED)**: expected for a federated API record — the location is an API base, not a file prefix; the verifier cannot list it. Contents checked instead by running `example.py` against the live API (2026-10-19).
- **data360 404/400 (HIGH)**: the bare /data360/data base returns 400 without DATABASE_ID; with `DATABASE_ID=IMF_FM&REF_AREA=TGO` it returns 200 JSON.
- **imf.org 404/403 (HIGH/MED)**: bot-blocked; https://www.imf.org/en/Publications/FM opened in a browser and is live (October 2026 Fiscal Monitor, 14 Oct 2026).
- **source version not pinned (LOW)**: set at review to the Fiscal Monitor vintage (e.g. October 2026) if Data360 has picked it up — _TBC_.
