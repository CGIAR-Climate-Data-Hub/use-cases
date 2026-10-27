"""Climate-tagged aid to one country from the OECD Rio markers (bilateral providers only).

Federated example for the CDH record `oecd-rio-markers`. No key needed.
Answers: how much adaptation and mitigation aid was committed to the country each year (principal
and significant separately), and which providers and sector groups fund adaptation?

Positional key: DONOR.RECIPIENT.SECTOR.MEASURE.ALLOCABLE.MARKER.SCORE.FLOW_TYPE.PRICE_BASE.MD_DIM.MD_ID.UNIT_MEASURE
Fixed in this dataset: MEASURE 100, ALLOCABLE 2, FLOW_TYPE C, MD_DIM _T, MD_ID 0, UNIT_MEASURE USD.
Values are USD million, commitments. Never add adaptation and mitigation together (one activity
can carry both). Multilateral providers are not in this dataset.
Cite: OECD (2026), RioMarkers, OECD Data Explorer.
"""
import io
import xml.etree.ElementTree as ET

import pandas as pd
import requests

BASE = "https://sdmx.oecd.org/dcd-public/rest/data/OECD.DCD.FSD,DSD_RIOMRKR@DF_RIOMARKERS"  # no version = latest
RECIPIENT = "KEN"
START = 2015
MARKERS = {"30": "Adaptation", "20": "Mitigation"}
SCORES = {"2": "principal", "1": "significant"}


def get(key: str) -> pd.DataFrame:
    r = requests.get(f"{BASE}/{key}", params={"startPeriod": START, "format": "csvfilewithlabels"}, timeout=300)
    r.raise_for_status()
    return pd.read_csv(io.StringIO(r.text), dtype=str).assign(OBS_VALUE=lambda d: d["OBS_VALUE"].astype(float))


# 1. All DAC members + EU Institutions (DAC_EC), all sectors (1000), both markers, scores 2 and 1
df = get(f"DAC_EC.{RECIPIENT}.1000.100.2.30+20.2+1.C.V._T.0.USD")
df["series"] = df["MARKER"].map(MARKERS) + " (" + df["SCORE"].map(SCORES) + ")"
t = df.pivot_table(index="TIME_PERIOD", columns="series", values="OBS_VALUE").round(1)
latest = t.index.max()
print(f"Climate-tagged ODA commitments to {RECIPIENT}, bilateral providers, USD million (current prices):")
print(t.to_string())
print(f"Note: {latest} is likely incomplete until the December release; use the last complete year.\n")

complete = t.index[t.index < latest]
years = list(complete[-5:])
yr = "+".join(years) if years else latest

# 2. Top single providers for adaptation (principal + significant), last five complete years
prov = get(f".{RECIPIENT}.1000.100.2.30.2+1.C.V._T.0.USD")
prov = prov[prov["TIME_PERIOD"].isin(years) & (prov["DONOR"] != "DAC_EC")]
print(f"Top providers of adaptation aid to {RECIPIENT}, {years[0]}-{years[-1]}, USD million:")
print(prov.groupby("Donor")["OBS_VALUE"].sum().nlargest(8).round(1).to_string())

# 3. Sectors for adaptation. Sector codes are nested several levels deep (1000 > 450 > 100 > 140 ...),
#    so take one level only: the sectors directly above the 5-digit purpose codes (none overlap).
NS = {"s": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure"}
cl = ET.fromstring(requests.get("https://sdmx.oecd.org/dcd-public/rest/codelist/OECD.DCD.FSD/CL_DAC_SECTOR/1.3", timeout=120).content)
groups = sorted({c.find("s:Parent/Ref", NS).get("id") for c in cl.iter("{%s}Code" % NS["s"])
                 if len(c.get("id")) == 5 and c.find("s:Parent/Ref", NS) is not None})
sec = get(f"DAC_EC.{RECIPIENT}.{'+'.join(groups)}.100.2.30.2+1.C.V._T.0.USD")
sec = sec[sec["TIME_PERIOD"].isin(years)]
print(f"\nAdaptation aid to {RECIPIENT} by sector, {years[0]}-{years[-1]}, USD million:")
print(sec.groupby("Sector")["OBS_VALUE"].sum().nlargest(8).round(1).to_string())
