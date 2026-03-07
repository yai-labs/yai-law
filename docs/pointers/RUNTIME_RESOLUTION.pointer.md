# Runtime Resolution & Path Authority Pointer

## Intent
This document defines the normative concepts used by runtime/path discovery across YAI repositories.

## Normative Concepts
- `runtime_home`: canonical base for runtime sockets, pid files, and runtime logs.
- `install_root`: canonical root used to discover runtime binaries.
- `workspace_root`: canonical workspace filesystem root.
- `control_endpoint`: canonical root control socket endpoint.
- `deploy_mode`: one of `repo_dev`, `local_install`, `packaged`, `qualification`.

## Resolution Precedence
1. Explicit CLI/config override
2. Environment override
3. Canonical resolver defaults
4. Deterministic failure

## Environment Override Policy
Allowed overrides are explicit and bounded. Examples:
- `YAI_RUNTIME_HOME`
- `YAI_INSTALL_ROOT`
- `YAI_ROOT_SOCK`
- Runtime binary overrides (`YAI_BOOT_BIN`, `YAI_ROOT_BIN`, `YAI_KERNEL_BIN`, `YAI_ENGINE_BIN`)

## Constraints
- Machine-specific absolute paths are forbidden in production runtime callers.
- Repository-relative binary assumptions are allowed only in `repo_dev` mode, and only via canonical resolver APIs.
- Command surfaces must consume shared resolver APIs; they must not maintain local fallback lists.

## Binding
Programmatic implementation details are owned by `yai-sdk` runtime/path resolver APIs.
