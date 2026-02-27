# Protocol

`contracts/protocol/` contains the canonical protocol and transport surfaces of `yai-law`.

These artifacts define the shared wire, envelope, transport, session, role, audit, and identifier contracts consumed across YAI implementations and validation tooling.

## Scope

The protocol surface includes:

* wire and envelope structure
* transport-facing constants and contracts
* canonical protocol identifiers
* error and authorization-related protocol definitions
* role and session contracts
* audit-facing protocol definitions
* runtime-bound protocol support under `runtime/`

## Normative artifacts

Canonical headers:

* `include/protocol.h`
* `include/transport.h`
* `include/yai_protocol_ids.h`
* `include/errors.h`
* `include/auth.h`
* `include/roles.h`
* `include/session.h`
* `include/audit.h`

Runtime-bound protocol artifact:

* `runtime/include/rpc_runtime.h`

## Normative role

Artifacts in this directory are normative.

The header files are canonical interface definitions for protocol-facing consumers.
They must remain aligned with:

* `foundation/` for normative primacy
* `registry/` for canonical machine-readable references
* `formal/` for traceability and formal alignment
* `vectors/` for conformance validation

If a downstream implementation diverges from these contracts, the implementation is non-conforming.

## Versioning and compatibility rules

* Protocol constants, identifiers, envelope rules, and required semantics are compatibility-critical
* Breaking changes require compatibility review and an appropriate repository version change
* New identifiers require coordinated updates to canonical registries, protocol headers, and `CHANGELOG.md`
* Additive changes must preserve backward compatibility within the active compatibility line

## Consumers

Typical consumers include:

* `yai`
* `yai-cli`
* `yai-yx`
* validation and qualification tooling that depends on canonical protocol surfaces

## Change discipline

A protocol change must update, as applicable:

* canonical headers in this directory
* `REGISTRY.md`
* `SPEC_MAP.md`
* `CHANGELOG.md`
* relevant registries and schemas
* vectors and validation artifacts when behavior changes

Silent protocol drift is non-compliant by definition.
