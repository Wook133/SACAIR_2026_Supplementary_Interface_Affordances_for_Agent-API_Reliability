# Aggregate results

The following tables are calculated directly from the per-trial CSVs in `results/`. A trial is classified as `full` when every applicable scoring assertion for its scenario holds; these assertions are defined under `scenarios/`. Total tokens are the sum of input and output tokens reported in the provider's usage telemetry.

Results are reported separately by batch because `AF_111` is the shared baseline in three batches with different sample sizes. Pooling these observations would change the manuscript's contrasts.

## ArchiveFlow, Claude Sonnet 4.6, temperature 1.0

Source: `results/archiveflow_sonnet.csv` (1080 trials)

**Batch `20260711_174927_archiveflow_cycle3_temp10`**

Cycle-2/3 cells (AF_111, AF_F, AF_FO, AF_FX), n=30 per condition-scenario cell

| Condition | n | full | full % | mean tool calls | mean total tokens |
|---|---:|---:|---:|---:|---:|
| `AF_111` | 120 | 120 | 100.0% | 6.23 | 9,294 |
| `AF_F` | 120 | 120 | 100.0% | 4.20 | 10,089 |
| `AF_FO` | 120 | 118 | 98.3% | 1.12 | 6,795 |
| `AF_FX` | 120 | 120 | 100.0% | 1.00 | 5,122 |

**Batch `20260711_224255_archiveflow_sonnet_temp10`**

2x2x2 factorial (AF_000-AF_111), n=15 per condition-scenario cell

| Condition | n | full | full % | mean tool calls | mean total tokens |
|---|---:|---:|---:|---:|---:|
| `AF_000` | 60 | 0 | 0.0% | 0.40 | 2,232 |
| `AF_001` | 60 | 0 | 0.0% | 0.00 | 1,477 |
| `AF_010` | 60 | 2 | 3.3% | 1.33 | 4,674 |
| `AF_011` | 60 | 2 | 3.3% | 1.60 | 5,704 |
| `AF_100` | 60 | 60 | 100.0% | 6.50 | 8,846 |
| `AF_101` | 60 | 60 | 100.0% | 6.27 | 9,350 |
| `AF_110` | 60 | 60 | 100.0% | 6.60 | 9,182 |
| `AF_111` | 60 | 60 | 100.0% | 6.25 | 9,266 |

**Batch `20260712_092638_archiveflow_prompt_ablation_temp10`**

Prompt ablation, discovery clause removed, n=10 per condition-scenario cell

| Condition | n | full | full % | mean tool calls | mean total tokens |
|---|---:|---:|---:|---:|---:|
| `AF_111` | 40 | 40 | 100.0% | 6.22 | 9,216 |
| `AF_F` | 40 | 40 | 100.0% | 3.65 | 9,761 |
| `AF_FO` | 40 | 40 | 100.0% | 1.07 | 6,599 |

## ArchiveFlow, Claude Haiku 4.5, temperature 1.0

Source: `results/archiveflow_haiku.csv` (320 trials)

**Batch `20260714_202928_archiveflow_haiku_temp10`**

2x2x2 factorial on Haiku 4.5, n=10 per condition-scenario cell

| Condition | n | full | full % | mean tool calls | mean total tokens |
|---|---:|---:|---:|---:|---:|
| `AF_000` | 40 | 0 | 0.0% | 0.70 | 2,537 |
| `AF_001` | 40 | 0 | 0.0% | 0.65 | 2,649 |
| `AF_010` | 40 | 3 | 7.5% | 1.80 | 5,349 |
| `AF_011` | 40 | 1 | 2.5% | 1.18 | 4,007 |
| `AF_100` | 40 | 40 | 100.0% | 6.15 | 8,883 |
| `AF_101` | 40 | 39 | 97.5% | 5.47 | 9,112 |
| `AF_110` | 40 | 35 | 87.5% | 5.33 | 7,828 |
| `AF_111` | 40 | 33 | 82.5% | 4.88 | 7,706 |

## AWS Support, Claude Sonnet 4.6, temperature 1.0

Source: `results/aws_support.csv` (180 trials)

**Batch `20260712_151304_aws_support_temp10`**

Conditions A/B/F across A1-A4 and C2-C3, n=10 per condition-scenario cell

| Condition | n | full | full % | mean tool calls | mean total tokens |
|---|---:|---:|---:|---:|---:|
| `A` | 60 | 21 | 35.0% | 4.62 | 21,873 |
| `B` | 60 | 60 | 100.0% | 3.75 | 35,261 |
| `F` | 60 | 60 | 100.0% | 2.17 | 18,355 |

**Case creation on the mutation scenarios (A1-A4)**

The B-versus-A contrast reported in the manuscript uses case creation across scenarios A1-A4.

| Condition | mutation trials | cases created | rate |
|---|---:|---:|---:|
| `A` | 40 | 21 | 52.5% |
| `B` | 40 | 40 | 100.0% |
| `F` | 40 | 40 | 100.0% |
