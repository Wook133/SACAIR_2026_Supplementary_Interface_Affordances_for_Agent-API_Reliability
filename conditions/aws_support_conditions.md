# AWS Support interface conditions

These definitions correspond to Table 1. Machine-specific launch commands, cloud profiles, and branch pointers are excluded because they do not form part of the evaluated interface and may disclose account information.

## `without_describe` (paper code A)

- **Label:** Without describe tools
- **Theoretical role:** `latent_model_guessing`

Condition A withholds the domain-discovery tools. The model therefore relies on latent knowledge and the remaining tool descriptions when selecting AWS Support API values.

**Tools exposed to the model**

- `create_support_case`
- `describe_support_cases`
- `add_communication_to_case`
- `resolve_support_case`

**Tools withheld**

- `describe_services`
- `describe_severity_levels`
- `describe_create_case_options`
- `describe_supported_languages`

## `with_describe` (paper code B)

- **Label:** With describe tools
- **Theoretical role:** `discovery_affordance`

Condition B exposes the domain-discovery tools, including `describe_services` and `describe_severity_levels`.

**Tools exposed to the model**

- `create_support_case`
- `describe_services`
- `describe_severity_levels`

## `generic_aws_mcp` (paper code C)

- **Label:** Generic AWS MCP
- **Theoretical role:** `generic_tool_access`

Condition C replaces the domain-specific AWS Support tools with the generic `call_aws` interface and command suggestion.

**Tools exposed to the model**

- `call_aws`

**Tools withheld**

- `create_support_case`

## `alias` (paper code D)

- **Label:** With alias resolution
- **Theoretical role:** `normalization_affordance`

Condition D retains the discovery surface and normalises predictable service-code aliases before mutation.

**Tools exposed to the model**

- `create_support_case`
- `describe_services`
- `describe_severity_levels`

## `embedded_service_codes` (paper code F)

- **Label:** Embedded service codes + optional describes
- **Theoretical role:** `embedded_normalization_affordance`

Condition F retains Condition B's tool surface and replaces the `create_support_case` description with an embedded canonical service-code table, Optional auxiliary lookups, and inline severity guidance.

**Tools exposed to the model**

- `create_support_case`
- `describe_services`
- `describe_severity_levels`
- `describe_create_case_options`
- `describe_supported_languages`

## `nosev` (paper code E)

- **Label:** Alias + minimal describes
- **Theoretical role:** `minimal_guidance`

Condition E retains alias normalisation and `describe_services`, whilst withholding the three auxiliary discovery tools.

**Tools exposed to the model**

- `create_support_case`
- `describe_services`

**Tools withheld**

- `describe_severity_levels`
- `describe_create_case_options`
- `describe_supported_languages`

## Evaluated `create_support_case` descriptions

Conditions A and B use the base `create_support_case` description; their manipulation is whether the discovery tools are withheld or exposed. Condition F replaces that description with the second block. The condition entries above give the complete exposed and withheld tool sets.

**Third-party provenance and adaptations.** These blocks reproduce or adapt tool-description text from AWS Labs MCP, AWS Support MCP Server v0.1.19. Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. The AWS-derived portions are licensed under Apache-2.0. The research variants add the embedded service-code catalogue, Optional auxiliary-lookup guidance and inline severity guidance documented below. See [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) and the included license/notice copies.

### Base `create_support_case` description

~~~text
Create a new AWS Support case.

## Prerequisites — call these first
1. **describe_services** → get valid `service_code` and `category_code` values
2. **describe_severity_levels** → get valid `severity_code` values
3. **describe_create_case_options** → check support hours and language availability
4. **describe_supported_languages** → check if your preferred language is supported

## Attaching files
Call **add_attachments_to_set** first to upload files, then pass the returned
`attachmentSetId` as the `attachment_set_id` parameter here.

## Example
```
create_support_case(
    subject='EC2 instance not starting',
    service_code='amazon-elastic-compute-cloud-linux',
    category_code='using-aws',
    severity_code='urgent',
    communication_body='My EC2 instance i-1234567890abcdef0 is not starting.',
)
```

## Severity Level Guidelines
- low (General guidance): You have a general development question or want to request a feature.
- normal (System impaired): Non-critical functions are behaving abnormally or you have a time-sensitive development question.
- high (Production system impaired): Important functions are impaired but a workaround exists.
- urgent (Production system down): Your business is significantly impacted and no workaround exists.
- critical (Business-critical system down): Your business is at risk and critical functions are unavailable.
~~~

### Condition F `create_support_case` description

~~~text
## Common Service Codes (use with create_support_case)

Use these codes directly — only call describe_services if the service isn't listed here or you need category codes.

| Service | service_code | Common Categories |
|---------|-------------|-------------------|
| EC2 (Linux) | amazon-elastic-compute-cloud-linux | general-guidance, using-aws |
| EC2 (Windows) | amazon-elastic-compute-cloud-windows | general-guidance, using-aws |
| S3 | amazon-simple-storage-service | general-guidance, using-aws |
| RDS | amazon-relational-database-service | general-guidance, using-aws |
| Lambda | aws-lambda | general-guidance, using-aws |
| ECS | ec2-container-service | general-guidance, using-aws |
| EKS | amazon-elastic-kubernetes-service | general-guidance, using-aws |
| DynamoDB | amazon-dynamodb | general-guidance, using-aws |
| CloudFormation | aws-cloudformation | general-guidance, using-aws |
| IAM | aws-identity-and-access-management | general-guidance, using-aws |
| VPC | amazon-virtual-private-cloud | general-guidance, using-aws |
| CloudWatch | amazon-cloudwatch | general-guidance, using-aws |
| Route 53 | amazon-route53 | general-guidance, using-aws |
| ELB | elastic-load-balancing | general-guidance, using-aws |
| SQS | amazon-simple-queue-service | general-guidance, using-aws |
| SNS | amazon-simple-notification-service | general-guidance, using-aws |
| CloudFront | amazon-cloudfront | general-guidance, using-aws |
| ElastiCache | amazon-elasticache | general-guidance, using-aws |
| Bedrock | amazon-bedrock | general-guidance, using-aws |
| SageMaker | amazon-sagemaker | general-guidance, using-aws |
| Account | account | general-guidance, using-aws |
| Billing | billing | general-guidance, using-aws |

NOTE: Service codes are NOT intuitive (e.g., ECS is `ec2-container-service`, not `amazon-ecs`).
When unsure, call describe_services to search.

## Severity Quick Reference

| Code | Name | When to use |
|------|------|-------------|
| low | General guidance | Development question or feature request |
| normal | System impaired | Non-critical functions behaving abnormally |
| high | Production system impaired | Important functions impaired, workaround exists |
| urgent | Production system down | Business significantly impacted, no workaround |
| critical | Business-critical system down | Business at risk, critical functions unavailable |

Create a new AWS Support case.

## Prerequisites
1. **describe_services** → get valid `service_code` and `category_code` values
2. (Optional) **describe_create_case_options** → check support hours and language availability
3. (Optional) **describe_supported_languages** → check if your preferred language is supported

Severity codes are: low, normal, high, urgent, critical. Pick based on impact — no need to call describe_severity_levels.

## Attaching files
Call **add_attachments_to_set** first to upload files, then pass the returned
`attachmentSetId` as the `attachment_set_id` parameter here.

## Example
```
create_support_case(
    subject='EC2 instance not starting',
    service_code='amazon-elastic-compute-cloud-linux',
    category_code='using-aws',
    severity_code='urgent',
    communication_body='My EC2 instance i-1234567890abcdef0 is not starting.',
)
```

## Severity Level Guidelines
- low (General guidance): You have a general development question or want to request a feature.
- normal (System impaired): Non-critical functions are behaving abnormally or you have a time-sensitive development question.
- high (Production system impaired): Important functions are impaired but a workaround exists.
- urgent (Production system down): Your business is significantly impacted and no workaround exists.
- critical (Business-critical system down): Your business is at risk and critical functions are unavailable.
~~~

The Condition F block is the exact composite string supplied to the model: the embedded service-code catalogue followed by the case-creation description with Optional auxiliary lookups and inline severity guidance.
