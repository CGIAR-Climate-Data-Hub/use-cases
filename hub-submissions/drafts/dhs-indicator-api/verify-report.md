# Verification — `dhs-indicator-api` (v8.1, schema v0.5.0)

File `dhs-indicator-api/dhs-indicator-api.yaml` · 8 URLs probed · 0 assets opened · **HIGH 2** · MED 0 · LOW 0 · INFO 1

| Sev | Path | Check | Finding | Record says | Observed | Hint |
|---|---|---|---|---|---|---|
| HIGH | `/data/0/locations/0` | asset-url | primary data location unreachable (404) | https://api.dhsprogram.com/rest/dhs/data |  |  |
| HIGH | `/data/0/locations/0/url` | link | URL unreachable (404) | https://api.dhsprogram.com/rest/dhs/data |  | bot-blocked hosts (403) need a browser check; drop URLs you cannot source |
| INFO | `/` | schema | validate-yaml.js (v0.5.0): ok |  |  |  |

Rule (standard §4.6): nothing above is auto-fixed; an authored value wins until a person decides which side is wrong.


## Triage (2026-10-20, before human review)

- **data endpoint 404/400 (HIGH x2)**: the bare /rest/dhs/data returns 400 without a filter. With `countryIds=TG&indicatorIds=CN_NUTS_C_HA2&breakdown=subnational&f=json` it returns 200 JSON; `example.py` ran against it (2026-10-20).
- **Licence**: the API terms ask only for the citation (quoted in `attribution`, also served at /rest/dhs/info/citation). Kept as a LicenseRef because no open licence is named.
- **Client bug found while drafting**: `cdh_federated/dhs.py` read `Precision` (decimal places) as a percent flag. Units now come from indicator `MeasurementType`.
