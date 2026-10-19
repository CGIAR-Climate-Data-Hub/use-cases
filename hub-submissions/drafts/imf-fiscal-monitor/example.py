"""IMF Fiscal Monitor series for one country via the World Bank Data360 API (no key)."""
import pandas as pd
import requests

rows, skip = [], 0
while True:
    r = requests.get("https://data360api.worldbank.org/data360/data",
                     params={"DATABASE_ID": "IMF_FM", "REF_AREA": "TGO", "skip": skip}, timeout=120)
    r.raise_for_status()
    d = r.json()
    rows += d["value"]
    skip += len(d["value"])
    if not d["value"] or skip >= d["count"]:
        break
df = pd.DataFrame(rows)
df["OBS_VALUE"] = pd.to_numeric(df["OBS_VALUE"])
print(df.pivot_table(index="TIME_PERIOD", columns="INDICATOR", values="OBS_VALUE").tail(8).round(1))
