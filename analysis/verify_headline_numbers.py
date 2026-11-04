#!/usr/bin/env python
"""Recompute the paper's headline numbers from the CSVs in this supplement.

Standard library only. No arguments, no network, no cloud account:

    python analysis/verify_headline_numbers.py

Prints each headline quantity as printed in the manuscript beside the value
recomputed from results/*.csv, and exits non-zero if any pair disagrees.
"""

import csv
import sys
from pathlib import Path

RESULTS = Path(__file__).resolve().parents[1] / "results"


def load(name):
    with (RESULTS / name).open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def sel(rows, batch=None, conds=None, scens=None):
    out = rows
    if batch:
        out = [r for r in out if batch in r["batch"]]
    if conds:
        out = [r for r in out if r["condition_code"] in conds]
    if scens:
        out = [r for r in out if r["scenario_id"] in scens]
    return out


def full(rows):
    return sum(1 for r in rows if r["success_level"] == "full"), len(rows)


def mean(rows, key):
    if key == "tokens":
        v = [float(r["input_tokens"] or 0) + float(r["output_tokens"] or 0) for r in rows]
    else:
        v = [float(r[key] or 0) for r in rows]
    return sum(v) / len(v) if v else float("nan")


def truthy(v):
    return str(v).strip().lower() in {"1", "true", "yes"}


def main():
    af = load("archiveflow_sonnet.csv")
    hk = load("archiveflow_haiku.csv")
    aws = load("aws_support.csv")

    fac = sel(af, "sonnet_temp10")
    d1 = [r for r in fac if r["condition_code"][3] == "1"]
    d0 = [r for r in fac if r["condition_code"][3] == "0"]
    h1 = [r for r in hk if r["condition_code"][3] == "1"]
    h0 = [r for r in hk if r["condition_code"][3] == "0"]
    fo = sel(af, "cycle3_temp10", {"AF_FO"})
    b1 = sel(af, "cycle3_temp10", {"AF_111"})
    ff = sel(af, "cycle3_temp10", {"AF_F"})
    muts = {"A1", "A2", "A3", "A4"}

    def created(c):
        rs = sel(aws, None, {c}, muts)
        return sum(1 for r in rs if truthy(r["case_created"])), len(rs)

    checks = [
        ("discovery D=1 full (Sonnet)", "240/240", "%d/%d" % full(d1)),
        ("discovery D=0 full (Sonnet)", "4/240", "%d/%d" % full(d0)),
        ("discovery D=1 full (Haiku)", "147/160", "%d/%d" % full(h1)),
        ("discovery D=0 full (Haiku)", "4/160", "%d/%d" % full(h0)),
        ("AF_FO full", "118/120", "%d/%d" % full(fo)),
        ("AF_111 full", "120/120", "%d/%d" % full(b1)),
        ("AF_FO mean tool calls", "1.12", "%.2f" % mean(fo, "n_tool_calls")),
        ("AF_111 mean tool calls", "6.23", "%.2f" % mean(b1, "n_tool_calls")),
        ("AF_FO mean tokens", "6,795", "{:,.0f}".format(mean(fo, "tokens"))),
        ("AF_111 mean tokens", "9,294", "{:,.0f}".format(mean(b1, "tokens"))),
        ("AF_F mean tokens", "10,089", "{:,.0f}".format(mean(ff, "tokens"))),
        ("AWS B cases created (A1-A4)", "40/40", "%d/%d" % created("B")),
        ("AWS A cases created (A1-A4)", "21/40", "%d/%d" % created("A")),
        ("AWS F mean tokens", "18,355", "{:,.0f}".format(mean(sel(aws, None, {"F"}), "tokens"))),
        ("AWS B mean tokens", "35,261", "{:,.0f}".format(mean(sel(aws, None, {"B"}), "tokens"))),
    ]

    bad = 0
    print("%-34s %-12s %-12s %s" % ("quantity", "paper", "recomputed", "ok"))
    print("-" * 72)
    for label, paper, got in checks:
        ok = paper == got
        bad += 0 if ok else 1
        print("%-34s %-12s %-12s %s" % (label, paper, got, "yes" if ok else "NO"))

    print()
    print("AF4 commit-versus-defer (export_job_created):")
    for c in ("AF_111", "AF_F", "AF_FO", "AF_FX"):
        rs = sel(af, "cycle3_temp10", {c}, {"AF4"})
        acted = sum(1 for r in rs if truthy(r["export_job_created"]))
        print("  %-7s acted %2d / %d, asked %2d" % (c, acted, len(rs), len(rs) - acted))

    print()
    print("%d of %d headline numbers reproduce." % (len(checks) - bad, len(checks)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
