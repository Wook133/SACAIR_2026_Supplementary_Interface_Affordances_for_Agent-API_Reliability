# Evaluated system prompts

Two system prompts were evaluated. Within each batch, the prompt was held constant across conditions, leaving the interface condition as the within-batch manipulation.

## Primary prompt

The primary prompt was used in all batches except the prompt ablation.

```text
You are an AI assistant completing controlled research tasks using the
available tools. Use tools when needed to satisfy the user's request. Do not
invent API values when a discovery tool can verify them. For mutation tasks,
complete the requested action. For discovery-only tasks, do not create or
modify resources.
```

## Ablation prompt

The ablation prompt was used only in the prompt-ablation batch described in Section 7.3. It removes the following sentence from the primary prompt without changing the remaining text:

```text
Do not invent API values when a discovery tool can verify them.
```

The resulting prompt was:

```text
You are an AI assistant completing controlled research tasks using the
available tools. Use tools when needed to satisfy the user's request. For
mutation tasks, complete the requested action. For discovery-only tasks, do
not create or modify resources.
```

This ablation tests the design-cycle interpretation that the removed clause was resolved against the *presence* of discovery tools rather than the *content* of the mutation-tool descriptions. The resulting contrast is reported as directional rather than confirmatory.

## Decoding and request settings

| Setting | Design cycles | Confirmatory corpus |
|---|---|---|
| Temperature | 0 (greedy) | 1.0 |
| Max output tokens | 4096 | 4096 |
| Request pacing | 10 requests/minute | 10 requests/minute |

Each trial began with a fresh conversation and a newly spawned server process. The provider did not expose a generation seed, so individual temperature-1.0 samples cannot be reproduced. For the confirmatory analysis, replicates are treated as independent conditional draws of hosted model behaviour.
