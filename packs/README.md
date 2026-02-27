# packs/

`packs/` contains published normative overlays of `yai-law`.

These packs package scoped, versioned, machine-readable law material for downstream consumption without redefining the foundational core of the repository.

## Scope

Artifacts under `packs/` include publishable overlays such as:

* compliance packs
* domain-specific packaged law material, where introduced
* versioned machine-readable defaults, taxonomies, and pack metadata

## Normative role

Published packs are normative within their declared scope.

They do not replace:

* `foundation/` as the normative core
* `registry/` and `schema/` as canonical machine-readable references
* `contracts/` and `runtime/` as canonical law surfaces

Instead, they apply or specialize those canonical surfaces for a bounded domain or policy context.

## Current published area

* `compliance/` — published compliance overlays

Current versioned pack lineage includes:

* `packs/compliance/gdpr-eu/2026Q1/`

## Publication discipline

Packs must be:

* versioned
* machine-readable
* scoped
* compatible with the canonical law they extend
* traceable through repository indexes and release discipline

A pack that conflicts with foundational law or canonical registry/schema artifacts is invalid unless an explicit higher-authority rule states otherwise.

## Consumer expectation

Consumers should pin pack revisions deliberately and treat them as normative overlays, not as standalone replacements for the repository core.
