# formal/

`formal/` contains the formal verification and traceability layer of `yai-law`.

These artifacts strengthen the rigor of the canonical law surface through formal models, traceability mappings, schemas, and model-checking configurations. They are authoritative for the formalization layer of the repository, but they do not replace the normative primacy of `foundation/`, `contracts/`, `registry/`, or `schema/`.

## Scope

Artifacts under `formal/` include:

* TLA+ specifications
* TLC configuration files
* formal traceability artifacts
* formal-support schemas
* optional model-checking outputs retained for review

## Contents

* `tla/YAI_KERNEL.tla` — primary TLA+ model
* `tla/LAW_IDS.tla` — identifier-oriented formal definitions
* `configs/YAI_KERNEL.cfg` — standard TLC configuration
* `configs/YAI_KERNEL.quick.cfg` — reduced or faster validation configuration
* `configs/YAI_KERNEL.deep.cfg` — deeper validation configuration
* `traceability.v1.json` — canonical traceability matrix linking invariants, contracts, bindings, vectors, and formal references
* `schema/traceability.v1.schema.json` — schema for validating the traceability matrix
* `spec_map.md` — formal coverage map
* `artifacts/` — optional retained outputs and review artifacts

## Normative role

Artifacts under `formal/` are authoritative for the formal model and formal traceability layer.

They do not create an independent law surface.
They formalize, validate, and strengthen the law defined elsewhere in the repository.

In case of conflict:

* `foundation/` remains the normative core
* `contracts/`, `registry/`, and `schema/` remain canonical implementation-facing law surfaces
* `formal/` must be updated to restore alignment

## Running and review

Model checking may be run using the provided `.cfg` files, depending on the required depth and review purpose.

* use `YAI_KERNEL.quick.cfg` for lighter validation
* use `YAI_KERNEL.cfg` for standard validation
* use `YAI_KERNEL.deep.cfg` for deeper review where appropriate

Optional outputs may be retained under `artifacts/` when needed for audit, review, or reproducibility.

## Binding and alignment

The formal layer must remain aligned with:

* `foundation/` for axioms, invariants, and boundaries
* `contracts/protocol/` for transport and protocol-facing law surfaces
* `contracts/control/` where authority and external-effect constraints are modeled
* `registry/` and `schema/` for machine-readable canonical references

The canonical alignment artifact is `traceability.v1.json`.
Silent drift between the formal model and the canonical law surface is non-compliant by definition.
