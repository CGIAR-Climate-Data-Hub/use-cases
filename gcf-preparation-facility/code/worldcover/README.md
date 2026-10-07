# WorldCover → admin-level land cover (derive-then-host product)

`worldcover_admin.py` turns the 10 m ESA WorldCover maps into the admin-level tables the Hub
will host, straight from the public S3 COGs — no mirror of the 10 m rasters. One run per country
emits, for adm0 / adm1 / adm2 (GAUL 2024, the Atlas analysis-ready boundaries):

| file | content | consumer |
| --- | --- | --- |
| `worldcover_admin_area_<ISO3>` | year (2020 v100, 2021 v200) × class → `area_ha`, `share` | GCF Theme 6 activity data (AFOLU areas for EX-ACT / IPCC factors) |
| `worldcover_admin_change_<ISO3>` | class-2020 × class-2021 → `area_ha` (transition matrix) | land-use-change baseline — **flag, see caveat** |
| `worldcover_admin_cropland_<ISO3>` | year → `cropland_ha`, `cropland_share` (class 40) | AgWise cropland fraction (sibling product, same run) |
| `worldcover_admin_<ISO3>.json` | inputs, method, classes, licences, caveats, run stats | the metadata record's provenance block |

## Run

```bash
python3 -m venv .venv && .venv/bin/pip install rasterio numpy pandas pyarrow shapely
.venv/bin/python worldcover_admin.py TGO --out out/            # downloads the adm2 parquet (91 MB) once
.venv/bin/python worldcover_admin.py KEN --out out/ --boundaries gaul24_a2_africa.parquet
```

Togo (4 tiles, ~5.7 Mha) runs in a few minutes on a laptop over HTTP; larger countries scale
with area. Reads are anonymous (`AWS_NO_SIGN_REQUEST`), windowed 2048×2048, retried.

## Method

adm2 polygons are rasterised on the WorldCover grid (1/12000°) per window, pixel → the polygon
containing its centre (`all_touched=False`); pixel area = R²·Δlat·Δlon·cos(lat) in ha; the
2020 and 2021 tiles share one grid, so transitions are per pixel. adm1/adm0 are sums over GAUL
codes, not dissolved geometries. No-data (0) is kept as class 0 so areas reconcile.

## Caveats (also written to the sidecar)

- **v100 (2020) vs v200 (2021) differ in algorithm**: ESA states changes between the two maps
  contain method change as well as real change. The change table is published for
  land-use-change *baselines*, `not_recommended_for: trend claims`.
- Centre-pixel attribution: a 10 m boundary pixel goes to one unit; sums equal the rasterised
  country, not the vector area.
- Boundaries are GAUL 2024 (Atlas). The Hub-wide boundary standard (GAUL vs World Bank vs
  geoBoundaries) is still an open decision — rerun if it changes.

Licence: WorldCover CC BY 4.0 (v100 DOI 10.5281/zenodo.5571936, v200 DOI 10.5281/zenodo.7254221).
