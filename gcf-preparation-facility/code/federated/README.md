# Federated-source clients — GCF Preparation Facility

Small Python clients for the review's **P1 "federate" datasets**: each one hits the provider's
live API for a country and returns a tidy admin0/admin1 table in one common schema. They prove
the federation route end to end and are the data layer the planned `climate-rationale` skill
reads. Every request URL is kept on the row (`source_url`) — a deterministic query *is* the
citation.

Queue + routes: [`../../data/ingestion-queue.csv`](../../data/ingestion-queue.csv) ·
licences and rescreen results: [`../../methods/evidence/sources.md`](../../methods/evidence/sources.md).

## Run

```bash
pip install -r requirements.txt           # requests, pandas, pyarrow
python -m cdh_federated TGO --out out     # all sources for Togo
python -m cdh_federated KEN --only inform,dhs,fews_net
```

Outputs per source `out/<source>_<ISO3>.parquet` (+ `.csv`), a combined
`out/federated_<ISO3>.parquet`, and `out/manifest_<ISO3>.json` (row counts, retrieval
timestamps, request URLs, licences). One failing provider never stops the others; the manifest
records `status` per source.

## Sources (verified live 2026-10-07)

| key | provider / endpoint | admin | key? | licence |
| --- | --- | --- | --- | --- |
| `inform` | INFORM Risk, JRC `Countries/Scores/?WorkflowId=&Iso3=&IndicatorId=` | 0 | no | CC BY 4.0 (EC reuse policy) |
| `fews_net` | FEWS NET FDW `api/ipcphase/?country_code=` | 0 + food-security units | no | open (US Gov / USAID) |
| `dhs` | DHS Indicator API `rest/dhs/data?breakdown=subnational` | 0, 1 | no | open aggregates (microdata excluded) |
| `oecd_crs` | OECD SDMX `dcd-public` `DSD_CRS@DF_CRS` — ODA disbursements by sector | 0 | no | CC BY 4.0 |
| `oecd_rio_markers` | OECD SDMX `dcd-public` `DSD_RIOMRKR@DF_RIOMARKERS` — adaptation/mitigation-marked commitments | 0 | no | CC BY 4.0 |
| `data360_imf_fm` | World Bank Data360 `IMF_FM` (debt, revenue, expenditure, balance % GDP) | 0 | no | CC BY 4.0 |
| `data360_wb_ids` | World Bank Data360 `WB_IDS` (external debt stocks / service) | 0 | no | CC BY 4.0 |
| `climate_watch` | Climate Watch `ndcs/<ISO3>/content_overview` + `/text` | 0 | no | CC BY 4.0 |
| `unicef_jmp` | UNICEF SDMX `WASH_HOUSEHOLDS` (JMP WASH ladders) | 0 | no | CC BY-NC-SA 3.0 IGO (reports) |
| `gfw` | GFW Data API `gadm__tcl__{iso,adm1}_summary` | 0, 1 | **yes** — `GFW_API_KEY` | CC BY 4.0 |

Not here (key-gated, pending registration): IATI Datastore (API Gateway subscription), Protected
Planet (token), IPC/CH API (key). GFW runs once `GFW_API_KEY` is set (free: `/auth/sign-up` →
`/auth/token` → `/auth/apikey`).

## Schema

One row = one observation for one admin unit (`cdh_federated.common.TIDY_COLUMNS`):
`iso3, admin_level, admin_name, admin_code, source, dataset, indicator_id, indicator, value,
value_text, unit, period, scenario, qualifiers (JSON), retrieved_at, source_url, licence`.
Provider-specific dimensions (donor, sector, marker, residence, survey id …) live in `qualifiers`.

## Gotchas learned while building this

- **OECD**: the CRS / Rio-marker dataflows are external references — query
  `sdmx.oecd.org/dcd-public/rest/`, not `/public/rest/`. SDMX-3 `c[RECIPIENT]=` filters are
  ignored (you get the whole 1.2 GB cube); use positional keys (dimension order in `oecd.py`).
  All-DAC donor is `DAC` in CRS but `DAC_EC` in Rio markers. Values are USD millions.
- **INFORM**: `Iso3=` filters; `CountryIso3Codes=` is silently ignored and returns every country.
  `workflow_id` = INFORM release — the workflow listing endpoint is not public, confirm the id on
  the INFORM site. **Unresolved:** one workflow × one indicator returns ~72 distinct scores per
  country with no year/node label; the client keeps them all and tags
  `qualifiers.semantics = "unresolved"`. Don't average. Ask INFORM (or use the annual results
  file) before quoting a single number.
- **FEWS NET**: Togo has no `admin1`/`admin2` rows — its subnational units are `fsc_admin_lhz`
  (admin × livelihood zone), kept as admin_level 1 with `unit_type` in qualifiers.
- **DHS**: country codes are DHS's own two-letter codes (`NER` → `NI`, `BDI` → `BU`); the map in
  `dhs.py` covers the current GCF pipeline countries — extend as needed.
- **Data360**: IMF indicator ids are `IMF_FM_G_XWDG_G01_GDP_PT`-style (with the odd `G_X`), not the
  IMF's own `GGXWDG_NGDP`; list them with `/indicators?datasetId=IMF_FM`.
- Several providers reset connections mid-response (INFORM, FEWS); `common.get` retries.
