# YAI Law — Canonical Contracts and Constraints

YAI = “YAI Ain’t Intelligence”  
Law is where intelligence becomes governable.

`yai-law` is the canonical normative repository for the YAI ecosystem: contracts, schemas, ABI surfaces, policy packs, registries, and formal artifacts that define what conforming runtimes and consumers must implement.

This repository is not documentation-first. It is the source of authority that downstream consumers pin, audit, validate, and upgrade deliberately.

---

## 1) What this repository is

YAI Law is the single source of truth for:

- Wire and transport contracts
- Vault ABI and low-level state authority surfaces
- Control-plane schemas and governance-facing interfaces
- Runtime-layer constraints across boot, root, kernel, engine, and mind-facing surfaces
- Formal law artifacts: axioms, invariants, boundaries, traceability, and formal models
- Machine-readable registries and transversal schemas
- Versioned compliance packs

If a runtime, tool, or client diverges from this law, the implementation is wrong.

---

## 2) What this repository is not

- Not a playground for product experiments
- Not a best-effort reference
- Not an implementation repository
- Not a qualification/evidence repository
- Not something to copy and fork downstream casually

Consumers pin a revision and integrate it as a dependency.

---

## 3) Normative vs informative

### Normative artifacts
Normative artifacts are binding. They define contracts that must be implemented, validated, or enforced.

Examples include:

- Canonical registries (`registry/**`)
- Canonical schemas (`registry/schema/**`, `schema/**`)
- Protocol and ABI headers (`contracts/protocol/include/*.h`, `contracts/vault/include/*.h`)
- Foundational law (`foundation/**`)
- Published normative packs (`packs/**`)
- Validation vectors (`vectors/**`)

### Informative artifacts
Informative artifacts explain, map, or clarify the law.

Examples include:

- Section README files
- Notes and explanatory markdown
- Navigation and mapping documents, where not explicitly marked normative

If there is a conflict, normative artifacts win.

---

## 4) Repository structure

- `authority/` — publication, status, compatibility, and deprecation rules
- `foundation/` — axioms, invariants, boundaries, terminology, normative extensions
- `runtime/` — canonical runtime-layer model for boot, root, kernel, engine, and mind
- `contracts/` — public cross-layer interfaces and related bindings
- `registry/` — canonical machine-readable registries and registry-bound schemas
- `schema/` — transversal schemas for artifacts and policy payloads
- `formal/` — formal models, configurations, and traceability artifacts
- `packs/` — versioned normative overlays, including compliance packs
- `vectors/` — validation vectors
- `tools/` — repository validation and release tooling

---

## 5) How to consume (pinning model)

Treat this repository as a pinned dependency:

- Git submodule, preferred for auditability, or
- Vendored snapshot with a recorded commit hash

Upgrades are deliberate:

1. Read `VERSIONING.md`
2. Check `COMPATIBILITY.md`
3. Review `CHANGELOG.md`
4. Validate against your conformance gates before adoption

Consumers do not redefine law locally. They pin, integrate, validate, and upgrade with intent.

---

## 6) Canonical indexes

- `SPEC_MAP.md` — authoritative structure and navigation map
- `REGISTRY.md` — canonical registries and allocation rules
- `VERSIONING.md` — versioning and compatibility policy
- `COMPATIBILITY.md` — consumer compatibility expectations
- `CHANGELOG.md` — contract and surface change log
- `SECURITY.md` — disclosure and security policy

---

## 7) Conformance model

`yai-law` is consumed by implementation and program repositories.

- Runtime repositories such as `yai` conform to the law defined here
- Program and qualification repositories such as `yai-ops` validate and package evidence against the law defined here

Authority originates here.  
Conformance is measured elsewhere.

---

## 8) Status

Unless explicitly marked otherwise, published artifacts in this repository are treated as canonical public law for the corresponding YAI surface.