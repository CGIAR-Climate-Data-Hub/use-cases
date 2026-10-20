"""Climate Watch NDC Content: every coded row for one country, split by source.

Federated example for the CDH record `climate-watch-ndc-content`. No key needed.
Only rows with source == "Climate Watch" are CC BY 4.0; other sources keep their own terms.
"""
import pandas as pd
import requests

API = "https://www.climatewatchdata.org/api/v1/data/ndc_content"
ISO3 = "TGO"

rows, page = [], 1
while True:
    r = requests.get(API, params={"countries[]": ISO3, "per_page": 500, "page": page}, timeout=120)
    r.raise_for_status()
    batch = r.json()["data"]
    rows += batch
    if len(rows) >= int(r.headers.get("Total", 0)) or not batch:
        break
    page += 1
df = pd.DataFrame(rows)

print(f"{ISO3}: {len(df)} rows; by source:\n{df['source'].value_counts().to_string()}\n")
cw = df[df["source"] == "Climate Watch"]
print("Adaptation rows coded by Climate Watch (first 10):")
print(cw[cw["global_category"] == "Adaptation"][["indicator_name", "sector", "value"]].head(10).to_string(index=False))
print("\nSectors with any coded content:", sorted(df["sector"].dropna().unique())[:15])
