# Kernel

`runtime/kernel/` contains the canonical kernel-layer law surface of `yai-law`.

This directory represents the kernel as a runtime authority layer, not as an implementation. It defines how the kernel is understood in the law model and how kernel-facing behavior must remain aligned with the foundational law, machine-readable registries, and formal artifacts.

## Scope

The kernel layer covers:

* kernel-level authority boundaries
* participation in effect gating and enforcement
* traceability-preserving runtime behavior
* kernel-facing alignment with the formal runtime model

This directory does not contain the kernel implementation itself.
It defines the law-facing interpretation of the kernel layer.

## Normative artifacts

Primary artifact in this directory:

* `BINDING.md` — normative mapping between foundational law and kernel runtime behavior

## Normative role

The kernel layer is normative where it defines law-facing constraints on kernel behavior.

Kernel-facing consumers and implementations must remain aligned with:

* `foundation/axioms/`
* `foundation/invariants/`
* `foundation/boundaries/L1-kernel.md`
* `foundation/boundaries/L0-vault.md` where vault interaction is relevant
* `registry/` for canonical machine-readable references
* `formal/` for runtime-model and traceability alignment

If a kernel implementation diverges from the binding and the foundational law it references, the implementation is non-conforming.

## Relationship to formal artifacts

The kernel layer is one of the primary connection points between foundational law and formal runtime modeling.

The main formal references are:

* `formal/tla/YAI_KERNEL.tla`
* `formal/configs/YAI_KERNEL.cfg`
* `formal/configs/YAI_KERNEL.quick.cfg`
* `formal/configs/YAI_KERNEL.deep.cfg`
* `formal/traceability.v1.json`

The formal model does not replace the kernel law surface.
It strengthens verification and traceability of that surface.

## Binding and enforcement expectations

Kernel behavior is expected to remain aligned with the binding document for:

* traceability preservation
* explicit authority gating
* non-bypassable external-effect participation
* compliance-context enforcement where required
* consistency with modeled state-machine transitions

See `BINDING.md` for the normative mapping.

## Change discipline

Any kernel-law change that affects state, transitions, guards, or authority interpretation must update, as applicable:

* `BINDING.md`
* relevant foundational artifacts
* relevant formal artifacts
* `REGISTRY.md`
* `SPEC_MAP.md`
* `CHANGELOG.md`

Silent drift between kernel behavior, kernel binding, and canonical law is non-compliant by definition.
