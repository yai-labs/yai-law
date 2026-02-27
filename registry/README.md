# registry/

`registry/` contains the canonical machine-readable registries of `yai-law`.

These registries define stable public allocation surfaces consumed by tooling, validation logic, and downstream implementations.

## Scope

The registry layer contains:

- versioned registries under `registry/`
- registry-bound JSON Schemas under `registry/schema/`
- identifier-related supporting material under `registry/ids/`

## Normative role

Artifacts in `registry/` are normative.

They define canonical machine-readable references for:

- primitives
- commands
- artifact roles

These registries are consumed directly by tooling and by downstream repositories that need stable law-aligned interfaces.

## Relationship to other repository layers

`registry/` works together with:

- `foundation/` for normative primacy
- `contracts/` for public interface surfaces
- `schema/` for transversal artifact and policy schemas
- `formal/` for traceability and proof-support alignment

If a human-readable note conflicts with a canonical registry entry, the registry entry prevails unless an explicit higher-authority rule states otherwise.

## Contents

- `primitives.v1.json` — canonical primitives registry
- `commands.v1.json` — canonical command registry
- `artifacts.v1.json` — canonical artifact-role registry
- `schema/` — JSON Schemas validating registry structure
- `ids/` — supporting identifier notes and allocation context

For repository-wide registry interpretation, see `../REGISTRY.md`.