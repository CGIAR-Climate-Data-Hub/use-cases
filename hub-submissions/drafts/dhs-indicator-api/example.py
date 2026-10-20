"""DHS Program Indicator Data API: latest subnational values for one country, with units.

Federated example for the CDH record `dhs-indicator-api`. No key needed.
Cite: The DHS Program Indicator Data API, ICF (see the record's attribution).
"""
import pandas as pd
import requests

API = "https://api.dhsprogram.com/rest/dhs"
COUNTRY = "TG"  # DHS country code (Togo); not always ISO alpha-2
INDICATORS = ["CN_NUTS_C_HA2", "HC_WIXQ_P_LOW", "HC_ELEC_H_ELC", "WS_SRCE_P_IMP",
              "ED_LITR_W_LIT", "CM_ECMR_C_U5M", "HC_HEFF_H_MPH", "FP_CUSA_W_MOD"]

meta = requests.get(f"{API}/indicators", params={"indicatorIds": ",".join(INDICATORS), "f": "json"},
                    timeout=120).json()["Data"]
units = {m["IndicatorId"]: m["MeasurementType"] for m in meta}

r = requests.get(f"{API}/data", params={"countryIds": COUNTRY, "indicatorIds": ",".join(INDICATORS),
                                        "breakdown": "subnational", "surveyYearStart": 2005,
                                        "f": "json", "perpage": 5000}, timeout=120)
r.raise_for_status()
df = pd.DataFrame(r.json()["Data"])
df = df[df["IsTotal"] != 1]
# latest survey per indicator and region
df = df.sort_values("SurveyYear").groupby(["IndicatorId", "RegionId"]).tail(1)
df["unit"] = df["IndicatorId"].map(units)
df["region"] = df["CharacteristicLabel"].str.lstrip(".")
print(df.pivot_table(index="region", columns="IndicatorId", values="Value").round(1).to_string())
print("\nsurveys:", sorted(df["SurveyId"].unique()), "| units:", units)
