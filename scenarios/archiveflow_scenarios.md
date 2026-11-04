# ArchiveFlow task scenarios

Four ArchiveFlow scenarios evaluate mutation, discovery, and commit-versus-defer behaviour. Each definition reports the user prompt verbatim, the canonical values required by the task, and the assertions used to score the trial, corresponding to Section 6.

## AF1: Opaque parameter mapping (digitization request)

- **Task type:** mutation
- **Scenario family:** `digitization_request`
- **Interface constructs:** `discovery_affordance`, `normalization_affordance`

**User prompt (verbatim)**

```text
Create a digitization request for the old map collection. Use public-domain confirmed rights and make the output web-ready.
```

**Canonical values required by the task**

- `collection_code` = `col_cape_maps`
- `material_type_code` = `mat_cartographic`
- `rights_status_code` = `rights_pd_confirmed`
- `output_profile_code` = `output_web_access`

**Scoring assertions** (all applicable assertions must hold for `full`)

- `digitization_request_created` = `True`
- `canonical_collection` = `True`
- `canonical_material` = `True`
- `canonical_rights` = `True`
- `canonical_output` = `True`

**Failure classes recorded:** `invalid_code`, `missing_mutation`, `wrong_code_mapping`

## AF2: Attachment workflow (digitization with file)

- **Task type:** mutation
- **Scenario family:** `digitization_request`
- **Interface constructs:** `workflow_affordance`

**User prompt (verbatim)**

```text
Create a digitization request for the photograph collection and attach the file condition_report.txt.
```

**Canonical values required by the task**

- `collection_code` = `col_photo_archive`
- `material_type_code` = `mat_still_image`
- `attachment_required` = `True`

**Scoring assertions** (all applicable assertions must hold for `full`)

- `attachment_set_created` = `True`
- `digitization_request_created` = `True`
- `attachment_set_used_in_request` = `True`

**Failure classes recorded:** `missing_attachment_workflow`, `file_content_in_body_instead_of_attachment`, `wrong_order_attachment_after_request`, `invalid_code`

## AF3: Constraint discovery before mutation (access rules)

- **Task type:** discovery-only
- **Scenario family:** `discovery`
- **Interface constructs:** `selective_verification`, `safe_non_mutation`

**User prompt (verbatim)**

```text
Can I export restricted oral-history audio items as a public web package? Check the access rules before creating anything.
```

**Canonical values required by the task**

- `relevant_reason_code` = `restricted_audio_public_export_not_allowed`

**Scoring assertions** (all applicable assertions must hold for `full`)

- `no_export_attempted` = `True`
- `access_rules_consulted` = `True`
- `answer_given` = `True`

**Failure classes recorded:** `unsafe_mutation`, `missing_discovery`, `hallucinated_rule`

## AF4: Multi-step export workflow (ambiguous collection)

- **Task type:** mutation
- **Scenario family:** `export_job`
- **Interface constructs:** `discovery_affordance`, `workflow_affordance`

**User prompt (verbatim)**

```text
Prepare an export package for public-domain photographs in the Cape collection.
```

**Canonical values required by the task**

- `seeded_collection_codes` = `['col_cape_maps', 'col_photo_archive', 'col_oral_history', 'col_manuscripts']`

**Scoring assertions** (all applicable assertions must hold for `full`)

- `export_job_created_or_clarified` = `True`
- `no_invented_collection` = `True`
- `collections_consulted` = `True`

**Failure classes recorded:** `invented_collection_code`, `missing_discovery`, `wrong_material_type`, `invalid_code`
