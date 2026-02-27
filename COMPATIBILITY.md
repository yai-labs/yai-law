# Compatibility

Compatibility in `yai-law` is evaluated against the active law compatibility line.

Current compatibility line: `v1`.

This identifier represents the consumer-facing compatibility baseline for canonical contracts, registries, schemas, and ABI surfaces.

## Compatibility matrix

| Compatibility line | yai | yai-cli | yai-yx | Notes |
| --- | --- | --- | --- | --- |
| v1 | v0.1.x | v0.1.x | UNSET | Initial public law baseline |

## Rules

- Consumers MUST reject major compatibility-line mismatches
- Minor or patch-level repository changes may be accepted only when backward compatibility is preserved
- Every consumer release MUST record the pinned `yai-law` revision, tag, or commit used for validation
- Any upgrade that changes the active compatibility line MUST be treated as an explicit integration event
- Compatibility claims MUST be supported by the canonical artifacts in `REGISTRY.md`, `SPEC_MAP.md`, and `CHANGELOG.md`

## Interpretation

Repository release versions and compatibility lines are related, but not identical.

A repository may continue to evolve through compatible changes while remaining on the same compatibility line.  
A compatibility-line change indicates that conforming consumers may require review, adaptation, or explicit migration.

## Consumer expectations

A conforming consumer is expected to:

- pin a specific `yai-law` revision or release
- validate compatibility before upgrade
- reject unsupported compatibility lines
- record the validated baseline used for release or qualification