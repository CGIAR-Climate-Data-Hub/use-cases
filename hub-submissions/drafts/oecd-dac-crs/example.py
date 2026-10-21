"""ODA disbursements from all DAC members to one recipient, by CRS sector (OECD SDMX REST).

Positional key: DONOR.RECIPIENT.SECTOR.MEASURE.CHANNEL.MODALITY.FLOW_TYPE.PRICE_BASE.MD_DIM.MD_ID.UNIT_MEASURE
An empty position is a wildcard. Values are USD millions (UNIT_MULT 6).
"""
import io

import pandas as pd
import requests

BASE = "https://sdmx.oecd.org/dcd-public/rest/data/OECD.DCD.FSD,DSD_CRS@DF_CRS,1.6"
recipient = "TGO"
key = f"DAC.{recipient}..100._T._T.D.V._T.0.USD"  # all DAC, every sector, ODA, disbursements, current USD
r = requests.get(f"{BASE}/{key}", params={"startPeriod": 2015, "format": "csvfilewithlabels"}, timeout=180)
r.raise_for_status()
df = pd.read_csv(io.StringIO(r.text), dtype={"SECTOR": str})
total = df[df["SECTOR"] == "1000"][["TIME_PERIOD", "OBS_VALUE"]].sort_values("TIME_PERIOD")
print(total.to_string(index=False))  # USD millions, all sectors
