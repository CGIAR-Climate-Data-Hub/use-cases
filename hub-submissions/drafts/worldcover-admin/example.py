"""ESA WorldCover by admin unit: cropland and land-cover shares per district for one country.

Example for the CDH record `worldcover-admin`. The data are NOT YET UPLOADED (planned location
below); until then pass a local folder written by worldcover_admin.py:
    python example.py /path/to/out
"""
import sys

import pandas as pd

BASE = sys.argv[1] if len(sys.argv) > 1 else "https://digital-atlas.s3.amazonaws.com/cdh/data/worldcover-admin/v1"
ISO3 = "TGO"

area = pd.read_parquet(f"{BASE}/worldcover_admin_area_{ISO3}.parquet")
crop = pd.read_parquet(f"{BASE}/worldcover_admin_cropland_{ISO3}.parquet")

# 2021 only: 2020 (v100) and 2021 (v200) use different algorithms, so do not difference them
c21 = crop[(crop["year"] == 2021) & (crop["admin_level"] == 1)]
print(c21[["admin1_name", "cropland_ha", "cropland_share"]].round(3).to_string(index=False))

a21 = area[(area["year"] == 2021) & (area["admin_level"] == 0)]
print("\nCountry land cover 2021 (share):")
print(a21.set_index("lc_label")["share"].sort_values(ascending=False).round(3).to_string())
