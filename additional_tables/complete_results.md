# Complete per-condition, per-scenario breakdown

These tables provide the scenario-level decomposition of `results/aggregate_results.md`. They also show the AF4 commit-versus-defer split: under AF_FO, trials that ask for confirmation can complete correctly without a tool call, which contributes to a pooled mean below one call per trial.

## ArchiveFlow, Claude Sonnet 4.6, temperature 1.0

**Batch `20260711_174927_archiveflow_cycle3_temp10`** -- Cycle-2/3 cells (AF_111, AF_F, AF_FO, AF_FX), n=30 per condition-scenario cell

| Condition | Scenario | n | full | mean tool calls | mean total tokens |
|---|---|---:|---:|---:|---:|
| `AF_111` | AF1 | 30 | 30 | 6.00 | 8,152 |
| `AF_111` | AF2 | 30 | 30 | 8.00 | 14,659 |
| `AF_111` | AF3 | 30 | 30 | 4.00 | 4,790 |
| `AF_111` | AF4 | 30 | 30 | 6.93 | 9,576 |
| `AF_F` | AF1 | 30 | 30 | 5.67 | 10,199 |
| `AF_F` | AF2 | 30 | 30 | 4.13 | 14,146 |
| `AF_F` | AF3 | 30 | 30 | 1.00 | 5,472 |
| `AF_F` | AF4 | 30 | 30 | 6.00 | 10,538 |
| `AF_FO` | AF1 | 30 | 30 | 1.00 | 5,955 |
| `AF_FO` | AF2 | 30 | 30 | 3.00 | 13,776 |
| `AF_FO` | AF3 | 30 | 30 | 0.07 | 3,159 |
| `AF_FO` | AF4 | 30 | 28 | 0.43 | 4,291 |
| `AF_FX` | AF1 | 30 | 30 | 1.00 | 4,751 |
| `AF_FX` | AF2 | 30 | 30 | 3.00 | 11,234 |
| `AF_FX` | AF3 | 30 | 30 | 0.00 | 2,310 |
| `AF_FX` | AF4 | 30 | 30 | 0.00 | 2,193 |

**Batch `20260711_224255_archiveflow_sonnet_temp10`** -- 2x2x2 factorial (AF_000-AF_111), n=15 per condition-scenario cell

| Condition | Scenario | n | full | mean tool calls | mean total tokens |
|---|---|---:|---:|---:|---:|
| `AF_000` | AF1 | 15 | 0 | 0.00 | 1,251 |
| `AF_000` | AF2 | 15 | 0 | 1.53 | 4,704 |
| `AF_000` | AF3 | 15 | 0 | 0.00 | 1,606 |
| `AF_000` | AF4 | 15 | 0 | 0.07 | 1,368 |
| `AF_001` | AF1 | 15 | 0 | 0.00 | 1,419 |
| `AF_001` | AF2 | 15 | 0 | 0.00 | 1,520 |
| `AF_001` | AF3 | 15 | 0 | 0.00 | 1,590 |
| `AF_001` | AF4 | 15 | 0 | 0.00 | 1,380 |
| `AF_010` | AF1 | 15 | 0 | 0.00 | 1,262 |
| `AF_010` | AF2 | 15 | 2 | 5.13 | 14,249 |
| `AF_010` | AF3 | 15 | 0 | 0.00 | 1,615 |
| `AF_010` | AF4 | 15 | 0 | 0.20 | 1,570 |
| `AF_011` | AF1 | 15 | 0 | 0.20 | 1,795 |
| `AF_011` | AF2 | 15 | 2 | 6.13 | 17,944 |
| `AF_011` | AF3 | 15 | 0 | 0.00 | 1,589 |
| `AF_011` | AF4 | 15 | 0 | 0.07 | 1,487 |
| `AF_100` | AF1 | 15 | 15 | 5.87 | 7,585 |
| `AF_100` | AF2 | 15 | 15 | 8.00 | 13,015 |
| `AF_100` | AF3 | 15 | 15 | 5.53 | 4,908 |
| `AF_100` | AF4 | 15 | 15 | 6.60 | 9,877 |
| `AF_101` | AF1 | 15 | 15 | 6.00 | 8,100 |
| `AF_101` | AF2 | 15 | 15 | 8.00 | 14,383 |
| `AF_101` | AF3 | 15 | 15 | 4.07 | 4,761 |
| `AF_101` | AF4 | 15 | 15 | 7.00 | 10,158 |
| `AF_110` | AF1 | 15 | 15 | 6.00 | 7,731 |
| `AF_110` | AF2 | 15 | 15 | 8.00 | 13,138 |
| `AF_110` | AF3 | 15 | 15 | 5.47 | 4,922 |
| `AF_110` | AF4 | 15 | 15 | 6.93 | 10,937 |
| `AF_111` | AF1 | 15 | 15 | 6.00 | 8,157 |
| `AF_111` | AF2 | 15 | 15 | 8.00 | 14,765 |
| `AF_111` | AF3 | 15 | 15 | 4.00 | 4,793 |
| `AF_111` | AF4 | 15 | 15 | 7.00 | 9,348 |

**Batch `20260712_092638_archiveflow_prompt_ablation_temp10`** -- Prompt ablation, discovery clause removed, n=10 per condition-scenario cell

| Condition | Scenario | n | full | mean tool calls | mean total tokens |
|---|---|---:|---:|---:|---:|
| `AF_111` | AF1 | 10 | 10 | 6.00 | 8,112 |
| `AF_111` | AF2 | 10 | 10 | 8.00 | 13,420 |
| `AF_111` | AF3 | 10 | 10 | 3.90 | 4,739 |
| `AF_111` | AF4 | 10 | 10 | 7.00 | 10,594 |
| `AF_F` | AF1 | 10 | 10 | 4.30 | 9,555 |
| `AF_F` | AF2 | 10 | 10 | 4.00 | 13,892 |
| `AF_F` | AF3 | 10 | 10 | 1.00 | 5,439 |
| `AF_F` | AF4 | 10 | 10 | 5.30 | 10,159 |
| `AF_FO` | AF1 | 10 | 10 | 1.00 | 5,911 |
| `AF_FO` | AF2 | 10 | 10 | 3.00 | 13,720 |
| `AF_FO` | AF3 | 10 | 10 | 0.00 | 2,951 |
| `AF_FO` | AF4 | 10 | 10 | 0.30 | 3,815 |

## ArchiveFlow, Claude Haiku 4.5, temperature 1.0

**Batch `20260714_202928_archiveflow_haiku_temp10`** -- 2x2x2 factorial on Haiku 4.5, n=10 per condition-scenario cell

| Condition | Scenario | n | full | mean tool calls | mean total tokens |
|---|---|---:|---:|---:|---:|
| `AF_000` | AF1 | 10 | 0 | 0.00 | 1,259 |
| `AF_000` | AF2 | 10 | 0 | 1.80 | 4,809 |
| `AF_000` | AF3 | 10 | 0 | 0.00 | 1,392 |
| `AF_000` | AF4 | 10 | 0 | 1.00 | 2,686 |
| `AF_001` | AF1 | 10 | 0 | 0.00 | 1,417 |
| `AF_001` | AF2 | 10 | 0 | 1.60 | 4,770 |
| `AF_001` | AF3 | 10 | 0 | 0.00 | 1,413 |
| `AF_001` | AF4 | 10 | 0 | 1.00 | 2,995 |
| `AF_010` | AF1 | 10 | 0 | 1.00 | 2,794 |
| `AF_010` | AF2 | 10 | 3 | 5.20 | 14,440 |
| `AF_010` | AF3 | 10 | 0 | 0.00 | 1,442 |
| `AF_010` | AF4 | 10 | 0 | 1.00 | 2,719 |
| `AF_011` | AF1 | 10 | 0 | 0.30 | 1,914 |
| `AF_011` | AF2 | 10 | 1 | 3.40 | 9,664 |
| `AF_011` | AF3 | 10 | 0 | 0.00 | 1,439 |
| `AF_011` | AF4 | 10 | 0 | 1.00 | 3,011 |
| `AF_100` | AF1 | 10 | 10 | 5.90 | 8,139 |
| `AF_100` | AF2 | 10 | 10 | 8.00 | 15,107 |
| `AF_100` | AF3 | 10 | 10 | 4.50 | 4,407 |
| `AF_100` | AF4 | 10 | 10 | 6.20 | 7,879 |
| `AF_101` | AF1 | 10 | 10 | 5.30 | 8,040 |
| `AF_101` | AF2 | 10 | 9 | 7.90 | 15,562 |
| `AF_101` | AF3 | 10 | 10 | 2.50 | 4,212 |
| `AF_101` | AF4 | 10 | 10 | 6.20 | 8,634 |
| `AF_110` | AF1 | 10 | 9 | 5.80 | 7,678 |
| `AF_110` | AF2 | 10 | 6 | 7.00 | 11,957 |
| `AF_110` | AF3 | 10 | 10 | 2.20 | 3,965 |
| `AF_110` | AF4 | 10 | 10 | 6.30 | 7,714 |
| `AF_111` | AF1 | 10 | 8 | 5.30 | 7,535 |
| `AF_111` | AF2 | 10 | 5 | 6.40 | 12,799 |
| `AF_111` | AF3 | 10 | 10 | 2.20 | 4,194 |
| `AF_111` | AF4 | 10 | 10 | 5.60 | 6,298 |

## AWS Support, Claude Sonnet 4.6, temperature 1.0

**Batch `20260712_151304_aws_support_temp10`** -- Conditions A/B/F across A1-A4 and C2-C3, n=10 per condition-scenario cell

| Condition | Scenario | n | full | mean tool calls | mean total tokens |
|---|---|---:|---:|---:|---:|
| `A` | A1 | 10 | 2 | 6.20 | 28,708 |
| `A` | A2 | 10 | 1 | 4.90 | 21,680 |
| `A` | A3 | 10 | 10 | 3.80 | 18,249 |
| `A` | A4 | 10 | 8 | 6.20 | 33,257 |
| `A` | C2 | 10 | 0 | 2.60 | 14,258 |
| `A` | C3 | 10 | 0 | 4.00 | 15,087 |
| `B` | A1 | 10 | 10 | 4.10 | 115,952 |
| `B` | A2 | 10 | 10 | 3.00 | 15,880 |
| `B` | A3 | 10 | 10 | 3.30 | 18,479 |
| `B` | A4 | 10 | 10 | 4.20 | 19,374 |
| `B` | C2 | 10 | 10 | 3.00 | 21,071 |
| `B` | C3 | 10 | 10 | 4.90 | 20,808 |
| `F` | A1 | 10 | 10 | 2.60 | 22,079 |
| `F` | A2 | 10 | 10 | 1.00 | 11,727 |
| `F` | A3 | 10 | 10 | 3.10 | 26,537 |
| `F` | A4 | 10 | 10 | 2.00 | 19,882 |
| `F` | C2 | 10 | 10 | 2.20 | 17,523 |
| `F` | C3 | 10 | 10 | 2.10 | 12,383 |
