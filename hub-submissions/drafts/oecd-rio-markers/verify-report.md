# Verification — `oecd-rio-markers` (v1.6, schema v0.5.0)

File `oecd-rio-markers/oecd-rio-markers.yaml` · 4 URLs probed · 0 assets opened · HIGH 0 · MED 2 · LOW 1 · INFO 2

| Sev | Path | Check | Finding | Record says | Observed | Hint |
|---|---|---|---|---|---|---|
| MED | `/` | authored | authored fields were machine-drafted and no person has reviewed them yet | # yaml-language-server: $schema=https://cgiar-climate-data-hub.github.io/cdh-metadata-standard/v0.5.0/schemas/profiles/… |  | a person must confirm title, description, note, usage and every cdh field (REVIEW.md) |
| MED | `/data/0/locations/0` | asset-prefix | prefix location without href_template or file_index — cannot verify contents | https://sdmx.oecd.org/dcd-public/rest/data/OECD.DCD.FSD,DSD_RIOMRKR@DF_RIOMARKERS,1.6/ |  |  |
| LOW | `/contact/0/url` | link | URL unreachable (403) | https://www.oecd.org/en/about/directorates/development-co-operation-directorate.html |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| INFO | `/` | schema | validate-yaml.js (v0.5.0): ok |  |  |  |
| INFO | `/data/0` | inspect | no inspector for media_type 'application/vnd.sdmx.genericdata+xml' — contents not verified | https://sdmx.oecd.org/dcd-public/rest/data/OECD.DCD.FSD,DSD_RIOMRKR@DF_RIOMARKERS,1.6/ |  |  |

Rule (standard §4.6): nothing above is auto-fixed; an authored value wins until a person decides which side is wrong.

## Triage (2026-10-19, before human review)

- **asset-prefix (MED)**: expected for a federated API record — the location is an API base, not a file prefix; the verifier cannot list it. Contents checked instead by running `example.py` against the live API (2026-10-19).
- **oecd.org 403**: bot-blocked; DCD page live in a browser.
- **Fixed after the first verify run**: dead citation URL replaced; `derived_from.id: oecd-dac-crs` (not yet a catalog record) swapped for the CRS Data Explorer URL; marker/score categories checked against CL_CRS_MARKER / CL_CRS_SCORE and the live TGO data (only markers 10-50, scores 0/1/2/99, MD_DIM _T occur); removed advice to deduplicate via MD_DIM DD, which this dataflow does not serve.
