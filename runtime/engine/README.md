# Engine

`runtime/engine/` contains the canonical engine-layer law surface of `yai-law`.

This directory represents the engine as a runtime authority layer. It defines the law-facing structure of engine behavior where that behavior is exposed through canonical machine-readable artifacts.

## Scope

The engine layer covers:

* engine-layer runtime structure
* engine-facing canonical schema surfaces
* engine-layer alignment with foundational law and runtime authority boundaries

This directory does not contain the engine implementation itself.
It defines the law-facing model of the engine layer.

## Normative artifacts

Canonical engine artifact:

* `schema/engine_cortex.v1.json`

## Normative role

Artifacts in this directory are normative where they define canonical engine-layer schema structure.

They must remain aligned with:

* `foundation/boundaries/L2-engine.md`
* `foundation/invariants/` for determinism, governance, and accountability constraints
* `registry/` for canonical machine-readable references
* `formal/` where engine-related behavior is traced or modeled

If an engine implementation or consumer diverges from the canonical engine-layer schema surface, it is non-conforming.

## Versioning and compatibility rules

* File names encode schema major versions where applicable
* Breaking engine-layer schema changes require a new major schema line and compatibility review
* Additive compatible changes require repository version review and `CHANGELOG.md` coverage
* Engine-facing semantic changes that alter validation, interoperability, or accountability expectations must be treated as compatibility-sensitive

## Consumers

Typical consumers include:

* `yai`
* `yai-cli`
* `yai-yx`
* validation and qualification tooling that consumes engine-layer canonical schemas

## Change discipline

An engine-layer change must update, as applicable:

* canonical schemas in this directory
* relevant foundational artifacts
* relevant formal artifacts
* `REGISTRY.md`
* `SPEC_MAP.md`
* `CHANGELOG.md`

Silent drift between engine behavior and canonical engine-layer law is non-compliant by definition.
