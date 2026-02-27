# Providers

`contracts/providers/` contains the canonical provider-facing schema surface of `yai-law`.

These artifacts define the machine-readable contracts used to describe provider-facing behavior, expectations, and compatibility-relevant structure across downstream consumers.

## Scope

The provider surface covers:

* provider-facing schema contracts
* canonical structure for provider-related payloads
* validation-facing constraints for provider-bound integrations

## Normative artifacts

Canonical provider artifact:

* `schema/providers.v1.json`

Supporting material:

* `notes/PROVIDERS_TRUST.md`

## Normative role

Artifacts in this directory are normative where they define canonical schema structure.

They must remain aligned with:

* `foundation/invariants/` for governance and external-effect constraints
* `foundation/extensions/` where provider behavior intersects policy or compliance overlays
* `registry/` for canonical machine-readable references
* `formal/` where provider-relevant authority or effect constraints are traced

If a downstream consumer interprets provider behavior in a way that conflicts with these canonical schemas, the consumer is non-conforming.

## Versioning and compatibility rules

* File names encode schema major versions where applicable
* Breaking changes require a new major schema line and compatibility review
* Additive compatible changes require repository version review and `CHANGELOG.md` coverage
* Provider-facing semantic changes that alter validation or enforcement expectations must be treated as compatibility-sensitive

## Consumers

Typical consumers include:

* `yai`
* `yai-cli`
* `yai-yx`
* validation and governance tooling that consumes canonical provider-facing schemas

## Change discipline

A provider-surface change must update, as applicable:

* canonical schemas in this directory
* `REGISTRY.md`
* `SPEC_MAP.md`
* `CHANGELOG.md`
* relevant validation artifacts when behavior changes

Silent drift between provider-facing behavior and canonical provider schemas is non-compliant by definition.
