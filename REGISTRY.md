# Registry

This registry defines the canonical location of normative artifacts and the rules for allocating IDs.

## ID Registry

The authoritative ID registry lives in `specs/protocol/include/yai_protocol_ids.h`.

Rules:
- IDs are never reused.
- Reserved ranges must remain reserved and documented in the header.
- New IDs require a corresponding spec change and a `CHANGELOG.md` entry.
- Any change that adds or reclassifies IDs must be reviewed for compatibility impact.

## Normative JSON Contracts

- `specs/cli/schema/commands.v1.json`
- `specs/cli/schema/commands.schema.json`
- `compliance/compliance.context.v1.json`
- `compliance/retention.policy.v1.json`
- `compliance/packs/gdpr-eu/2026Q1/pack.meta.json`
- `compliance/packs/gdpr-eu/2026Q1/retention.defaults.json`
- `compliance/packs/gdpr-eu/2026Q1/taxonomy.data_classes.json`
- `compliance/packs/gdpr-eu/2026Q1/taxonomy.legal_basis.json`
- `compliance/packs/gdpr-eu/2026Q1/taxonomy.purposes.json`
- `specs/control/schema/control_plane.v1.json`
- `specs/control/schema/authority.json`
- `specs/engine/schema/engine_cortex.v1.json`
- `specs/graph/schema/graph.v1.json`
- `specs/providers/schema/providers.v1.json`
- `specs/vault/schema/vault_abi.json`

## Normative C Headers

- `specs/protocol/include/protocol.h`
- `specs/protocol/include/transport.h`
- `specs/protocol/include/yai_protocol_ids.h`
- `specs/protocol/include/errors.h`
- `specs/protocol/include/auth.h`
- `specs/protocol/include/roles.h`
- `specs/protocol/include/session.h`
- `specs/protocol/include/audit.h`
- `specs/protocol/runtime/include/rpc_runtime.h`
- `specs/vault/include/yai_vault_abi.h`

## Conformance Vectors

Vectors are informative but should be updated when normative behavior changes.

- `vectors/transport_vectors.json`
- `vectors/auth_vectors.json`
- `vectors/audit_vectors.json`
