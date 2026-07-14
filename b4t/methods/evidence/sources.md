# Evidence & sources log

## Licence summary (verified 2026-07-03)

Permissive (CDH can host/redistribute): CHIRPS v3 (public domain + CC-BY 4.0); NEX-GDDP-CMIP6 (CC-BY 4.0 / CC0); FAO GAEZ v5 (CC-BY 4.0; HWSD sub-component CC-BY-NC-SA); Aqueduct 4.0 (CC-BY 4.0); Aqueduct Floods (open, attribution requested); SPEIbase (ODbL); L-WRSI (CC0) / crop-WRSI (USGS public domain); **FAO ASI = CC-BY 4.0** (current FAO catalog record — supersedes an older CC-BY-NC-SA 3.0 IGO reference); **GEHE = CC-BY 4.0** (NASA CMR UseConstraints: explicitly commercial **and** non-commercial); ISRIC SoilGrids 2.0 & salinity (CC-BY 4.0); Stocker 2023 (CC-BY 4.0); **Gupta 2023 = CC-BY 4.0** (Zenodo 6777126); Mehta AEI + Gao projected AEI (CC-BY 4.0); Copernicus CDS sea-level indicators (coastal driver, F-03 Phase-2) = CC-BY. CDH SPEI = internal (Hub-owned).

**Non-commercial — usable, since CDH/CGIAR is a non-profit NGO (NC restricts *commercial* use):** **Global Flood Database (F-01) = CC BY-NC 4.0** (GEE) / CC BY-NC-**ND** (HydroShare — avoid the ND mirror; use GEE so derivatives are allowed); **GIRI (F-02) = non-commercial + attribution, via registration**. Terms respected: attribution on all, **share-alike where required (ODbL, SPEIbase)**, NC passed through on redistribution. **One item still to confirm:** **FAO GSASmap (S-01)** = licence not printed on the product page — CC-BY 4.0 by FAO's default database policy, but a third-party-data carve-out may apply (~257k national points, 118+ countries); confirm on the GloSIS platform record. *(Gupta 2023 and GEHE, previously unconfirmed, now verified CC-BY 4.0; FAO ASI resolved to CC-BY 4.0.)*

One entry per external source consulted, with what it verified and when. Candidate-dataset claims in [../dataset-review.md](../dataset-review.md) must trace to an entry here. Verified live via WebFetch on the date shown.

## Internal CDH assets (build on these first)

Per the CDH team (July 2026). Recommendations build on these ready-to-adopt products first.

### CHIRPS-CHIRTS-ERA5 SPEI (observational track) — recommended for D-01

- **SPEI** at 1, 3, 6, 12, 24-month accumulation scales. **No pure SPI** produced (precip-only index = backlog).
- Precip = CHIRPS v3 monthly (station-merged satellite); Temp = CHIRTS-ERA5 monthly TMAX/TMIN/TAVG (for PET).
- PET = **Hargreaves 1985** (FAO-56 Allen 1998, latitude-based Ra). Chain: CWB = PTOT − PET → `SPEI::spei()`. Distribution log-Logistic, ub-pwm fit. Reference period **1991–2020** (WMO/AR6).
- Grid: native CHIRPS **0.05°**, currently produced for **Africa (−20…55°E, −40…40°N)**; the same pipeline **extends to global** (CHIRPS bounds coverage to 60°N–60°S). Coverage 1981-01 → present. Extending globally is a pipeline re-run (modest compute/storage), not a new indicator.
- Artifacts: per-pixel monthly SPEI COGs (Tier 3, cglabs/Afrilabs local only, ~13.5k files/~50 GB, NOT on S3); SPEI **climatology** COGs (Tier 2, published to `s3://digital-atlas/domain=climate/type=observational/source=chirps-chirts-era5/…processing=climatology/variable=SPEI-NN/…`); admin-aggregated SPEI parquet at adm0/adm1.
- Caveats for the review: SPEI ≠ SPI/WASP (includes evaporative demand, partly overlaps the heat hazard); Africa-only (not global); ±Inf tails masked→NA before aggregation (~0.018% cell-months, benign).

### NASA NEX-GDDP-CMIP6 v2 (projections track)

- Internal CMIP6/SSP downscaled projections track — the natural modernization source for the future-facing rows (R-01/02 LGP, T-02 heat, changed-rainfall projections). Distinct PET implementation from the observational track.

### Water-balance v2 (projections track) — NDWS / NDWL

- FAO-56 Penman-Monteith ET₀ water-balance products (number of water-stress / water-logging days). Candidate for soil-water / water-stress rows (W-*), and relevant to flooding/waterlogging.
- Note: two separate PET implementations across tracks — Hargreaves (observational SPEI) vs FAO-56 Penman-Monteith (projections water-balance).

## D-01 — Drought (SPI / drought-event frequency)

### CHIRPS v3 — Climate Hazards Center, UC Santa Barbara

- Official page: <https://www.chc.ucsb.edu/data/chirps3>
- Data root: <https://data.chc.ucsb.edu/products/CHIRPS/v3.0/>
- 3-monthly GeoTIFFs (confirmed directory chain resolves): <https://data.chc.ucsb.edu/products/CHIRPS/v3.0/3-monthly/global/tifs/>
- Verified 2026-07-02, cross-checked by adversarial pass same date: 0.05° resolution; coverage **60°N–60°S**, all longitudes (expanded from v2's 50°N–50°S); 1981–near-present; fundamentally a pentad+monthly product with daily/dekad/annual and 2–6-month aggregations derived; improvements over v2 = new CHIRP3 algorithm (better high-rainfall estimation), IMERG **v6 Final** feeding the CHPclim2 climatological baseline, ~4× more gauge sources, gauge-undercatch (Legates-Willmott) correction; licence — the CHC v3 page states BOTH **public domain** (CHC "waived all copyright", registered with Creative Commons) AND **CC-BY 4.0**, i.e. effectively public-domain-with-attribution (adversarial re-check 2026-07-03 corrected the earlier "CC-BY-only, not public domain" note); both a "final" and a "preliminary" product stream exist. v2 production continues through 2026 during transition.
- CHIRPS v2 page (<https://www.chc.ucsb.edu/data/chirps>) verified same date: v2 coverage 50°S–50°N; public-domain (CC waiver) — this is the source of the earlier public-domain note, which applies to v2, not v3; "Production of CHIRPS v2 will end after December 2026. Users are encouraged to transition to CHIRPS v3."

### SPEIbase — SPEI Global Database (CSIC)

- Official page: <https://spei.csic.es/database.html>
- Access: <https://spei.csic.es/spei_database>
- Verified 2026-07-02: index = SPEI = precipitation **minus** potential evapotranspiration (FAO-56 Penman-Monteith; underlying climate CRU TS) — incorporates temperature/ET, not precip-only; **0.5°** resolution; global emerged-land only; **1901–2024** (v2.11), updated as data arrives; monthly; timescales 1–48 months; licence **ODbL** (attribution + share-alike); netCDF, one file per timescale covering the whole world.

### Metric definitions (verified against WMO)

- Standard **SPI** (McKee, Doesken & Kleist 1993; WMO-endorsed, WMO-No. 1090, 2012) = standardized probability transform of precipitation over a chosen timescale; precipitation-only. **SPEI** adds PET (climatic water balance). The CRI's "≥3 consecutive months with <50% of average precipitation" is a fixed-threshold event/run count — a distinct metric, not SPI, not WMO-standard. WMO SPI user guide: <https://www.droughtmanagement.info/literature/WMO_standardized_precipitation_index_user_guide_en_2012.pdf>

### Other open precipitation baselines (candidate breadth for D-01; reported, not all deep-verified)

- **ERA5-Land** — ECMWF reanalysis, 0.1° (~9 km), hourly, global land, 1950–present; fully open via Copernicus CDS; model-based (precip less directly observed).
- **CHELSA** — ~1 km downscaled climatologies + time series, global land; open GeoTIFFs at chelsa-climate.org; more a climatology product than a near-real-time feed.
- **TAMSAT** — thermal-IR satellite rainfall, Africa only, 0.0375° (~4 km), 1983–present, daily–seasonal; open. (Nature Sci Data: <https://www.nature.com/articles/sdata201763>)
- **MSWEP** — gauge+satellite+reanalysis, ~0.1°, 3-hourly, global, 1979–present; often tops independent comparisons, but registration/request-gated (gloh2o.org) → weaker on the ungated hard filter.

### FAO ASIS — Agricultural Stress Index System (ASI) — agriculture-specific alternative for D-01

- Official / catalog: <https://data.apps.fao.org/catalog/dataset/agricultural-stress-index-system-asis-fao-global-agricultural-drought-monitoring-system>
- Verified via search of official FAO sources 2026-07-02 (direct page fetch pending): global agricultural-drought monitoring, FAO-operated. **ASI** = seasonal index detecting severe agricultural drought, derived from weighted mean **VHI** (Vegetation Health Index), **masked to cropland and timed to each area's crop growing cycle**. Satellite vegetation + land-surface temperature (METOP-AVHRR, 1 km, dekadal, 2007+; record from 1984). Global, **1 km**, **1984–present**, 17,000+ layers. Open: FAO Agro-informatics Platform, WMTS / Image Services, ArcGIS Online, Google Earth Engine (no documented FTP — earlier "FAO FTP" note was unsupported). Construct = realised crop/vegetation stress (not a precipitation index; observational, no future projections).
- **Licence (verified 2026-07-03, FAO data catalog ISO record for "Agricultural stress index near real time (Global – Dekadal – 1 km)", <https://data.apps.fao.org/catalog/iso/66b7d407-edd4-490e-8b71-a9b7db6527f3>):** quoted verbatim — "This work is made available under the Creative Commons Attribution 4.0 International licence (CC-BY-4.0)." The older **CC-BY-NC-SA 3.0 IGO** reference in some documentation is superseded by this current CC-BY-4.0 record.

### Copernicus Combined Drought Indicator (CDI) — multi-indicator agricultural drought

- Factsheet: <https://drought.emergency.copernicus.eu/data/factsheets/factsheet_combinedDroughtIndicator_v4.pdf>
- Verified via search 2026-07-02: combines **SPI + soil-moisture anomaly + fAPAR (vegetation) anomaly** with crop/snow masks; classes Watch / Warning / Alert / Recovery for agricultural drought. EDO (Europe) 1/24° (~5 km), dekadal, 2012+; a global version is available via the Global Drought Observatory (global specs to confirm on direct fetch). Open via EDO/GDO.

### Copernicus Global Drought Observatory (GDO) — NOT YET VERIFIED

- <https://drought.emergency.copernicus.eu/> — download page did not expose product specifics on fetch (2026-07-02). Potential secondary source for ready-made SPI at finer resolution; **do not cite until verified**.

## Aqueduct 4.0 (shared) — D-03/04/05, R-04/05

### WRI Aqueduct 4.0 (Kuzma et al. 2023)

- Research/data: <https://www.wri.org/research/aqueduct-40-updated-decision-relevant-global-water-risk-indicators> · technical note <https://openresearch.amsterdam/image/2023/11/2/aqueduct_40_technical_note.pdf> · GEE <https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Water_Risk_V4_future_annual>
- Verified via search 2026-07-02: hydrology **PCR-GLOBWB 2** forced by **CMIP6** climate. Baseline GCM historical **1960–2014** (future series 2015–2100), bias-corrected to observed forcing. Future periods **2030, 2050, 2080**; scenarios **SSP1-2.6** (optimistic), **SSP3-7.0** (business-as-usual), **SSP5-8.5** (pessimistic). **5 GCMs** (incl. MPI-ESM1-2-HR, MRI-ESM2-0, UKESM1-0-LL), bias-corrected, chosen to span temperature–precipitation variation. Sub-basin spatial unit. Open (WRI data page, Google Earth Engine; CC-BY 4.0).
- **Confirms the "retain if CMIP6" condition.** Open data-use questions for Bert: which version (4.0 vs older CMIP5-era), which scenario + period, ensemble vs single GCM, exact layers/aggregation used in the CRI.

## Salinity, soil water & irrigation (S-01/02, W-01–04, I-01) — all off-the-shelf, verified 2026-07-02

- **S-01 FAO GSASmap** (Global Soil Partnership): salt-affected soils, measured data from 118 countries (~257k national points), EC/ESP/pH + classes at 0–30 & 30–100 cm, GeoTIFF. Access via the **GloSIS data platform** (product pages route to it: <http://54.229.242.119/GloSIS/>) — no plain direct download on the product page. Product pages (<https://www.fao.org/global-soil-partnership/gsasmap/en/>, FAO Soils Portal) checked 2026-07-03: **licence not printed inline.** FAO's default database terms are CC-BY 4.0, but carry a third-party-data carve-out ("data provided by third parties … may not be redistributed or reused without consent"), which GSASmap may fall under given its national-contribution basis. → **CC-BY 4.0 by FAO default policy, unconfirmed for this specific product; confirm on the GloSIS record.** Authoritative; static.
- **S-02 ISRIC Global Soil Salinity** (Ivushkin et al. 2019): remote-sensing salinity for 1986/92/2000/02/05/09/2016, random-forest + WoSIS ECe. Open — ISRIC file server (VRT/GeoTIFF, files.isric.org/public/global_soil_salinity). Overlaps S-01.
- **W-01/W-02 ISRIC SoilGrids 2.0** (soil.copernicus.org/articles/7/217/2021): global soil properties, 250 m, six depths, CC-BY 4.0, open (isric.org/explore/soilgrids, GEE `ISRIC/SoilGrids250m/v2_0`). Volumetric water content at 33/1500 kPa → water retention (W-01) and available water capacity (W-02, FC−WP). Update from the 2017 SoilGrids250m citation.
- **W-03 Stocker et al. 2023** (Nature Geoscience): global rooting-zone water storage capacity + rooting depth. Open — Zenodo 10885724. (A newer GRACE-based root-zone estimate, HESS 2025, exists as an alternative.)
- **W-04 Gupta et al. 2023** (JAMES, 10.1029/2022MS003277): global potential + climatic plant-available soil water. **Dataset verified open 2026-07-03 — Zenodo 6777126 (DOI 10.5281/zenodo.6777126), CC-BY 4.0.** Four 1 km global rasters per 1 m soil depth (matric potential & water content at field capacity; potential & climatic plant-available soil water), ~2.2 GB each. Note: the Zenodo record predates final JAMES publication and doesn't print the 10.1029 DOI, but authors/title/content match — this is the dataset for that paper.
- **I-01 Mehta et al. 2024** (Nature Water): Global Area Equipped for Irrigation 1900–2015, built on FAO GMIA. Open — Zenodo 14219723. A **projected AEI 2020–2100 under SSPs** also exists (Zenodo 14177960) — off-the-shelf future irrigation option.

## High temperature (T-01, T-02)

### GEHE — Global Extreme Heat Estimates (Tuholske et al. 2023) — T-01

- NASA SEDAC: <https://www.earthdata.nasa.gov/data/catalog/sedac-ciesin-sedac-sdei-gehe-1.00> ; DOI 10.7927/hff0-k565.
- Verified via search 2026-07-02: annual counts of days with WBGTmax above ISO occupational thresholds (>28/30/32 °C), + annual rate of change. 0.05° (~5 km), 1983–2016, global. WBGT built on the CHC CHIRTS temperature record. Open (NASA SEDAC, Earthdata). Modern + open → Keep. Caveats: ends 2016 (no update-to-present), observational (no future) — pair with CMIP6 future heat (NEX-GDDP v2) for the future slot.
- **Licence confirmed 2026-07-03** via NASA CMR UseConstraints (SEDAC server was refusing connections; CMR is authoritative): quoted verbatim — "This work is licensed under the Creative Commons Attribution 4.0 International License … Users are free to use, copy, distribute, transmit, and adapt the work for commercial and non-commercial purposes, without restriction, as long as clear attribution of the source is provided." → **CC-BY 4.0** (was marked "verify").

### NASA NEX-GDDP-CMIP6 v2 (internal CDH track) — modernization for T-02

- Bias-corrected statistically-downscaled (BCSD) CMIP6 daily data, 0.25°, multi-GCM, SSP scenarios, 1950–2100. Internal CDH projections track. Route to derive a growing-season Tmax-flip (needs a growing-season mask, e.g. from the LGP/GAEZ work). FAO GAEZ v5 thermal-regime indicators (CMIP6, ready, ~9 km) = alternative.

## Flooding (F-01, F-02, F-03)

### Global Flood Database (Tellman et al. 2021, Nature) — modern successor to Dartmouth (F-01)

- Nature paper + Cloud to Street; GEE `GLOBAL_FLOOD_DB/MODIS_EVENTS/V1`; HydroShare; GitHub cloudtostreet/MODIS_GlobalFloodDatabase.
- Verified 2026-07-02; adversarial re-check 2026-07-03: satellite-**observed** flood extents, **913 events / 169 countries, 2000–2018**, MODIS-based (~250 m). Available via **Google Earth Engine + Cloud to Street**; reportedly built on the Dartmouth Flood Observatory catalogue and mirrored on HydroShare (not verified verbatim — Nature methods paywalled). **Licence: CC BY-NC 4.0 (GEE) / CC BY-NC-ND (HydroShare) — NON-COMMERCIAL** (verified 2026-07-03); a constraint for open Hub redistribution. Observed/historic — modern analogue for the F-01 Dartmouth proxy.

### Google Flood Hub — "Inundation History" (F-01 secondary option)

- Resources: <https://sites.research.google/gr/floodforecasting/resources/> · dataset README: <https://storage.googleapis.com/flood-forecasting/inundation_history/README.txt> · GLAD source: <https://glad.umd.edu/dataset/global-surface-water-dynamics>
- Verified 2026-07-03 (README + GLAD page): per-pixel **frequency** of inundation, **1999–2020, 128 m**, Google Cloud Storage, **CC-BY 4.0**. README (quoted): "based on the GLAD dataset"; "how often each 128-meter pixel … has been wet between 1999 and 2020, derived from satellite imagery"; "raw GLAD data was processed to remove noise and smooth the results." So it is a **repackaging of the GLAD Global Surface Water Dynamics dataset** (Pickens et al. 2020, *RSE* 243:111792, Univ. Maryland) — **Landsat 5/7/8** optical, 30 m native, resampled/smoothed to 128 m. Legend thresholds (README): **High = wet ≥5%**, **Medium = ≥1%**, **Low = ≥0.5%** of the period. Coverage band excludes the far north/south. **This is a surface-water-occurrence product (peer of JRC Global Surface Water), NOT a flood-event catalogue** — complements the Global Flood Database, does not replace it. Distinct from Flood Hub's **operational** inundation nowcast (Sentinel-1 SAR + Sentinel-2; support.google.com/flood-hub/answer/15636595). Flood Hub also = operational riverine forecast (>100 countries, ≤7-day; no climate projection).

### WRI Aqueduct Floods (Ward et al. 2020) — current F-02/F-03

- Methodology <https://www.wri.org/research/aqueduct-floods-methodology> · data <https://www.wri.org/data/aqueduct-floods> · GEE V2.
- Verified via search 2026-07-02: riverine + coastal flood hazard, 1-in-X return periods, baseline (1980) + future **2030/2050/2080**; scenarios **RCP4.5 & RCP8.5 (IPCC AR5 / CMIP5-era)**; ISI-MIP multi-model forcing; Deltares/VU-Amsterdam/Utrecht/PBL. Open (WRI, GEE). CMIP5-era → modernization candidate under the CMIP5-obsolete policy.

### GIRI global flood hazard model (CIMA / UNEP-GRID, for UNDRR/CDRI) — CMIP6 modernization for F-02 (riverine only)

- Background paper <https://giri.unepgrid.ch/sites/default/files/2023-09/CIMA_GIRI_Flood_BGpaper.pdf> · CDRI.
- Verified + adversarially re-checked (CIMA background paper) 2026-07-03: fully probabilistic global flood hazard, **riverine (fluvial) ONLY** — the CIMA model covers rivers, NOT coastal (the GIRI *platform* hosts coastal layers from other sources); **90 m**; CMIP6 scenarios **SSP1-2.6 (SSP126) and SSP5-8.5 (SSP585)** using **IPSL-CM6A-LR** (single GCM, ISIMIP3b). Access: free but **download via registration form** (organisation + purpose; non-commercial + attribution) — not unconditional open. Use for F-02 (river) only; F-03 (coastal) has no ready CMIP6 model. Limitation = single-GCM ensemble (vs Aqueduct Floods' multi-model but CMIP5).

### F-03 coastal — CMIP6 driver search (2026-07-03)

- **No ready open CMIP6/SSP coastal *inundation* (flood-extent) product exists.** Verified candidates:
  - **Copernicus CDS `sis-water-level-change-indicators-cmip6`** (Muis et al. 2023, "Global sea level change indicators … high resolution CMIP6"; <https://cds.climate.copernicus.eu/datasets/sis-water-level-change-indicators-cmip6>, DOI 10.24381/cds.6edf04e0): CMIP6 HighResMIP GCMs + ERA5, **future = SSP5-8.5**, epochs 1951–1980 / 1985–2014 / 2021–2050, global, **CC-BY**, coastal grid 0.1° (GTSMv3.0 ~2.5 km coastal). **BUT it is a water-level *indicator* product** (tides, surge, total water levels, return periods at coastal points) — **NOT flood inundation extent/depth.** = the open CMIP6 **driver** to build a coastal-hazard layer, not a finished hazard layer.
  - **Kirezci et al. 2020** (Sci Rep, <https://www.nature.com/articles/s41598-020-67736-6>): produces inundation area but **CMIP5/RCP4.5 & 8.5** (2050/2100), 1 km, not openly packaged as a licensed downloadable layer.
  - **WRI Aqueduct Floods coastal** — confirmed still **CMIP5/RCP** (not upgraded to CMIP6). **DIVA** = coastal-segment impact model, not a raster hazard layer. **GIRI** = riverine-only. Copernicus **GloFAS/EMS** = riverine operational, explicitly not coastal.
- Verdict: keep Aqueduct Floods coastal (CMIP5) short-term; modernized coastal = a **Phase-2 build** on the Copernicus CDS CMIP6 SSP5-8.5 sea-level indicators. *(Wiley/Nature/WRI full-text PDFs paywalled; findings rest on the Copernicus CDS dataset page + user guide, PMC Kirezci full text, and WRI/GIRI/Deltares official pages — CMIP5-vs-CMIP6 basis directly quoted.)*

## D-02 — Failed season (cropping reliability)

### WRSI — Water Requirement Satisfaction Index (FAO / USGS FEWS NET / CHC GeoWRSI)

- Pages: USGS FEWS <https://earlywarning.usgs.gov/fews/product/899/> · CHC GeoWRSI <https://www.chc.ucsb.edu/tools/geowrsi> · IDMP <https://www.droughtmanagement.info/water-requirement-satisfaction-index-wrsi-and-geo-wrsi/>
- Verified 2026-07-02 (page fetch): WRSI = ratio of seasonal actual crop ET to crop water requirement (AETc/PETc); **WRSI < 50 = crop failure** — a direct operational analogue of "failed season." FAO-developed, USGS-adapted for FEWS NET (GeoWRSI tool). Gridded historical availability:
  - **L-WRSI (Landscape WRSI):** global, GeoTIFF, dekadal, **1982–present**, open (USGS, CC0); 40-yr median 1982–2021. Landscape-level (whole landscape, not crop-specific).
  - **Crop WRSI (CHIRPS-Croplands, USGS/FEWS):** gridded, **crop-specific** (maize, sorghum, millet, wheat…), **0.1° (~10 km)**, dekadal, **2001–present**, driven by **CHIRPS v3 (0.05°) + Global Daily Reference ETos (0.125°)** — but **regional only** (E/S/W Africa, Central America, Caribbean/Hispaniola). ZIP raster archives, direct download.
  - **Global crop-specific WRSI** = run **GeoWRSI** on CHIRPS (a derivation, same stack as the D-01 SPEI recommendation), not a ready global download.

### FAO GAEZ v5 — agro-climatic resources incl. LGP (CMIP6) — for R-01/R-02

- What's new in GAEZ v5: <https://www.fao.org/statistics/highlights-archive/highlights-detail/what-s-new-in-gaez-v5/en> · portal <https://www.fao.org/gaez/en>
- Verified via search 2026-07-02: GAEZ v5 (FAO/IIASA, released 2025), 2020 baseline. Future climate = CMIP6 IPCC AR6 forcing under **three SSPs**; four periods 2021–2040, 2041–2060, 2061–2080, 2081–2100. 180+ variables incl. agro-climatic **length of growing period (LGP)** — the exact R-01/R-02 construct.
- **Download verified 2026-07-03** (FAO catalog <https://data.apps.fao.org/catalog/dataset/agro-climatic-resources-gaez-v-5>): the moisture-and-temperature-constrained LGP is published under the **Growing Period** sub-theme as **"Total number of growing period days"** (20-yr-average product carries the future projections; id 43045b86-fedc-4682-9edf-09aac3949278) — *not literally labelled "LGP".* GeoTIFF (Int16), **~10 km** (0.08333°), EPSG:4326, global; **CC-BY 4.0**; also WMTS + Google Cloud Storage access; historical 1981–2000 & 2001–2020 + 3 SSPs × 4 future periods. Thermal **LGPt** (Ta>5/10/20/30 °C) are separate layers. Model docs: <https://github.com/un-fao/gaezv5/wiki>. **Caveat:** the exact SSP scenario codes (SSP1-2.6 / 3-7.0 / 5-8.5?) were **not verifiable** in the reachable metadata — confirm via the layer's dimension-filter JSON before citing specific scenarios. Threshold-flip derived by comparing baseline vs future against 120/90 days. (GAEZ v4 was CMIP5-era; v5 is the CMIP6 version.)

### FAO GAEZ v4 — agro-climatic resources (LGP / cropping reliability)

- Portal: <https://gaez.fao.org/> · catalog <https://data.apps.fao.org/catalog/dataset/agro-climatic-resources-gaezv4>
- Verified via search 2026-07-02: water-balance length-of-growing-period, dry/rain days, ET deficit, multi-cropping/reliability indicators. 5 arc-min (~9 km); historical 1961–2010 (time series + 30-yr averages) and future periods 2011–2040 / 2041–2070 / 2070–2099. Open via GAEZ portal. Coarser and more LGP-oriented; also relevant to the changed-rainfall LGP rows.

## Bert / Philip Thornton emails (primary; supersede the CRI doc on actual data)

From the B4T notebook PDF (Bert's emails 2026-04-29/30, relaying Philip Thornton personal communication) — higher authority than the published doc for what is *actually* used:

- **Drought:** WASP (Weighted Anomaly of Standardized Precipitation, IRI), 2.5°×2.5°, monthly precip 1980–2000; drought event = monthly deficit ≤50% of long-term median for 3+ consecutive months; masked where 3-mo running mean <1 mm/day; high-risk = top two deciles of Dilley (2005).
- **Flood (past):** Dilley (2005) top two deciles + Dartmouth Flood Observatory events 1985–2003.
- **Changed rainfall (CV):** CV of annual rainfall > global 75th pct (28%); current variability used as proxy for future.
- **Future hazards (2050s):** downscaled projections from **17 CMIP5 GCMs under RCP8.5**, Jones & Thornton (2009/2013/2015). LGP-flip (>120→<120; reliable-growing-days >90→<90, Nachtergaele 2002) and Tmax-flip (<30→>30 °C, growing season, LGP>40 mask; 30 °C critical per Boote 1998, Prasad 2008). Bert unsure of exact provenance; notebook annotation flags Ericksen 2011 data as "pre-CMIP5 (some seem CMIP3)" → conflicted.
- **Aqueduct:** Bert — "seems CMIP5 is being used in the CRI, but Aqueduct v4.0 is available using CMIP6"; different future timeframes across hazards (2030 vs 2050). → verify version.
- **HII:** AI (ChatGPT-5/Copilot-5/Gemini) used only to rough-cut which conditions to include + first score, then literature + expert correction, run across tools/versions for consistency; fallback where no literature/expert input. Pete flagged heavy AI hallucination in the analogous AAA Atlas matrix work.
- **CCC:** gridded crop-specific hazard frequency (baseline + projected) from Ecocrop temperature/water requirements + a soil water-balance model (waterlogging/water stress); covers MapSPAM crops (not all of Appendix Table 2); no changed-rainfall/LGP or salinity; perennial-crop issues.
- **Todd's ask:** show old-vs-new projection comparison and whether the data-source change is meaningful for breeding; Pete to rebuild the pipeline in code. Use-case coordination: Bia.

## Primary B4T sources (OneDrive, not in repo)

- `Crop Risk Index-documentation v1.pdf` (Lenaerts & Badayos, 2025-12-15) — CRI method, Appendix Table 1 (23 datasets), Appendix Table 2 (50 crops), Appendix Text 1 (HII prompt), Appendix Table 3 (HII literature).
- `ccafsreport5-climate_hotspots_final.pdf` (Ericksen et al. 2011, CCAFS Report No. 5) — source of the legacy drought (Map 2.13, 1974–2004), Dartmouth flood, LGP-flip and CV-rainfall layers. Future layers: 4 CMIP3 GCMs, A2 SRES, futureclim.info (Jones et al. 2009).
- `HII-scoring matrix.pdf` — HII matrix (for Phase-2 methods review).
- `Crop x region priority- 2025.xlsx` — B4T prioritization workbook.

## B4T feedback incorporated — Bert Lenaerts, 2026-07-13 (review page v1.1)

Answers to the review's open questions, posted in the giscus threads and folded into the review page as inline "Answered" notes. New / confirmed facts:

- **Failed season (D-02):** source is **CIAT RTBMaps** (`gisweb.ciat.cgiar.org/RTBMaps`), still in production; uses a different LGP definition from Philip's layer. Ref: **Hyman, G. et al. 2008**, *Agricultural Systems* 98:50–61.
- **Aqueduct Flood (F-02/03; and the D-03/04/05 water thread):** the flood layer used is **CMIP5-era, not Aqueduct 4.0** (which is CMIP6). Product = **Aqueduct Floods Hazard Maps — inundation depth (m), coastal + riverine, Version 2 (20 Oct 2020)**; **10-year** return period. Confirms the vintage flag; cross-hazard future-horizon harmonisation still open.
- **LGP (T-02 / R-01):** Philip's LGP = mean days/yr with Tavg > 6 °C AND actual/potential evapotranspiration > 0.35. Non-production-corrected hazards masked by the share of land under crop production. **The LGP definition was accidentally pasted into T-03 and R-01** (a documentation slip — not the same layer). Rainfall uses two LGP lengths; temperature has LGP-corrected + uncorrected versions (both used). Coarser GAEZ (~9 km) acceptable.
- **Rainfall CV (R-03):** combine historic + projected; weighting open (currently 50–50).
- **Heat growing season (T-03):** 30 °C critical threshold — Philip citing **Boote et al. 1998; Prasad et al. 2008** (already noted under Future hazards above).
- **Salinity / soil water (S, W):** S-01 + S-02 kept to avoid single-source reliance (not both strictly needed); source data categorical (levels only), so quantifying it adds noise. All four soil-water layers used; a future / projected layer preferred.
- **Drought (D-01):** the CRI already has a hazard-interaction component → merging drought + temperature risks double-counting; near-global coverage required for B4T; current layer 1980–2000; the Philip-notes vs Ericksen-2011 discrepancy is a B4T-side omission.
- **Flood proxy (F-01):** historic + projected combined (Bert flagged the question as unclear — rephrase next round).
- **Still open:** T-01 heat window (1983–2016) — not yet answered.
