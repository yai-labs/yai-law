# Versioning

`yai-law` follows Semantic Versioning for repository releases.

Version changes apply to repository tags and to explicitly versioned canonical artifacts where applicable.

Public release baseline: `v0.1.0` (2026-02-17).

## Repository version scheme

- `MAJOR` — incompatible normative or contract change
- `MINOR` — backward-compatible additive normative change
- `PATCH` — compatible corrections, clarifications, documentation updates, or non-breaking metadata changes

## Compatibility line

The repository also maintains an explicit law compatibility line.

Current compatibility line: `v1`.

Important:

- Repository release versions (`v0.1.0`, `v0.1.1`, ...) and the compatibility line (`v1`) are related but not identical
- The repository may remain in `0.x` release development while exposing a stable compatibility line for public law consumption
- A repository version bump does not automatically imply a compatibility-line change

## What is breaking

A change is breaking when a conforming consumer can no longer interoperate or validate successfully without code, contract, or enforcement changes.

Examples include:

- removing required fields, commands, or artifact roles
- changing required types, semantics, or validation behavior
- altering ABI or protocol constants
- changing wire-envelope rules
- reusing identifiers or changing identifier meaning
- changing registry or schema behavior in a way that invalidates previously conforming consumers

## What is non-breaking

Examples of non-breaking changes include:

- additive fields or commands introduced under backward-compatible rules
- new optional schemas or artifact roles
- clarifications that do not alter contract meaning
- documentation improvements
- additional validation vectors that do not redefine normative behavior

## Pinning and releases

- Consumers MUST pin a specific repository revision or release tag
- Pin updates MUST be reviewed against `CHANGELOG.md`, `COMPATIBILITY.md`, and the canonical indexes
- Tags SHOULD follow `vMAJOR.MINOR.PATCH`
- Breaking changes MUST be reflected both in release versioning and in compatibility evaluation
- Releases that affect public law surfaces SHOULD include explicit migration or review notes when relevant