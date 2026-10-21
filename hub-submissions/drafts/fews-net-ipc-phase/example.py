"""FEWS NET acute food-insecurity phases for one country (FEWS NET Data Warehouse API, no key)."""
import pandas as pd
import requests

r = requests.get("https://fdw.fews.net/api/ipcphase/", params={"format": "json", "country_code": "TG"}, timeout=120)
r.raise_for_status()
df = pd.DataFrame(r.json())
current = df[df["scenario_name"].str.strip() == "Current Situation"]
latest = current.sort_values("projection_start").groupby("geographic_unit_full_name").tail(1)
print(latest[["geographic_unit_full_name", "unit_type", "projection_start", "projection_end", "value", "description"]].to_string(index=False))
