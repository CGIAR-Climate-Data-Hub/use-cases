# CHIRPS v3 → admin rainfall baseline, anomalies, trend (Theme 1, any country 60°S–60°N)

`chirps_admin.py` fills the Theme 1 gap the review flagged: the Climate Rationale notebook's
observed rainfall is Africa-only, but the GCF pipeline includes Syria, Iraq, Sri Lanka and Egypt.
It reads Andrés Aguilar's **CHIRPS v3.0 daily (`rnl`) Zarr v3 cube on Hugging Face** (global
60°S–60°N, 0.05°, 1981–2026-08, CC0 — a CDH v0.3.0 record ships beside it) and writes per
adm0 / adm1 / adm2 on Atlas GAUL 2024 boundaries:

| file | content |
| --- | --- |
| `chirps_admin_annual_<ISO3>` | year × unit → `ptot_mm`, `anomaly_mm`, `anomaly_pct` vs 1991–2020 |
| `chirps_admin_summary_<ISO3>` | unit → baseline mean/SD, Theil–Sen trend (mm/decade, 95 % CI), Mann–Kendall p, last-5-year anomaly, wettest/driest year |
| `chirps_admin_monthly_clim_<ISO3>` | unit × month → 1991–2020 mean monthly total (seasonality) |
| `chirps_admin_<ISO3>.json` | inputs, method, caveats, run stats |

```bash
python3 -m venv .venv && .venv/bin/pip install "zarr>=3" xarray numpy pandas pyarrow shapely rasterio scipy
.venv/bin/python chirps_admin.py SYR --out out/                      # downloads the GAUL adm2 parquet once
.venv/bin/python chirps_admin.py TGO --out out/ --boundaries gaul24_a2_africa.parquet
```

Reads only the chunks intersecting the country bbox (one year at a time, ~4 s/year for a
Togo-sized country); no dask needed (`xr.open_zarr(..., chunks=None)`). The trend uses Theil–Sen
with Mann–Kendall as the GCF memo asks (the statistics Harold's deferred sprint was to add).

Caveats (also in the sidecar): `rnl` ≠ `sat` flavour; int16 × 0.1 mm storage; station-density
drift can masquerade as trend (CHC); 0.05° pixels — tiny adm2s use their centroid pixel.
Boundaries default to the Atlas Africa GAUL 2024 adm2 file. For other countries extract from the
Atlas **global** raw GAUL 2024 file (725 MB; the raw column names `iso3_code`, `gaul*_name` are
accepted) — GDAL's Parquet driver does it over HTTP without downloading the whole file:

```bash
AWS_NO_SIGN_REQUEST=YES ogr2ogr -f Parquet gaul24_a2_SYR_LKA_IRQ.parquet -where "iso3_code IN ('SYR','LKA','IRQ')" \
  '/vsicurl/https://digital-atlas.s3.amazonaws.com/domain=boundaries/type=admin/source=gaul2024/region=global/processing=raw/level=adm2/gaul_a2.parquet'
.venv/bin/python chirps_admin.py SYR --out out/ --boundaries gaul24_a2_SYR_LKA_IRQ.parquet
```

(The Hub-wide boundary standard — GAUL vs World Bank vs geoBoundaries — is still open.)
