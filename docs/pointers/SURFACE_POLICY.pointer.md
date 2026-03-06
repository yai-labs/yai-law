# Surface Policy v1 Pointer

Status: active
Class: normative pointer
Owner: yai-law

## Purpose
This policy defines command exposure rules across default help, `--all`, and `--plumbing` views.
It prevents uncontrolled surface growth.

## Surface Dimensions

Every command record is classified by:
- `surface`: `surface | ancillary | plumbing`
- `visibility`: `public | advanced | internal | hidden`
- `stability`: `stable | experimental | planned | deprecated`
- `command_scope`: `global | workspace | session | runtime`
- `audience`: `user | operator | developer | internal`

## Exposure Rules

Default help (`yai help` / `yai --help`) MAY expose a command only when:
- `surface=surface`
- `visibility=public`
- `stability in {stable, experimental}`
- `audience in {user, operator}`
- `hidden=false`

`yai help --all` MAY include:
- `surface=surface` and `surface=ancillary`
- `visibility in {public, advanced}`
- excludes `hidden=true` by default

`yai help --plumbing` MAY include:
- `surface=plumbing`
- and explicit internal/hidden diagnostics surfaces when requested

## Workspace Scope Gate

For `command_scope=workspace` commands:
1. explicit `--ws-id` wins
2. current workspace binding may be used
3. unresolved workspace context must fail deterministically

## Promotion Rules

A command may be promoted to default surface only when:
- canonical path is stable
- reply contract is coherent
- scope/effect/authority classes are set
- implementation status is coherent with stability
- minimum tests exist
- docs/help exposure is defined

## De-Exposure Rules

A command may be moved out of default surface when:
- moved to `deprecated` lifecycle
- replaced by a canonical path
- reclassified to `ancillary` or `plumbing`
- visibility downgraded from `public` to `advanced/internal`

Legacy aliases may remain for compatibility windows but must not dominate default help.
