"""Fragment builders — one function per rationale section.

Each builder returns a list of ``Fragment`` dicts. A fragment is a labelled, citable statement:

    {section, theme, serves: {cn, fp}, fragment_type, admin_level, admin_name,
     text, values: {...}, source_citation: {dataset, indicator_id, period, url, licence, retrieved_at},
     caveats: [...]}

Rules (the guardrails from the review page's Skills tab): every number comes from a row in the
inputs; the citation is that row's own request URL; nothing is invented — when a section has no
input the builder emits one ``gap`` fragment saying what is missing and where it is queued.
"""
from __future__ import annotations

import json
import math

import pandas as pd

from .loaders import HAZ_FREQ_LICENCE

HAZARD_LABEL = {"NDWS": "drought stress (NDWS, days of water stress)", "NDWL0": "waterlogging (NDWL0, days of excess water)",
                "NTx35": "crop heat stress (days > 35 °C)", "THI": "cattle heat stress (THI)", "TAVG": "mean temperature",
                "PTOT": "rainfall deficit", "HSH_max": "human heat stress"}
SCENARIO_LABEL = {"ssp126": "SSP1-2.6", "ssp245": "SSP2-4.5", "ssp370": "SSP3-7.0", "ssp585": "SSP5-8.5", "historic": "historical"}


def _f(x, nd=1):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "n/a"
    return f"{x:,.{nd}f}"


def _pct(x, nd=0):
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{100 * x:.{nd}f}%"


def _cite(row: pd.Series | dict, dataset=None, licence=None) -> dict:
    g = row.get if isinstance(row, dict) else (lambda k, d=None: row[k] if k in row.index and pd.notna(row[k]) else d)
    return {"dataset": dataset or g("dataset"), "source": g("source"), "indicator_id": g("indicator_id"),
            "period": None if g("period") is None else str(g("period")), "url": g("source_url"),
            "licence": licence or g("licence"), "retrieved_at": g("retrieved_at")}


def frag(section: dict, ftype: str, text: str, values: dict, cite: dict, *, admin_level=0, admin_name=None, caveats=None):
    return {"section": section["id"], "theme": section["theme"], "serves": section.get("serves", {}),
            "fragment_type": ftype, "admin_level": admin_level, "admin_name": admin_name, "text": text,
            "values": {k: (None if (isinstance(v, float) and math.isnan(v)) else v) for k, v in values.items()},
            "source_citation": cite, "caveats": caveats or []}


def gap(section: dict, what: str, where: str):
    return frag(section, "gap", f"GAP — {what}. {where}", {}, {"dataset": None, "url": None}, caveats=["no data in inputs; not fabricated"])


def _latest(df: pd.DataFrame, by: list[str]) -> pd.DataFrame:
    d = df.copy()
    d["_p"] = d["period"].astype(str)
    return d.sort_values("_p").groupby(by, dropna=False).tail(1)


def _q(fed: pd.DataFrame, source: str, **eq) -> pd.DataFrame:
    if fed.empty:
        return fed
    d = fed[fed["source"] == source]
    for k, v in eq.items():
        d = d[d[k] == v]
    return d


# ---------------------------------------------------------------- Section 1 — climate trends
RAIN_URL = "https://huggingface.co/datasets/aaguilar90/chirps-v3-daily-rnl/resolve/main/chirps-v3-daily-rnl.zarr"
RAIN_LIC = "CC0-1.0 (CHIRPS v3.0, Climate Hazards Center; HF redistribution by A. Aguilar)"


def section_1(sec, ctx):
    fr = []
    rain = ctx.get("rainfall", {})
    summ, ann, mclim = rain.get("summary"), rain.get("annual"), rain.get("monthly_clim")
    if summ is None or summ.empty:
        fr.append(gap(sec, "observed rainfall baseline and trend not loaded",
                      "Run code/rainfall/chirps_admin.py <ISO3> (CHIRPS v3 daily from the Hugging Face cube, global 60°S–60°N) and pass --rainfall."))
    else:
        cite = {"dataset": "CHIRPS v3.0 daily (rnl) → admin rainfall product (derived)", "source": "chirps_admin", "indicator_id": "ptot_annual",
                "url": RAIN_URL, "licence": RAIN_LIC, "retrieved_at": ctx["now"]}
        for lvl in ([0, 1] if ctx["subnational"] else [0]):
            for r in summ[summ.admin_level == lvl].itertuples():
                name = r.admin0_name if lvl == 0 else r.admin1_name
                sig = "statistically significant" if r.mk_p < 0.05 else "not statistically significant"
                direction = "wetter" if r.last5_mean_anomaly_mm > 0 else "drier"
                nd = 1 if abs(r.trend_mm_per_decade) < 10 else 0
                text = (f"{name}: mean annual rainfall {_f(r.baseline_mean_mm, 0)} mm over 1991–2020 (SD {_f(r.baseline_sd_mm, 0)} mm, CHIRPS v3). "
                        f"Theil–Sen trend {r.trend_mm_per_decade:+.{nd}f} mm/decade over {r.years} (95% CI {r.trend_ci_low:+.{nd}f} to {r.trend_ci_high:+.{nd}f}; "
                        f"Mann–Kendall p = {r.mk_p:.2f}, {sig}). The last five years averaged {abs(r.last5_mean_anomaly_pct):.0f}% {direction} than the baseline; "
                        f"wettest year {r.wettest_year}, driest {r.driest_year}.")
                fr.append(frag(sec, "trend_description", text,
                               {"baseline_mean_mm": r.baseline_mean_mm, "baseline_sd_mm": r.baseline_sd_mm, "trend_mm_per_decade": r.trend_mm_per_decade,
                                "trend_ci": [r.trend_ci_low, r.trend_ci_high], "mk_p": r.mk_p, "last5_anomaly_pct": r.last5_mean_anomaly_pct,
                                "wettest_year": int(r.wettest_year), "driest_year": int(r.driest_year), "years": r.years},
                               {**cite, "period": r.years}, admin_level=lvl, admin_name=name,
                               caveats=["CHIRPS rnl flavour (ERA5-disaggregated pentads); station-density drift can masquerade as trend (CHC caveat)",
                                        "0.05° pixels, area-weighted means over GAUL 2024 units"]))
        if mclim is not None and not mclim.empty:
            n = mclim[mclim.admin_level == 0].sort_values("month")
            if not n.empty:
                wet = n.nlargest(3, "ptot_mm")["month"].astype(int).tolist()
                fr.append(frag(sec, "baseline_value", f"{n.iloc[0].admin0_name}: seasonality 1991–2020 — monthly totals peak in months {', '.join(map(str, sorted(wet)))} "
                               f"({_f(n.ptot_mm.max(), 0)} mm in the wettest month, {_f(n.ptot_mm.min(), 0)} mm in the driest).",
                               {str(int(r.month)): float(r.ptot_mm) for r in n.itertuples()}, {**cite, "indicator_id": "ptot_monthly_climatology", "period": "1991-2020"}))
    fr.append(gap(sec, "observed temperature baseline/trend (CHIRTS-ERA5) and NEX-GDDP projections not wired",
                  "Projections are in the CR notebook parquet (Africa only); CHIRTS-ERA5 daily cube pending (asked Andrés)."))
    return fr


# ---------------------------------------------------------------- Section 2 — extreme events
def section_2(sec, ctx):
    hz = ctx["haz_freq"]
    if hz.empty:
        return [gap(sec, "per-GCM hazard frequency not loaded", "Atlas haz_freq.parquet (processing=hazard-change) — Africa only; "
                    "extension request drafted in ingestion-notes §2.")]
    fr = []
    url = hz["source_url"].iloc[0]
    periods = ("2041-2060", "2081-2100") if ctx.get("all_periods") else ("2041-2060",)
    base_caveats = ["threshold-based classification (haz_classes.csv), not a z-score", "annual timeframe; jagermeyr crop-calendar axis requested"]
    for lvl, grp in hz.groupby("admin_level"):
        if lvl > 0 and not ctx["subnational"]:
            continue
        for (name, hazard, sev), d in grp.groupby(["admin1_name" if lvl else "admin0_name", "hazard", "severity"], dropna=False):
            hist = d[d["scenario"] == "historic"]["value"]
            if hist.empty:
                continue
            h_med = hist.median()
            # Data-quality guard (found 2026-10-07): historic NDWS frequency is 1.0 for every GCM and every
            # African adm0 in haz_freq.parquet — a saturated baseline that cannot be compared with the
            # projections. Never state it as fact; emit the projection with an explicit caveat instead.
            saturated = bool((hist >= 0.999).all())
            cite = {"dataset": "Atlas haz_freq (NEX-GDDP-CMIP6 hazard-change)", "source": "atlas_haz_freq",
                    "indicator_id": f"frequency:{hazard}:{sev}", "url": url, "licence": HAZ_FREQ_LICENCE, "retrieved_at": ctx["now"]}
            for scen in ("ssp245", "ssp585"):
                for tf in periods:
                    fut = d[(d["scenario"] == scen) & (d["timeframe"] == tf)]["value"]
                    if fut.empty:
                        continue
                    med, q17, q83 = fut.median(), fut.quantile(0.17), fut.quantile(0.83)
                    if not saturated and h_med == 0 and q83 == 0:
                        continue  # nothing happens historically or in projection — uninformative
                    lab = f"{sev} {HAZARD_LABEL.get(hazard, hazard)}"
                    if saturated:
                        text = (f"In {name}, under {SCENARIO_LABEL[scen]} the share of years with {lab} is projected at {_pct(med)} in {tf} "
                                f"(likely range {_pct(q17)}–{_pct(q83)}, 17–83rd percentile across 18 GCMs). The 1995–2014 baseline for this hazard is "
                                f"saturated at 100% in the source table and is not quoted — see caveat.")
                        cav = base_caveats + ["DATA DEFECT: historic (1995–2014) frequency = 1.0 for every GCM and unit in haz_freq.parquet for this hazard; "
                                              "raised with the hazards pipeline (ingestion-notes §2, ask #6). Do not compare with projections until fixed."]
                    else:
                        text = (f"In {name}, the share of years with {lab} was {_pct(h_med)} over 1995–2014 (18-GCM ensemble median); "
                                f"under {SCENARIO_LABEL[scen]} it is projected at {_pct(med)} in {tf} (likely range {_pct(q17)}–{_pct(q83)}, "
                                f"17–83rd percentile across GCMs).")
                        cav = base_caveats
                    fr.append(frag(sec, "event_frequency", text,
                                   {"hazard": hazard, "severity": sev, "scenario": scen, "period": tf,
                                    "hist_median": None if saturated else h_med, "hist_saturated": saturated,
                                    "future_median": med, "q17": q17, "q83": q83, "n_gcm": int(fut.shape[0]), "baseline": "1995-2014"},
                                   {**cite, "period": f"1995-2014 vs {tf}"}, admin_level=int(lvl), admin_name=name, caveats=cav))
    return fr or [gap(sec, f"no haz_freq rows for {ctx['iso3']}", "Country outside the Africa hazard-change product.")]


# ---------------------------------------------------------------- Section 3 — exposure
def section_3(sec, ctx):
    fr = [gap(sec, "hazard × crop-value exposure matrix not wired", "Served by the CR notebook's canonical tiers "
              "(domain=hazard_exposure/source=nex-gddp-cmip6, ENSEMBLEmean, SSA only); GMIA-NEXT irrigated share queued.")]
    wc = ctx["worldcover"].get("cropland")
    if wc is not None and not wc.empty:
        n = wc[(wc.admin_level == 0) & (wc.year == 2021)]
        if not n.empty:
            r = n.iloc[0]
            fr.append(frag(sec, "exposed_area_ha", f"Cropland covers {_f(r.cropland_ha, 0)} ha ({_pct(r.cropland_share, 1)} of {r.admin0_name}) in 2021 (ESA WorldCover v200).",
                           {"cropland_ha": float(r.cropland_ha), "cropland_share": float(r.cropland_share), "year": 2021},
                           {"dataset": "ESA WorldCover admin product (derived)", "source": "worldcover_admin", "indicator_id": "cropland_share",
                            "period": "2021", "url": "s3://esa-worldcover/v200/2021/map/", "licence": "CC BY 4.0", "retrieved_at": ctx["now"]},
                           admin_name=r.admin0_name))
    return fr


# ---------------------------------------------------------------- Section 4 — vulnerability
def section_4(sec, ctx):
    fed = ctx["fed"]
    fr = []
    # FEWS NET latest national phase
    fews = _q(fed, "fews_net", admin_level=0)
    if not fews.empty:
        cur = fews[fews["scenario"].astype(str).str.contains("Current", na=False)]
        d = _latest(cur if not cur.empty else fews, ["admin_name"]).iloc[0]
        fr.append(frag(sec, "prevalence", f"FEWS NET classifies {d.admin_name} at IPC Phase {int(d.value)} ({d.value_text}) for {d.period} ({d.scenario}).",
                       {"ipc_phase": float(d.value), "label": d.value_text, "window": d.period}, _cite(d), admin_name=d.admin_name))
    # DHS national + subnational extremes
    for ind, label, unit in (("CN_NUTS_C_HA2", "children under five stunted", "%"), ("HC_WIXQ_P_LOW", "population in the lowest wealth quintile", "%"),
                             ("WS_SRCE_P_IMP", "population using an improved water source", "%"), ("CM_ECMR_C_U5M", "under-five mortality", "per 1,000 live births")):
        nat = _q(fed, "dhs", indicator_id=ind, admin_level=0)
        sub = _q(fed, "dhs", indicator_id=ind, admin_level=1)
        if nat.empty:
            continue
        n = _latest(nat, ["indicator_id"]).iloc[0]
        txt = f"{n.admin_name}: {_f(n.value)}{unit if unit == '%' else ' ' + unit} {label} (DHS {n.period})."
        vals = {"national": float(n.value), "survey_year": n.period}
        if not sub.empty:
            s = _latest(sub, ["admin_name"]).copy()
            s["admin_name"] = s["admin_name"].astype(str).str.lstrip(". ")  # DHS region labels carry leading dots
            hi, lo = s.loc[s["value"].idxmax()], s.loc[s["value"].idxmin()]
            txt += f" Subnational range {_f(lo.value)} ({lo.admin_name}) to {_f(hi.value)} ({hi.admin_name})."
            vals.update({"sub_min": float(lo.value), "sub_min_name": lo.admin_name, "sub_max": float(hi.value), "sub_max_name": hi.admin_name})
        fr.append(frag(sec, "index_value", txt, vals, _cite(n), admin_name=n.admin_name))
    # JMP latest at-least-basic water & sanitation, total residence
    jmp = _q(fed, "unicef_jmp")
    if not jmp.empty:
        jmp = jmp[jmp["qualifiers"].astype(str).str.contains('"residence": "_T"')]
        for ind, label in (("WS_PPL_W-ALB", "at least basic drinking water"), ("WS_PPL_S-ALB", "at least basic sanitation")):
            d = jmp[jmp["indicator_id"] == ind]
            if d.empty:
                continue
            r = _latest(d, ["indicator_id"]).iloc[0]
            fr.append(frag(sec, "prevalence", f"{_f(r.value)}% of the population used {label} services in {r.period} (WHO/UNICEF JMP).",
                           {"value_pct": float(r.value), "year": r.period}, _cite(r), admin_name=ctx["iso3"], caveats=["CC BY-NC-SA — carry the licence through"]))
    # INFORM — unresolved semantics: report range only
    inf = _q(fed, "inform", indicator_id="INFORM")
    if not inf.empty:
        fr.append(frag(sec, "index_value", f"INFORM Risk composite for {ctx['iso3']}: values returned by the JRC API span {_f(inf.value.min())}–{_f(inf.value.max())} "
                       f"(0–10) across {len(inf)} rows of workflow {json.loads(inf.iloc[0].qualifiers).get('workflow_id')}; a single headline value is not quotable until INFORM confirms the row semantics.",
                       {"min": float(inf.value.min()), "max": float(inf.value.max()), "n_rows": int(len(inf))}, _cite(inf.iloc[0]),
                       caveats=["INFORM API returns multiple unlabelled scores per indicator — see cdh_federated.inform"]))
    return fr or [gap(sec, "no vulnerability inputs", "Run cdh_federated first (inform, fews_net, dhs, unicef_jmp).")]


# ---------------------------------------------------------------- Section 5 — NDC / NAP
def section_5(sec, ctx):
    fed = ctx["fed"]
    cw = _q(fed, "climate_watch")
    if cw.empty:
        return [gap(sec, "Climate Watch NDC content not loaded", "Run cdh_federated climate_watch.")]
    fr = []
    sectors = cw[cw["indicator_id"] == "ndc_sector_covered"]["value_text"].dropna().tolist()
    if sectors:
        r = cw[cw["indicator_id"] == "ndc_sector_covered"].iloc[0]
        ag = [s for s in sectors if s in ("Agriculture", "Water", "LULUCF/Forestry", "Coastal Zone", "Disaster Risk Management (DRM)")]
        fr.append(frag(sec, "ndc_sector_coverage", f"The NDC covers {len(sectors)} sectors on Climate Watch, including {', '.join(ag) if ag else 'none of the agriculture/land/water sectors'}.",
                       {"sectors": sectors, "flw_sectors": ag}, _cite(r)))
    for slug, label in (("ndc_adaptation", "adaptation component included"), ("ndc_ghg_target_type", "GHG target type"),
                        ("ndc_time_target_year", "target year"), ("ndc_indc_summary", "NDC summary")):
        d = cw[cw["indicator_id"] == slug]
        if d.empty:
            continue
        r = d.iloc[0]
        fr.append(frag(sec, "target_statement", f"{label} ({r.period}): {str(r.value_text)[:400]}", {"value": r.value_text, "document": r.period}, _cite(r)))
    docs = cw[cw["indicator_id"] == "ndc_document"]
    if not docs.empty:
        fr.append(frag(sec, "document_link", f"{len(docs)} NDC documents available on Climate Watch: " + "; ".join(docs["value_text"].tolist()),
                       {"documents": docs["value_text"].tolist()}, _cite(docs.iloc[0])))
    return fr


# ---------------------------------------------------------------- Section 6 — impact / beneficiaries
def section_6(sec, ctx):
    wc = ctx["worldcover"].get("area")
    fr = []
    if wc is None or wc.empty:
        fr.append(gap(sec, "WorldCover admin areas not loaded", "Run code/worldcover/worldcover_admin.py <ISO3>."))
    else:
        n = wc[(wc.admin_level == 0) & (wc.year == 2021) & (wc.lc_class > 0)].sort_values("area_ha", ascending=False)
        top = "; ".join(f"{r.lc_label} {_f(r.area_ha, 0)} ha ({_pct(r.share, 1)})" for r in n.head(5).itertuples())
        fr.append(frag(sec, "activity_data_table", f"Land cover 2021 (ESA WorldCover v200), {n.iloc[0].admin0_name}: {top}.",
                       {r.lc_label: float(r.area_ha) for r in n.itertuples()},
                       {"dataset": "ESA WorldCover admin product (derived)", "source": "worldcover_admin", "indicator_id": "class_area_ha", "period": "2021",
                        "url": "s3://esa-worldcover/v200/2021/map/", "licence": "CC BY 4.0", "retrieved_at": ctx["now"]},
                       caveats=["activity data for IPCC Tier-1 / EX-ACT accounting; 2020→2021 change table is NOT a trend (v100→v200 algorithm change)"]))
        crop = ctx["worldcover"].get("cropland")
        if crop is not None and ctx["subnational"]:
            s = crop[(crop.admin_level == 1) & (crop.year == 2021)].sort_values("cropland_share", ascending=False)
            fr.append(frag(sec, "activity_data_table", "Cropland share by first-level unit (2021): " + "; ".join(f"{r.admin1_name} {_pct(r.cropland_share)}" for r in s.itertuples()),
                           {r.admin1_name: float(r.cropland_share) for r in s.itertuples()},
                           {"dataset": "ESA WorldCover admin product (derived)", "source": "worldcover_admin", "indicator_id": "cropland_share", "period": "2021",
                            "url": "s3://esa-worldcover/v200/2021/map/", "licence": "CC BY 4.0", "retrieved_at": ctx["now"]}, admin_level=1))
    fr.append(gap(sec, "tCO2e estimates require an accounting engine", "EX-ACT routed as a self-hosted engine (ingestion-notes §6); IPCC EFDB on hold."))
    return fr


# ---------------------------------------------------------------- Section 7 — portfolio
def section_7(sec, ctx):
    fed = ctx["fed"]
    rio = _q(fed, "oecd_rio_markers")
    fr = []
    if rio.empty:
        fr.append(gap(sec, "Rio-marker climate ODA not loaded", "Run cdh_federated oecd_rio_markers."))
    else:
        rio = rio.copy(); rio["_q"] = rio["qualifiers"].apply(json.loads)
        rio["marker"] = rio["_q"].apply(lambda q: q.get("marker")); rio["score"] = rio["_q"].apply(lambda q: q.get("score"))
        years = sorted(rio["period"].astype(str).unique())[-3:]
        for marker, label in (("30", "adaptation"), ("20", "mitigation")):
            d = rio[(rio.marker == marker) & (rio.score.isin(["1", "2"])) & (rio.period.astype(str).isin(years))]
            if d.empty:
                continue
            tot = d.groupby("period")["value"].sum()
            fr.append(frag(sec, "comparable_projects", f"DAC members committed USD {_f(tot.mean(), 1)} million/year (avg {years[0]}–{years[-1]}) of ODA marked for climate {label} "
                           f"(Rio marker {marker}, principal + significant) to {d.iloc[0].admin_name}.",
                           {"marker": marker, "years": years, "usd_m_per_year": float(tot.mean()), "by_year": {str(k): float(v) for k, v in tot.items()}},
                           _cite(d.iloc[0]), admin_name=d.iloc[0].admin_name, caveats=["commitments, current USD; OECD CRDF Rio markers"]))
    fr.append(gap(sec, "comparable GCF/GEF/AF projects list not wired", "CACC1 MCF dataset (5,115 projects) pending the champion's final version; IATI Datastore needs an API key."))
    return fr


# ---------------------------------------------------------------- Section 8 — safeguards
def section_8(sec, ctx):
    fr = []
    gfw = _q(ctx["fed"], "gfw")
    if gfw.empty:
        fr.append(gap(sec, "tree-cover loss not loaded", "GFW client needs GFW_API_KEY."))
    wc = ctx["worldcover"].get("area")
    if wc is not None and not wc.empty:
        t = wc[(wc.admin_level == 0) & (wc.year == 2021) & (wc.lc_class.isin([10, 95, 90, 80]))]
        if not t.empty:
            fr.append(frag(sec, "overlay_statistic", "Natural cover 2021 (WorldCover): " + "; ".join(f"{r.lc_label} {_f(r.area_ha, 0)} ha ({_pct(r.share, 1)})" for r in t.itertuples()),
                           {r.lc_label: float(r.area_ha) for r in t.itertuples()},
                           {"dataset": "ESA WorldCover admin product (derived)", "source": "worldcover_admin", "indicator_id": "class_area_ha", "period": "2021",
                            "url": "s3://esa-worldcover/v200/2021/map/", "licence": "CC BY 4.0", "retrieved_at": ctx["now"]}))
    fr.append(gap(sec, "protected areas / KBA / Indigenous lands overlays not built", "WDPA (token), KBA (request), LandMark (CC BY-SA) queued; MFL/Mosaic asked."))
    return fr


# ---------------------------------------------------------------- Section 9 — finance
def section_9(sec, ctx):
    fed = ctx["fed"]
    fr = []
    crs = _q(fed, "oecd_crs", indicator_id="crs_oda_disb_1000")
    if not crs.empty:
        s = crs.sort_values("period").tail(5)
        fr.append(frag(sec, "finance_flow_total", f"Total ODA disbursements from DAC members to {s.iloc[-1].admin_name}: " +
                       ", ".join(f"{r.period}: USD {_f(r.value, 0)} m" for r in s.itertuples()) + " (current prices).",
                       {str(r.period): float(r.value) for r in s.itertuples()}, _cite(s.iloc[-1]), admin_name=s.iloc[-1].admin_name))
        sect = _q(fed, "oecd_crs").copy()
        sect["sector_code"] = sect["qualifiers"].apply(lambda q: str(json.loads(q).get("sector_code", "")))
        # 5-digit CRS purpose codes only — the 3-digit codes are aggregates (e.g. 1000 all, 100 social infra)
        sect = sect[(sect.sector_code.str.len() == 5) & (sect.period.astype(str) == str(s.iloc[-1].period))].nlargest(5, "value")
        if not sect.empty:
            fr.append(frag(sec, "finance_flow_total", f"Largest ODA purpose codes in {s.iloc[-1].period}: " + "; ".join(f"{r.indicator.replace('ODA disbursements — ', '')} USD {_f(r.value, 1)} m" for r in sect.itertuples()),
                           {r.indicator: float(r.value) for r in sect.itertuples()}, _cite(sect.iloc[0])))
    imf = _q(fed, "data360_imf_fm", indicator_id="IMF_FM_G_XWDG_G01_GDP_PT")
    if not imf.empty:
        imf = imf.copy(); imf["_y"] = imf["period"].astype(int)
        last_actual = imf[imf._y <= ctx["year"]].sort_values("_y").iloc[-1]
        proj = imf[imf._y > ctx["year"]].sort_values("_y")
        txt = f"General government gross debt was {_f(last_actual.value)}% of GDP in {last_actual.period} (IMF Fiscal Monitor via World Bank Data360; latest year ≤ {ctx['year']} treated as actual/estimate)"
        if not proj.empty:
            txt += f", projected {_f(proj.iloc[-1].value)}% by {proj.iloc[-1].period}"
        fr.append(frag(sec, "fiscal_indicator", txt + ".", {"debt_pct_gdp": float(last_actual.value), "year": last_actual.period,
                                                           "projection": {str(r.period): float(r.value) for r in proj.itertuples()}}, _cite(last_actual)))
    for ind, label in (("IMF_FM_GGXCNL_G01_GDP_PT", "net lending/borrowing"), ("IMF_FM_GGR_G01_GDP_PT", "revenue")):
        d = _q(fed, "data360_imf_fm", indicator_id=ind)
        if d.empty:
            continue
        d = d.copy(); d["_y"] = d["period"].astype(int); r = d[d._y <= ctx["year"]].sort_values("_y").iloc[-1]
        fr.append(frag(sec, "fiscal_indicator", f"General government {label}: {_f(r.value)}% of GDP ({r.period}).", {"value_pct_gdp": float(r.value), "year": r.period}, _cite(r)))
    return fr or [gap(sec, "no finance inputs", "Run cdh_federated oecd_crs, data360_imf_fm.")]


BUILDERS = {1: section_1, 2: section_2, 3: section_3, 4: section_4, 5: section_5, 6: section_6, 7: section_7, 8: section_8, 9: section_9}
