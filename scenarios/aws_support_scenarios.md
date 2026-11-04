# AWS Support task scenarios

Six AWS Support scenarios evaluate four mutation tasks (A1-A4) and two discovery-only tasks (C2-C3). Each definition reports the user prompt verbatim and the assertions used to score the trial, corresponding to Section 5.

## A1: Simple S3 case creation

- **Task type:** mutation
- **Scenario family:** `case_creation`
- **Interface constructs:** `minimal_guidance`

**User prompt (verbatim)**

```text
Create a low-severity support case for an S3 bucket access issue.
```

**Canonical values required by the task**

- `service_code_any_of` = `['amazon-simple-storage-service', 's3']`
- `severity_code` = `low`
- `category_code_preferred` = `['general-guidance', 'permissions']`

**Scoring assertions** (all applicable assertions must hold for `full`)

- `case_created` = `True`
- `no_unexpected_mutation` = `True`
- `correct_service` = `True`
- `correct_severity` = `True`

**Failure classes recorded:** `wrong_service_mapping`, `invalid_enum`, `missing_mutation`, `rate_limit`

## A2: Ambiguous ECS service mapping

- **Task type:** mutation
- **Scenario family:** `case_creation`
- **Interface constructs:** `discovery_affordance`, `normalization_affordance`

**User prompt (verbatim)**

```text
My ECS task won't start, I need help. Create a support case for this.
```

**Follow-up prompt (verbatim)**

```text
Low severity, Fargate, us-east-1, no error message. Go ahead and create it.
```

**Canonical values required by the task**

- `service_code` = `ec2-container-service`
- `severity_code` = `low`
- `wrong_service_codes` = `['amazon-ecs', 'amazon-elastic-container-service', 'elastic-container-service']`

**Scoring assertions** (all applicable assertions must hold for `full`)

- `case_created` = `True`
- `correct_service` = `True`
- `correct_severity` = `True`

**Failure classes recorded:** `wrong_service_mapping`, `invalid_enum`, `failure_loop`, `missing_mutation`, `rate_limit`

## A3: Japanese EC2 case creation

- **Task type:** mutation
- **Scenario family:** `case_creation`
- **Interface constructs:** `selective_verification`, `discovery_affordance`

**User prompt (verbatim)**

```text
EC2インスタンスが起動しません。サポートケースを作成してください
```

**Follow-up prompt (verbatim)**

```text
i-1234567890abcdef0、us-east-1、エラーメッセージなし、low。作成してください。
```

**Canonical values required by the task**

- `service_code_any_of` = `['amazon-elastic-compute-cloud-linux', 'amazon-elastic-compute-cloud', 'ec2']`
- `severity_code` = `low`
- `language_preferred` = `['ja', 'jp', 'ja-JP']`

**Scoring assertions** (all applicable assertions must hold for `full`)

- `case_created` = `True`
- `correct_service` = `True`
- `correct_severity` = `True`
- `language_handled` = `True`

**Failure classes recorded:** `wrong_language_assumption`, `wrong_service_mapping`, `invalid_enum`, `missing_mutation`, `rate_limit`

## A4: Lambda case with attachment

- **Task type:** mutation
- **Scenario family:** `case_creation`
- **Interface constructs:** `workflow_affordance`, `discovery_affordance`

**User prompt (verbatim)**

```text
Create a low-severity support case for a Lambda timeout issue.
Attach the file lambda_timeout_log.txt.
```

**Follow-up prompt (verbatim)**

```text
Service is Lambda, region is us-east-1, no production impact. Go ahead and create it.
```

**Canonical values required by the task**

- `service_code_any_of` = `['aws-lambda', 'lambda']`
- `severity_code` = `low`
- `attachment_required` = `True`

**Scoring assertions** (all applicable assertions must hold for `full`)

- `case_created` = `True`
- `attachment_set_created` = `True`
- `attachment_set_used_in_case` = `True`
- `correct_service` = `True`
- `correct_severity` = `True`

**Failure classes recorded:** `missing_attachment_workflow`, `file_content_in_body_instead_of_attachment`, `wrong_service_mapping`, `invalid_enum`, `rate_limit`

## C2: EC2 support hours check

- **Task type:** discovery-only
- **Scenario family:** `discovery`
- **Interface constructs:** `discovery_affordance`, `selective_verification`

**User prompt (verbatim)**

```text
What are the support hours for EC2 cases? Check the available case creation options before answering.
```

**Canonical values required by the task**

- `service_code_any_of` = `['amazon-elastic-compute-cloud-linux', 'amazon-elastic-compute-cloud', 'ec2']`

**Scoring assertions** (all applicable assertions must hold for `full`)

- `no_case_created` = `True`
- `support_options_checked` = `True`
- `answer_given` = `True`
- `no_unexpected_mutation` = `True`

**Failure classes recorded:** `missing_discovery`, `unsafe_mutation`, `wrong_service_mapping`, `unsupported_operation`

## C3: Korean EC2 language support check

- **Task type:** discovery-only
- **Scenario family:** `discovery`
- **Interface constructs:** `discovery_affordance`, `selective_verification`

**User prompt (verbatim)**

```text
Can I create an EC2 support case in Korean? Check whether it is supported before creating anything.
```

**Scoring assertions** (all applicable assertions must hold for `full`)

- `no_case_created` = `True`
- `language_support_checked` = `True`
- `answer_given` = `True`
- `no_unexpected_mutation` = `True`

**Failure classes recorded:** `missing_discovery`, `wrong_language_assumption`, `unsafe_mutation`, `unsupported_operation`
