#!/usr/bin/env python
"""Recompute the manuscript's confirmatory statistics from shipped CSVs.

Run from anywhere with:

    python analysis/statistical_tests.py

Requires NumPy and SciPy. No repository checkout, network access, cloud
account, raw transcript, or experiment configuration is required. The script
prints every declared confirmatory family and exits non-zero if a recomputed
value differs from the validated analysis values used by the manuscript.
"""

from __future__ import annotations

import csv
import math
import random
import sys
from pathlib import Path

import numpy as np
from scipy.stats import bootstrap, fisher_exact, mannwhitneyu


RESULTS = Path(__file__).resolve().parents[1] / "results"
AF_FACTORIAL = "20260711_224255_archiveflow_sonnet_temp10"
AF_CYCLE3 = "20260711_174927_archiveflow_cycle3_temp10"
AF_PROMPT = "20260712_092638_archiveflow_prompt_ablation_temp10"
AF_HAIKU = "20260714_202928_archiveflow_haiku_temp10"
AWS_TEMP10 = "20260712_151304_aws_support_temp10"
N_RESAMPLES = 10_000
SEED = 42


def load(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def select(
    rows: list[dict[str, str]],
    *,
    batch: str | None = None,
    conditions: set[str] | None = None,
    scenarios: set[str] | None = None,
) -> list[dict[str, str]]:
    return [
        row
        for row in rows
        if (batch is None or row["batch"] == batch)
        and (conditions is None or row["condition_code"] in conditions)
        and (scenarios is None or row["scenario_id"] in scenarios)
    ]


def truthy(value: object) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes"}


def full_values(rows: list[dict[str, str]]) -> list[bool]:
    return [row["success_level"] == "full" for row in rows]


def numeric(rows: list[dict[str, str]], field: str) -> list[float]:
    if field == "total_tokens":
        return [float(row["input_tokens"] or 0) + float(row["output_tokens"] or 0) for row in rows]
    return [float(row[field] or 0) for row in rows]


def factorial_flag(row: dict[str, str], index: int) -> bool:
    bits = row["condition_code"].removeprefix("AF_")
    if len(bits) != 3 or not bits.isdigit():
        raise ValueError(f"not a factorial condition: {row['condition_code']}")
    return bits[index] == "1"


def wilson_ci(successes: int, n: int, z: float = 1.959963984540054) -> tuple[float, float]:
    if n == 0:
        return float("nan"), float("nan")
    p = successes / n
    denominator = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denominator
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denominator
    return max(0.0, centre - half), min(1.0, centre + half)


def risk_ratio(a: int, n_a: int, b: int, n_b: int) -> tuple[float, float, float]:
    """Risk ratio and log-normal CI with Haldane-Anscombe correction."""
    corrected = a == 0 or b == 0 or a == n_a or b == n_b
    if corrected:
        a_c, b_c, n_a_c, n_b_c = a + 0.5, b + 0.5, n_a + 1, n_b + 1
    else:
        a_c, b_c, n_a_c, n_b_c = float(a), float(b), float(n_a), float(n_b)
    rr = (a_c / n_a_c) / (b_c / n_b_c)
    se = math.sqrt(1 / a_c - 1 / n_a_c + 1 / b_c - 1 / n_b_c)
    log_rr = math.log(rr)
    return rr, math.exp(log_rr - 1.96 * se), math.exp(log_rr + 1.96 * se)


def cliffs_delta(x: list[float], y: list[float]) -> float:
    greater = sum(xi > yi for xi in x for yi in y)
    less = sum(xi < yi for xi in x for yi in y)
    return (greater - less) / (len(x) * len(y))


def bootstrap_mean_ci(values: list[float]) -> tuple[float, float]:
    array = np.asarray(values, dtype=float)
    result = bootstrap(
        (array,),
        statistic=np.mean,
        n_resamples=N_RESAMPLES,
        confidence_level=0.95,
        method="BCa",
        random_state=SEED,
    )
    return float(result.confidence_interval.low), float(result.confidence_interval.high)


def bootstrap_diff_ci(x: list[float], y: list[float]) -> tuple[float, float]:
    def difference(a: np.ndarray, b: np.ndarray) -> float:
        return float(np.mean(a) - np.mean(b))

    result = bootstrap(
        (np.asarray(x, dtype=float), np.asarray(y, dtype=float)),
        statistic=difference,
        n_resamples=N_RESAMPLES,
        confidence_level=0.95,
        method="percentile",
        paired=False,
        random_state=SEED,
    )
    return float(result.confidence_interval.low), float(result.confidence_interval.high)


def proportion_result(name: str, a: list[bool], b: list[bool]) -> dict[str, object]:
    a_pass, b_pass = sum(a), sum(b)
    _, p_value = fisher_exact(
        [[a_pass, len(a) - a_pass], [b_pass, len(b) - b_pass]],
        alternative="two-sided",
    )
    rr, rr_low, rr_high = risk_ratio(a_pass, len(a), b_pass, len(b))
    return {
        "name": name,
        "kind": "proportion",
        "a": (a_pass, len(a)),
        "b": (b_pass, len(b)),
        "a_ci": wilson_ci(a_pass, len(a)),
        "b_ci": wilson_ci(b_pass, len(b)),
        "p": float(p_value),
        "rr": rr,
        "rr_ci": (rr_low, rr_high),
    }


def continuous_result(name: str, x: list[float], y: list[float]) -> dict[str, object]:
    test = mannwhitneyu(x, y, alternative="two-sided")
    return {
        "name": name,
        "kind": "continuous",
        "n": (len(x), len(y)),
        "means": (float(np.mean(x)), float(np.mean(y))),
        "mean_cis": (bootstrap_mean_ci(x), bootstrap_mean_ci(y)),
        "mean_diff_ci": bootstrap_diff_ci(x, y),
        "u": float(test.statistic),
        "p": float(test.pvalue),
        "delta": cliffs_delta(x, y),
    }


def apply_holm(results: list[dict[str, object]]) -> None:
    ordered = sorted(results, key=lambda result: float(result["p"]))
    previous = 0.0
    for index, result in enumerate(ordered):
        adjusted = min(float(result["p"]) * (len(ordered) - index), 1.0)
        adjusted = max(previous, adjusted)
        result["holm"] = adjusted
        previous = adjusted


def prompt_interaction_p(
    neutral_fo: list[float],
    original_fo: list[float],
    neutral_f: list[float],
    original_f: list[float],
) -> tuple[float, float]:
    def mean(values: list[float]) -> float:
        return sum(values) / len(values)

    def interaction(fo_n: list[float], fo_o: list[float], f_n: list[float], f_o: list[float]) -> float:
        return (mean(fo_n) - mean(fo_o)) - (mean(f_n) - mean(f_o))

    observed = interaction(neutral_fo, original_fo, neutral_f, original_f)
    rng = random.Random(SEED)
    fo_pool = list(neutral_fo) + list(original_fo)
    f_pool = list(neutral_f) + list(original_f)
    n_fo_neutral, n_f_neutral = len(neutral_fo), len(neutral_f)
    extreme = 0
    for _ in range(N_RESAMPLES):
        rng.shuffle(fo_pool)
        rng.shuffle(f_pool)
        permuted = interaction(
            fo_pool[:n_fo_neutral],
            fo_pool[n_fo_neutral:],
            f_pool[:n_f_neutral],
            f_pool[n_f_neutral:],
        )
        extreme += abs(permuted) >= abs(observed)
    return observed, (extreme + 1) / (N_RESAMPLES + 1)


def fmt_p(value: float) -> str:
    if value < 0.001:
        return f"{value:.6g}"
    return f"{value:.6f}"


def print_family(name: str, results: list[dict[str, object]]) -> None:
    print(f"\n{name} (m={len(results)})")
    for result in results:
        if result["kind"] == "proportion":
            rr_low, rr_high = result["rr_ci"]
            detail = f"RR={result['rr']:.6g} [{rr_low:.6g}, {rr_high:.6g}]"
        else:
            means = result["means"]
            detail = f"means={means[0]:.6g}/{means[1]:.6g}; U={result['u']:.6g}; delta={result['delta']:.6g}"
        print(f"  {result['name']}: p={fmt_p(float(result['p']))}; Holm={fmt_p(float(result['holm']))}; {detail}")


def main() -> int:
    af = load("archiveflow_sonnet.csv")
    haiku = load("archiveflow_haiku.csv")
    aws = load("aws_support.csv")
    mutation_scenarios = {"A1", "A2", "A3", "A4"}

    aws_a = select(aws, batch=AWS_TEMP10, conditions={"A"}, scenarios=mutation_scenarios)
    aws_b_mut = select(aws, batch=AWS_TEMP10, conditions={"B"}, scenarios=mutation_scenarios)
    aws_f_mut = select(aws, batch=AWS_TEMP10, conditions={"F"}, scenarios=mutation_scenarios)
    aws_b = select(aws, batch=AWS_TEMP10, conditions={"B"})
    aws_f = select(aws, batch=AWS_TEMP10, conditions={"F"})
    aws_family = [
        proportion_result("A vs B case creation", [truthy(r["case_created"]) for r in aws_a], [truthy(r["case_created"]) for r in aws_b_mut]),
        proportion_result("F vs B case creation", [truthy(r["case_created"]) for r in aws_f_mut], [truthy(r["case_created"]) for r in aws_b_mut]),
        continuous_result("F vs B total tokens", numeric(aws_f, "total_tokens"), numeric(aws_b, "total_tokens")),
    ]
    apply_holm(aws_family)

    factorial = select(af, batch=AF_FACTORIAL)
    d1 = [r for r in factorial if factorial_flag(r, 0)]
    d0 = [r for r in factorial if not factorial_flag(r, 0)]
    af_main = [proportion_result("Sonnet discovery main effect", full_values(d1), full_values(d0))]
    apply_holm(af_main)

    fo = select(af, batch=AF_CYCLE3, conditions={"AF_FO"})
    f = select(af, batch=AF_CYCLE3, conditions={"AF_F"})
    full = select(af, batch=AF_CYCLE3, conditions={"AF_111"})
    fx_af4 = select(af, batch=AF_CYCLE3, conditions={"AF_FX"}, scenarios={"AF4"})
    fo_af4 = select(af, batch=AF_CYCLE3, conditions={"AF_FO"}, scenarios={"AF4"})
    cycle3 = [
        continuous_result("AF_FO vs AF_111 tool calls", numeric(fo, "n_tool_calls"), numeric(full, "n_tool_calls")),
        continuous_result("AF_FO vs AF_111 total tokens", numeric(fo, "total_tokens"), numeric(full, "total_tokens")),
        continuous_result("AF_F vs AF_111 total tokens", numeric(f, "total_tokens"), numeric(full, "total_tokens")),
        proportion_result("AF_FX vs AF_FO full success on AF4", full_values(fx_af4), full_values(fo_af4)),
    ]
    apply_holm(cycle3)
    equivalence = proportion_result("AF_FO vs AF_111 full success", full_values(fo), full_values(full))
    eq_low, eq_high = equivalence["rr_ci"]
    equivalence_passed = 0.90 <= eq_low and eq_high <= 1.10

    h_d1 = [r for r in haiku if r["batch"] == AF_HAIKU and factorial_flag(r, 0)]
    h_d0 = [r for r in haiku if r["batch"] == AF_HAIKU and not factorial_flag(r, 0)]
    h_af2 = select(haiku, batch=AF_HAIKU, scenarios={"AF2"})
    h_w1 = [truthy(r["assert_attachment_set_used_in_request"]) for r in h_af2 if factorial_flag(r, 2)]
    h_w0 = [truthy(r["assert_attachment_set_used_in_request"]) for r in h_af2 if not factorial_flag(r, 2)]
    haiku_family = [
        proportion_result("Haiku discovery main effect", full_values(h_d1), full_values(h_d0)),
        proportion_result("Haiku workflow docstring on AF2", h_w1, h_w0),
    ]
    apply_holm(haiku_family)

    neutral = select(af, batch=AF_PROMPT, conditions={"AF_F", "AF_FO", "AF_111"})
    original = select(af, batch=AF_CYCLE3, conditions={"AF_F", "AF_FO", "AF_111"})
    neutral_f = select(neutral, conditions={"AF_F"})
    original_f = select(original, conditions={"AF_F"})
    prompt_shift = continuous_result("AF_F neutral vs original tool calls", numeric(neutral_f, "n_tool_calls"), numeric(original_f, "n_tool_calls"))
    observed, interaction_p = prompt_interaction_p(
        numeric(select(neutral, conditions={"AF_FO"}), "n_tool_calls"),
        numeric(select(original, conditions={"AF_FO"}), "n_tool_calls"),
        numeric(neutral_f, "n_tool_calls"),
        numeric(original_f, "n_tool_calls"),
    )
    interaction = {"name": "Prompt-by-description interaction", "kind": "permutation", "p": interaction_p, "observed": observed}
    prompt_family = [prompt_shift, interaction]
    apply_holm(prompt_family)

    neutral_success = full_values(neutral)
    original_success = full_values(original)
    prompt_rr = risk_ratio(sum(neutral_success), len(neutral_success), sum(original_success), len(original_success))
    cells_ok = all(
        sum(full_values(select(neutral, conditions={condition}, scenarios={scenario}))) / len(select(neutral, conditions={condition}, scenarios={scenario}))
        >= sum(full_values(select(original, conditions={condition}, scenarios={scenario}))) / len(select(original, conditions={condition}, scenarios={scenario}))
        for condition in ("AF_F", "AF_FO", "AF_111")
        for scenario in ("AF1", "AF2", "AF3", "AF4")
    )
    # The manuscript uses the complete-CI criterion specified during analysis.
    # Preserve the earlier one-sided/per-cell diagnostic for traceability.
    prompt_interval_passed = 0.90 <= prompt_rr[1] and prompt_rr[2] <= 1.10
    legacy_prompt_gate_passed = prompt_rr[1] >= 0.90 and cells_ok

    print("Confirmatory statistics recomputed from results/*.csv")
    print_family("aws_temp10", aws_family)
    print_family("af_temp10_main", af_main)
    print_family("af_temp10_cycle3", cycle3)
    print_family("haiku_temp10", haiku_family)
    print("\naf_prompt_ablation (m=2)")
    print(f"  {prompt_shift['name']}: p={fmt_p(float(prompt_shift['p']))}; Holm={fmt_p(float(prompt_shift['holm']))}; delta={prompt_shift['delta']:.6g}")
    print(f"  {interaction['name']}: observed={observed:.6g}; permutation p={fmt_p(interaction_p)}; Holm={fmt_p(float(interaction['holm']))}; n={N_RESAMPLES}; seed={SEED}")
    print("\nInterval gates (outside Holm families)")
    print(f"  AF_FO equivalence: RR={equivalence['rr']:.6g} [{eq_low:.6g}, {eq_high:.6g}]; inside [0.90, 1.10]={equivalence_passed}")
    print(f"  Prompt correctness (manuscript criterion): RR={prompt_rr[0]:.6g} [{prompt_rr[1]:.6g}, {prompt_rr[2]:.6g}]; inside [0.90, 1.10]={prompt_interval_passed}")
    print(f"  Legacy prompt non-inferiority diagnostic: lower bound >= 0.90; cells_ok={cells_ok}; passed={legacy_prompt_gate_passed}")

    expected = {
        "aws A/B raw p": (aws_family[0]["p"], 2.2652081427119452e-07),
        "aws A/B Holm p": (aws_family[0]["holm"], 6.795624428135836e-07),
        "aws A/B RR": (aws_family[0]["rr"], 0.5308641975308642),
        "aws F/B tokens raw p": (aws_family[2]["p"], 0.04873749080385425),
        "aws F/B tokens Holm p": (aws_family[2]["holm"], 0.0974749816077085),
        "aws F/B tokens delta": (aws_family[2]["delta"], -0.2088888888888889),
        "sonnet discovery raw p": (af_main[0]["p"], 2.5360399800832823e-135),
        "sonnet discovery RR": (af_main[0]["rr"], 53.44444444444444),
        "cycle3 calls raw p": (cycle3[0]["p"], 4.0716268025365083e-41),
        "cycle3 calls Holm p": (cycle3[0]["holm"], 1.6286507210146033e-40),
        "cycle3 calls delta": (cycle3[0]["delta"], -0.9916666666666667),
        "cycle3 tokens raw p": (cycle3[1]["p"], 1.2195065057015526e-06),
        "cycle3 tokens Holm p": (cycle3[1]["holm"], 3.658519517104658e-06),
        "cycle3 tokens delta": (cycle3[1]["delta"], -0.3625),
        "AF_F regression raw p": (cycle3[2]["p"], 0.0002765660494178273),
        "AF_F regression Holm p": (cycle3[2]["holm"], 0.0005531320988356546),
        "AF_F regression delta": (cycle3[2]["delta"], 0.27166666666666667),
        "AF4 raw p": (cycle3[3]["p"], 0.4915254237288136),
        "equivalence RR": (equivalence["rr"], 0.983402489626556),
        "equivalence RR low": (eq_low, 0.9559512880123304),
        "equivalence RR high": (eq_high, 1.0116419829450918),
        "haiku discovery raw p": (haiku_family[0]["p"], 4.021177306411524e-69),
        "haiku discovery Holm p": (haiku_family[0]["holm"], 8.042354612823048e-69),
        "haiku discovery RR": (haiku_family[0]["rr"], 36.74999999999999),
        "haiku workflow raw p": (haiku_family[1]["p"], 0.4977664009596055),
        "prompt shift raw p": (prompt_shift["p"], 0.041467746663608335),
        "prompt shift Holm p": (prompt_shift["holm"], 0.08293549332721667),
        "prompt shift delta": (prompt_shift["delta"], -0.20333333333333334),
        "prompt interaction": (observed, 0.5000000000000002),
        "prompt interaction raw p": (interaction_p, 0.23397660233976603),
        "prompt gate RR": (prompt_rr[0], 1.0028124531738074),
        "prompt gate RR low": (prompt_rr[1], 0.9885240279470519),
        "prompt gate RR high": (prompt_rr[2], 1.017307407619569),
    }
    failures = []
    for label, (actual, target) in expected.items():
        if not math.isclose(float(actual), target, rel_tol=1e-12, abs_tol=1e-15):
            failures.append(f"{label}: expected {target!r}, got {actual!r}")
    if not equivalence_passed:
        failures.append("AF_FO equivalence gate did not pass")
    if not prompt_interval_passed:
        failures.append("prompt complete-CI correctness criterion did not pass")
    if not legacy_prompt_gate_passed:
        failures.append("legacy prompt non-inferiority diagnostic did not pass")

    print(f"\nValidated values: {len(expected) - len(failures)}/{len(expected)} numeric checks match; interval criteria and legacy diagnostic pass={not failures}")
    if failures:
        for failure in failures:
            print(f"  FAIL {failure}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
