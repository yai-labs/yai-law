# Graph v1

`GRAPH_V1.md` defines the canonical graph-facing law note for the currently modeled graph surface under `runtime/mind/graph/`.

This note explains the intended graph structure, persistence model, constraints, and authority posture associated with Graph v1. It is subordinate to the canonical schema and binding artifacts in the same directory.

## 1) Scope

Graph v1 defines the currently modeled canonical graph surface for the Mind layer.

It describes a layered, deterministic graph model intended to support governed execution without granting the graph surface independent authority over kernel, vault, or other higher-authority runtime layers.

Graph v1 is therefore a constrained law-facing graph surface, not an unrestricted knowledge substrate.

## 2) Canonical data model

### Semantic layer (source of truth)

The semantic layer is the canonical persisted graph layer.

#### Node

* `id` — stable identifier, format: `node:<kind>:<slug>`
* `kind` — semantic type
* `meta` — JSON object for associated metadata
* `last_seen` — Unix epoch seconds

#### Edge

* `id` — stable identifier, format: `edge:<rel>:<src>:<dst>`
* `src` — source node identifier
* `dst` — destination node identifier
* `rel` — relationship type
* `weight` — floating-point edge weight

The semantic store is the single source of truth for graph meaning.

### Episodic layer (derived)

The episodic layer is derived.

* Ingests from `events.log` only
* Does not accept direct CLI writes as a canonical mutation surface

### Vector layer (derived)

The vector layer is rebuildable and derived from semantic nodes.

* Stores embeddings only
* Does not store canonical semantic meaning
* Must remain reconstructable from the semantic layer

### Activation layer (runtime only)

The activation layer is runtime-only.

* Has no canonical persistence
* Uses semantic and vector layers as inputs
* Exists to support active graph use during execution without becoming a source of truth

### Authority layer (read-only)

The authority layer is derived and read-only.

* Derived from law artifacts and trusted policy inputs
* Does not accept runtime mutation
* Must not be treated as a writable policy surface

## 3) Persistence model

Canonical persistence expectations are:

* **Semantic** — `~/.yai/run/<ws>/semantic.sqlite`
* **Episodic** — `~/.yai/run/<ws>/events.log` (append-only NDJSON)
* **Vector** — `~/.yai/run/<ws>/vector.usearch` (rebuildable)
* **Activation** — no persistence
* **Authority** — `<workspace>/deps/yai-law/contracts/control/schema/authority.json`

These paths describe the expected law-facing layout for Graph v1 and must remain aligned with the current runtime model where adopted.

## 4) Indexing and rebuildability

* Embeddings are stored in the vector layer only
* The vector index must remain rebuildable from semantic nodes
* Rebuildability is required so that the vector layer never becomes a hidden or independent semantic authority

## 5) Query model

A canonical graph-facing query pattern is:

`query_active_subgraph(query_text, k, hops=1)`

Expected behavior:

* return the top-`k` nodes by similarity from the vector layer
* apply hop expansion through the activation layer
* preserve deterministic behavior for the same declared inputs and graph state within the declared execution scope

## 6) Constraints

Graph v1 is constrained by the following requirements:

* no LLM is required
* local execution is sufficient
* outputs must remain deterministic for the same relevant inputs within declared scope
* the semantic layer remains the single source of truth
* derived layers must not silently redefine semantic meaning

## 7) Authority boundary (non-negotiable)

Graph is read-only with respect to higher-authority runtime layers.

In particular:

* Graph may read events and derived data
* Graph must never mutate kernel authority
* Graph must never mutate vault layout
* Graph must never mutate runtime state through an ungoverned path
* Any policy or action proposal must be mediated through kernel enforcement, not graph-side writes

Graph participation in governed execution does not grant graph authority over the execution substrate.

## 8) Relationship to canonical law

Graph v1 is subordinate to:

* `runtime/mind/graph/schema/graph.v1.json`
* `runtime/mind/graph/BINDING.md`
* `foundation/invariants/I-002-determinism.md`
* `foundation/invariants/I-003-governance.md`
* `foundation/invariants/I-005-abstract-cost-accountability.md`
* `foundation/boundaries/L3-mind.md`

If this note conflicts with the canonical schema, binding, or foundational law, the higher-authority artifact prevails.
