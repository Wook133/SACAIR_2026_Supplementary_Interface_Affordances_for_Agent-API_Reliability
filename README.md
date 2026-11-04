# Supplementary material: Interface Affordances for Agent–API Reliability

**John de Villiers** — Independent Researcher, Cape Town, South Africa.

Companion artifact for *Interface Affordances for Agent–API Reliability: A Design Science Study of Model Context Protocol Servers*, accepted for the SACAIR 2026 Springer CCIS volume. Final proceedings bibliographic details and DOI will be added when available. Citation metadata for this artifact are in `CITATION.cff`.

Repository: <https://github.com/Wook133/SACAIR_2026_Supplementary_Interface_Affordances_for_Agent-API_Reliability>

The research was conducted independently, in a personal capacity. This artifact is not an AWS publication or endorsement.

This supplement accompanies the camera-ready paper, *Interface Affordances for Agent-API Reliability: A Design Science Study of Model Context Protocol Servers*. It provides scenario definitions, evaluated interface conditions, confirmatory trial records, and executable analysis supporting the reported results. The trial data are unchanged from the reviewed supplement; the documentation and correctness-criterion reporting have been aligned with the revised manuscript. This is a curated evidence bundle, not a complete environment for rerunning the hosted experiments.

## Data minimisation

The bundle omits private revision history, cloud-account identifiers, ARNs, credentials, absolute machine paths and raw customer/support-case content. The author identity, companion-repository URL and upstream attribution are intentional public metadata. An automated scan retains narrowly scoped exceptions for those documented repository URLs and rejects other detected repository/account identifiers.

## Contents and manuscript mapping

| Path | Contents | Paper |
|---|---|---|
| `scenarios/aws_support_scenarios.md` | The six AWS Support tasks: verbatim prompts, canonical values, scored assertions | Sec. 5 |
| `scenarios/archiveflow_scenarios.md` | The four ArchiveFlow tasks: verbatim prompts, canonical values, scoring assertions | Sec. 6 |
| `conditions/aws_support_conditions.md` | The six interface variants and the tool set each exposes | Table 1 |
| `conditions/archiveflow_conditions.md` | Condition/scenario/cycle code key and evaluated ArchiveFlow interfaces | Sec. 4.2, Table 2 |
| `prompts/evaluated_prompts.md` | Both system prompts verbatim, and the single clause separating them | Sec. 3, Sec. 7.3 |
| `results/*.csv` | Every confirmatory trial, one row each | Sec. 5-8 |
| `results/aggregate_results.md` | Per-condition aggregates recomputed from those CSVs | Sec. 5-8 |
| `results/paper_number_map.md` | Each headline paper number beside its recomputed value | Table 3 |
| `additional_tables/complete_results.md` | Per-condition, per-scenario breakdown | Sec. 5-8 |
| `analysis/statistical_methods.md` | Estimators, correction families, and equivalence criterion | Sec. 3 |
| `analysis/statistical_tests.py` | Executable confirmatory tests, effect sizes, Holm families, and interval criteria | Sec. 3, Sec. 5-8 |
| `analysis/reproduce_results.md` | Column dictionary and how to recompute | - |

## Reproducing the reported values

Use Python 3.12 or newer in a clean virtual environment, then run:

```text
python -m pip install -r requirements.txt
python analysis/verify_headline_numbers.py
python analysis/statistical_tests.py
```

The pinned analysis dependencies were verified with Python 3.12.9. Expected checks: 15/15 headline values and 33/33 numerical statistical checks, plus the reported correctness interval criteria. The CSVs contain 1,080 ArchiveFlow Sonnet trials, 320 ArchiveFlow Haiku trials and 180 AWS Support trials.

`results/paper_number_map.md` places each headline value printed in the manuscript beside the value recomputed from the supplied CSVs. Its `Match` column is calculated during bundle generation. The two scripts under `analysis/` reproduce the descriptive and inferential results.

## Provenance

The bundle is generated in one build step from the recorded trial data, validated configuration, evaluated tool-description source, and authored explanatory material. The per-trial CSVs are exported from the trial records. All aggregate tables and inferential comparisons are recomputed from these supplied CSVs rather than copied from the analysis output used during manuscript preparation.

`SHA256SUMS` records the byte identity of the shipped supplementary files, excluding the checksum manifest itself. Git repository-control files are separate from this data manifest. This release contains the data and analysis artifact, not the Springer-formatted paper, consent documents or internal research logs.

## Third-party material and licensing

Portions of `conditions/aws_support_conditions.md` reproduce or adapt AWS Labs MCP tool descriptions under Apache-2.0. See `THIRD_PARTY_NOTICES.md` and `licenses/` for the retained copyright notice, license text, source and adaptation details. This third-party license applies to the identified AWS-derived material; no repository-wide reuse license has yet been selected for the author's original research code and data.

## Scope of the supplement

- Private revision history, contribution records, and issue references are excluded because they are unnecessary for recomputation. Public artifact and upstream-license links are retained for attribution.
- Experiment configuration files are not reproduced verbatim because they contain a cloud application-inference-profile ARN and absolute machine paths. The scientifically relevant condition fields are extracted instead.
- Credentials and profile names are excluded.
- Raw model transcripts are excluded because they carry residual identifying metadata and licensing risk. The per-trial records retain the scored assertions, mutation indicators, and ordered tool-call sequence used in the reported analysis.
- Internal research-agent and audit material is excluded because it does not form part of the evaluated interface or reported analysis.
