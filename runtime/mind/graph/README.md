# Graph

`runtime/mind/graph/` contains the canonical graph-facing law surface of `yai-law`.

This directory defines the scoped graph surface currently modeled within the Mind layer. It captures the schema, binding, and supporting notes required to keep graph-facing behavior aligned with YAI law.

## Scope

The graph surface covers:

* graph-facing schema structure
* governance posture for graph operations
* alignment with determinism, governance, and accountability constraints
* graph-related evidence expectations where graph operations participate in governed execution

## Normative artifacts

Canonical graph artifacts in this directory include:

* `schema/graph.v1.json`
* `BINDING.md`

Supporting material:

* `notes/GRAPH_V1.md`

## Normative role

Artifacts in this directory are normative where they define canonical graph schema structure or explicit binding obligations.

They must remain aligned with:

* `foundation/invariants/I-002-determinism.md`
* `foundation/invariants/I-003-governance.md`
* `foundation/invariants/I-005-abstract-cost-accountability.md`
* `registry/primitives.v1.json`
* `registry/commands.v1.json`
* `registry/artifacts.v1.json`
* `formal/` where graph-facing behavior is indirectly traced through shared governance or traceability artifacts

If a graph implementation or consumer diverges from these canonical graph artifacts, it is non-conforming.

## Evidence expectations

When graph operations are part of governed execution, evidence should support, as applicable:

* `decision_record`
* `containment_metrics`
* `evidence_index`
* `bundle_manifest`
* `verification_report`

## Formal linkage

There is currently no dedicated graph-specific TLA module.

Formal linkage is presently indirect, through shared runtime governance constraints and the canonical traceability layer.

## Change discipline

A graph-surface change must update, as applicable:

* canonical artifacts in this directory
* relevant foundational artifacts
* relevant traceability or formal artifacts
* `REGISTRY.md`
* `SPEC_MAP.md`
* `CHANGELOG.md`

Silent drift between graph behavior and canonical graph law is non-compliant by definition.
