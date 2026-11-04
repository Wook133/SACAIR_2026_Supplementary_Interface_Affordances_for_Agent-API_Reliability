# Reproducing the reported results

The tables in `results/` and `additional_tables/` are derived from the three per-trial CSVs in `results/`. Their calculation requires no additional data, network access, or cloud account.

## Verification scripts

The following commands, run from the root of this folder, reproduce the reported values:

```text
python analysis/verify_headline_numbers.py
python analysis/statistical_tests.py
```

The headline-number script uses only the Python standard library. The statistical script requires NumPy and SciPy, consistent with the manuscript's analysis environment. It recomputes the Wilson intervals, Fisher tests, risk ratios, Mann-Whitney tests, Cliff's delta, bootstrap intervals, Holm adjustments, seeded permutation test, and both interval criteria directly from the supplied CSVs.

## Files

| File | Trials | Batches it contains |
|---|---:|---|
| `results/archiveflow_sonnet.csv` | 1080 | factorial, cycle-2/3, prompt ablation |
| `results/archiveflow_haiku.csv` | 320 | factorial on the smaller model |
| `results/aws_support.csv` | 180 | conditions A/B/F |

Rows must be grouped by `batch` before aggregation. `AF_111` is the shared baseline in three batches with different sample sizes, and pooling these rows would change the manuscript's contrasts.

## Column dictionary

| Column | Meaning |
|---|---|
| `batch` | Which experimental batch the trial belongs to |
| `trial_id` | Unique trial identifier |
| `condition_code` | Interface condition (see `conditions/`) |
| `scenario_id` | Task scenario (see `scenarios/`) |
| `run_num` | Replicate index within the condition-scenario cell |
| `success_level` | `full` only if every scored assertion for that scenario held |
| `n_tool_calls` | Tool invocations made during the trial |
| `input_tokens`, `output_tokens` | Provider usage telemetry; the paper's cost metric is their sum |
| `duration_s` | Wall-clock trial duration |
| `cost_usd` | Provider cost recorded for the trial; included for completeness but not used by the manuscript's headline comparisons |
| `tool_call_sequence` | Ordered tool names, for checking workflow ordering claims |
| `assert_*` | Individual assertion outcomes behind `success_level` |
| `sent_*` | Canonical code the model actually submitted, for checking fabrication claims |
| `case_created`, `export_job_created`, `digitization_request_created` | Whether the mutation occurred (1/0) |

## Illustrative calculations

**Discovery main effect (Sec. 6).** In `archiveflow_sonnet.csv`, restrict to the factorial batch and split on the first digit of `condition_code` after `AF_`: `AF_1**` is discovery-enabled, `AF_0**` is not. Count `success_level == full`. This gives 240/240 against 4/240.

**AF_FO efficiency (Sec. 7.2).** Restrict to the cycle-2/3 batch. Compare mean `n_tool_calls` and mean `input_tokens + output_tokens` for `AF_FO` against `AF_111`. The resulting means are 1.12 against 6.23 calls and 6,795 against 9,294 tokens.

The mean below one tool call arises because AF3 can be answered from the inline catalogue, whilst deferral on AF4 is a correct outcome; neither requires a tool call. Successful trials on the mutation scenarios AF1 and AF2 always contain at least one call, as shown in `additional_tables/complete_results.md`.

**Commit versus defer (Sec. 7.2).** Restrict to the cycle-2/3 batch and scenario `AF4`, then read `export_job_created`. AF_111 and AF_F act on all 30 trials, AF_FO acts on 13 of 30, and AF_FX acts on none.

## Scope of reproduction

This supplement supports recomputation of the reported results from the recorded trials. Full trial re-execution requires cloud credentials, a live AWS Support account, and the digitisation service used for the second domain; it is therefore reserved for the post-acceptance reproducibility package.
