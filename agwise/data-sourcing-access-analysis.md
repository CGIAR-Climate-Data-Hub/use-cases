# AgWise data-sourcing workflow: dataset access analysis

**Purpose:** Self-contained handoff for another AI session working on the CGIAR Climate Data Hub (CDH) AgWise use case.

**Reviewed:** 2026-10-07

## Scope and evidence boundary

This note analyses the workflow implemented in [`byliz-ai/data_sourcing`](https://github.com/byliz-ai/data_sourcing), whose Python package is named `agwise-data`. It answers two questions:

1. Which datasets can this workflow pull?
2. For each dataset, does the workflow request a spatial subset through an API/service, read a remote file selectively, download a large source file, or require data to be staged locally first?

This note does **not** establish behaviour for other packages or services mentioned in the AgWise brief, including `ag-cube-cm`, `aggeodata`, Jemal's Climate API, or CHIRTS. Those require separate review.

Background references supplied for this work:

- [AgWise data-sourcing repository](https://github.com/byliz-ai/data_sourcing)
- [CDH use-cases repository](https://github.com/CGIAR-Climate-Data-Hub/use-cases)
- [Private Teams conversation](https://teams.microsoft.com/l/chat/19:06752cfca2ce472e81f5ce869461f9f9@thread.v2/conversations?context=%7B%22contextType%22%3A%22chat%22%7D) — reference only; conversation content was not available for this review and is not represented below.

## Executive answer

The workflow does not download every catalogued dataset on every run. Users request variables, region, and time period; the workflow selects the corresponding source and caches harmonized regional output.

Most sources support regional retrieval through an API, standards-based service, Earth Engine, or Cloud Optimized GeoTIFF (COG) range reads. Main bulk-data exceptions are:

- **CHIRPS v2 large-domain/fallback path:** downloads one full global NetCDF for each requested year, then crops it.
- **CHIRPS v3:** requires full global yearly files to have been staged locally; no network retrieval path is wired into the workflow.
- **iSDAsoil:** requires Africa-wide property/depth rasters to have been staged locally; provider REST API exists but is not used by this workflow.
- **geoBoundaries:** downloads complete boundary file for requested country and administrative level, not global boundary collection.

No implemented path downloads an entire multi-decade global archive in one operation.

## Source-selection logic

Configured CGLabs runs generally follow this order:

1. Reuse compatible source data already staged in `Global_GeoData/Landing`.
2. Reuse harmonized regional product already present in shared `Global_GeoData/Processed` cache.
3. Retrieve missing regional data through source-specific driver.
4. Harmonize variable names and units, then cache regional result.

Local reuse means two different quantities must not be confused:

- **Data present on shared storage:** source file may be global, continental, yearly, or tiled.
- **Data read into a request:** workflow normally reads only requested spatial window from that staged file.

## Dataset-by-dataset access map

| Dataset | Variables used by workflow | Workflow access order | Network transfer behaviour | Authentication | Full-source requirement |
| --- | --- | --- | --- | --- | --- |
| **AgERA5 v2** | `TMAX`, `TMIN`, `TEMP`, `SRAD`, `RHUM`, `WIND`; optional `PRCP` | Staged yearly NetCDF first; otherwise Copernicus CDS API | CDS request includes requested bounding box, year, variable, statistic, months, and days | CDS account and token | **No network full-source download.** Staged file may be global; NetCDF hyperslab reads only requested bbox. |
| **ECMWF SEAS5 system 51** | Forecast/hindcast `PRCP`, `TMAX`, `TMIN`, `TEMP`, `SRAD` | Copernicus CDS API | Request includes bbox, initialization, members, lead times, and requested variable | CDS account and token | **No.** CDS returns requested subset. |
| **SoilGrids 2.0** | Texture, pH, SOC, nitrogen, CEC, bulk density, coarse fragments, water-retention variables | Staged property/depth GeoTIFFs first; otherwise OGC WCS | `GetCoverage` requests requested bbox, split into chunks no larger than 2 degrees per side | None | **No network full-source download.** Local global rasters are read by raster window. |
| **iSDAsoil v0.13** | Alternative `CLAY`, `SAND`, `SILT`, `PH`, `SOC`, `CEC`, `BDOD`, `EXTP` | Local staged raster only | No network request implemented | None during workflow run | **Yes, before use.** Africa-wide raster for each needed property/depth must already be staged; workflow then reads bbox window only. |
| **MODIS MOD13Q1 (Terra)** | `NDVI`, `EVI` | Domain-tagged local composites first; otherwise Google Earth Engine | Earth Engine `computePixels` requests tiled bbox for each available composite | Earth Engine credentials and Google Cloud project | **No.** Only requested bbox/composites transferred. |
| **MODIS MYD13Q1 (Aqua)** | `NDVI`, `EVI` | Google Earth Engine | Same tiled `computePixels` approach | Earth Engine credentials and project | **No.** Only requested bbox/composites transferred. |
| **ESA WorldCover 2021 v200** | Cropland mask derived from land-cover class 40 | Google Earth Engine | Cropland fraction computed server-side, aggregated to MODIS-aligned grid, then requested bbox transferred through `computePixels` | Earth Engine credentials and project | **No.** Only derived regional grid transferred. |
| **Copernicus DEM GLO-30** | Elevation; slope, aspect, TPI, and TRI derived locally | Staged 1-degree tile first; otherwise public AWS COG | Opens only intersecting 1-degree tiles and reads required windows through HTTP range requests | None | **No.** No full-tile or global download required by driver. CGLabs separately maintains staged Africa tiles. |
| **CHIRPS v2** | Daily precipitation | For small regions: daily COG windows; then Earth Engine mirror; finally yearly global NetCDF fallback. Large domains go to yearly NetCDF. Local staged file can supersede network retrieval. | COG path transfers bbox windows. Earth Engine transfers bbox. NetCDF fallback downloads about 1.1 GB global file per requested year, then crops. | None for CHC HTTP/COG; Earth Engine credentials for GEE fallback | **Conditional.** Full global **yearly** file downloaded only for large-domain or fallback path—not full historical archive. |
| **CHIRPS v3** | Daily precipitation | Local staged yearly NetCDF only | No network fetch wired | None during workflow run | **Yes, before use.** Global yearly files must already be staged; workflow reads bbox hyperslab. Catalog currently describes staged 1981–2025 coverage. |
| **geoBoundaries** | Country/admin geometries used to define and clip AOIs | geoBoundaries HTTP JSON API, followed by geometry-file download | Retrieves metadata, then downloads complete GeoJSON for requested ISO3 country and ADM level | None | **Partial.** Complete requested country/admin-level file downloaded; no global collection download. |

## Access-interface classification for CDH

CDH should describe these under **Data access interfaces**, not force every route into a generic “API” category.

| Dataset | Recommended CDH interface type | Primary identifier or endpoint |
| --- | --- | --- |
| AgERA5 | CDS API; STAC discovery; local-file alternative | `sis-agrometeorological-indicators` |
| SEAS5 | CDS API; STAC discovery | `seasonal-original-single-levels` |
| SoilGrids | OGC WCS; WMS for visualization; local-file alternative | `https://maps.isric.org/mapserv?map=/map/{property}.map` |
| iSDAsoil | Local staged raster in current workflow; provider REST API as separate documented option | Provider API base: `https://api.isda-africa.com`; current workflow does not call it |
| MOD13Q1 | Earth Engine platform API; local-file alternative | `MODIS/061/MOD13Q1` |
| MYD13Q1 | Earth Engine platform API | `MODIS/061/MYD13Q1` |
| ESA WorldCover | Earth Engine platform API | `ESA/WorldCover/v200` |
| Copernicus DEM | Public S3 object storage; COG; STAC | `s3://copernicus-dem-30m` |
| CHIRPS v2 | HTTPS COG/file distribution; Earth Engine platform API; local-file alternative | `UCSB-CHG/CHIRPS/DAILY` for Earth Engine |
| CHIRPS v3 | Local staged file in current workflow; CHC file distribution as separate provider access route | CHC CHIRPS v3 repository |
| geoBoundaries | REST-like HTTP JSON API plus downloadable GeoJSON | `https://www.geoboundaries.org/api/current/gbOpen/{iso3}/ADM{level}/` |

## Decision implications for CDH

### Good candidates for direct regional retrieval

- AgERA5 through CDS
- SEAS5 through CDS
- SoilGrids through WCS
- MODIS Terra/Aqua through Earth Engine
- ESA WorldCover through Earth Engine
- Copernicus DEM through COG window reads
- CHIRPS v2 through COG or Earth Engine for small regions
- geoBoundaries through country/admin-level downloads

### Sources needing storage or ingestion decisions

- **CHIRPS v2:** decide whether CDH should rely on COG/Earth Engine regional requests or retain yearly global NetCDF fallback. Large yearly files create bandwidth, latency, and temporary-storage costs.
- **CHIRPS v3:** decide whether CDH will preserve local yearly staging, add direct CHC retrieval, add Earth Engine retrieval, or publish a CDH-managed regional/subsetting service.
- **iSDAsoil:** decide whether CDH will keep Africa-wide staged rasters or implement provider API access. Provider API gives point values, while current workflow needs regional rasters; these are not equivalent interfaces.
- **Earth Engine sources:** document account/project dependency and decide whether CDH execution uses user credentials, service credentials, or a CDH-hosted derived-data layer.
- **CDS sources:** document personal-token or service-account model, request limits, cache ownership, and expected refresh process.

## Recommended catalog metadata

Each CDH dataset record should distinguish provider capabilities from workflow implementation. Suggested fields:

- `provider`
- `dataset_id`
- `version`
- `variables`
- `spatial_extent`
- `temporal_extent`
- `spatial_resolution`
- `temporal_resolution`
- `provider_access_interfaces`
- `workflow_access_interface`
- `endpoint_or_collection_id`
- `authentication`
- `supports_spatial_subset`
- `supports_temporal_subset`
- `transfer_granularity` — bbox, tile, day, month, year, country/admin file, or full archive
- `local_staging_required`
- `cache_location_and_scope`
- `fallback_sequence`
- `output_format`
- `license`
- `citation`
- `update_frequency`
- `last_verified`
- `known_service_constraints`

## Important reconciliation items

Current public AgWise brief and `byliz-ai/data_sourcing` workflow are related but not identical inventories:

- AgWise brief mentions **CHIRTS**, `ag-cube-cm`, `aggeodata`, and Jemal's **Climate API**. None were assessed here.
- `byliz-ai/data_sourcing` additionally catalogs SEAS5, iSDAsoil, MODIS, ESA WorldCover, Copernicus DEM, and geoBoundaries.
- Brief describes CHIRPS as unauthenticated. This is true for CHC file/COG access, but workflow may use Earth Engine fallback, which requires credentials.
- Brief lists SoilGrids without access details. Current workflow uses WCS regional subsets or local windowed rasters.
- Before updating canonical `agwise/BRIEF.md`, team should confirm whether `byliz-ai/data_sourcing` supersedes, complements, or remains separate from `aggeodata` and `ag-cube-cm`.

## Source-code evidence

- [Workflow overview and source list](https://github.com/byliz-ai/data_sourcing/blob/main/README.md)
- [AgERA5 driver](https://github.com/byliz-ai/data_sourcing/blob/main/src/agwise_data/drivers/agera5.py)
- [SEAS5 driver](https://github.com/byliz-ai/data_sourcing/blob/main/src/agwise_data/drivers/seasonal.py)
- [SoilGrids driver](https://github.com/byliz-ai/data_sourcing/blob/main/src/agwise_data/drivers/soil.py)
- [iSDAsoil driver](https://github.com/byliz-ai/data_sourcing/blob/main/src/agwise_data/drivers/isda.py)
- [MODIS driver](https://github.com/byliz-ai/data_sourcing/blob/main/src/agwise_data/drivers/modis.py)
- [ESA WorldCover driver](https://github.com/byliz-ai/data_sourcing/blob/main/src/agwise_data/drivers/worldcover.py)
- [Copernicus DEM driver](https://github.com/byliz-ai/data_sourcing/blob/main/src/agwise_data/drivers/dem.py)
- [CHIRPS v2 driver](https://github.com/byliz-ai/data_sourcing/blob/main/src/agwise_data/drivers/chirps.py)
- [CHIRPS v3 catalog entry](https://github.com/byliz-ai/data_sourcing/blob/main/src/agwise_data/catalog/chirps_v3.yaml)
- [Local-file adapter](https://github.com/byliz-ai/data_sourcing/blob/main/src/agwise_data/drivers/local.py)
- [Earth Engine tiled pixel retrieval](https://github.com/byliz-ai/data_sourcing/blob/main/src/agwise_data/drivers/gee.py)
- [geoBoundaries integration](https://github.com/byliz-ai/data_sourcing/blob/main/src/agwise_data/boundaries.py)

## Suggested next prompt for another AI session

> Read `agwise/BRIEF.md` and `agwise/data-sourcing-access-analysis.md`. Reconcile the public AgWise use-case brief with the `byliz-ai/data_sourcing` workflow without inventing relationships between repositories. Identify confirmed overlaps, discrepancies, and `_TBC_` items. Propose minimal edits to `agwise/BRIEF.md`, but do not edit until requested. Preserve the distinction between provider access interfaces and the access path actually implemented by the workflow.
