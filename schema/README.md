# schema/

`schema/` contains the canonical transversal schemas of `yai-law`.

These schemas define repository-wide artifact and policy payloads that are not limited to a single registry file or a single contract surface.

## Scope

Artifacts under `schema/` include canonical schemas for:

- bundle manifests
- decision records
- evidence indexes
- containment metrics
- policy payloads
- verification reports
- compliance context payloads
- retention policy payloads

## Normative role

Artifacts in `schema/` are normative.

They define the canonical structure of machine-readable payloads produced, validated, exchanged, or retained across YAI qualification, evidence, governance, and compliance workflows.

These schemas do not replace `registry/schema/`.

- `registry/schema/` validates registry files
- `schema/` validates transversal artifact and policy payloads

## Relationship to other repository layers

`schema/` is consumed alongside:

- `registry/` for machine-readable canonical references
- `contracts/` for public interface surfaces
- `packs/` for published normative overlays
- `formal/` for traceability and proof-support alignment

If a payload is claimed to conform to YAI law, it must validate against the relevant canonical schema defined here or in `registry/schema/`, as applicable.

## Current canonical schemas

- `bundle_manifest.v1.schema.json`
- `containment_metrics.v1.schema.json`
- `decision_record.v1.schema.json`
- `evidence_index.v1.schema.json`
- `policy.v1.schema.json`
- `verification_report.v1.schema.json`
- `compliance.context.v1.json`
- `retention.policy.v1.json`