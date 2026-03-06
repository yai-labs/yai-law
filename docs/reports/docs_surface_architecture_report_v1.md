# Docs + Surface Architecture Report v1

Status: active
Owner: yai-law
Scope: cross-repo (`yai-law`, `yai-sdk`, `yai-cli`, `yai`)

## 1) Document Class Matrix

### yai-law
- Normative: contracts, schema, registry, architecture pointers
- Informative: docs navigation/pointers
- Source role: normative authority

### yai-sdk
- Programmatic: API surface, compatibility, versioning
- Informative: integration guidance
- Source role: SDK surface authority

### yai-cli
- Operational: command usage, output modes, help behavior
- Informative: operator onboarding
- Source role: CLI UX/usage authority

### yai
- Runtime procedural: runbooks, lifecycle, runtime architecture procedures
- Informative: platform implementation onboarding
- Source role: runtime implementation behavior authority

## 2) Truth-Boundary Matrix

- Command/reply/workspace normative semantics -> `yai-law`
- SDK API/ABI discipline -> `yai-sdk`
- CLI usage/help/render semantics -> `yai-cli`
- Runtime procedures/runbooks -> `yai`

## 3) Surface Exposure Matrix (v1)

Default help:
- `surface=surface`
- `visibility=public`
- `stability in {stable, experimental}`
- `audience in {user, operator}`

`--all`:
- includes `ancillary`
- includes `advanced`

`--plumbing`:
- includes `plumbing`
- may include internal diagnostics surfaces

## 4) Drift Risks Identified

1. Cross-repo duplication of policy prose.
2. Mixed terminology (`group` legacy vs `entrypoint/topic/op`).
3. Operational docs occasionally containing normative-level language.
4. README drift where repos explain topics outside their authority.

## 5) Remediation Applied in this wave

- Added `DOCS_ARCHITECTURE.pointer.md` in `yai-law`.
- Added `SURFACE_POLICY.pointer.md` in `yai-law`.
- Aligned README/doc entrypoints in SDK/CLI/runtime to point to proper authorities.
- Corrected CLI docs path references to canonical law registry locations.

## 6) Residual Items

1. `yai-cli` `help_guardrail.sh` still expects a legacy help header string.
2. Some runtime runbooks can be further tagged with explicit document class labels.
3. Future docs linting can enforce class labels in front matter.

## 7) Governance Rule

Any semantic conflict across docs must be resolved by authority class order:
`normative > programmatic > operational > runtime_procedural > intro_navigational`.
