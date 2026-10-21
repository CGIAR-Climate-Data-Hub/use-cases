"""Climate-marked ODA commitments to one recipient (OECD DAC Rio markers, SDMX REST).

Positional key: DONOR.RECIPIENT.SECTOR.MEASURE.ALLOCABLE.MARKER.SCORE.FLOW_TYPE.PRICE_BASE.MD_DIM.MD_ID.UNIT_MEASURE
MARKER 30 = adaptation, 20 = mitigation; SCORE 2 principal, 1 significant, 0 screened not targeted.
Only commitments (C) are published. Values are USD millions.
"""
import io

import pandas as pd
import requests

BASE = "https://sdmx.oecd.org/dcd-public/rest/data/OECD.DCD.FSD,DSD_RIOMRKR@DF_RIOMARKERS,1.6"
key = "DAC_EC.TGO.1000.100.2.30+20..C.V._T.0.USD"  # all DAC members, all sectors, adaptation + mitigation, any score
r = requests.get(f"{BASE}/{key}", params={"startPeriod": 2015, "format": "csvfilewithlabels"}, timeout=180)
r.raise_for_status()
df = pd.read_csv(io.StringIO(r.text))
climate = df[df["SCORE"].astype(str).isin(["1", "2"])]
print(climate.pivot_table(index="TIME_PERIOD", columns="Marker", values="OBS_VALUE", aggfunc="sum").round(1))
