# foundation/

`foundation/` contains the foundational normative corpus of `yai-law`.

These documents define the core law that all other canonical surfaces in the repository derive from or must remain compatible with.

## Scope

The foundational corpus is organized into five normative areas:

* `axioms/` — irreducible principles that define the YAI law model
* `invariants/` — properties that must remain true across conforming implementations
* `boundaries/` — authority and responsibility limits across runtime layers
* `terminology/` — canonical meaning of legal and technical terms
* `extensions/` — scoped normative extensions subordinate to the foundational core

## Normative role

Artifacts under `foundation/` are normative.

They are not implementation guides and they are not optional commentary.
They define the legal and conceptual basis for the rest of the repository, including:

* `runtime/`
* `contracts/`
* `registry/`
* `schema/`
* `formal/`
* `packs/`

If a lower-level artifact conflicts with the foundational corpus, the foundational corpus prevails unless an explicit compatibility or deprecation rule states otherwise.

## Registry discipline

Foundational documents MUST reference canonical machine-readable artifacts through the current canonical locations in:

* `registry/`
* `registry/schema/`
* `schema/`
* `packs/`

Legacy paths and deprecated authority locations must not be introduced in foundational documents.

## Navigation

* `axioms/`
* `invariants/`
* `boundaries/`
* `terminology/`
* `extensions/`

For the root-level statement of the foundational model, see `FOUNDATION.md`.
