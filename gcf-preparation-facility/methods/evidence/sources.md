<!-- URL-dense evidence table; bare URLs in cells are intentional and more readable than wrapped autolinks -->
<!-- markdownlint-disable MD034 -->
# Evidence log — GCF Preparation Facility

One entry per external dataset referenced in the use-case review page
([`public/gcf-preparation-facility/gcf-prep-review.html`](../../../public/gcf-preparation-facility/gcf-prep-review.html)).
Every claim about a dataset (URL, what it is, licence) traces to an entry here.

**Method.** Each URL was fetched live on **2026-07-07** (WebFetch, with `curl` + browser
headers as fallback) and re-checked adversarially (tried to refute the URL choice: older/alternate
domains, version churn, redirects). Licences are quoted from the provider's own terms where
readable. Rows marked *bot-blocked* returned HTTP 403 to automated fetches (Cloudflare / WAF) —
the pages are genuine and canonical (confirmed via search index + terms URLs) but could not be
content-verified programmatically; **re-check in a browser before external circulation.**

> **Licence matters for CDH hosting.** The Hub can only *mirror-host* openly-licensed data.
> Non-commercial / no-redistribute datasets (flagged **⚠ NC** below) must be **federated or
> linked**, never copied into the catalogue as raw data. **But** — for our strictly
> non-commercial research use — nearly all of them permit **computing and publishing derived
> admin1/admin2 products** (the whole notebook model). The constraint is on redistributing the
> *source* data, not on derived statistics. See the [derived-products guidance](#derived-products-non-commercial-use)
> and the [licence-constraint summary](#licence-constraint-summary).

---

## Section 1–2 — Climate trends, projections & extreme events

| Dataset | Official URL | Licence | Verified | Notes |
| --- | --- | --- | --- | --- |
| NEX-GDDP-CMIP6 | https://www.nccs.nasa.gov/services/data-collections/land-based-products/nex-gddp-cmip6 | **CC0** (blanket, since Sep 2022; pre-Sep-2022 files were CC-BY-SA 4.0) | ✅ live | Licence stated on the AWS Open Data registry entry, not the NCCS landing page. Versions 1.0/1.1/1.2 coexist — cite the version used. |
| ERA5 | https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels | **CC-BY** (Copernicus attribution licence) | ✅ live | Single-levels record (DOI 10.24381/cds.adbb2d47). Pressure-levels / ERA5-Land are separate CDS records — pick the one matching variables used. |
| AgERA5 | https://cds.climate.copernicus.eu/datasets/sis-agrometeorological-indicators | **CC-BY** (Copernicus) | ✅ live | Daily agrometeorological indicators derived from ERA5. |
| CHIRPS | https://www.chc.ucsb.edu/data/chirps | **Public domain** (CC0 waiver) | ✅ live | UCSB Climate Hazards Center. Quasi-global 50°S–50°N precipitation, 1981–near-present. |
| CHIRTS | https://www.chc.ucsb.edu/data/chirtsdaily | **Public domain** (CC0 waiver) | ✅ live | Verified page is CHIRTS-**daily** (0.05°, Tmax/Tmin); monthly CHIRTSmax is a separate CHC page — name which product. |
| Atlas `haz_freq.parquet` (per-GCM hazard frequency) | `s3://digital-atlas/domain=climate/type=hazard-indices/source=nex-gddp-cmip6/region=africa/processing=hazard-change/timeframe=annual/variable=haz_freq.parquet` (public, anonymous read) | derived from NEX-GDDP-CMIP6 (CC0); Atlas product, licence to be stated in its CDH record | ✅ 2026-10-07 (`aws s3 ls --no-sign-request` + DuckDB) | 12,467,664 rows · 4,292 adm2 · 18 GCMs · historic 1995-2014 + 4 SSPs × 4 periods · NDWS/NDWL0 × severe/extreme · `frequency` (0–1) and `frequency_n`. Read with `hive_partitioning=false`. Extension request: `../ingestion-notes.md` §2. |

## Section 3 — Crop & livestock hazard exposure

| Dataset | Official URL | Licence | Verified | Notes |
| --- | --- | --- | --- | --- |
| MapSPAM 2020 | https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/SWPENT | **CC BY 4.0** (confirmed via Dataverse API) | ✅ via API | Project home `mapspam.info` returned 403 to automated fetch — Dataverse DOI is the canonical data record. Cite "2020 v2.0 r2". |
| FAOSTAT | https://www.fao.org/faostat/en/ | **CC BY 4.0** | ✅ live | Licence on FAO Statistical Database Terms of Use, not the FAOSTAT app page. Prescribed citation format; third-party series may carry other terms. |
| FAO GLEAM | https://www.fao.org/gleam/en/ | **CC BY 4.0** for data served through the GLEAM 3 dashboard (its Terms of Use, read 2026-10-07) — supersedes the earlier conflict note (FAO data catalog indexed GLEAM under CC-BY-NC-SA-3.0-IGO) | ✅ live | Dashboard: https://foodandagricultureorganization.shinyapps.io/GLEAMV3_Public/. R package `un-fao/GLEAM` is AGPL-3. See the Rescreen 2026-10-07 table. |
| WRI Aqueduct 4.0 | https://www.wri.org/data/aqueduct-global-maps-40-data | **CC BY 4.0** (per Aqueduct FAQ) | ✅ live | Data page says only "Creative Commons"; FAQ confirms CC BY 4.0. Distinct from the Water Risk Atlas *tool* page (no licence stated). Methodology on GitHub `wri/Aqueduct40`. |

## Section 4 — Vulnerability & socioeconomic context

| Dataset | Official URL | Licence | Verified | Notes |
| --- | --- | --- | --- | --- |
| World Bank WDI | https://datatopics.worldbank.org/world-development-indicators/ | **CC BY 4.0** | ✅ live | Query interface at `databank.worldbank.org`. |
| ND-GAIN Country Index | https://gain.nd.edu/our-work/country-index/ | **⚠ Unclear** — "free and open-access" + suggested citation, © Univ. of Notre Dame; no CC licence | ✅ live | Old host `gain-new.crc.nd.edu` circulates in citations — not canonical. |
| INFORM Risk Index | https://drmkc.jrc.ec.europa.eu/inform-index | **CC BY 4.0** (EC reuse policy, Decision 2011/833/EU) — not printed on INFORM site | ✅ live (page) | `data.europa.eu` record lists CC-BY-4.0. Flag: licence inferred from EC-wide policy, not stated in situ. |
| IPC / Cadre Harmonisé | https://www.ipcinfo.org/ (CH: https://www.ipcinfo.org/cadre-harmonise) | **⚠ NC** — CC BY-NC-SA 3.0 IGO (IPC-CH API terms) | ⚠ bot-blocked | Domain live but Cloudflare 403 to fetches. Licence from API-terms search snippets. HDX/FEWS NET copies are mirrors. |
| WHO/UNICEF JMP (WASH) | https://washdata.org/ | **⚠ NC** on reports (CC BY-NC-SA 3.0 IGO); data licence not stated on site | ✅ live (page) | Report PDFs carry the NC-SA licence; data pages show none. `who.int` / `data.unicef.org` are republications. |
| WorldPop | https://www.worldpop.org/ | **CC BY 4.0** | ✅ live | Downloads at `hub.worldpop.org` (same producer). |
| DHS Program | https://dhsprogram.com/ | **⚠ NC / restricted** — registered use only; "datasets will not be shared with other researchers without written consent"; treat as confidential | ✅ via curl | WebFetch 403; verified via curl+browser UA. Per-project approval required. |
| UNICEF MICS | https://mics.unicef.org/ | **⚠ NC / restricted** — registration required; "requested not to redistribute datasets" | ⚠ bot-blocked | Cloudflare 403. IPUMS MICS / WB Microdata are third-party redistributions. |
| UNDP HDI | https://hdr.undp.org/data-center/human-development-index | **CC BY 3.0 IGO** (note: 3.0, not 4.0) | ✅ live | Attribution required; commercial use allowed. |
| ACLED | https://acleddata.com/ | **⚠ NC / no-redistribute** — proprietary EULA; commercial entities need a corporate licence; outputs must be "transformative … cannot be reverse engineered to recreate the Licensed Content" | ✅ live | **Not open data.** Can cite/aggregate transformatively; cannot republish. Mandatory attribution incl. AI/LLM uses. |

## Section 5 — NDC & NAP alignment (deprioritised)

| Dataset | Official URL | Licence | Verified | Notes |
| --- | --- | --- | --- | --- |
| UNFCCC NDC Registry | https://unfccc.int/NDCREG | UNFCCC Terms of Use — free download, content unchanged, source acknowledged; no open licence | ✅ live | 343 submissions. |
| NAP Central | https://napcentral.org | © UNFCCC; UNFCCC Terms of Use presumed | ✅ live | Old `www4.unfccc.int/sites/NAPC` retired → maintenance page. `napcentral.org` is canonical. |
| Climate Watch | https://www.climatewatchdata.org | **CC BY 4.0** for Climate-Watch-produced data; third-party datasets keep original licences | ✅ live | JS SPA; `/about/permissions` confirmed via indexed copy. |
| GCF country programmes | https://www.greenclimate.fund/resources/operational-documents?type%5B0%5D=country%20programme | GCF Terms — non-commercial/study copying, attribution "First published by the Green Climate Fund" | ✅ live | No standalone "country programmes" page post-redesign; this is the filtered operational-documents view. |

## Section 6 — Impact potential & beneficiary estimates

| Dataset | Official URL | Licence | Verified | Notes |
| --- | --- | --- | --- | --- |
| IPCC Emission Factor Database (EFDB) | https://www.ipcc-nggip.iges.or.jp/EFDB/main.php | **⚠ Unclear / effectively NC** — no explicit data licence; IPCC copyright default ("personal, non-commercial use … no right to resell or redistribute") | ✅ live | `iges.or.jp` host is legitimate (IPCC TFI TSU at IGES Japan). A "more user-friendly EF database" planned early 2026 — recheck for migration. |
| FAO EX-ACT | https://www.fao.org/in-action/epic/ex-act-tool/en/ | **⚠ Unclear** — no tool-specific licence; FAO general terms (typically CC BY-NC-SA 3.0 IGO); register/login required | ✅ live | Renamed "Environmental eXternalities ACcounting Tool" (acronym retained). App at `exact.apps.fao.org`. Excel versions being phased out. |
| Atlas yield gaps / GYGA | https://www.globalyieldgap.org/ | **⚠ NC** — CC BY-NC-SA 4.0; company downloads count as commercial (paid licence) | ✅ live | **2026 fork:** `yieldgap.org` now 301s to `yieldgap.com` (YPYGA, a *different* Nebraska+Wageningen successor, launched Mar 2026). For "GYGA" cite `globalyieldgap.org`; contact gyga.support@wur.nl. |
| WOCAT SLM database | https://wocat.net/en/database/ | **⚠ NC** — CC BY-NC-SA 4.0; notify wocat.cde@unibe.ch on reuse | ✅ live | Moved from `qcat.wocat.net` (301). ~2,449 practices. UNCCD's recommended SLM database. |
| National census | — | per-country | — | Per-country acquisition; no single URL. Feasibility 4. |

## Section 7 — Theory of change & GCF portfolio evidence

| Dataset | Official URL | Licence | Verified | Notes |
| --- | --- | --- | --- | --- |
| GCF project/programme database | https://www.greenclimate.fund/projects | GCF Terms — attribution, no commercial derivatives without consent | ✅ live | "Portfolio Explorer"; machine-readable data at `data.greenclimate.fund` (Open Data Library). 360 approved projects, USD 20.5 bn. |
| GEF projects database | https://www.thegef.org/projects-operations/database | © GEF, All Rights Reserved; `/legal` defers to World Bank Group T&C; no open licence | ✅ live | 6,700+ projects (1991–2026). |
| Adaptation Fund projects database | https://www.adaptation-fund.org/projects-programmes/ | © Adaptation Fund, All Rights Reserved; no open licence | ✅ live | Table view at `/projects-programmes/project-information/projects-table-view/`. |
| Climate Project Explorer | https://climateprojectexplorer.org | **⚠ Unclear** — © Climate Project Explorer; JS `/terms-of-use` not extractable | ✅ live | Joint portal of the 4 multilateral funds (AF, CIF, GCF, GEF), powered by Climate Policy Radar. **Launched at COP29 (Nov 2024)** — note: some internal notes say "December", the public launch was COP29. |
| UNFCCC data portal | https://data.unfccc.int | UNFCCC Terms of Use | ✅ live | Rebranded "UNFCCC Climate Data Hub" (was GHG Data Interface). |
| CGIAR evidence maps | — | per-source | — | No single canonical URL; scope with the team. |
| World Bank IEG evaluations | https://ieg.worldbankgroup.org/evaluations | not verified (bot-blocked) | ⚠ 403 | `worldbank.org/ieg` points here; search index shows live pages. Recheck in browser. |
| IFAD independent evaluations (IOE) | https://ioe.ifad.org/en/ | not verified (bot-blocked) | ⚠ 403 | `ifad.org/en/web/ioe/home` 301s here. Reports at `/en/latest-reports`. Recheck in browser. |
| Cesare's MCF project dataset | *(internal — OneDrive)* | TBD (DOI via CGSpace/Dataverse planned) | n/a | Partial CSV delivered 2026-06-17; food/land/water public subset. See the Notebook tab. |

## Section 8 — Safeguards & gender screening

| Dataset | Official URL | Licence | Verified | Notes |
| --- | --- | --- | --- | --- |
| WDPA / Protected Planet | https://www.protectedplanet.net/en | **⚠ NC / no-redistribute** — no Commercial Use or redistribution without UNEP-WCMC written permission; download = accept T&C | ✅ live | Rebranded Nov 2025 to WDPCA (WDPA + WD-OECM merged); same domain. "Commercial Use" defined broadly. Commercial access via IBAT. |
| IUCN Red List | https://www.iucnredlist.org/ (terms: /terms/terms-of-use) | **⚠ NC / no-redistribute** — no Commercial Use without IUCN permission; non-transferable licence for conservation/education/research; versioned citation required | ⚠ bot-blocked | Cloudflare 403 to automated fetch; URL unambiguously canonical (cross-checked GBIF/IBAT/IUCN). Loads fine in a browser. |
| FAO Gender & Land Rights Database | **⚠ DEFUNCT — no verified URL** | n/a | ❌ 404 | `/gender-landrights-database/` 301s to `/en/` which **404s**; bare URL is a soft-404 (serves the FAO homepage). Wayback last 200 = 2023-07-16. Google still indexes stale titles — do not trust snippets. Nearest live official reference: FAO SDG Indicators Data Portal, indicator 5.a.2 (`https://www.fao.org/sustainable-development-goals-data-portal/data/indicators/5a2-women-s-equal-rights-to-land-ownership/en`). Leave unlinked on the page. |
| OECD SIGI | https://www.oecd.org/en/about/programmes/social-institutions-and-gender-index-sigi.html | **CC BY 4.0** for OECD content published from 1 Jul 2024 (Open Access Policy); pre-2024 free reuse w/ citation | ⚠ bot-blocked | OECD Akamai 403 to automated fetch; live data confirmed at `data-explorer.oecd.org` (DSD_SIGI@DF_SIGI_2023). Former domain `genderindex.org` is dead (DNS) — do not cite. |
| World Bank CPIA | https://databank.worldbank.org/source/country-policy-and-institutional-assessment | **CC BY 4.0** ("Public"; per Data Catalog #0038988) | ✅ live | Canonical full-dataset portal is DataBank (86 countries, 21 series). Note `worldbank.org/en/data/datatopics/cpia` is the **regional "CPIA Africa"** report hub, not the global dataset. |
| Climate Security Programming Dashboard (CSO) | — | per-source | — | CGIAR Climate Security Observatory product; scope the exact URL with the team. |

## Section 9 — Financial context & justification

| Dataset | Official URL | Licence | Verified | Notes |
| --- | --- | --- | --- | --- |
| OECD DAC CRS | https://www.oecd.org/en/publications/creditor-reporting-system_22180907.html | OECD terms (free reuse w/ attribution); not stated inline | ⚠ bot-blocked | OECD WAF 403. Interactive at `data-explorer.oecd.org` (DSD_CRS). Legacy `stats.oecd.org` CRS1 retiring. |
| CPI Global Landscape of Climate Finance | https://www.climatepolicyinitiative.org/publication/global-landscape-of-climate-finance-2025/ | **CC BY-NC-SA** (report front-matter: 4.0 recent / 3.0 older) — non-commercial; commercial use by contacting CPI | ⚠ PDF-indexed | **Corrected:** the website landing page shows only "© All rights reserved", but the report PDF inside-cover grants CC BY-NC-SA for non-commercial use — cite the PDF front-matter as the operative grant. ShareAlike applies to derivatives. Confirm in a browser (website-vs-PDF discrepancy). |
| IMF fiscal data (Fiscal Monitor / GFS) | https://www.imf.org/en/publications/fm | IMF Copyright & Usage terms (reuse w/ attribution; some redistribution limits); not stated inline | ⚠ bot-blocked | IMF WAF 403. Structured data at `data.imf.org` (IMF.FAD:FM; GFS separate). |

## Cross-cutting reference — GCF / Togo

| Source | URL / location | Notes |
| --- | --- | --- |
| GCF/B.33/05 — "Steps to enhance the climate rationale of GCF-supported activities" | GCF Board document, 24 June 2022 | Defines climate rationale + the four adaptation principles (Identification, Response, Alignment, M&E) + the evidence-confidence matrix. Local copy in OneDrive background materials. |
| GCF Concept Note template v3.1 | greenclimate.fund (Partner Portal digital template prevails from 1 Apr 2025) | Section codes (A.1–A.17, C.1–C.5, D.1–D.4) that the memo's nine sections map onto. |
| Togo SAT rapid climate risk assessment | GCA + Alliance Bioversity-CIAT, April 2025 | Gold-standard reference. Table 5 = the hazard-exposure matrix target output. Hazard layers sourced from the African Adaptation Atlas (adaptationatlas.cgiar.org). Local copy in OneDrive. |
| African Adaptation Atlas | https://adaptationatlas.cgiar.org | The hazard-exposure source cited in Togo Table 5; CGIAR's own product. |

---

## Derived products (non-commercial use)

Our use is **strictly non-commercial research**. Two rights are separate: (1) mirror-hosting the
**raw source data**, and (2) computing + publishing **derived admin1/admin2 products** (zonal stats,
exposure tables, maps). The notebook is almost entirely (2). Verified against each licence's
derivative/redistribution clause on 2026-07-07.

**Bottom line: every restricted dataset here permits non-commercial derived admin products AND
their publication. None forbids it outright.** The recurring bar is on re-serving the *source*
data, not on derived outputs.

| Dataset | Derive admin1/2 (NC)? | Publish the derived product? | Binding condition |
| --- | --- | --- | --- |
| ACLED | ✅ | ✅ **only if transformative** | Output "must be transformative, such that they cannot be reverse engineered to recreate the Licensed Content" — coarse admin aggregates pass; a reorganized dump fails. Attribution per ACLED policy (incl. AI/LLM). |
| WDPA / Protected Planet | ✅ | ✅ | May publish "in whole or in part, including on-line, providing (a) the … Data are not downloadable and (b) proper attribution is clearly visible." So: publish stats/maps; **do not make the raw layer downloadable**. UNEP-WCMC + IUCN citation + release month/yr. NC only. |
| IUCN Red List | ✅ (grant covers "scientific analyses and research") | ✅ | **Do not redistribute Red List data, even within derived works.** Send IUCN a copy of any publication (electronic / 2 paper). Versioned citation. NC only. |
| IPC / Cadre Harmonisé | ✅ | ✅ | CC BY-NC-SA — derived product must carry **CC BY-NC-SA**. Attribution. |
| WHO/UNICEF JMP | ✅ | ✅ | CC BY-NC-SA 3.0 IGO — **ShareAlike** on derivatives. |
| GYGA | ✅ | ✅ | CC BY-NC-SA 4.0 — **ShareAlike**; companies pay. |
| WOCAT | ✅ | ✅ | CC BY-NC-SA 4.0 — **ShareAlike**; notify wocat.cde@unibe.ch on reuse. |
| CPI Global Landscape | ✅ | ✅ | CC BY-NC-SA (report front-matter) — **ShareAlike**; cite the PDF grant, not the website footer. |
| DHS | ✅ (for the registered study) | ✅ (derived indicators) | **Microdata must not be passed to other researchers without DHS written consent**; no re-identification. Prefer the **DHS API / STATcompiler** aggregate indicators — freely open, no login — over deriving from restricted microdata. Submit publications to DHS. |
| UNICEF MICS | ✅ | ✅ (aggregate indicators) | "Requested not to redistribute datasets"; a data subset may be posted only to meet a journal's data-availability rule. Cite UNICEF MICS. |

**Two design constraints that follow:**

1. **ShareAlike cascade.** IPC, JMP, GYGA, WOCAT and CPI are all CC BY-NC-SA. Any published
   derivative of them must itself be CC BY-NC-SA — and if you **combine** a ShareAlike source with
   an all-rights-reserved or incompatible source in one downloadable product, that combined output
   has a licence conflict. Keep ShareAlike-derived layers separable, or licence the combined export
   CC BY-NC-SA.
2. **"Publish stats, not the raw layer."** For WDPA, IUCN, DHS, MICS the raw source stays with the
   provider — the notebook exposes derived numbers/maps and links back, it does not offer the
   underlying dataset for download.

**⚠ Verify in a browser before external circulation** (these clauses were confirmed via bot-blocked
pages / PDF-indexed text, not a live automated fetch): DHS terms, MICS FAQ, IUCN main terms page,
CPI report front-matter (website footer disagrees with the PDF grant).

---

## Licence-constraint summary

**Openly licensed — CDH may mirror-host the raw data (with attribution):**
NEX-GDDP-CMIP6 (CC0), ERA5, AgERA5, CHIRPS, CHIRTS, MapSPAM 2020, FAOSTAT, WRI Aqueduct 4.0,
World Bank WDI, World Bank CPIA, WorldPop (all CC BY 4.0), UNDP HDI (CC BY 3.0 IGO), Climate Watch
(CC BY 4.0 for its own data).

**⚠ Non-commercial — raw data federate/link only, but derived NC products ARE publishable**
(see [derived-products guidance](#derived-products-non-commercial-use)):
ACLED, DHS, UNICEF MICS, WDPA/Protected Planet, IUCN Red List, IPC/Cadre Harmonisé,
WHO/UNICEF JMP, GYGA, WOCAT, CPI Global Landscape.

**⚠ Licence unclear — resolve before cataloguing:**
FAO GLEAM (CC BY vs NC-SA-IGO conflict), ND-GAIN, INFORM (EC-policy default, not stated),
IPCC EFDB, FAO EX-ACT, FAO Gender & Land Rights (defunct), OECD SIGI, OECD DAC CRS, IMF fiscal data.
GEF and Adaptation Fund project databases are "all rights reserved" (link only).

**Bot-blocked / flaky to automated checkers — re-verify in a browser before external circulation:**
IUCN Red List, IPC, UNICEF MICS, OECD SIGI, OECD DAC CRS, IMF Fiscal Monitor,
World Bank IEG, IFAD IOE, CPI (report-PDF grant), ACLED (returns HTTP 415 to
link-checkers), Climate Watch (its TLS certificate had **expired** at the
2026-07-09 check — provider-side, should renew; confirm in a browser).

---

## Rescreen 2026-10-07 — queued datasets (adversarial re-check)

Every dataset queued for ingestion on 2026-10-07 (see
[`../../data/ingestion-queue.csv`](../../data/ingestion-queue.csv) and
[`../ingestion-notes.md`](../ingestion-notes.md)) was re-tested from this machine with `curl`
(browser UA, 25 s timeout) against the live access route, and screened for a stronger open
alternative — including entries added to the CDH `climate-assets` catalogue since July. Rows new
to this log carry the licence as read on the day.

| Dataset | Access route tested | HTTP | Licence (2026-10-07) | Verdict |
| --- | --- | --- | --- | --- |
| **GMIA-NEXT** *(new)* | https://zenodo.org/records/17627111 (API) | 200 | **CC BY 4.0** (Zenodo record); 30 m, 2023/24 season, v0; 5.2 GB binary + continental probability GeoTIFFs | **Supersedes AQUASTAT GMIA v5** for irrigated extent — derive admin shares, don't mirror 30 m |
| AQUASTAT GMIA v5 | https://www.fao.org/aquastat/en/geospatial-information/global-maps-irrigated-areas/ | 200 | open (cite-as) | legacy "% equipped" only |
| FAO FishStat | https://www.fao.org/fishery/en/fishstat | 200 | CC BY-NC-SA 3.0 IGO | keep P2 |
| INFORM Risk | https://drmkc.jrc.ec.europa.eu/inform-index/INFORM-Risk/API (endpoint `…/Inform-Index/API/InformAPI/countries/Scores/?WorkflowId=…&CountryIso3Codes=TGO&IndicatorId=INFORM`) | 200 (JSON, ~2 MB all countries) | CC BY 4.0 (EC reuse policy) | keep P1; confirm filter params |
| INFORM Subnational *(new)* | https://drmkc.jrc.ec.europa.eu/inform-index/INFORM-Subnational-Risk | 200 | CC BY 4.0 | P2, regional coverage |
| **FEWS NET FDW** *(new)* | https://fdw.fews.net/api/ipcphase/?country_code=TG | 200 (JSON, no key) | open — US Government / USAID, attribution | keep P1 |
| DHS Indicator API | https://api.dhsprogram.com/rest/dhs/data?countryIds=TG&breakdown=subnational | 200 (JSON) | aggregate API open; microdata restricted | keep P1; DHS now ships an MCP server |
| **Meta RWI** *(new)* | https://data.humdata.org/api/3/action/package_search?q=relative%20wealth%20index | 200 | CC0 | keep P1 |
| **GDL SHDI** *(new)* | https://globaldatalab.org/shdi/ | 200 | non-commercial + attribution | keep P1 derive-then-host |
| IPC / Cadre Harmonisé | https://api.ipcinfo.org/ (docs path 404) | 200 / 404 | CC BY-NC-SA 3.0 IGO | keep P1; key-gated |
| ND-GAIN | https://gain.nd.edu/our-work/country-index/download-data/ | 200 | **no licence text on page** | P2; still verify |
| WHO/UNICEF JMP | https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/dataflow/UNICEF/WASH_HOUSEHOLDS/ (data query `…/rest/data/UNICEF,WASH_HOUSEHOLDS,1.0/TGO.WS_PPL_W-ALB.?format=csv`) | 200 (CSV) | CC BY-NC-SA 3.0 IGO (reports) | P2 federate SDMX |
| UNDP HDI | https://hdr.undp.org/data-center/documentation-and-downloads | 200 | CC BY 3.0 IGO | P2 |
| Climate Watch | /api/v1/ndcs/TGO/text · /ndcs/TGO/content_overview · /ndcs?filter=sectoral | 200 / 200 / 200 | CC BY 4.0 | works; `location` ignored on list endpoint |
| EDGAR | https://edgar.jrc.ec.europa.eu/dataset_ghg2024 | 200 | CC BY 4.0 | keep P1 |
| FAOSTAT emissions | bulk https://bulks-faostat.fao.org/production/Emissions_Totals_E_All_Data.zip · REST | 200 (14 MB) · 401/timeout | CC BY 4.0 | bulk for Hub copy |
| **ESA WorldCover** *(new)* | https://registry.opendata.aws/esa-worldcover-vito/ · s3://esa-worldcover/ (no-sign) | 200 · 200 | **CC BY 4.0**; STAC endpoint | derive admin product; federate 10 m |
| IPCC EFDB | https://www.ipcc-nggip.iges.or.jp/EFDB/main.php | 200 | none stated; IPCC © | on hold — DB being rebuilt ("early 2026") |
| World Bank IEG | https://ieg.worldbankgroup.org/data · DDH API | 403 · 429 | CC BY 4.0 (logged) | verify in browser |
| **OECD CRDF** *(new)* | https://sdmx.oecd.org/public/rest/dataflow/all | 200 (SDMX 2.1) | CC BY 4.0 (from Jul 2024) | keep P1; same client as CRS |
| OECD DAC CRS | https://sdmx.oecd.org/public/rest/dataflow/OECD.DCD.FSD/DSD_CRS@DF_CRS/ | 200 | CC BY 4.0 (from Jul 2024) | keep P1 |
| **IATI Datastore** *(new)* | https://developer.iatistandard.org/ (endpoint `api.iatistandard.org/datastore/activity/select`) | **401** without key — subscription required | open (per publisher) | keep P1; register a Hub key |
| WDPA / Protected Planet | https://api.protectedplanet.net/documentation | 200; token via request form | NC, no-redistribute | derive overlay stat only |
| **CSPD / CSO** *(new)* | https://cso.cgiar.org/ | 200 | CC BY-NC 4.0 | federate link; coordinate with CSO |
| **Global Forest Watch** *(new)* | https://data-api.globalforestwatch.org/dataset/umd_tree_cover_loss | 200 | **CC BY 4.0** (dataset metadata; v1.9.1) | keep P1 |
| **LandMark** *(new)* | https://www.landmarkmap.org/data-methods/access-data | 200 | **CC BY-SA 4.0** (June 2026) + LandMark ToS; form-gated | promoted P1; ShareAlike on derivatives |
| **Key Biodiversity Areas** *(new)* | https://www.keybiodiversityareas.org/en/request-gis-data | 200 | non-commercial via request form (5–10 working days); commercial via IBAT | promoted P1; budget lead time |
| FAO SDG 5.a.2 | https://www.fao.org/sustainable-development-goals-data-portal/data/indicators/5a2-women-s-equal-rights-to-land-ownership/en | 200 | FAO open terms | promoted P1 |
| Land Portal | `landportal.org` (403 to automated fetch — excluded from the link checker) | 403 (bot) | — | verify in browser |
| **WB Data360 (IMF FM, IDS)** *(new)* | https://data360api.worldbank.org/data360/indicators?datasetId=IMF_FM · data?DATABASE_ID=WB_IDS&REF_AREA=TGO | 200 · 200 | CC BY 4.0 | keep P1 route for IMF |
| **FAO EX-ACT codebase** *(new)* | https://github.com/un-fao/exact-django-webapp · https://exact.apps.fao.org/api/swagger/ | 200 · 200 (SPA shell, no API) | **AGPL-3.0-or-later** (code); app login | engine via self-host |
| **GLEAM 3 dashboard** *(new)* | https://foodandagricultureorganization.shinyapps.io/GLEAMV3_Public/ (Terms of Use tab) | 200 (Shiny; read in a browser 2026-10-07) | **CC BY 4.0** — "The data provided through the GLEAM Dashboard is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license" + FAO Statistical Database Terms of Use | **resolves the GLEAM licence conflict** — federate dashboard data (animal population, products, emissions, emission intensities); R package `un-fao/GLEAM` AGPL-3 |
| **iCLEANED** *(new)* | https://icleaned.alliance.cgiar.org/ · https://github.com/CIAT/icleaned · https://github.com/CIAT/cleaned | 200 · 200 · 200 | MIT (both repos) | method / tool case study |
| **Annual gridded livestock 1961–2021** *(candidate)* | https://essd.copernicus.org/preprints/essd-2025-175/ | 200 | open (ESSD) | time-series complement to GLW4; not queued |

Alternatives screened and **not** adopted: satellite foundation-model wealth products (arXiv
2604.23166 — preprint, licence unconfirmed; RWI CC0 stays), Sea Around Us (NC; only if marine
sub-national detail is needed), GYGA / WOCAT (parked P2), UNICEF MICS (dropped P3).
