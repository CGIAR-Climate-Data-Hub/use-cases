"""WHO/UNICEF JMP: headline WASH service ladder for one country, urban vs rural, latest year.

Federated example for the CDH record `who-unicef-jmp-wash`. No key needed.
Query at use time and cite JMP; do not re-host the table.
"""
import io

import pandas as pd
import requests

BASE = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/UNICEF,WASH_HOUSEHOLDS,1.0"
ISO3 = "TGO"
HEADLINE = {
    "WS_PPL_W-SM": "Safely managed drinking water",
    "WS_PPL_W-ALB": "At least basic drinking water",
    "WS_PPL_S-SM": "Safely managed sanitation",
    "WS_PPL_S-ALB": "At least basic sanitation",
    "WS_PPL_S-OD": "Open defecation",
    "WS_PPL_H-B": "Basic hygiene",
}

r = requests.get(f"{BASE}/{ISO3}....", params={"format": "csv", "startPeriod": 2000}, timeout=120)
r.raise_for_status()
df = pd.read_csv(io.StringIO(r.text))
df = df[df["INDICATOR"].isin(HEADLINE)]
latest = df["TIME_PERIOD"].max()
t = (df[df["TIME_PERIOD"] == latest]
     .pivot_table(index="INDICATOR", columns="RESIDENCE", values="OBS_VALUE")
     .rename(index=HEADLINE, columns={"_T": "total", "U": "urban", "R": "rural"}))
print(f"{ISO3}, {latest}, % of population:\n{t.round(1).to_string()}")
