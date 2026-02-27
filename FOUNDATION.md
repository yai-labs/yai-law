# Foundation

`FOUNDATION.md` defines the constitutional basis of `yai-law`.

If `README.md` explains the repository and `SPEC_MAP.md` maps its canonical artifacts, this file explains the foundational law model that justifies the repository structure itself.

YAI law begins from one assumption: intelligence is not trusted because it is capable; it is trusted only when it is bounded, governable, and auditable.

## 1) Foundational premise

YAI does not treat intelligence as an opaque feature.

It treats intelligence as a governed system surface that must operate inside explicit authority boundaries, under verifiable contracts, with machine-checkable artifacts, and with traceable effects.

The purpose of `yai-law` is therefore not descriptive. It is constitutive.

It defines the law that conforming runtimes, tools, and consumers must follow.

## 2) Foundational law areas

The foundation of YAI law is organized into five areas:

* **Axioms** — the irreducible principles that define what YAI is
* **Invariants** — properties that must remain true across conforming implementations
* **Boundaries** — authority and responsibility limits across runtime layers
* **Terminology** — canonical meaning of core legal and technical terms
* **Extensions** — normative overlays that extend, but do not replace, the core law

These foundational areas live under `foundation/` and form the normative core for the rest of the repository.

## 3) Primacy of foundation

All other canonical surfaces in `yai-law` derive authority from the foundational layer.

That includes:

* runtime-layer definitions under `runtime/`
* public interfaces under `contracts/`
* machine-readable registries under `registry/`
* transversal schemas under `schema/`
* formal traceability artifacts under `formal/`
* published normative packs under `packs/`

No lower-level artifact may redefine or contradict the foundational law.

If such a conflict exists, the foundational layer prevails unless an explicit compatibility or deprecation rule states otherwise.

## 4) Relationship to implementation

The foundation does not implement behavior.

It defines the conditions under which behavior is considered conforming.

A runtime may optimize, extend, or specialize its implementation, but it may not violate the foundational law and still claim conformance.

If implementation and foundation diverge, the implementation is wrong.

## 5) Relationship to formalization

The foundational law is not replaced by formal modeling.

Formal artifacts in `formal/` exist to strengthen traceability, verification, and rigor, but they do not supersede the normative force of the foundational law unless explicitly stated by repository policy.

In other words:

* `foundation/` defines the law
* `formal/` supports validation of the law
* `contracts/`, `registry/`, and `schema/` operationalize the law

## 6) Relationship to extensions and packs

Normative extensions and published packs may refine or specialize application of the law in scoped contexts, such as compliance overlays.

They do not nullify the foundational layer.

Extensions remain subordinate to the foundational core unless an explicit authority rule states otherwise.

## 7) Conformance principle

A consumer, runtime, or downstream tool can claim conformance only if it is compatible with and subordinate to the foundational law defined in this repository.

Foundational law is therefore not optional context.
It is the root authority for every canonical YAI surface.

## 8) Navigation

For the concrete foundational corpus, see:

* `foundation/README.md`
* `foundation/axioms/`
* `foundation/invariants/`
* `foundation/boundaries/`
* `foundation/terminology/`
* `foundation/extensions/`
