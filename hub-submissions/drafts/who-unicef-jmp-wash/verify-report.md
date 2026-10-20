# Verification — `who-unicef-jmp-wash` (v1.0, schema v0.5.0)

File `who-unicef-jmp-wash/who-unicef-jmp-wash.yaml` · 4 URLs probed · 1 assets opened · HIGH 0 · MED 1 · LOW 0 · INFO 1

| Sev | Path | Check | Finding | Record says | Observed | Hint |
|---|---|---|---|---|---|---|
| MED | `/data/0/locations/0` | asset-prefix | prefix location without href_template or file_index — cannot verify contents | https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/UNICEF,WASH_HOUSEHOLDS,1.0/ |  |  |
| INFO | `/` | schema | validate-yaml.js (v0.5.0): ok |  |  |  |

Rule (standard §4.6): nothing above is auto-fixed; an authored value wins until a person decides which side is wrong.


## Triage (2026-10-20, before human review)

- **asset-prefix (MED)**: expected for a federated SDMX record. Contents checked by running `example.py` against the live API (2026-10-20).
- **Licence _TBC_**: no data licence on washdata.org; the UNICEF legal page asks for permission before republishing. The record says federate only; confirm with JMP before any hosted derivative.
