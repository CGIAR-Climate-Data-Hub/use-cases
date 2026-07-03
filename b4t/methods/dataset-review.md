# B4T CRI — dataset review & CDH integration recommendations

Reviews the 23 hazard/vulnerability datasets in Appendix Table 1 of the CRI documentation, recommends modern **open** alternatives feasible for CDH integration, and flags what belongs to the Phase-2 methodology review. Method context: [cri-formulation.md](./cri-formulation.md). Canonical dataset list: [appendix-table-1.csv](./appendix-table-1.csv).

**How to read.** §1 headline; §2 decisions at a glance; §3 current vs recommended (identical axes — the core comparison); §4 what CDH should ingest; §5 what this does *not* fix; §6 per-row audit detail. Backing data: [current-datasets.csv](./current-datasets.csv), [improved-options.csv](./improved-options.csv), sources: [evidence/sources.md](./evidence/sources.md).

**Verdict** (about the CRI): **Keep** · **Replace** (swap in a ready open layer) · **Re-derive** (recompute the metric on a modern open input) · **Clarify** (need B4T input) · **No open replacement confirmed**.
**CDH action** (about the hub): **Catalogue-as-is** · **Ingest-new** · **Derive-in-pipeline** · **No-action**.

**Evidence rule.** Current facts come only from B4T source documents; candidate facts only from steward pages, verified live and adversarially re-checked. **Where Bert's emails (2026-04-29/30) and the CRI documentation disagree, the emails describe the *actual* data used and take precedence — the published doc is not fully up to date.** Such disagreements are marked `conflicted`. Unknowns are written as unknowns (`pending`).

**Reuse rule.** Recommendations **build on datasets the Hub already produces or can catalogue**, so they are ready to adopt. Internal assets to draw on first: the **CHIRPS-CHIRTS-ERA5 SPEI** observational track (drought/rainfall, Africa), the **NASA NEX-GDDP-CMIP6 v2** projections track (CMIP6/SSP source for future rows), and the **water-balance v2** track (NDWS/NDWL, FAO-56 Penman-Monteith ET₀) for soil-water/water-stress rows. New datasets can follow as later enhancements where needed.

> **Status:** All 23 Appendix Table 1 rows scoped (draft). Each has a verdict, a recommended direction (off-the-shelf ready product or CDH-derived), and open questions for Bert where relevant. Current-state lineage corrected against Bert's emails. Next: consolidate the Bert questions, confirm lineage gaps, and (per Todd) rebuild the pipeline for the old-vs-new comparison.

---

## 1. Executive summary

Fills as rows complete. Current shape, from the §3 interrogation:

- **The problem is mixed lineage, not uniform age.** The 23 inputs span several eras in one score. The CCAFS/Thornton future layers (R-01, R-02, T-02, T-03) are **CMIP5 / RCP8.5** — 17 GCMs, Jones & Thornton (2009/2013/2015), 2050s, per Philip Thornton's account (provenance not fully confirmed; possibly older in part). The historic layers are observational (drought = **WASP at a coarse 2.5°**, 1980–2000; Dartmouth floods 1985–2003; rainfall CV historic). The **WRI Aqueduct family** (D-03/04/05, R-04/05, F-02/03) *may* be running on **CMIP5-era Aqueduct**, not the CMIP6 Aqueduct 4.0 the doc cites — to verify.
- **Horizons are mixed:** historic (drought 1980–2000, floods 1985–2003), 2030 (Aqueduct), 2050s (CCAFS/Thornton) — averaged 50-50 present/future in one index.
- **Everything is pre-CMIP6 / pre-SSP.** No layer yet uses CMIP6 or SSP scenarios; the future layers are RCP8.5. Modernizing to CMIP6/SSP is warranted across the future-facing rows.
- **Two labelling issues for B4T:** `T-03` appears to be a verbatim duplicate of `R-01`; and `D-01` is mislabelled "SPI" — the actual index is **WASP** (a different IRI index), not the WMO-standard SPI.

## 2. Decisions at a glance

**Table 1.** Verdict (about the CRI) and CDH action (about the Hub) for all 23 datasets.

**Temporal** reflects the CRI's 50-50 present/future design: *Future* = already carries projections; *Historic + future (ready/derive)* = present-climate now, with a future element off-the-shelf or via a CDH build; *Historic (static)* = observational, no meaningful future.

| Code | Variable | Hazard | Temporal | Verdict | CDH action | Effort |
| --- | --- | --- | --- | --- | --- | --- |
| D-01 | SPI/WASP (drought-event frequency) | Drought | Historic + future (derive) | **Adopt SPEI** — extend CDH pipeline global | Re-run CDH SPEI pipeline globally; ASI complementary | Low–med |
| D-02 | Failed season | Drought | Historic + future (derive) | **Clarify** — confirm source &amp; role | Confirm w/ Bert; WRSI if retained | — |
| D-03 | Available blue water | Drought | Future (CMIP6) | **Keep** — Aqueduct 4.0 (CMIP6) | Catalogue-as-is; confirm version + slice | Low |
| D-04 | Gross water demand / net consumption | Drought | Future (CMIP6) | **Keep** — Aqueduct 4.0 (CMIP6) | Catalogue-as-is; confirm version + slice | Low |
| D-05 | Baseline water stress | Drought | Future (CMIP6) | **Keep** — Aqueduct 4.0 (CMIP6) | Catalogue-as-is; confirm version + slice | Low |
| F-01 | Dartmouth flood frequency | Flooding | Historic (observed) | **Replace** — Global Flood Database | Ingest GFD (satellite-observed, GEE) | Low |
| F-02 | River flood hazard | Flooding | Future (CMIP5→6) | **Modernize** → GIRI (CMIP6) | Ingest GIRI; Aqueduct Floods = CMIP5 alt | Med |
| F-03 | Coastal flood hazard | Flooding | Future (CMIP5→6) | **Modernize pending** — coastal gap | No open CMIP6 *inundation* layer; open CMIP6 *driver* exists (Copernicus CDS sea-level indicators) → build, not off-the-shelf; keep Aqueduct Floods coastal meanwhile | Med |
| R-01 | LGP flip over 120 days | Changed rainfall | Future (CMIP5→6) | **Modernize** → GAEZ v5 (CMIP6) | GAEZ v5 LGP; or derive from NEX-GDDP v2 | Med |
| R-02 | LGP flip over 90 days | Changed rainfall | Future (CMIP5→6) | **Modernize** → GAEZ v5 (CMIP6) | GAEZ v5 LGP; or derive from NEX-GDDP v2 | Med |
| R-03 | Annual rainfall CV | Changed rainfall | Historic + future (derive) | **Re-derive** on CHIRPS v3 | CHIRPS-derived annual CV (SPEI stack) | Low |
| R-04 | Intra-annual variability | Changed rainfall | Future (CMIP6) | **Keep** — Aqueduct 4.0 (CMIP6) | Catalogue-as-is; confirm version + slice | Low |
| R-05 | Seasonal variability | Changed rainfall | Future (CMIP6) | **Keep** — Aqueduct 4.0 (CMIP6) | Catalogue-as-is; confirm version + slice | Low |
| T-01 | Extreme humid heat days | High temperature | Historic + future (derive) | **Keep** — GEHE (modern, open) | Catalogue-as-is; pair CMIP6 future | Low |
| T-03 | LGP-linked temperature stress | High temperature | Future (CMIP5→6) | **Clarify** — duplicate of R-01 (drop/merge) | Confirm w/ Bert; drop or merge | — |
| T-02 | Growing-season Tmax flip 30C | High temperature | Future (CMIP5→6) | **Modernize** → NEX-GDDP v2 (CMIP6) | Derive growing-season Tmax flip; GAEZ v5 alt | Med |
| S-01 | Salt-affected soils map | Salinity | Historic (static) | **Keep** — FAO GSASmap (off-the-shelf) | Catalogue-as-is | Low |
| S-02 | Global soil salinity | Salinity | Historic (static) | **Keep** — ISRIC (off-the-shelf) | Catalogue; clarify overlap w/ S-01 | Low |
| W-01 | Water retention 1500 kPa | Soil water | Historic (static) | **Keep** — SoilGrids 2.0 (off-the-shelf) | Update to SoilGrids 2.0 | Low |
| W-02 | Available water capacity | Soil water | Historic (static) | **Keep** — SoilGrids 2.0 (off-the-shelf) | Update to SoilGrids 2.0 | Low |
| W-03 | Rooting zone water storage | Soil water | Historic (static) | **Keep** — Stocker 2023 (off-the-shelf) | Catalogue (Zenodo); consolidate | Low |
| W-04 | Plant-available soil water | Soil water | Historic (static) | **Keep** — Gupta 2023 (off-the-shelf) | Catalogue (Zenodo 6777126, CC-BY); consolidate | Low |
| I-01 | Area equipped with irrigation | Irrigation | Historic + future (ready) | **Keep** — Mehta 2024 (off-the-shelf) | Catalogue (Zenodo); projected AEI for future | Low |

## 3. Current inputs

What B4T uses **now**, on 12 lineage axes. Populated from primary sources and **corrected against Bert's emails** (which describe the actual data; the CRI doc lags). `conflicted` = sources disagree; `pending` = not yet verified. Rendered from [current-datasets.csv](./current-datasets.csv).

**Table 2.** Current-state lineage of the 23 inputs on twelve axes, from B4T source documents and corrected against Bert's emails. In *Downscaling / bias*: a named technique (delta, quantile-mapping, neural-net) where known; `present (…)` = a step was applied but technique not stated; `none` = no climate downscaling/bias; `N/A` = not applicable (historical/observational); `pending` = unverified. `CMIP5*` = provenance not fully confirmed. Specifics: R-01/02, T-02/03 use Jones-&-Thornton downscaling + bias-correction, exact technique unstated; F-02 = rainfall bias-correction only; W-01's random-forest pedotransfer is soil modelling, not a climate step → `none`.

| Hazard | Code | Variable | Resolution | Baseline dataset | Baseline period | Future dataset | Future period | Scenario | CMIP | Downscaling / bias | GCM ensemble |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Drought | D-01 | SPI/WASP (event freq.) | 2.5° → 0.05° grid | WASP (IRI); Dilley 2005 — *doc says SPI/Ericksen* | 1980–2000 *(doc: 1974–2004)* | N/A | N/A | N/A | N/A | N/A | N/A |
| Drought | D-02 | Failed season | pending | Hyman et al. 2025 | 100 years | N/A | N/A | N/A | N/A | pending | N/A |
| Drought | D-03 | Available blue water | pending | Aqueduct (version?) | 1960–2019 | Aqueduct | 2030 | pending | doc: 4.0/CMIP6 · Bert: maybe CMIP5-era | pending | pending |
| Drought | D-04 | Gross water demand | pending | Aqueduct (version?) | 1960–2019 | Aqueduct | 2030 | pending | doc: 4.0/CMIP6 · Bert: maybe CMIP5-era | pending | pending |
| Drought | D-05 | Baseline water stress | pending | Aqueduct (version?) | 1960–2019 | Aqueduct | 2030 | pending | doc: 4.0/CMIP6 · Bert: maybe CMIP5-era | pending | pending |
| Flooding | F-01 | Dartmouth flood freq. | ~1° → 0.05° | Dartmouth Flood Obs. (Dilley 2005) | 1985–2003 | N/A | N/A | N/A | N/A | N/A | N/A |
| Flooding | F-02 | River flood hazard | pending | ISI-MIP forcing | — | ISI-MIP (GCM×RCP) | 2030 (2010–49) | RCP8.5 | CMIP5-era | present | pending |
| Flooding | F-03 | Coastal flood hazard | MERIT 30″ → 0.05° | GTSR water levels | 1979–2014 | SLR projection | 2030 | RCP | CMIP5-era | pending | pending |
| Changed rainfall | R-01 | LGP flip >120d | 0.05° | Thornton baseline (Jones & Thornton) | ~2000s | Downscaled CMIP5 (Jones & Thornton 2009/13/15) | 2050s | **RCP8.5** | **CMIP5** *(uncertain)* | present | 17 CMIP5 GCMs *(Thornton pers. comm.)* |
| Changed rainfall | R-02 | LGP flip >90d | 0.05° | Thornton baseline | ~2000s | Downscaled CMIP5 (Jones & Thornton) | 2050s | **RCP8.5** | **CMIP5** *(uncertain)* | present | 17 CMIP5 GCMs |
| Changed rainfall | R-03 | Annual rainfall CV | 0.05° | Observed rainfall (Dilley 2005 / Thornton) | Historic | current used as future proxy | N/A | N/A | N/A | N/A | N/A |
| Changed rainfall | R-04 | Intra-annual variability | pending | Aqueduct (version?) | 1960–2019 | Aqueduct | 2030 | pending | doc: 4.0/CMIP6 · Bert: maybe CMIP5-era | pending | pending |
| Changed rainfall | R-05 | Seasonal variability | pending | Aqueduct (version?) | 1960–2019 | Aqueduct | 2030 | pending | doc: 4.0/CMIP6 · Bert: maybe CMIP5-era | pending | pending |
| High temperature | T-01 | Extreme humid heat days | 0.05° (~5 km) | Tuholske 2023 GEHE | 1983–2016 | N/A | N/A | N/A | N/A | pending | N/A |
| High temperature | T-03 | LGP-linked temp stress | 0.05° | Thornton baseline | ~2000s | Downscaled CMIP5 (Jones & Thornton) | 2050s | **RCP8.5** | **CMIP5** *(uncertain)* | present | 17 CMIP5 GCMs · likely duplicate of R-01 |
| High temperature | T-02 | Tmax flip >30C | 0.05° | Thornton baseline | ~2000s | Downscaled CMIP5 (Jones & Thornton) | 2050s | **RCP8.5** | **CMIP5** *(uncertain)* | present | 17 CMIP5 GCMs |
| Salinity | S-01 | Salt-affected soils | pending | FAO GSASmap (Omuto 2020) | 1970–2005 | N/A | N/A | N/A | N/A | N/A | N/A |
| Salinity | S-02 | Global soil salinity | pending | ISRIC (Ivushkin 2019) | 1986–2016 | N/A | N/A | N/A | N/A | N/A | N/A |
| Soil water | W-01 | Water retention 1500 kPa | pending | ISRIC WoSIS (Batjes 2024) | 1918–2013 | N/A | N/A | N/A | N/A | none | N/A |
| Soil water | W-02 | Available water capacity | 250 m | SoilGrids250m (Hengl 2017) | 1950–2016 | N/A | N/A | N/A | N/A | N/A | N/A |
| Soil water | W-03 | Rooting zone storage | pending | Stocker et al. 2023 | 2003–2018 | N/A | N/A | N/A | N/A | N/A | N/A |
| Soil water | W-04 | Plant-available soil water | pending | Gupta et al. 2023 | 1979–2016 | N/A | N/A | N/A | N/A | N/A | N/A |
| Irrigation | I-01 | Area equipped w/ irrigation | pending | Mehta et al. 2024 | 2000–2015 | N/A | N/A | N/A | N/A | N/A | N/A |

> **Recommended alternatives** are held in [improved-options.csv](./improved-options.csv) and shown inline (as shaded → rows) in the rendered report. So far only D-01 is reviewed → **CDH SPEI-03** (existing CDH product: CHIRPS v3 + CHIRTS-ERA5, 0.05°, Africa; SPEI = precipitation − PET). The CMIP5/pre-CMIP6 layers are replaced by default (via the internal NEX-GDDP-CMIP6 v2 track); other rows carry no recommendation until reviewed.

## 4. CDH integration plan

*(Fills as rows complete; feeds the brief's "Data assets for the hub" table.)* For each recommended dataset: catalogue-as-is vs ingest-new vs derive-in-pipeline, with a 1–5 feasibility rating. Prefer internal CDH tracks (SPEI observational; NEX-GDDP-CMIP6 v2 projections; water-balance v2) over new builds. **D-01:** catalogue the existing CDH SPEI climatology/admin tiers — no new build; feasibility ~1/5 for Africa (the gap is coverage + construct, not build).

> **Planned deliverable (per Todd, 2026-05):** a rebuilt CRI pipeline in code that produces the current index and a modernized (CMIP6/open-input) version **side by side**, so B4T can see whether the data-source change is *meaningful for what they breed*. This dataset review scopes that rebuild; the old-vs-new comparison is the payoff. (Use-case coordination: Bia.)

**Licences of recommended datasets** (load-bearing for Hub redistribution; verified 2026-07-03). Most are permissive — **CC-BY 4.0**: CHIRPS v3 (also public domain), NEX-GDDP-CMIP6 (also CC0), GAEZ v5, Aqueduct 4.0, **FAO ASI** (current FAO catalog record; supersedes an older CC-BY-NC-SA 3.0 IGO reference), **GEHE** (SEDAC/Earthdata — explicitly commercial **and** non-commercial), ISRIC SoilGrids 2.0 & salinity, Stocker 2023, **Gupta 2023** (Zenodo 6777126), Mehta AEI; **CC0 / public domain**: L-WRSI, crop-WRSI; **ODbL**: SPEIbase; Aqueduct Floods = open with attribution; Copernicus CDS sea-level indicators (coastal driver, Phase-2) = CC-BY; CDH SPEI = internal (Hub-owned). **Non-commercial (usable — CDH/CGIAR is a non-profit NGO):** **Global Flood Database (F-01) = CC BY-NC** (use the GEE version, not the CC-BY-NC-**ND** HydroShare mirror, so derivatives are allowed); **GIRI (F-02) = non-commercial + registration**. NC restricts *commercial* use, which doesn't apply — but terms are respected: attribution on all, **share-alike where required (ODbL, SPEIbase)**, NC passed through on redistribution. **One item still to confirm:** **FAO GSASmap (S-01)** — no licence printed on the product page; **CC-BY 4.0 by FAO's default database policy**, but a third-party-data carve-out may apply (built from ~257k national points, 118+ countries), so confirm on the GloSIS platform record. *(Gupta 2023 and GEHE, previously unconfirmed, are now verified CC-BY 4.0.)*

## 5. What this review does **not** solve

The 2026-04 meetings and outreach ask for climate information that is **crop-specific, timed to growth stage, and linked to market segments / TPPs**, projected ~20–25 years forward. Modernizing dataset *inputs* does not deliver that — a generic annual hazard layer stays generic regardless of input vintage. That gap — hazard timing, crop-stage sensitivity, HII provenance (see below), CCC crop-vs-variety, the yield step — is the **Phase-2 methodology review**, intended as the shared PoD input for 2026/27 planning.

**An existing asset for that work:** CDH / the AAA Atlas already hold crop-relevant **maximum-temperature (tmax)** data that could support crop-specific temperature thresholds — so crop-specificity can also build on an existing product. To be scoped in the Phase-2 methodology review.

**HII note (Phase 2).** Bert confirms AI (ChatGPT-5/Copilot-5/Gemini) was used only to *rough-cut* which environmental conditions to include and give a first interaction score, then literature + expert review corrected it, run across tools/versions to check consistency — treated as a fallback where literature/expert input was absent. Pete has flagged, from the AAA Atlas experience, that AI hazard-matrix work hallucinated heavily once reference-checked. Provenance depth of the HII matrix is a central Phase-2 question.

## 6. Dataset details (per-row audit layer)

Each row is split into **Present** — the variable as the CRI defines it plus the data actually used now (source, resolution, period, scenario/CMIP where relevant, known issues) — and **Recommended** — the modern open alternative and the CDH action. Depth scales with the decision, but every row carries both sides so old and new line up.

### D-01 — "SPI" (actually WASP) — drought-event frequency

**Verdict: Adopt CDH's existing SPEI product** *(reuse an asset the Hub already produces rather than build a new layer; construct needs a B4T decision).* Adopt **SPEI** as the drought hazard, delivered by **extending CDH's existing SPEI pipeline to global 0.05°** (a re-run of a proven pipeline, not a new indicator) — with FAO ASI as a complementary agriculture-specific layer. See the researched decision below.

**At a glance.**

| Field | Present | Recommended |
| --- | --- | --- |
| Dataset | WASP (IRI) via Dilley 2005 — doc labels it "SPI" (Ericksen 2011) | **CDH SPEI** (internal) — CHIRPS v3 + CHIRTS-ERA5; SPEI-03 |
| Resolution | 2.5° (~275 km) → 0.05° grid | 0.05° |
| Temporal | 1980–2000 (doc: 1974–2004) · historic | 1981–present (ref 1991–2020) |
| Scenario · CMIP | N/A (observational) | N/A (observational) |
| GCM ensemble | N/A | N/A |
| Access · licence | legacy / internal | CDH Digital-Atlas (S3 COGs; adm0/adm1 parquet) · internal (Hub-owned) |
| CDH action / status | conflicted · not standard SPI · very coarse | Extend existing SPEI pipeline to global 0.05° (re-run) · effort Low–med · FAO ASI complementary |

The rest of this row is the full worked example (present-data conflict, SPEI spec, caveats, decision) — resolved end-to-end to set the pattern.

**Present — what the CRI uses now.** Supplies the drought hazard layer: how often a location suffers a drought event, where an event = three or more consecutive months receiving ≤50% of normal precipitation. Historic, not a future projection.

**Present data — sources conflict.** Per Bert & Philip Thornton's emails (the actual data): the drought layer is the **Weighted Anomaly of Standardized Precipitation (WASP)** developed by IRI, computed on a **2.5°×2.5°** grid from monthly precipitation for **1980–2000**, with high-risk areas taken from the top two deciles of Dilley (2005). The CRI documentation instead labels it "SPI" over 1974–2004 (Ericksen 2011). Either way:

1. **It is not the standard SPI.** WMO-standard SPI (McKee et al. 1993) is a normalised probability index. WASP is a different IRI index; the CRI's layer is a precipitation-deficit event count. Publishing it as "SPI" misrepresents it.
2. **The current resolution is very coarse.** WASP at **2.5°** is roughly 275 km per cell — far coarser than the CRI's 0.05° working grid, so the current layer is heavily interpolated up.
3. **Provenance conflicts** between the emails (WASP, 2.5°, 1980–2000) and the doc (SPI, 1974–2004) → **question for Bert**.

**Recommended — CDH's existing SPEI product** (internal Digital-Atlas observational track, CHIRPS v3 + CHIRTS-ERA5). Already produced and gridded — no new derivation. Spec per the CDH team (July 2026):

**Table 4.** The existing CDH SPEI product (CHIRPS-CHIRTS-ERA5 observational track) and its fit to D-01. Internal spec, CDH team, July 2026.

| Property | CDH SPEI product | Fit to CRI |
| --- | --- | --- |
| Index | SPEI at 1, 3, 6, 12, 24-month scales | SPEI-03 matches the 3-month window — but SPEI, not SPI/WASP (see caveats) |
| Inputs | CHIRPS v3 precip + CHIRTS-ERA5 temperature; PET = Hargreaves 1985 | Adds evaporative demand (temperature), unlike the current precip-only layer |
| Resolution | 0.05° | Same as the CRI grid — ~50× finer than the current 2.5° WASP |
| Coverage | Africa now (−20…55°E, −40…40°N); pipeline **extends to global** | Global run bounded by CHIRPS to **60°N–60°S** — covers essentially all B4T crops |
| Time span | 1981-01 → present; reference 1991–2020 | More current than 1980–2000; WMO/AR6 baseline |
| Availability | SPEI climatology COGs on S3 (digital-atlas); monthly per-pixel local only; adm0/adm1 parquet | Climatology + admin tiers ready to catalogue; monthly grids local (Tier 3) |

**Why this is the strong choice.** It runs at the CRI's native 0.05° on a proven, maintained CHIRPS-based pipeline — extending it from Africa to global is a re-run, not a new indicator, so it fits within capacity. It is also a genuine upgrade on the coarse 2.5° WASP layer (finer, more current, temperature-aware). But it is not a like-for-like swap.

**Caveats B4T must weigh.** (1) **SPEI, not SPI/WASP** — SPEI subtracts evaporative demand (Hargreaves PET), making drought temperature-sensitive; arguably better under warming, but it partly overlaps the CRI's separate high-temperature hazard (possible double-counting — Phase 2). (2) **Coverage — extend globally** — currently produced for Africa, but the same pipeline re-runs at global extent (0.05°, bounded by CHIRPS to 60°N–60°S, covering essentially all B4T crops); a re-run within capacity, not a new indicator. (3) **No pure SPI in the Hub yet** — a precipitation-only index would be a new addition rather than an existing product.

**SPEIbase (CSIC) — independent cross-check.** Global land, 1901–2024, monthly, 0.5°, ODbL, open. Useful to validate the extended CDH product; not needed for coverage now that the CDH pipeline runs globally at the finer 0.05°.

**Best-in-class agriculture-specific alternative — FAO ASI (Agricultural Stress Index System).** Built *for* agriculture: crop-season drought from satellite vegetation health (VHI), **masked to cropland and timed to each growing season**. Global, **1 km, dekadal, 1984–present**, operational at FAO, open (Google Earth Engine, ArcGIS Online, FAO FTP). Cutting-edge cousin: **Copernicus Combined Drought Indicator (CDI)** — SPI + soil-moisture + fAPAR anomaly, crop-masked, Watch/Warning/Alert classes (global via GDO, open). Both measure *realised crop/vegetation stress* — a different construct from a climatic index, and observational (no future projections).

**Recommended baseline (researched decision).** Adopt **SPEI** as the drought-hazard index. *Why SPEI, not ASI/CDI:* the CRI's drought slot is a **hazard** layer and the CRI already scores the crop's response separately (coping capacity), so the hazard should be the *climatic* water deficit (SPEI) — a realised-stress index like ASI would double-count crop response. SPEI is also temperature-aware. **Deliver it by extending CDH's existing SPEI pipeline to global 0.05°** (CHIRPS-CHIRTS-ERA5) — a re-run of a proven pipeline, not a new indicator, and within capacity. Coverage is bounded by CHIRPS to **60°N–60°S**, which covers essentially all B4T crop areas (the practical availability caveat; a modest compute/storage cost for the global run). Keep **FAO ASI** (global, 1 km, crop-masked, open) as a complementary agriculture-specific / validation layer, with **SPEIbase** as an independent global cross-check. Get B4T sign-off on moving from the precipitation-deficit count to SPEI, and stop calling it "SPI".

**CDH integration.** Use existing CDH asset — catalogue the published SPEI climatology/admin tiers (no new build). Feasibility ~1/5 for Africa; the gap is coverage + construct, not build.

**Bridge to the B4T ask.** A modern drought input still yields a *generic annual* drought layer. B4T's stated need — drought severity/duration timed to crop growth stage, per market segment — is a Phase-2 method question.

**Open questions for Bert.** Is temperature-aware SPEI acceptable for the drought hazard in place of the precip-only WASP layer (and does it overlap the heat hazard)? What covers the non-Africa footprint? Is the current layer WASP (2.5°, 1980–2000) or the doc's "SPI 1974–2004"?

**Sources.** Internal CDH SPEI product spec (CDH team, July 2026); CHIRPS v3 / SPEIbase steward pages — [evidence/sources.md](./evidence/sources.md).

### D-02 — Failed season (cropping reliability)

**Verdict: Clarify — confirm source &amp; role with Bert.** Can't finalise until the mis-cited source and production status are confirmed; a clear modern route exists if retained.

**Measures:** probability of a failed growing season — germination/establishment, then fewer than 50 growing days before season end. Reported as % cropping reliability; production-specific (a season "fails" when production cost exceeds harvest value).

| Field | Present | Recommended (if retained) |
| --- | --- | --- |
| Dataset | **Unverifiable** — cited "Hyman et al. 2025" is a mis-citation (arXiv 2503.17293 is a fisheries paper); likely intended Glenn Hyman (Alliance/CIAT), paper not locatable | **WRSI** — L-WRSI (global, landscape-level) · crop-specific WRSI (FEWS regions) · GeoWRSI-on-CHIRPS (global crop-specific, derive) |
| Resolution | unknown | L-WRSI landscape · crop-WRSI 0.1° |
| Temporal | "100 years" (doc) · historic | L-WRSI 1982–present · crop-WRSI 2001–present |
| Scenario · CMIP | N/A (observational) | N/A (observational) |
| GCM ensemble | N/A | N/A |
| Access · licence | unknown | USGS FEWS / CHC GeoWRSI · CC0 (L-WRSI) |
| CDH action / status | conflicted — source & production status unconfirmed | Clarify first; if retained, GeoWRSI-on-CHIRPS (same stack as D-01) |

**Alternatives:** FAO GAEZ growing-period / reliability (open, ~9–10 km, historical + future); CDH internal **water-balance v2** (NDWS/NDWL). **Overlap (Phase 2):** failed-season overlaps the LGP-flip rows and drought — confirm it is a distinct, needed input (double-count risk). Keep the production cost-vs-value test as a B4T economic assumption, separate from the climate layer.

**Sources.** FAO/USGS WRSI &amp; CHC GeoWRSI; FAO GAEZ v4 — [evidence/sources.md](./evidence/sources.md).

### Aqueduct 4.0 (shared) — D-03, D-04, D-05 (drought) · R-04, R-05 (changed rainfall)

**Verdict: Keep — on Aqueduct 4.0 (CMIP6); confirm the version.** Light touch — retain, don't replace — *if* B4T is on 4.0. Bert flagged the CRI may still run an older CMIP5-era Aqueduct, so the one real action is confirming the version.

**Measures:** five WRI Aqueduct water indicators — D-03 available blue water; D-04 gross water demand / net consumption (8 monthly sectoral sets, 1960–2019); D-05 baseline water stress; R-04 intra-annual variability; R-05 seasonal variability.

**Version uncertain:** Bert notes *"seems CMIP5 is being used in the CRI, but Aqueduct v4.0 is available using CMIP6"* — the current layers may be an older CMIP5-era Aqueduct. Confirming the running version is the one real action; the spec below is the CMIP6 4.0 target.

**Recommended (Keep) — WRI Aqueduct 4.0 (CMIP6).**

| Field | Aqueduct 4.0 (CMIP6) |
| --- | --- |
| Dataset | 5 water-quantity indicators; hydrology model PCR-GLOBWB 2 |
| Access | WRI data page · Google Earth Engine |
| Resolution | sub-basin (hydrological unit) |
| Temporal | baseline GCM historical 1960–2014 (bias-corrected) · future 2030 / 2050 / 2080 |
| Scenario · CMIP | SSP1-2.6 / SSP3-7.0 / SSP5-8.5 · CMIP6 |
| GCM ensemble | 5 GCMs — GFDL-ESM4, IPSL-CM6A-LR, MPI-ESM1-2-HR, MRI-ESM2-0, UKESM1-0-LL |
| Licence | CC-BY 4.0 |
| CDH action | Keep — catalogue as-is · effort Low · confirm running version is 4.0/CMIP6 (not CMIP5-era) + scenario/period slice |

**Questions for Bert.** Confirm the Aqueduct version (4.0/CMIP6, not CMIP5-era); which scenario + period; 5-GCM ensemble vs single model; exact indicator layers used; and harmonise the 2030 horizon with the CRI's other future layers.

**Sources.** WRI Aqueduct 4.0 (Kuzma et al. 2023) technical note + data page — [evidence/sources.md](./evidence/sources.md).

### F-01 — Dartmouth flood frequency (historic)

**Verdict: Replace — Global Flood Database.** A modern satellite-observed successor to the same Dartmouth lineage.

**Measures:** historic flood-frequency proxy — relative frequency of flood occurrence per pixel. Observational, no future element.

| Field | Present | Recommended |
| --- | --- | --- |
| Dataset | Dartmouth Flood Observatory event catalogue (Dilley 2005, top-two-deciles) | **Global Flood Database** (Tellman 2021) — 913 satellite-observed flood events, 169 countries |
| Resolution | nearest degree (→ 0.05° grid) | ~250 m (MODIS) |
| Temporal | 1985–2003 · historic | 2000–2018 · observed |
| Scenario · CMIP | N/A (observational) | N/A (observational) |
| GCM ensemble | N/A | N/A |
| Access · licence | legacy / internal | Google Earth Engine (Cloud to Street) · CC-BY-NC 4.0 (non-profit OK; use GEE, not the ND HydroShare mirror) |
| CDH action / status | coarse & dated; poor data early-mid 1990s | Ingest; derive per-pixel flood-frequency · effort Low |

**Secondary option:** Google Flood Hub *"Inundation History"* — per-pixel *frequency* of inundation (1999–2020, 128 m; wet ≥5 / ≥1 / ≥0.5% = High/Med/Low), Google Cloud Storage, CC-BY 4.0. Its README confirms it is a **repackaging of the GLAD Global Surface Water Dynamics dataset** (Pickens et al. 2020, UMD; **Landsat 5/7/8**, 30 m native → 128 m, smoothed) — i.e. a **surface-water-occurrence** product (peer of JRC Global Surface Water), **not a flood-event catalogue**, coverage band excludes far north/south. Useful context; complements GFD, doesn't replace it. (Distinct from Flood Hub's operational Sentinel-1/2 nowcast model.)

**Sources.** Global Flood Database (Tellman et al. 2021) — [evidence/sources.md](./evidence/sources.md).

### Flood hazard (shared) — F-02 river · F-03 coastal (Aqueduct Floods)

**Verdict: Modernize CMIP5 → CMIP6.** Current Aqueduct Floods is RCP/CMIP5-era — a modernization candidate, *not* an automatic Keep like Aqueduct 4.0 (CMIP6).

**Measures:** WRI Aqueduct Floods (Ward et al. 2020) — a **1-in-10-year** flood hazard, no protection assumed. Two layers: F-02 river, F-03 coastal.

#### F-02 — river flood hazard

| Field | Present | Recommended |
| --- | --- | --- |
| Dataset | WRI Aqueduct Floods — riverine (ISI-MIP forcing) | **GIRI riverine** (CIMA/UNEP-GRID) — probabilistic fluvial hazard |
| Resolution | ~30″ (pending confirm) | 90 m |
| Temporal | future 2030 (input 2010–2049) | baseline + SSP future periods |
| Scenario · CMIP | RCP8.5 · CMIP5-era (ISI-MIP) | SSP1-2.6 & SSP5-8.5 · CMIP6 |
| GCM ensemble | multi-model (ISI-MIP) | single GCM (IPSL-CM6A-LR) |
| Access · licence | WRI · GEE | giri.unepgrid.ch (registration) · non-commercial + attribution (non-profit OK) |
| CDH action / status | CMIP5-obsolete | Ingest · effort Med · trade-off: single-GCM vs Aqueduct multi-model (CMIP5) |

#### F-03 — coastal flood hazard

| Field | Present | Recommended (driver only) |
| --- | --- | --- |
| Dataset | WRI Aqueduct Floods coastal — MERIT DEM 30″ + GTSR | **No ready CMIP6 inundation layer.** Driver = Copernicus CDS "sea level change indicators" (Muis 2023) — extreme-sea-level / surge indicators, *not* flood extent |
| Resolution | MERIT DEM 30″ → 0.05° grid | ~2.5 km coastal (0.1°) |
| Temporal | baseline 1979–2014 · SLR projection 2030 | epochs to 2021–2050 |
| Scenario · CMIP | RCP · CMIP5-era | SSP5-8.5 · CMIP6 HighResMIP |
| GCM ensemble | multi-model | HighResMIP ensemble |
| Access · licence | WRI · GEE | Copernicus CDS · CC-BY |
| CDH action / status | CMIP5 — no CMIP6 upgrade exists | Phase-2 **build** a coastal-hazard layer on the driver; keep Aqueduct Floods coastal (CMIP5) meanwhile |

**Cross-checks:** Kirezci 2020 is CMIP5/RCP and not openly packaged; GIRI is riverine-only. Harmonise the return-period/horizon with the rest of the CRI.

**Sources.** WRI Aqueduct Floods (Ward et al. 2020); GIRI (CIMA/UNEP-GRID) — [evidence/sources.md](./evidence/sources.md).

### Changed-rainfall LGP flips (shared) — R-01 (>120 d) · R-02 (>90 d)

**Verdict: Modernize CMIP5 → CMIP6 (GAEZ v5).** Legacy Thornton LGP layers → ready CMIP6 agro-climatic LGP.

**Measures:** length of growing period (LGP). R-01 flags LGP flipping >120→<120 days/yr by the 2050s; R-02 the >90→<90 threshold (growing day = mean air temp >6 °C and actual/potential ET > 0.35; R-02 per Nachtergaele et al. 2002).

| Field | Present | Recommended |
| --- | --- | --- |
| Dataset | Legacy CCAFS/Thornton LGP threshold-flips (Jones & Thornton 2009/13/15) | **FAO GAEZ v5** — "Total number of growing period days" (Growing Period sub-theme) |
| Resolution | 0.05° | ~10 km |
| Temporal | baseline ~2000s → 2050s | historical 1981–2000, 2001–2020 · future 2021–2100 (4 periods) |
| Scenario · CMIP | RCP8.5 · CMIP5 (provenance uncertain) | 3 SSPs · CMIP6 AR6 *(exact SSP codes to confirm)* |
| GCM ensemble | 17 CMIP5 GCMs (Thornton, pers. comm.) | multi-GCM · CMIP6 AR6 (count not confirmed) |
| Access · licence | legacy / internal | FAO catalog (GeoTIFF · WMTS · GCS) · CC-BY 4.0 |
| CDH action / status | pre-CMIP6/SSP — CMIP5-obsolete · conflicted | Derive threshold-flip from baseline-vs-future LGP · effort Med · internal alt: NEX-GDDP-CMIP6 v2 |

**Why GAEZ v5:** it computes LGP directly from an agro-climatic water balance — the exact construct — as a ready CMIP6 product. (Thermal LGPt Ta>5/10/20/30 °C are separate layers.) *Provenance of the present layer:* Ericksen (2011) describes an older CMIP3/A2/4-GCM set; Bert is unsure — but either way it is pre-CMIP6/SSP.

**Note — likely duplicate + overlap.** T-03 (High temperature) is word-for-word the R-01 LGP-flip — resolve before implementing. LGP adequacy also overlaps failed-season (D-02) and drought — Phase-2 consolidation.

**Sources.** FAO GAEZ v5; CDH NEX-GDDP-CMIP6 v2 — [evidence/sources.md](./evidence/sources.md).

### R-03 — Annual rainfall coefficient of variation (historic)

**Verdict: Re-derive on CHIRPS v3.** Modern open precipitation, same stack as D-01.

**Measures:** flags areas where the coefficient of variation of annual rainfall exceeds the global 75th percentile (28%). Historic; current variability used as a proxy for the future (little info on how variability itself changes).

| Field | Present | Recommended |
| --- | --- | --- |
| Dataset | Observed rainfall (Dilley 2005 / Thornton) | **CHIRPS v3** — re-derive annual rainfall CV (same stack as D-01) |
| Resolution | 0.05° | 0.05° |
| Temporal | historic (current used as future proxy) | 1981–present |
| Scenario · CMIP | N/A (observational) | N/A (observational) |
| GCM ensemble | N/A | N/A |
| Access · licence | legacy / internal | CHC / UCSB · public domain + CC-BY 4.0 |
| CDH action / status | verified-current | Re-derive CV on CHIRPS v3 · effort Low · Phase-2: CMIP6 future-variability (GAEZ v5 / NEX-GDDP v2) |

**Sources.** CHIRPS v3 (CHC/UCSB) — [evidence/sources.md](./evidence/sources.md).

### T-01 — Extreme humid heat days (GEHE)

**Verdict: Keep — modern & open.** Tuholske GEHE is a current, open WBGT humid-heat product.

**Measures:** annual count of days with max Wet Bulb Globe Temperature (WBGTmax) above ISO thresholds (>28/30/32 °C) — physiologically-relevant humid heat; manually masked.

**Recommended (Keep) — GEHE (Tuholske et al. 2023).**

| Field | GEHE |
| --- | --- |
| Dataset | Global Extreme Heat Estimates — WBGT on the CHC CHIRTS record |
| Access | NASA SEDAC / Earthdata (DOI 10.7927/hff0-k565) |
| Resolution | 0.05° (~5 km) |
| Temporal | 1983–2016 · observed |
| Scenario · CMIP | N/A (observational) |
| GCM ensemble | N/A |
| Licence | CC-BY 4.0 (commercial & non-commercial) |
| CDH action | Keep — catalogue as-is · effort Low · caveat: ends 2016 · pair CMIP6 future heat (NEX-GDDP v2) for the future slot (Phase-2) |

**Sources.** GEHE (Tuholske et al. 2023, NASA SEDAC) — [evidence/sources.md](./evidence/sources.md).

### T-02 — Growing-season Tmax flip over 30 °C

**Verdict: Modernize CMIP5 → CMIP6.** Legacy Thornton heat-threshold layer → CMIP6 from an internal track.

**Measures:** areas where growing-season mean daily Tmax flips from <30 °C to >30 °C, masked where LGP > 40 days (30 °C = critical threshold; Boote 1998, Prasad 2008).

| Field | Present | Recommended |
| --- | --- | --- |
| Dataset | Legacy CCAFS/Thornton growing-season heat-threshold flip | **NASA NEX-GDDP-CMIP6 v2** (internal CDH track) — derive the growing-season Tmax-flip |
| Resolution | 0.05° | 0.25° |
| Temporal | baseline ~2000s → 2050s | 1950–2100 |
| Scenario · CMIP | RCP8.5 · CMIP5 (provenance uncertain) | SSPs · CMIP6 *(confirm which SSPs ingested)* |
| GCM ensemble | 17 CMIP5 GCMs (Thornton, pers. comm.) | up to 35 GCMs |
| Access · licence | legacy / internal | internal CDH projections track · CC-BY 4.0 / CC0 |
| CDH action / status | CMIP5-obsolete · conflicted | Derive flip (needs growing-season mask, reuse LGP rows') · effort Med · alt: GAEZ v5 thermal (ready, ~10 km) |

**Sources.** CDH NEX-GDDP-CMIP6 v2; FAO GAEZ v5 — [evidence/sources.md](./evidence/sources.md).

Note: T-03 is covered under the LGP-flips block — likely a verbatim duplicate of R-01; Clarify with Bert, drop or merge.

### Salinity, soil water & irrigation (off-the-shelf) — S-01/02, W-01–04, I-01

**Verdict: Keep — off-the-shelf.** All seven are modern, open, ready products from authoritative stewards; no build needed. The work is cataloguing + consolidation, not replacement.

Seven ready open datasets to **catalogue as-is** (no build). Present ≈ Recommended, except W-01/W-02 (update to SoilGrids 2.0).

| Row | Recommended dataset | Resolution | Temporal | Licence · access | CDH action |
| --- | --- | --- | --- | --- | --- |
| S-01 | FAO **GSASmap** (Omuto 2020) — salt-affected soils (ECe/ESP/pH) | — | 1970–2005 | CC-BY 4.0 by FAO default *(confirm)* · GloSIS platform | Keep · catalogue |
| S-02 | ISRIC Global Soil Salinity (Ivushkin 2019) | — | 1986–2016 | open · ISRIC file server | Keep · overlaps S-01 |
| W-01 | Water retention 1500 kPa → **SoilGrids 2.0** (from WoSIS, Batjes 2024) | 250 m | 1918–2013 | CC-BY 4.0 · ISRIC | Update to 2.0 |
| W-02 | Available water capacity → **SoilGrids 2.0** (FC−WP; from SoilGrids250m, Hengl 2017) | 250 m | 1950–2016 | CC-BY 4.0 · ISRIC | Update to 2.0 |
| W-03 | Rooting-zone water storage (Stocker 2023) | — | 2003–2018 | open · Zenodo | Keep · catalogue |
| W-04 | Plant-available soil water (Gupta 2023) | 1 km | 1979–2016 | CC-BY 4.0 · Zenodo 6777126 | Keep · catalogue |
| I-01 | Area equipped for irrigation (Mehta 2024) | — | 2000–2015 | open · Zenodo | Keep · + projected AEI (Gao, SSP) for future |

**Consolidation flags (Phase 2).** Two salinity products (S-01 vs S-02) and four soil-water products (W-01/02/03/04) all describe soil water-holding capacity — likely more layers than the CRI needs. Confirm which are load-bearing rather than modernising all of them. Bert also notes the crop **coping-capacity (CCC)** soil-water term uses a soil water-balance model (waterlogging / water stress) with MapSPAM crops — confirm how the W-01…04 layers relate to it (possible overlap/double-count).

**Recommendation.** Keep all seven off-the-shelf (catalogue; update W-01/W-02 to SoilGrids 2.0; verify W-04's dataset). No CDH build required. Phase 2: consolidate the salinity pair and soil-water quartet; add projected AEI (SSP) if a future irrigation layer is needed.

**Sources.** FAO GSASmap; ISRIC SoilGrids 2.0 / salinity; Stocker 2023 (Zenodo); Gupta 2023; Mehta 2024 (Zenodo) — [evidence/sources.md](./evidence/sources.md).

---

**All 23 Appendix Table 1 rows are now scoped.** Every current input has a verdict, a recommended direction (off-the-shelf or CDH-derived), and open questions for Bert where relevant. Next: consolidate the questions, confirm the lineage gaps, and (per Todd) rebuild the pipeline for the old-vs-new comparison.

## Feedback & corrections

This is a draft for review. Reviewers can raise corrections, concerns, and dataset suggestions **without a GitHub account**: a Microsoft Form (linked from the rendered report as a floating "💬 Feedback" button) feeds Power Automate, which opens a tracked GitHub issue labelled `review-feedback`. Setup and the form/flow spec: [feedback-loop.md](./feedback-loop.md).
