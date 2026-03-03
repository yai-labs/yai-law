#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CMDS = ROOT / "registry" / "commands.v1.json"
PRIMS = ROOT / "registry" / "primitives.v1.json"
PRIMS_SCHEMA = ROOT / "registry" / "schema" / "primitives.v1.schema.json"
REGISTRY_MD = ROOT / "REGISTRY.md"
SPEC_MAP_MD = ROOT / "SPEC_MAP.md"
CLI_README = ROOT / "contracts" / "cli" / "README.md"

GROUPS = [
    "boot", "bundle", "control", "engine", "governance", "inspect", "kernel",
    "lifecycle", "memory", "mind", "orch", "root", "substrate", "verify",
]
TARGET_PER_GROUP = 200

MISSING_PRIMITIVES = {
    "O-006": {
        "layer": 2,
        "family": "Orchestration",
        "domain": "Bundles",
        "name": "Bundle Assemble",
        "definition": "Assemble bundle payloads and manifests for governed delivery.",
        "ops": ["compose", "validate", "emit"],
        "depends_on": ["S-005", "S-011", "T-012"],
        "determinism": "deterministic",
        "failure_modes": ["E_BUNDLE_COMPOSE", "E_BUNDLE_VALIDATE"],
        "cli": {"canonical_id": "yai.bundle.bundle", "group": "bundle", "name": "bundle", "alias": "bundle-bundle"},
    },
    "O-007": {
        "layer": 2,
        "family": "Orchestration",
        "domain": "Verification",
        "name": "Verification Run",
        "definition": "Execute deterministic verification workflow and emit evidence pointers.",
        "ops": ["run", "report", "seal"],
        "depends_on": ["T-012", "S-014", "S-017"],
        "determinism": "deterministic",
        "failure_modes": ["E_VERIFY_FAIL", "E_VERIFY_INCOMPLETE"],
        "cli": {"canonical_id": "yai.verify.verify", "group": "verify", "name": "verify", "alias": "verify-verify"},
    },
    "T-016": {
        "layer": 1,
        "family": "Control",
        "domain": "Governance",
        "name": "Claim Registry",
        "definition": "Claim registry resolution for governance assertions and review.",
        "ops": ["resolve", "list", "bind"],
        "depends_on": ["S-007", "S-014"],
        "determinism": "deterministic",
        "failure_modes": ["E_CLAIM_UNKNOWN", "E_CLAIM_BIND"],
        "cli": {"canonical_id": "yai.governance.claim", "group": "governance", "name": "claim", "alias": "governance-claim"},
    },
    "T-017": {
        "layer": 1,
        "family": "Control",
        "domain": "Governance",
        "name": "Assertion Engine",
        "definition": "Evaluate governance assertions with deterministic reason codes.",
        "ops": ["assert", "explain", "diff"],
        "depends_on": ["T-016", "S-014"],
        "determinism": "deterministic",
        "failure_modes": ["E_ASSERT_FAIL", "E_ASSERT_INVALID"],
        "cli": {"canonical_id": "yai.governance.assert", "group": "governance", "name": "assert", "alias": "governance-assert"},
    },
    "T-018": {
        "layer": 1,
        "family": "Control",
        "domain": "Governance",
        "name": "Control Set",
        "definition": "Resolve and apply governance control sets for runtime decisions.",
        "ops": ["resolve", "apply", "audit"],
        "depends_on": ["T-016", "S-013"],
        "determinism": "deterministic",
        "failure_modes": ["E_CONTROLSET_MISSING", "E_CONTROLSET_INVALID"],
        "cli": {"canonical_id": "yai.governance.controls", "group": "governance", "name": "controls", "alias": "governance-controls"},
    },
    "T-020": {
        "layer": 1,
        "family": "Control",
        "domain": "Governance",
        "name": "Exception Handling",
        "definition": "Governed exception request and reconciliation lifecycle.",
        "ops": ["request", "review", "close"],
        "depends_on": ["T-016", "S-017"],
        "determinism": "deterministic",
        "failure_modes": ["E_EXCEPTION_DENIED", "E_EXCEPTION_INVALID"],
        "cli": {"canonical_id": "yai.governance.exception", "group": "governance", "name": "exception", "alias": "governance-exception"},
    },
    "T-022": {
        "layer": 1,
        "family": "Control",
        "domain": "Reporting",
        "name": "Report Emit",
        "definition": "Deterministic report emission and artifact linking.",
        "ops": ["build", "emit", "publish"],
        "depends_on": ["S-005", "S-011", "S-017"],
        "determinism": "deterministic",
        "failure_modes": ["E_REPORT_EMIT", "E_REPORT_SCHEMA"],
        "cli": {"canonical_id": "yai.orch.report", "group": "orch", "name": "report", "alias": "orch-report"},
    },
}


def load(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def dump(p: Path, obj):
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def derive_template(group: str, cmds: list[dict]) -> dict:
    group_cmds = [c for c in cmds if c.get("group") == group]
    if group_cmds:
        seed = sorted(group_cmds, key=lambda c: c.get("id", ""))[0]
        return {
            "args": seed.get("args", []),
            "outputs": seed.get("outputs", ["json"]),
            "side_effects": seed.get("side_effects", ["rpc_call"]),
            "law_hooks": seed.get("law_hooks", ["I-001", "I-002"]),
            "law_invariants": seed.get("law_invariants", ["I-001-traceability", "I-002-determinism"]),
            "law_boundaries": seed.get("law_boundaries", []),
            "uses_primitives": seed.get("uses_primitives", ["S-016", "T-003"]),
        }
    return {
        "args": [
            {"name": "ws", "flag": "--ws", "type": "string", "required": False},
            {"name": "json", "flag": "--json", "type": "bool", "required": False, "default": False},
        ],
        "outputs": ["json"],
        "side_effects": ["rpc_call"],
        "law_hooks": ["I-001", "I-002"],
        "law_invariants": ["I-001-traceability", "I-002-determinism"],
        "law_boundaries": [],
        "uses_primitives": ["S-016", "T-003"],
    }


def expand_commands():
    data = load(CMDS)
    cmds = data.get("commands", [])
    by_group = {g: [] for g in GROUPS}
    for c in cmds:
        g = c.get("group")
        if g in by_group:
            by_group[g].append(c)

    existing_ids = {c.get("id") for c in cmds if isinstance(c, dict)}

    generated = []
    for group in GROUPS:
        current = by_group[group]
        current_names = {c.get("name") for c in current}
        if len(current) > TARGET_PER_GROUP:
            raise SystemExit(f"group {group} already has {len(current)} > {TARGET_PER_GROUP}")
        t = derive_template(group, cmds)
        idx = 1
        while len(current) + len([x for x in generated if x["group"] == group]) < TARGET_PER_GROUP:
            name = f"op{idx:03d}"
            idx += 1
            if name in current_names:
                continue
            cid = f"yai.{group}.{name}"
            if cid in existing_ids:
                continue
            c = {
                "id": cid,
                "name": name,
                "group": group,
                "summary": f"Autogenerated {group} command {name} for registry-scale coverage.",
                "args": t["args"],
                "outputs": t["outputs"],
                "side_effects": t["side_effects"],
                "law_hooks": t["law_hooks"],
                "law_invariants": t["law_invariants"],
                "law_boundaries": t["law_boundaries"],
                "uses_primitives": t["uses_primitives"] if t["uses_primitives"] else ["S-016", "T-003"],
                "emits_artifacts": [],
                "consumes_artifacts": [],
            }
            generated.append(c)
            existing_ids.add(cid)

    cmds.extend(generated)
    cmds.sort(key=lambda c: (c.get("group", ""), c.get("name", ""), c.get("id", "")))
    data["commands"] = cmds
    dump(CMDS, data)


def expand_primitives_and_schema():
    p = load(PRIMS)
    items = p.get("primitives", [])
    have = {x.get("id") for x in items if isinstance(x, dict)}
    for pid, body in MISSING_PRIMITIVES.items():
        if pid in have:
            continue
        entry = {"id": pid}
        entry.update(body)
        items.append(entry)
    items.sort(key=lambda x: x.get("id", ""))
    p["primitives"] = items
    if "rules" not in p:
        p["rules"] = {
            "cli_alias_format": "<group>-<name>",
            "cli_canonical_id_format": "yai.<group>.<name>",
            "notes": ["Primitives define stable capability surfaces and deterministic command mappings."]
        }
    dump(PRIMS, p)

    s = load(PRIMS_SCHEMA)
    sprops = s.setdefault("properties", {})
    sprops.setdefault("generated_from", {"type": "string"})
    sprops.setdefault("rules", {"type": "object", "additionalProperties": True})
    pid = sprops["primitives"]["items"]["properties"]["id"]
    pid["pattern"] = "^(?:[STO]-\\d{3}|R-\\d{3}|CLI-\\d{3})$"
    did = sprops["primitives"]["items"]["properties"]["depends_on"]["items"]
    did["pattern"] = "^(?:[STO]-\\d{3}|R-\\d{3}|CLI-\\d{3})$"
    sprops["primitives"]["items"]["properties"].setdefault(
        "cli",
        {
            "type": "object",
            "properties": {
                "canonical_id": {"type": "string"},
                "group": {"type": "string"},
                "name": {"type": "string"},
                "alias": {"type": "string"},
                "related": {"type": "array", "items": {"type": "string"}}
            },
            "additionalProperties": True
        }
    )
    dump(PRIMS_SCHEMA, s)


def patch_docs():
    registry_add = "\n## Registry scale\n\nCurrent command registry target is **200 command_id per group** across 14 groups (total 2800 IDs).\nExpansion is generated via `tools/gen/commands_expand_v1.py` and validated via `make validate-law-registry`.\n"
    spec_add = "\n## 12) Registry scale target\n\nCommand registry is maintained at 14 groups x 200 command_id (2800 total) through generator-driven expansion (`tools/gen/commands_expand_v1.py`).\n"
    cli_add = "\n## Registry scale profile\n\nThe CLI contract is expected to remain deterministic with large registries (target: 2800 command_id, 200 per group).\nConsumers must support `yai help --all` and `yai help <command_id>` across the full canonical registry.\n"

    rtxt = REGISTRY_MD.read_text(encoding="utf-8")
    if "## Registry scale" not in rtxt:
        REGISTRY_MD.write_text(rtxt.rstrip() + "\n" + registry_add + "\n", encoding="utf-8")

    stxt = SPEC_MAP_MD.read_text(encoding="utf-8")
    if "## 12) Registry scale target" not in stxt:
        SPEC_MAP_MD.write_text(stxt.rstrip() + "\n" + spec_add + "\n", encoding="utf-8")

    ctxt = CLI_README.read_text(encoding="utf-8")
    if "## Registry scale profile" not in ctxt:
        CLI_README.write_text(ctxt.rstrip() + "\n" + cli_add + "\n", encoding="utf-8")


def main():
    expand_commands()
    expand_primitives_and_schema()
    patch_docs()


if __name__ == "__main__":
    main()
