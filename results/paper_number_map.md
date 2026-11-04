# Map from paper numbers to this supplement

Each row places a value reported in the manuscript beside the value recomputed from the supplied per-trial CSVs. The `Match` column is calculated during bundle generation.

| Paper location and quantity | Paper states | Recomputed here | Match |
|---|---|---|:--:|
| Sec. 6, discovery main effect (Sonnet), D=1 | 240/240 | 240/240 | yes |
| Sec. 6, discovery main effect (Sonnet), D=0 | 4/240 | 4/240 | yes |
| Sec. 8, discovery main effect (Haiku), D=1 | 147/160 (91.9%) | 147/160 (91.9%) | yes |
| Sec. 8, discovery main effect (Haiku), D=0 | 4/160 (2.5%) | 4/160 (2.5%) | yes |
| Sec. 7.2, AF_FO full scenario success | 118/120 | 118/120 | yes |
| Sec. 7.2, AF_111 full scenario success | 120/120 | 120/120 | yes |
| Sec. 7.2, AF_FO mean tool calls | 1.12 | 1.12 | yes |
| Sec. 7.2, AF_111 mean tool calls | 6.23 | 6.23 | yes |
| Sec. 7.2, AF_FO mean total tokens | 6,795 | 6,795 | yes |
| Sec. 7.2, AF_111 mean total tokens | 9,294 | 9,294 | yes |
| Sec. 7.1, AF_F mean total tokens | 10,089 | 10,089 | yes |
| Sec. 5.1, AWS Condition B case creation (A1-A4) | 40/40 | 40/40 | yes |
| Sec. 5.1, AWS Condition A case creation (A1-A4) | 21/40 (52.5%) | 21/40 (52.5%) | yes |
| Sec. 5.2, AWS Condition F mean total tokens | 18,355 | 18,355 | yes |
| Sec. 5.2, AWS Condition B mean total tokens | 35,261 | 35,261 | yes |

## Commit-versus-defer on AF4 (Section 7.2)

For AF4, `export_job_created` distinguishes acting on the ambiguous request from asking for confirmation.

| Condition | AF4 trials | acted (export created) | asked |
|---|---:|---:|---:|
| `AF_111` | 30 | 30 | 0 |
| `AF_F` | 30 | 30 | 0 |
| `AF_FO` | 30 | 13 | 17 |
| `AF_FX` | 30 | 0 | 30 |
