# Verification — `oecd-dac-crs` (v1.6, schema v0.5.0)

File `oecd-dac-crs/oecd-dac-crs.yaml` · 3 URLs probed · 0 assets opened · **HIGH 1** · MED 1 · LOW 2 · INFO 2

| Sev | Path | Check | Finding | Record says | Observed | Hint |
|---|---|---|---|---|---|---|
| HIGH | `/processing/0/derived_from/0/url` | link | URL unreachable (403) | https://www.oecd.org/en/about/directorates/development-co-operation-directorate.html |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| MED | `/data/0/locations/0` | asset-prefix | prefix location without href_template or file_index — cannot verify contents | https://sdmx.oecd.org/dcd-public/rest/data/OECD.DCD.FSD,DSD_CRS@DF_CRS,1.6/ |  |  |
| LOW | `/contact/0/url` | link | URL unreachable (403) | https://www.oecd.org/en/about/directorates/development-co-operation-directorate.html |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| LOW | `/processing/0/derived_from/0/version` | provenance | source version not pinned | OECD DAC and CRS statistical reporting by providers |  |  |
| INFO | `/` | schema | validate-yaml.js (v0.5.0): ok |  |  |  |
| INFO | `/data/0` | inspect | no inspector for media_type 'application/vnd.sdmx.genericdata+xml' — contents not verified | https://sdmx.oecd.org/dcd-public/rest/data/OECD.DCD.FSD,DSD_CRS@DF_CRS,1.6/ |  |  |

Rule (standard §4.6): nothing above is auto-fixed; an authored value wins until a person decides which side is wrong.


## Triage (2026-10-19, before human review)

- **asset-prefix (MED)**: expected for a federated API record — the location is an API base, not a file prefix; the verifier cannot list it. Contents checked instead by running `example.py` against the live API (2026-10-19).
- **oecd.org 403s**: Cloudflare blocks scripted requests; the DCD page was opened in a browser and is live (2026-10-19).
- **Fixed after the first verify run**: three oecd.org URLs drafted from memory were dead (404 in a browser) and were replaced with Data Explorer / SDMX codelist URLs; media_type corrected to SDMX-ML (the bare endpoint's default).
- **source version not pinned (LOW)**: provider reporting has no version; left unpinned.
