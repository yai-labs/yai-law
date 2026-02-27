# contracts/

`contracts/` contains the canonical public interface surfaces of `yai-law`.

These artifacts define the cross-layer contracts that downstream runtimes, tools, and clients consume directly. They are normative and must remain aligned with the foundational law, canonical registries, and canonical schemas elsewhere in the repository.

## Scope

The `contracts/` tree covers public interface surfaces such as:

* `protocol/` — wire envelope, transport, identifiers, and runtime protocol headers
* `control/` — control-plane schemas and authority-facing surfaces
* `cli/` — CLI-facing command and interface notes
* `vault/` — vault ABI headers and schema surfaces
* `providers/` — provider-facing schema contracts
* `compliance/` — compliance-facing contract attachments and references

## Normative role

Artifacts under `contracts/` are normative where they define canonical headers, schemas, or explicitly binding mappings.

These surfaces are consumed directly by implementations and validation tooling.
They must not drift from:

* `foundation/` for normative primacy
* `registry/` for canonical machine-readable registries
* `schema/` for transversal canonical schemas
* `formal/` for traceability and proof-support alignment

If a contract surface conflicts with foundational law or canonical registry/schema artifacts, the higher-authority artifact prevails.

## Relationship to runtime surfaces

`contracts/` does not contain every runtime-layer schema in the repository.

Runtime-layer-specific surfaces that belong to the runtime authority model live under `runtime/`, including engine-layer and mind-layer artifacts where those are modeled as layer-bound rather than cross-layer public interfaces.

## Navigation

* `../SPEC_MAP.md` — canonical navigation map
* `../REGISTRY.md` — canonical registries and ID allocation rules
* `../COMPATIBILITY.md` — compatibility expectations
* `../VERSIONING.md` — release and versioning policy
