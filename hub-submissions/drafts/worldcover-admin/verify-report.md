# Verification — `worldcover-admin` (v1, schema v0.5.0)

File `worldcover-admin/worldcover-admin.yaml` · 6 URLs probed · 0 assets opened · **HIGH 2** · MED 3 · LOW 1 · INFO 1

| Sev | Path | Check | Finding | Record says | Observed | Hint |
|---|---|---|---|---|---|---|
| HIGH | `/data/0/href_template` | template-expansion | 1/1 sampled template expansions do not exist | worldcover_admin_area_{iso3}.parquet | [["worldcover_admin_area_TGO.parquet", 404]] | dimension values and file names disagree (case, spelling, order) |
| HIGH | `/data/1/href_template` | template-expansion | 1/1 sampled template expansions do not exist | worldcover_admin_cropland_{iso3}.parquet | [["worldcover_admin_cropland_TGO.parquet", 404]] | dimension values and file names disagree (case, spelling, order) |
| MED | `/` | authored | authored fields were machine-drafted and no person has reviewed them yet | # yaml-language-server: $schema=https://cgiar-climate-data-hub.github.io/cdh-metadata-standard/v0.5.0/schemas/profiles/… |  | a person must confirm title, description, note, usage and every cdh field (REVIEW.md) |
| MED | `/data/0` | inspect | could not open asset: HTTPException: HTTP Error: HTTP GET error on 'https://digital-atlas.s3.amazonaws.com/cdh/data/worldcover-admin/v1/' (HTTP 404 Not Found | https://digital-atlas.s3.amazonaws.com/cdh/data/worldcover-admin/v1/ |  |  |
| MED | `/data/1` | inspect | could not open asset: HTTPException: HTTP Error: HTTP GET error on 'https://digital-atlas.s3.amazonaws.com/cdh/data/worldcover-admin/v1/' (HTTP 404 Not Found | https://digital-atlas.s3.amazonaws.com/cdh/data/worldcover-admin/v1/ |  |  |
| LOW | `/processing/1/code/version` | provenance | code version/commit not pinned | https://github.com/CGIAR-Climate-Data-Hub/use-cases/blob/main/gcf-preparation-facility/code/worldcover/worldcover_admin.py |  |  |
| INFO | `/` | schema | validate-yaml.js (v0.5.0): ok |  |  |  |

Rule (standard §4.6): nothing above is auto-fixed; an authored value wins until a person decides which side is wrong.

## Triage (2026-10-20, before human review)

- **template-expansion / inspect (HIGH x2, MED x2)**: expected. The data are not uploaded yet because the CDH bucket is pending (cdh-catalog#74), so the planned location returns 404. Checked instead against a local Togo run (2026-10-20, 462 s): every column in both structures is in the file and vice versa, dtypes match, classes present are 10, 20, 30, 40, 50, 60, 80, 90 and 95, and shares fall in 0-1. The Togo country total is 5,705,049 ha against an official land area of about 5.68 M ha (+0.5%, the centre-pixel rule).
- **Producer fix found while drafting**: gaul1_code and gaul2_code were written as float (NaN on higher-level rows). The script now writes nullable Int64.
- **code version not pinned (LOW)**: pin to the commit once this branch is merged and the upload run is done.
- **Not published**: the 2020 to 2021 change table the script also writes, following the esa-worldcover-2021 record's own warning that the two maps use different algorithms.
