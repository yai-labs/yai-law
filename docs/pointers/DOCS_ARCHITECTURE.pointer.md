# Docs Architecture v1 Pointer

Status: active
Class: normative pointer
Owner: yai-law

## Purpose
This document defines where documentation truth lives across the YAI repositories.
It prevents semantic drift between law, SDK, CLI, and runtime docs.

## Documentation Classes

1. `normative`
- Defines contracts, policies, schemas, invariants.
- Primary owner: `yai-law`.

2. `programmatic`
- Defines API surface, module boundaries, SDK compatibility behavior.
- Primary owner: `yai-sdk`.

3. `operational`
- Defines command usage, help behavior, output modes, operator-facing workflows.
- Primary owner: `yai-cli`.

4. `runtime_procedural`
- Defines runtime behavior, lifecycle procedures, runbooks, deployment/ops procedure.
- Primary owner: `yai`.

5. `intro_navigational`
- Defines orientation and learning paths.
- Never overrides normative/programmatic/operational/runtime truth.

## Truth-Boundary Matrix

- `yai-law` is authoritative for:
  - command taxonomy and command architecture
  - reply architecture
  - workspace model (normative side)
  - protocol and schema semantics
  - surface classification and promotion/deprecation policy

- `yai-sdk` is authoritative for:
  - SDK public API and ABI discipline
  - SDK compatibility/versioning behavior
  - programmatic catalog/reply/context models

- `yai-cli` is authoritative for:
  - command UX/help behavior
  - output/render modes
  - watch/interactivity behavior
  - workspace operator ergonomics

- `yai` is authoritative for:
  - runtime implementation behavior
  - root/kernel/engine operational procedures
  - runbooks and lifecycle operations

## Cross-Repo Linking Rules

1. Explain locally, define centrally.
2. If normative semantics are required, link to `yai-law` instead of duplicating.
3. If SDK API behavior is required, link to `yai-sdk/docs/*`.
4. If CLI usage behavior is required, link to `yai-cli/docs/guide/*`.
5. If runtime procedure is required, link to `yai/docs/program/23-runbooks/*`.
6. Pointer docs must remain concise and stable.

## Duplication Avoidance

- Do not copy contract tables across repos.
- Do not duplicate full command architecture in SDK/CLI docs.
- Do not duplicate SDK API contracts in runtime docs.
- Do not place normative policy text in runbooks.

## Update Responsibility

- A repo modifying semantics must update its own source-of-truth docs.
- Other repos update only pointers and short explanatory text.
- Conflicts are resolved by authoritative source class:
  - normative > programmatic > operational > runtime_procedural > intro_navigational.
