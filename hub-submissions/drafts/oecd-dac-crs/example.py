"""Development finance to one country from the OECD Creditor Reporting System (CRS).

Federated example for the CDH record `oecd-dac-crs`. No key needed.
Answers: how much ODA did the country receive each year, how much went to agriculture, water and
environment, and who were the main providers in the latest year?

Positional key: DONOR.RECIPIENT.SECTOR.MEASURE.CHANNEL.MODALITY.FLOW_TYPE.PRICE_BASE.MD_DIM.MD_ID.UNIT_MEASURE
An empty position means "all values". Always fix RECIPIENT (an unfiltered query is over 1 GB).
Values are USD million. Cite: OECD (2026), CRS: Creditor Reporting System (flows), OECD Data Explorer.
"""
import io
import xml.etree.ElementTree as ET

import pandas as pd
import requests

BASE = "https://sdmx.oecd.org/dcd-public/rest/data/OECD.DCD.FSD,DSD_CRS@DF_CRS,1.6"
RECIPIENT = "KEN"       # ISO3 of a country on the DAC list of ODA recipients
START = 2015
SECTORS = {"1000": "All sectors", "311": "Agriculture", "140": "Water supply & sanitation",
           "410": "General environment protection"}


def get(key: str) -> pd.DataFrame:
    r = requests.get(f"{BASE}/{key}", params={"startPeriod": START, "format": "csvfilewithlabels"}, timeout=180)
    r.raise_for_status()
    return pd.read_csv(io.StringIO(r.text), dtype={"SECTOR": str, "DONOR": str})


# Provider codes mix single providers with groups (DAC, ALLD = all official providers, G7, World Bank
# Group ...). The code list does not mark every group, so keep only: three-letter country codes, and
# codes that sit under a parent (e.g. IDA under World Bank) without being a parent themselves.
CODELIST = "https://sdmx.oecd.org/dcd-public/rest/codelist/OECD.DCD.FSD/CL_AREA_ORG/1.6"
NS = {"s": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure",
      "c": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common"}


def single_providers() -> set[str]:
    root = ET.fromstring(requests.get(CODELIST, timeout=120).content)
    codes = root.findall(".//s:Code", NS)
    parents = {ref.get("id") for c in codes for ref in c.findall("s:Parent/Ref", NS)}
    groups = {c.get("id") for c in codes if c.find(".//c:AnnotationType[.='COMP_RULE']", NS) is not None}
    ids = {c.get("id") for c in codes if c.get("id") not in parents | groups}
    has_parent = {c.get("id") for c in codes if c.find("s:Parent", NS) is not None}
    # "DAC" (all DAC countries) is the one three-letter code that is a group
    return {i for i in ids if (len(i) == 3 and i.isalpha()) or i in has_parent} - {"DAC"}


# 1. Everything Kenya received from all official providers (ALLD: countries + multilaterals), by sector.
#    DAC alone (DAC member countries) is less than half of this for Kenya.
df = get(f"ALLD.{RECIPIENT}..100._T._T.D.V._T.0.USD")
by_sector = (df[df["SECTOR"].isin(SECTORS)]
             .pivot_table(index="TIME_PERIOD", columns="SECTOR", values="OBS_VALUE")
             .rename(columns=SECTORS).round(1))
print(f"ODA disbursed to {RECIPIENT} by all official providers, USD million (current prices):")
print(by_sector.to_string())

# 2. Main single providers in the latest year: leave DONOR empty, all sectors (1000), drop groups
prov = get(f".{RECIPIENT}.1000.100._T._T.D.V._T.0.USD")
latest = prov["TIME_PERIOD"].max()
singles = single_providers()
top = prov[(prov["TIME_PERIOD"] == latest) & prov["DONOR"].isin(singles)].nlargest(10, "OBS_VALUE")
print(f"\nTop single providers to {RECIPIENT} in {latest}, USD million:")
print(top[["Donor", "OBS_VALUE"]].round(1).to_string(index=False))
print("\nNotes: disbursements = money actually paid that year. Only providers that report to the OECD are included.")
