# Statistical methods

This section records the estimators, correction families, and interval criterion used for the confirmatory analysis described in Section 3.

## Design-cycle and confirmatory corpora

Design-cycle batches used temperature 0 for artifact iteration and behavioural inspection. Their near-deterministic scored outcomes are reported as counts and effect sizes, rather than used for the intended inferential tests. Near-determinism alone does not establish dependence between trials.

Confirmatory statistics are computed on a separate corpus sampled at temperature 1.0, whose replicates are treated as independent conditional draws of hosted model behaviour. This supplement includes that corpus because the inferential claims are derived from it.

## Estimators

| Quantity | Method |
|---|---|
| Proportions | Wilson 95% confidence intervals |
| Difference in proportions | Fisher's exact, two-sided |
| Continuous metrics (tool calls, tokens) | Mann-Whitney U |
| Group-mean continuous confidence intervals | BCa bootstrap, 10,000 resamples |
| Between-group mean-difference intervals | Percentile bootstrap, 10,000 resamples |
| Effect size, proportions | Risk ratio, Haldane-Anscombe correction |
| Effect size, continuous | Cliff's delta |
| Multiplicity | Holm-Bonferroni within each declared family |

## Correction families

Holm correction is applied within, not across, these families:

- `af_temp10_main`: the discovery main effect (single test).
- `af_temp10_cycle3`: AF_FO vs AF_111 tool calls, AF_FO vs AF_111 tokens, AF_F vs AF_111 tokens, AF_FX vs AF_FO success on AF4.
- `af_prompt_ablation`: the AF_F tool-call shift and the prompt-by-description permutation test. The prompt correctness assessment uses a separate risk-ratio interval criterion outside the Holm family.
- `aws_temp10`: A vs B success, F vs B success, F vs B tokens.
- `haiku_temp10`: the discovery main effect and the workflow-docstring effect on AF2.

## Equivalence criterion and chronology

AF_FO versus AF_111 correctness is assessed using an interval criterion rather than treating a non-significant difference as evidence of equivalence. Equivalence is declared only when the complete 95% risk-ratio confidence interval falls within the plus-or-minus 10% margin `[0.90, 1.10]`. The Fisher p-value is reported descriptively and is not used to establish equivalence.

Both the margin and the complete-interval rule were specified after the confirmatory data had been collected, as an analysis-method clarification. No trial records were changed. No prospective power or precision calculation was performed.

The neutral-prompt correctness assessment uses the same complete-CI criterion, also specified after confirmatory data collection. Its pooled risk ratio and 95% CI are unchanged. For traceability, the analysis script additionally retains the earlier one-sided non-inferiority check (lower CI bound at least 0.90 plus no per-cell success-rate decrease), explicitly labelled as a legacy diagnostic. That diagnostic is not the manuscript's complete-CI criterion.

## Scope of inference

Replicates are treated as independent conditional draws of hosted model behaviour on a fixed scenario set. The inference concerns this stochastic behaviour rather than MCP tasks in general: the four ArchiveFlow and six AWS Support scenarios constitute a designed set, not a random sample from a population of tasks.
