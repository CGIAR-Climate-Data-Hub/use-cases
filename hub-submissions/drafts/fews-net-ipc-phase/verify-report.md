# Verification — `fews-net-ipc-phase` (vfdw-api, schema v0.5.0)

File `fews-net-ipc-phase/fews-net-ipc-phase.yaml` · 5 URLs probed · 1 assets opened · **HIGH 1** · MED 2 · LOW 0 · INFO 1

| Sev | Path | Check | Finding | Record says | Observed | Hint |
|---|---|---|---|---|---|---|
| HIGH | `/data/0/locations/0` | api | endpoint returned 500 | https://fdw.fews.net/api/ipcphase/ |  |  |
| MED | `/` | authored | authored fields were machine-drafted and no person has reviewed them yet | # yaml-language-server: $schema=https://cgiar-climate-data-hub.github.io/cdh-metadata-standard/v0.5.0/schemas/profiles/… |  | a person must confirm title, description, note, usage and every cdh field (REVIEW.md) |
| MED | `/data/0/locations/0` | asset-prefix | prefix location without href_template or file_index — cannot verify contents | https://fdw.fews.net/api/ipcphase/ |  |  |
| INFO | `/` | schema | validate-yaml.js (v0.5.0): ok |  |  |  |

Rule (standard §4.6): nothing above is auto-fixed; an authored value wins until a person decides which side is wrong.

## Triage (2026-10-19, before human review)

- **asset-prefix (MED)**: expected for a federated API record — the location is an API base, not a file prefix; the verifier cannot list it. Contents checked instead by running `example.py` against the live API (2026-10-19).
- **inspect timeout (MED)**: the bare /api/ipcphase/ (no filter) times out or returns 500 — the endpoint needs a country_code filter. Filtered request returns 200 JSON.
- **Licence _TBC_**: no FEWS NET terms-of-use page found (fews.net/terms-use 404); confirm terms before submission.
