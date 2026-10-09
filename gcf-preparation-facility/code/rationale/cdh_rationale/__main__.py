"""Climate-rationale prototype: Hub data → labelled, citable fragments per proposal section.

    python -m cdh_rationale TGO --federated ../federated/out --worldcover ../worldcover/out --out out

Reads `data/rationale-map.yaml` (section → datasets), the federated pulls, the WorldCover admin
products and the Atlas `haz_freq` table, and writes:
  rationale_<ISO3>.json      every fragment with values + source_citation
  rationale_<ISO3>.md        fragments grouped by section with numbered sources (fund-neutral);
                             GCF CN/FP codes shown per section from the map
  rationale_<ISO3>_coverage.csv   section × fragment_type counts and gaps — what the rationale can and cannot say yet
Nothing is authored beyond the fragments; narrative stays with the proposal writer.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import sys
from pathlib import Path

import pandas as pd

from . import fragments
from .loaders import load_federated, load_haz_freq, load_map, load_rainfall, load_worldcover

log = logging.getLogger("cdh_rationale")


def render_md(iso3: str, m: dict, frags: list[dict]) -> str:
    srcs, idx = [], {}

    def ref(c):
        key = (c.get("dataset"), c.get("url"))
        if key not in idx:
            idx[key] = len(srcs) + 1
            srcs.append(c)
        return idx[key]

    lines = [f"# Climate-rationale fragments — {iso3}", "",
             f"Generated {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%MZ} by `cdh_rationale` from Hub-catalogued or queued sources only. "
             "Each statement cites the exact request/object it came from; GAP lines mark what the data cannot yet say. "
             "Fund-neutral: the GCF Concept Note / Funding Proposal codes are shown per section from `rationale-map.yaml`.", ""]
    for sec in m["sections"]:
        sf = [f for f in frags if f["section"] == sec["id"]]
        sv = sec.get("serves", {})
        lines += [f"## {sec['id']} · {sec['theme']}", "",
                  f"*Serves:* CN {', '.join(sv.get('cn', [])) or '—'} · FP {', '.join(sv.get('fp', [])) or '—'}  ", f"*Question:* {sec.get('question', '')}", ""]
        for f in sf:
            if f["fragment_type"] == "gap":
                lines.append(f"- ⚠ {f['text']}")
            else:
                n = ref(f["source_citation"])
                lvl = "" if f["admin_level"] in (0, None) else f" (adm{f['admin_level']})"
                lines.append(f"- {f['text']}{lvl} [^{n}]")
        lines.append("")
    lines += ["## Sources", ""]
    for i, c in enumerate(srcs, 1):
        lines.append(f"[^{i}]: {c.get('dataset')} — {c.get('indicator_id') or ''} {c.get('period') or ''} · {c.get('licence') or ''} · "
                     f"retrieved {c.get('retrieved_at') or ''} · {c.get('url') or ''}")
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="cdh_rationale")
    ap.add_argument("iso3")
    ap.add_argument("--federated", help="directory with cdh_federated outputs (<source>_<ISO3>.parquet)")
    ap.add_argument("--worldcover", help="directory with worldcover_admin_*_<ISO3>.parquet")
    ap.add_argument("--rainfall", help="directory with chirps_admin_*_<ISO3>.parquet (code/rainfall)")
    ap.add_argument("--map", help="rationale-map.yaml (default: repo data/rationale-map.yaml)")
    ap.add_argument("--out", default="out")
    ap.add_argument("--no-remote", action="store_true", help="skip the Atlas haz_freq S3 query")
    ap.add_argument("--subnational", action="store_true", help="also emit adm1 fragments where inputs allow")
    ap.add_argument("--year", type=int, default=dt.date.today().year - 1,
                    help="last year treated as actual/estimate in actual-vs-projection splits (default: last year)")
    ap.add_argument("--all-periods", action="store_true", help="Section 2: also emit 2081-2100 (default 2041-2060 only)")
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if a.verbose else logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    iso3 = a.iso3.upper()
    m = load_map(a.map)
    ctx = {"iso3": iso3, "fed": load_federated(a.federated, iso3), "worldcover": load_worldcover(a.worldcover, iso3),
           "rainfall": load_rainfall(a.rainfall, iso3),
           "haz_freq": load_haz_freq(iso3, remote=not a.no_remote), "subnational": a.subnational, "year": a.year,
           "all_periods": a.all_periods,
           "now": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()}
    frags = []
    for sec in m["sections"]:
        b = fragments.BUILDERS.get(sec["id"])
        if not b:
            continue
        try:
            frags.extend(b(sec, ctx))
        except Exception as e:  # noqa: BLE001
            log.error("section %s failed: %s", sec["id"], e)
            frags.append(fragments.gap(sec, f"builder error: {e.__class__.__name__}: {e}", "fix the builder; nothing emitted"))
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    (out / f"rationale_{iso3}.json").write_text(json.dumps({"iso3": iso3, "generated_at": ctx["now"], "map_version": m.get("version"),
                                                           "fragments": frags}, indent=2, ensure_ascii=False, default=str))
    (out / f"rationale_{iso3}.md").write_text(render_md(iso3, m, frags))
    cov = pd.DataFrame([{"section": f["section"], "theme": f["theme"], "fragment_type": f["fragment_type"]} for f in frags])
    cov = cov.groupby(["section", "theme", "fragment_type"]).size().reset_index(name="n")
    cov.to_csv(out / f"rationale_{iso3}_coverage.csv", index=False)
    n_gap = sum(f["fragment_type"] == "gap" for f in frags)
    log.info("%d fragments (%d gaps) → %s", len(frags), n_gap, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
