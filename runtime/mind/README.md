# Mind

`runtime/mind/` contains the canonical mind-layer law surface of `yai-law`.

This directory represents the mind as a runtime authority layer, not as an implementation. It defines how mind-facing behavior is understood within the YAI law model and how modeled mind surfaces must remain aligned with foundational law, canonical registries, and formal traceability artifacts.

## Scope

The mind layer covers:

* mind-facing runtime authority surfaces
* modeled cognitive or memory-adjacent schema surfaces where explicitly defined
* alignment of mind-facing behavior with governance, determinism, and accountability constraints

This directory does not define the full implementation of YAI Mind.
It defines the law-facing interpretation of the mind layer where canonical artifacts are published.

## Normative role

Artifacts under `runtime/mind/` are normative where they define canonical mind-layer schema surfaces, bindings, or law-facing notes.

They must remain aligned with:

* `foundation/boundaries/L3-mind.md`
* `foundation/invariants/` for determinism, governance, and accountability constraints
* `registry/` for canonical machine-readable references
* `formal/` for traceability and proof-support alignment

If a mind-facing implementation or consumer diverges from the canonical law surfaces defined here, it is non-conforming.

## Current modeled surface

The currently modeled canonical sub-surface under `runtime/mind/` is:

* `graph/`

This reflects a scoped mind-facing surface, not the entirety of the Mind layer.

## Relationship to foundational law

Mind-layer artifacts remain subordinate to the foundational law.

In particular, mind-facing surfaces must not bypass or weaken:

* determinism requirements within declared scope
* governance and authority constraints
* accountability and evidence expectations
* external-effect constraints where mind behavior participates in governed execution

## Relationship to formal artifacts

No dedicated full Mind formal model is required by default.

Where mind-facing surfaces are currently connected to formal artifacts, that linkage may be indirect through shared runtime governance constraints and the traceability layer under `formal/`.

## Change discipline

Any mind-layer law change that affects schema structure, governance interpretation, evidence expectations, or compatibility semantics must update, as applicable:

* canonical artifacts under `runtime/mind/`
* relevant foundational artifacts
* relevant traceability or formal artifacts
* `REGISTRY.md`
* `SPEC_MAP.md`
* `CHANGELOG.md`

Silent drift between mind-facing behavior and canonical mind-layer law is non-compliant by definition.
