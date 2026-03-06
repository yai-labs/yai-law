# YAI CLI Output Contract v1

This document defines the canonical output contract consumed by SDK and CLI.

## Source Of Truth

- Schema: `contracts/control/schema/exec_reply.v1.json`
- Envelope type: `yai.exec.reply.v1`

## Canonical Shape

Required canonical fields:

- `outcome`: `ok|warn|deny|fail`
- `code`: canonical reason code
- `summary`: one-line summary
- `hint`: array of operator hints
- `data`: result object
- `trace`: traceability object
- `meta`: execution metadata object

`trace` fields:

- `trace_id`
- `claim_id`
- `workspace_id`
- `law_ref`
- `evidence_ref`

`meta` fields:

- `version`
- `ts`
- `duration_ms`
- `target_plane`
- `command_id`

## Compatibility

For transition, the schema accepts legacy execution fields (`status/reason/...`).
CLI and SDK must normalize replies into canonical shape before rendering.

## Determinism Rules

- Human output MUST be a deterministic rendering of ExecReply.
- JSON output MUST match ExecReply schema exactly.
