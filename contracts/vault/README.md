# Vault

`contracts/vault/` contains the canonical vault-facing ABI surface of `yai-law`.

These artifacts define the machine-readable and C-facing contracts used to represent vault ABI structure and compatibility expectations across downstream consumers.

## Scope

The vault surface covers:

* vault ABI structure
* vault-facing canonical headers
* schema-level vault compatibility contracts

## Normative artifacts

Canonical vault artifacts:

* `schema/vault_abi.json`
* `include/yai_vault_abi.h`

## Normative role

Artifacts in this directory are normative.

They must remain aligned with:

* `foundation/boundaries/` for vault-layer authority boundaries
* `foundation/invariants/` for determinism and governance constraints
* `registry/` for canonical machine-readable references
* `formal/` where vault-related behavior is modeled or traced

If a downstream implementation diverges from these vault ABI contracts, the implementation is non-conforming.

## Versioning and compatibility rules

* Vault ABI changes are compatibility-critical
* Breaking ABI changes require compatibility review and an appropriate repository version change
* Additive compatible fields or structures require version review and `CHANGELOG.md` coverage
* Identifier, type, or semantic changes that affect consumer interoperability must be treated as compatibility-sensitive

## Consumers

Typical consumers include:

* `yai`
* `yai-cli`
* `yai-yx`
* validation and qualification tooling that depends on canonical vault ABI surfaces

## Change discipline

A vault-surface change must update, as applicable:

* canonical vault artifacts in this directory
* `REGISTRY.md`
* `SPEC_MAP.md`
* `CHANGELOG.md`
* related formal or validation artifacts when semantics change

Silent drift between vault implementations and canonical ABI contracts is non-compliant by definition.
