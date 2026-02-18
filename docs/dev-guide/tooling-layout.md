# Tooling Layout Migration

## Scope

Repository: `yai-specs`
Target canonical layout: `tools/*` and `tests/*`

Baseline check on 2026-02-18:

- `scripts/` directories found: `0`
- `scripts/` references found: `0`

## Mapping Table

| OLD_PATH | NEW_PATH | CLASS | NOTES |
|---|---|---|---|
| `(none found under scripts/)` | `(no-op)` | entrypoint | No legacy entrypoint in this repository. |
| `(none found under scripts/)` | `(no-op)` | ops | No legacy gate/suite/verify scripts in this repository. |
| `(none found under scripts/)` | `(no-op)` | dev | No legacy dev helpers in this repository. |
| `(none found under scripts/)` | `(no-op)` | release | `tools/release/bump_version.sh` already canonical. |
| `(none found under scripts/)` | `(no-op)` | data | No data tooling migration required from `scripts/`. |
| `(none found under scripts/)` | `(no-op)` | test | No legacy script-based tests found. |
