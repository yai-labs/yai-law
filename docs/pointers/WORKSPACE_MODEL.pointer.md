# Workspace Model v2 (Pointer)

This document defines the Workspace Model v2 used across `yai-law`, `yai`, `yai-sdk`, and `yai-cli`.

## 1. Workspace identity

A workspace is a first-class runtime entity identified by `ws_id`.
It is not a CLI flag; it is a kernel-owned object with deterministic lifecycle and root binding.

Required model fields:

- `ws_id`
- `state`
- `root_path`
- `created_at`
- `updated_at`
- `exists`
- ownership semantics (`kernel` is authoritative owner)
- attachment placeholders (`attachments` / session bindings)
- metadata and capabilities (minimal, extensible)

## 2. Ownership and boundaries

- `root` mediates and routes commands.
- `kernel` validates, persists, and owns workspace runtime state.
- `cli` and `sdk` consume workspace state; they never own runtime truth.

## 3. Lifecycle model

State classes:

- `created`
- `active`
- `attached` (future-ready)
- `suspended` (future-ready)
- `destroyed`

Minimum operational states required now:

- `created`
- `active`
- `destroyed`

## 4. Root path model

`root_path` is part of the workspace model and must satisfy:

- canonicalized path
- no traversal (`..`) acceptance
- persisted with workspace state
- deterministic fallback when implicit

Modes:

- implicit root (runtime-derived)
- explicit root (`--root`)
- re-associated/pre-existing root (compatibility path)

## 5. Current workspace binding model

Current workspace is a user/session binding, not runtime ownership.

Resolution precedence:

1. explicit `--ws-id`
2. current workspace binding
3. unresolved context -> deterministic error for workspace-scoped commands

Binding invalidation:

- if bound workspace is destroyed or unavailable, binding becomes invalid
- CLI must report invalid binding clearly
- runtime remains the source of truth

## 6. Command scope interaction

Commands classified as `command_scope=workspace` MUST resolve effective workspace with the precedence above.
Global commands MUST NOT require current binding.

## 7. Invariants

- create -> status/list consistency
- destroy -> missing/destroyed consistency
- no cross-workspace side effects by default
- workspace isolation is primary tenant boundary for runtime operations

## 8. Forward compatibility

Workspace is the natural future container for:

- graph state
- mind state
- execution sessions
- workspace artifacts
- runtime-local bundle/query context
