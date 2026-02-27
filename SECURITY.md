# Security Policy

## Reporting

Report potential security issues privately through the designated maintainer security channel.

Do not disclose exploit details, proof-of-concept material, or weaponized reproduction steps publicly before coordinated triage and remediation.

## Scope

This repository defines canonical law surfaces for YAI. Security issues in scope therefore include weaknesses that can cause unsafe or incorrect downstream behavior even when no runtime exploit exists in this repository itself.

Examples include:

- protocol parsing or validation ambiguity
- malformed or unsafe contract definitions
- authorization, role, or authority-surface bypasses in canonical schemas or headers
- schema inconsistencies that enable unsafe consumer interpretation
- registry drift or identifier collisions
- compatibility changes that can silently break validation or enforcement behavior
- published pack errors that could cause incorrect compliance or policy enforcement

## Out of scope

The following are generally out of scope for this repository unless they originate from the canonical artifacts defined here:

- runtime implementation bugs in consumer repositories
- operational incidents in downstream deployments
- vulnerabilities caused solely by local integrator misuse
- private environment misconfiguration outside the repository contents

## Threat model notes

`yai-law` is an authority repository. The primary security concern is not remote code execution in the repository itself, but corruption, ambiguity, or misuse of canonical law artifacts that downstream consumers rely on.

Spec tampering is only effective if a consumer accepts untrusted, unpinned, or unverified law artifacts.

Consumers are therefore expected to:

- pin repository revisions explicitly
- verify provenance and integrity before adoption
- review compatibility impact before upgrade
- validate downstream conformance after upgrade

## Coordinated remediation

When a valid issue affects canonical contracts, schemas, registries, or packs:

1. the issue is triaged privately
2. impact on consumers and compatibility is assessed
3. corrective changes are prepared
4. release notes and changelog entries are updated as needed
5. public disclosure happens only after remediation guidance is available

## Repository hygiene

- Never commit secrets, tokens, credentials, or private keys
- Keep examples, fixtures, and vectors synthetic and non-sensitive
- Avoid embedding private operational details in notes or examples
- Treat machine-readable artifacts as security-relevant authority surfaces

## Consumer responsibility

Downstream consumers must not treat unreviewed snapshots of this repository as trusted inputs by default.

A consumer that does not pin, verify, and validate `yai-law` before adoption is operating outside the intended trust model.