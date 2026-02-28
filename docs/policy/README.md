# Docs Policy

`docs/` is the informative documentation layer of `yai-law`.

It exists to explain, index, and support consumption of the canonical law surface defined elsewhere in the repository. It does not create or replace normative authority.

## Role

Artifacts under `docs/` are informative.

They may:

* explain repository structure
* clarify how canonical artifacts are intended to be read or consumed
* support generated documentation flows
* point readers to canonical indexes and policy documents

They must not redefine law.

## Rules

* Keep links relative and repository-local where possible
* Do not duplicate normative contract text unnecessarily
* Point readers to canonical sources such as `SPEC_MAP.md`, `REGISTRY.md`, `COMPATIBILITY.md`, and `VERSIONING.md`
* Keep explanatory notes subordinate to canonical repository artifacts
* If an informative note conflicts with a normative artifact, the normative artifact prevails

## Normative sources

Normative authority lives outside `docs/`, especially in:

* `foundation/`
* `runtime/`
* `contracts/`
* `registry/`
* `schema/`
* `formal/`
* `packs/`

## Documentation discipline

Documentation should improve navigation and interpretation without introducing ambiguity, drift, or parallel sources of truth.

A good documentation artifact explains the law.
It does not compete with it.
