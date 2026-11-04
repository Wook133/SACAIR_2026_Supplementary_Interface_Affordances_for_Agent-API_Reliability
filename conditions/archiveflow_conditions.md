# ArchiveFlow interface conditions

These definitions correspond to Table 2. The eight factorial cells `AF_000`-`AF_111` and the three subsequent design-cycle conditions are reported with their construct flags and evaluated tool surfaces. The verbatim description variants follow the condition definitions.

**Code key.** Cycle 1B uses `AF_000`-`AF_111`: the three bits are D/N/W (discovery, normalisation, workflow guidance), with 1=on and 0=off; for example, `AF_101` enables D and W. Cycle 2 adds `AF_F` (embedded catalogue). Cycle 3 adds `AF_FO` (catalogue plus Optional discovery) and `AF_FX` (catalogue, no discovery). `AF1`-`AF4` are task scenarios reused across these conditions, not condition codes. AWS `A`-`F` belong to Cycle 1A. The legacy AFB/AFE names below correspond to AF_000/AF_111; they are not extra factorial cells.

## `archiveflow_baseline` (paper code AFB)

- **Label:** ArchiveFlow baseline
- **Theoretical role:** `latent_model_guessing`

The ArchiveFlow baseline is the second-domain transfer condition. It exposes three mutation tools without discovery, alias normalisation, or workflow guidance, and corresponds to AWS Support Condition A.

**Tools exposed to the model**

- `create_attachment_set`
- `create_digitization_request`
- `create_export_job`

**Tools withheld**

- `describe_collections`
- `describe_material_types`
- `describe_rights_statuses`
- `describe_access_levels`
- `describe_output_profiles`
- `describe_access_rules`

## `archiveflow_enhanced` (paper code AFE)

- **Label:** ArchiveFlow enhanced
- **Theoretical role:** `discovery_plus_normalization_affordance`

The ArchiveFlow enhanced condition exposes three mutation tools and six discovery tools, normalises mutation inputs, and provides workflow-aware descriptions. It is the second-domain analogue of the AWS Support discovery and embedded-normalisation conditions.

**Tools exposed to the model**

- `create_attachment_set`
- `create_digitization_request`
- `create_export_job`
- `describe_collections`
- `describe_material_types`
- `describe_rights_statuses`
- `describe_access_levels`
- `describe_output_profiles`
- `describe_access_rules`

## `AF_000` (paper code AF_000)

- **Label:** ArchiveFlow factorial (-discovery / -normalisation / -workflow_docstrings)
- **Theoretical role:** `latent_model_guessing`

AF_000 provides no discovery tools, alias normalisation, or workflow descriptions. It is equivalent to the legacy ArchiveFlow baseline.

**Tools exposed to the model**

- `create_attachment_set`
- `create_digitization_request`
- `create_export_job`

**Tools withheld**

- `describe_collections`
- `describe_material_types`
- `describe_rights_statuses`
- `describe_access_levels`
- `describe_output_profiles`
- `describe_access_rules`

## `AF_001` (paper code AF_001)

- **Label:** ArchiveFlow factorial (-discovery / -normalisation / +workflow_docstrings)
- **Theoretical role:** `workflow_docstrings_only`

AF_001 adds workflow-aware mutation descriptions without discovery tools or alias normalisation.

**Tools exposed to the model**

- `create_attachment_set`
- `create_digitization_request`
- `create_export_job`

**Tools withheld**

- `describe_collections`
- `describe_material_types`
- `describe_rights_statuses`
- `describe_access_levels`
- `describe_output_profiles`
- `describe_access_rules`

## `AF_010` (paper code AF_010)

- **Label:** ArchiveFlow factorial (-discovery / +normalisation / -workflow_docstrings)
- **Theoretical role:** `normalisation_only`

AF_010 normalises common natural-language aliases without exposing discovery tools or workflow descriptions.

**Tools exposed to the model**

- `create_attachment_set`
- `create_digitization_request`
- `create_export_job`

**Tools withheld**

- `describe_collections`
- `describe_material_types`
- `describe_rights_statuses`
- `describe_access_levels`
- `describe_output_profiles`
- `describe_access_rules`

## `AF_011` (paper code AF_011)

- **Label:** ArchiveFlow factorial (-discovery / +normalisation / +workflow_docstrings)
- **Theoretical role:** `normalisation_plus_workflow_docstrings`

AF_011 combines alias normalisation and workflow descriptions without exposing the discovery tools.

**Tools exposed to the model**

- `create_attachment_set`
- `create_digitization_request`
- `create_export_job`

**Tools withheld**

- `describe_collections`
- `describe_material_types`
- `describe_rights_statuses`
- `describe_access_levels`
- `describe_output_profiles`
- `describe_access_rules`

## `AF_100` (paper code AF_100)

- **Label:** ArchiveFlow factorial (+discovery / -normalisation / -workflow_docstrings)
- **Theoretical role:** `discovery_only`

AF_100 exposes the discovery tools without alias normalisation or workflow descriptions.

**Tools exposed to the model**

- `create_attachment_set`
- `create_digitization_request`
- `create_export_job`
- `describe_collections`
- `describe_material_types`
- `describe_rights_statuses`
- `describe_access_levels`
- `describe_output_profiles`
- `describe_access_rules`

## `AF_101` (paper code AF_101)

- **Label:** ArchiveFlow factorial (+discovery / -normalisation / +workflow_docstrings)
- **Theoretical role:** `discovery_plus_workflow_docstrings`

AF_101 combines discovery tools and workflow descriptions without alias normalisation.

**Tools exposed to the model**

- `create_attachment_set`
- `create_digitization_request`
- `create_export_job`
- `describe_collections`
- `describe_material_types`
- `describe_rights_statuses`
- `describe_access_levels`
- `describe_output_profiles`
- `describe_access_rules`

## `AF_110` (paper code AF_110)

- **Label:** ArchiveFlow factorial (+discovery / +normalisation / -workflow_docstrings)
- **Theoretical role:** `discovery_plus_normalisation`

AF_110 combines discovery tools and alias normalisation without workflow descriptions.

**Tools exposed to the model**

- `create_attachment_set`
- `create_digitization_request`
- `create_export_job`
- `describe_collections`
- `describe_material_types`
- `describe_rights_statuses`
- `describe_access_levels`
- `describe_output_profiles`
- `describe_access_rules`

## `AF_111` (paper code AF_111)

- **Label:** ArchiveFlow factorial (+discovery / +normalisation / +workflow_docstrings)
- **Theoretical role:** `discovery_plus_normalisation_plus_workflow`

AF_111 combines discovery tools, alias normalisation, and workflow descriptions. It is equivalent to the legacy ArchiveFlow enhanced condition and provides the reference cell for the factorial contrasts.

**Tools exposed to the model**

- `create_attachment_set`
- `create_digitization_request`
- `create_export_job`
- `describe_collections`
- `describe_material_types`
- `describe_rights_statuses`
- `describe_access_levels`
- `describe_output_profiles`
- `describe_access_rules`

## `AF_F` (paper code AF_F)

- **Label:** ArchiveFlow embedded catalogue (cycle-2 artifact)
- **Theoretical role:** `embedded_normalisation_affordance`

The cycle-2 AF_F condition replaces alias normalisation and workflow descriptions with an embedded catalogue. Canonical codes, display names, and access rules are included in the mutation-tool descriptions and are therefore available at call time without a separate discovery request.

**Tools exposed to the model**

- `create_attachment_set`
- `create_digitization_request`
- `create_export_job`
- `describe_collections`
- `describe_material_types`
- `describe_rights_statuses`
- `describe_access_levels`
- `describe_output_profiles`
- `describe_access_rules`

## `AF_FO` (paper code AF_FO)

- **Label:** ArchiveFlow embedded catalogue + Optional describes (cycle-3a)
- **Theoretical role:** `embedded_normalisation_plus_optional_marker`

The cycle-3 AF_FO condition retains the embedded catalogue and marks each discovery-tool description as Optional. It was introduced after AF_F continued to call each advertised discovery tool despite the catalogue being present in the mutation-tool descriptions.

**Tools exposed to the model**

- `create_attachment_set`
- `create_digitization_request`
- `create_export_job`
- `describe_collections`
- `describe_material_types`
- `describe_rights_statuses`
- `describe_access_levels`
- `describe_output_profiles`
- `describe_access_rules`

## `AF_FX` (paper code AF_FX)

- **Label:** ArchiveFlow embedded catalogue, describes hidden (cycle-3b)
- **Theoretical role:** `embedded_normalisation_strict`

The paired AF_FX condition retains the embedded catalogue but withholds the discovery tools. Comparison with AF_FO separates the Optional marker from complete removal of the discovery surface.

**Tools exposed to the model**

- `create_attachment_set`
- `create_digitization_request`
- `create_export_job`

**Tools withheld**

- `describe_collections`
- `describe_material_types`
- `describe_rights_statuses`
- `describe_access_levels`
- `describe_output_profiles`
- `describe_access_rules`

## Evaluated tool-description surfaces

The table maps each registry condition to the description variants supplied to the model. The verbatim text of each unique variant follows the table; identical variants are reported once.

| Registry key | D | N | W | E | O | attachment description | digitization description | export description | discovery descriptions |
|---|:--:|:--:|:--:|:--:|:--:|---|---|---|---|
| `archiveflow_baseline` | 0 | 0 | 0 | 0 | 0 | `attachment-W0` | `digitization-N0W0E0` | `export-N0W0E0` | `hidden` |
| `archiveflow_enhanced` | 1 | 1 | 1 | 0 | 0 | `attachment-W1` | `digitization-N1W1E0` | `export-N1W1E0` | `base` |
| `AF_000` | 0 | 0 | 0 | 0 | 0 | `attachment-W0` | `digitization-N0W0E0` | `export-N0W0E0` | `hidden` |
| `AF_001` | 0 | 0 | 1 | 0 | 0 | `attachment-W1` | `digitization-N0W1E0` | `export-N0W1E0` | `hidden` |
| `AF_010` | 0 | 1 | 0 | 0 | 0 | `attachment-W0` | `digitization-N1W0E0` | `export-N1W0E0` | `hidden` |
| `AF_011` | 0 | 1 | 1 | 0 | 0 | `attachment-W1` | `digitization-N1W1E0` | `export-N1W1E0` | `hidden` |
| `AF_100` | 1 | 0 | 0 | 0 | 0 | `attachment-W0` | `digitization-N0W0E0` | `export-N0W0E0` | `base` |
| `AF_101` | 1 | 0 | 1 | 0 | 0 | `attachment-W1` | `digitization-N0W1E0` | `export-N0W1E0` | `base` |
| `AF_110` | 1 | 1 | 0 | 0 | 0 | `attachment-W0` | `digitization-N1W0E0` | `export-N1W0E0` | `base` |
| `AF_111` | 1 | 1 | 1 | 0 | 0 | `attachment-W1` | `digitization-N1W1E0` | `export-N1W1E0` | `base` |
| `AF_F` | 1 | 0 | 0 | 1 | 0 | `attachment-W0` | `digitization-N0W0E1` | `export-N0W0E1` | `base` |
| `AF_FO` | 1 | 0 | 0 | 1 | 1 | `attachment-W0` | `digitization-N0W0E1` | `export-N0W0E1` | `optional` |
| `AF_FX` | 0 | 0 | 0 | 1 | 0 | `attachment-W0` | `digitization-N0W0E1` | `export-N0W0E1` | `hidden` |

`D`, `N`, `W`, `E`, and `O` denote discovery, normalisation, workflow docstrings, embedded catalogue, and the Optional marker respectively.

### Mutation-tool description variants

### `attachment-W0` — `create_attachment_set`

~~~text
Upload one or more files as an attachment set.
~~~

### `digitization-N0W0E0` — `create_digitization_request`

~~~text
Create a digitization request. All *_code fields must be exact canonical codes.
~~~

### `export-N0W0E0` — `create_export_job`

~~~text
Create an export job. All *_code fields must be exact canonical codes.
~~~

### `attachment-W1` — `create_attachment_set`

~~~text
Upload one or more files as an attachment set; returns an attachment_set_id. Workflow ordering: call this BEFORE create_digitization_request, then pass the returned attachment_set_id into the request. The API does not support attaching files after a digitization request has been created.
~~~

### `digitization-N1W1E0` — `create_digitization_request`

~~~text
Create a digitization request. Accepts either canonical codes or common aliases (e.g. 'maps' → mat_cartographic, 'public domain' → rights_pd_confirmed). To attach files, the workflow is: create the attachment set first, then pass the returned attachment_set_id into this call.
~~~

### `export-N1W1E0` — `create_export_job`

~~~text
Create an export job. Accepts either canonical codes or common aliases. Before creating an export, consider whether the requested combination is permitted: restricted oral-history audio cannot be exported as a public web package, items with unknown rights cannot be exported on the public web, and restricted items require curator_approval=true. If the user is asking whether an export IS ALLOWED, answer the question without creating the job.
~~~

### `digitization-N0W1E0` — `create_digitization_request`

~~~text
Create a digitization request. All *_code fields must be exact canonical codes. To attach files, the workflow is: create the attachment set first, then pass the returned attachment_set_id into this call.
~~~

### `export-N0W1E0` — `create_export_job`

~~~text
Create an export job. All *_code fields must be exact canonical codes. Before creating an export, consider whether the requested combination is permitted: restricted oral-history audio cannot be exported as a public web package, items with unknown rights cannot be exported on the public web, and restricted items require curator_approval=true. If the user is asking whether an export IS ALLOWED, answer the question without creating the job.
~~~

### `digitization-N1W0E0` — `create_digitization_request`

~~~text
Create a digitization request. Accepts either canonical codes or common aliases (e.g. 'maps' → mat_cartographic, 'public domain' → rights_pd_confirmed).
~~~

### `export-N1W0E0` — `create_export_job`

~~~text
Create an export job. Accepts either canonical codes or common aliases.
~~~

### `digitization-N0W0E1` — `create_digitization_request`

~~~text
Create a digitization request. All *_code fields must be exact canonical codes.
CATALOGUE — canonical codes you can use directly in *_code fields:

Collections (collection_code):
  col_cape_maps         Cape Historical Maps (default material: cartographic, reading-room only)
  col_photo_archive     Photograph Archive (default material: still image, open access)
  col_oral_history      Oral History Audio (default material: audio, restricted)
  col_manuscripts       Manuscripts Collection (default material: textual record, reading-room only)

Material types (material_type_code):
  mat_textual_record    text, documents, letters
  mat_still_image       photos, photographs, images
  mat_cartographic      maps, atlases
  mat_audio_object      audio, oral history, recordings
  mat_physical_artifact objects, artefacts

Rights statuses (rights_status_code):
  rights_pd_confirmed              public domain (confirmed)
  rights_in_copyright              in copyright
  rights_orphan_work               orphan work
  rights_unknown_review_required   unknown / needs review

Access levels (access_level_code):
  access_open
  access_reading_room_only
  access_restricted_curator_approval

Output profiles (output_profile_code):
  output_web_access          web access package
  output_preservation_tiff   preservation TIFF
  output_research_pdf        research PDF
  output_metadata_only       metadata only
~~~

### `export-N0W0E1` — `create_export_job`

~~~text
Create an export job. All *_code fields must be exact canonical codes.
CATALOGUE — canonical codes you can use directly in *_code fields:

Collections (collection_code):
  col_cape_maps         Cape Historical Maps (default material: cartographic, reading-room only)
  col_photo_archive     Photograph Archive (default material: still image, open access)
  col_oral_history      Oral History Audio (default material: audio, restricted)
  col_manuscripts       Manuscripts Collection (default material: textual record, reading-room only)

Material types (material_type_code):
  mat_textual_record    text, documents, letters
  mat_still_image       photos, photographs, images
  mat_cartographic      maps, atlases
  mat_audio_object      audio, oral history, recordings
  mat_physical_artifact objects, artefacts

Rights statuses (rights_status_code):
  rights_pd_confirmed              public domain (confirmed)
  rights_in_copyright              in copyright
  rights_orphan_work               orphan work
  rights_unknown_review_required   unknown / needs review

Access levels (access_level_code):
  access_open
  access_reading_room_only
  access_restricted_curator_approval

Output profiles (output_profile_code):
  output_web_access          web access package
  output_preservation_tiff   preservation TIFF
  output_research_pdf        research PDF
  output_metadata_only       metadata only

ACCESS RULES (enforced server-side before export creation):
  - Restricted oral-history audio (mat_audio_object + access_restricted_curator_approval)
    cannot be exported as a public web package (output_web_access). This rule is hard.
  - Items with rights_unknown_review_required cannot be exported on the public web.
  - Other restricted items can be web-exported only with curator_approval=true.

If the user is asking whether an export IS ALLOWED, answer the question
directly from these rules without calling create_export_job.
~~~

### Base discovery descriptions

Conditions mapped to `base` receive the following descriptions unchanged. Conditions mapped to `hidden` do not expose these tools.

### `describe_collections`

~~~text
List archive collections with their default material type and access level.
~~~

### `describe_material_types`

~~~text
List material type codes with their canonical names and aliases (e.g. 'photos' → mat_still_image).
~~~

### `describe_rights_statuses`

~~~text
List rights status codes with their canonical names and aliases (e.g. 'public domain' → rights_pd_confirmed).
~~~

### `describe_access_levels`

~~~text
List access level codes (open / reading room / restricted).
~~~

### `describe_output_profiles`

~~~text
List output profile codes (web access, preservation TIFF, research PDF, metadata only).
~~~

### `describe_access_rules`

~~~text
List the deterministic access rules. Use this to answer questions about whether a given (material, rights, access, output) combination is permitted, without attempting a mutation.
~~~

### Optional prefix used by `AF_FO`

~~~text
(Optional — the full catalogue is already embedded in the descriptions of create_digitization_request and create_export_job; calling this tool is only useful for edge cases not covered by the inline catalogue.)
~~~

For the `optional` surface, this prefix is prepended verbatim to each base discovery description.
