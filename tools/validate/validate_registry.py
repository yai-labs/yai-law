#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Set

REPO_ROOT = Path(__file__).resolve().parents[2]

PRIMITIVES_REG = REPO_ROOT / "law" / "abi" / "registry" / "primitives.v1.json"
PRIMITIVES_SCHEMA = REPO_ROOT / "law" / "abi" / "schema" / "primitives.v1.schema.json"

COMMANDS_REG = REPO_ROOT / "law" / "abi" / "registry" / "commands.v1.json"
COMMANDS_SCHEMA = REPO_ROOT / "law" / "abi" / "schema" / "commands.v1.schema.json"


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def validate_jsonschema(instance: Dict[str, Any], schema: Dict[str, Any]) -> List[str]:
    try:
        from jsonschema import Draft202012Validator
    except Exception as exc:
        return [f"jsonschema dependency is required (pip install jsonschema). import error: {exc}"]

    errors: List[str] = []
    v = Draft202012Validator(schema)
    for err in sorted(v.iter_errors(instance), key=lambda e: e.path):
        where = "$." + ".".join(str(x) for x in err.path) if err.path else "$"
        errors.append(f"schema error at {where}: {err.message}")
    return errors


def primitives_id_set(primitives: Dict[str, Any]) -> Set[str]:
    out: Set[str] = set()
    for p in primitives.get("primitives", []):
        pid = p.get("id")
        if isinstance(pid, str) and pid:
            out.add(pid)
    return out


def validate_command_links(commands: Dict[str, Any], prim_ids: Set[str]) -> List[str]:
    errors: List[str] = []

    cmd_list = commands.get("commands", [])
    if not isinstance(cmd_list, list):
        return ["commands.commands must be an array"]

    for c in cmd_list:
        if not isinstance(c, dict):
            errors.append("commands.commands[] must be objects")
            continue

        cid = c.get("id") or f"{c.get('group','?')}.{c.get('name','?')}"
        uses = c.get("uses_primitives", [])
        if uses is None:
            uses = []
        if not isinstance(uses, list):
            errors.append(f"{cid}: uses_primitives must be an array")
            continue

        for pid in uses:
            if not isinstance(pid, str):
                errors.append(f"{cid}: uses_primitives contains non-string value")
                continue
            if pid not in prim_ids:
                errors.append(f"{cid}: unknown primitive id referenced: {pid}")

        # Optional: verify schema_ref paths exist (only when present)
        for field in ("emits_artifacts", "consumes_artifacts"):
            items = c.get(field, [])
            if items is None:
                continue
            if not isinstance(items, list):
                errors.append(f"{cid}: {field} must be an array")
                continue
            for it in items:
                if not isinstance(it, dict):
                    errors.append(f"{cid}: {field} entries must be objects")
                    continue
                schema_ref = it.get("schema_ref")
                if isinstance(schema_ref, str) and schema_ref.strip():
                    p = (REPO_ROOT / schema_ref).resolve()
                    if not p.exists():
                        errors.append(f"{cid}: schema_ref not found: {schema_ref}")

    return errors


def main() -> int:
    missing = [p for p in [PRIMITIVES_REG, PRIMITIVES_SCHEMA, COMMANDS_REG, COMMANDS_SCHEMA] if not p.exists()]
    if missing:
        print("[registry] ERROR: missing required files:")
        for p in missing:
            print(f"- {rel(p)}")
        return 2

    prim = load_json(PRIMITIVES_REG)
    prim_schema = load_json(PRIMITIVES_SCHEMA)
    cmd = load_json(COMMANDS_REG)
    cmd_schema = load_json(COMMANDS_SCHEMA)

    errors: List[str] = []
    errors.extend(validate_jsonschema(prim, prim_schema))
    errors.extend(validate_jsonschema(cmd, cmd_schema))

    prim_ids = primitives_id_set(prim)
    if not prim_ids:
        errors.append("primitives registry contains no ids")

    errors.extend(validate_command_links(cmd, prim_ids))

    if errors:
        print("[registry] FAIL:")
        for e in errors:
            print(f"- {e}")
        return 1

    print("[registry] OK: primitives + commands schemas validated and links resolved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())