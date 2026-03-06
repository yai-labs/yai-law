#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COMMANDS_PATH = ROOT / "registry" / "commands.v1.json"
REPORT_PATH = ROOT / "tools" / "out" / "workspace_model_report.md"


def main() -> int:
    payload = json.loads(COMMANDS_PATH.read_text(encoding="utf-8"))
    commands = payload.get("commands", [])

    by_scope = Counter()
    by_domain = Counter()
    ws_by_entrypoint = Counter()
    ws_missing_requires = []
    ws_global_like = []

    for c in commands:
        scope = c.get("command_scope", "unknown")
        domain = c.get("domain", "unknown")
        entry = c.get("entrypoint", "unknown")
        cid = c.get("id", "<missing-id>")
        requires_ws = bool(c.get("requires_workspace", False))

        by_scope[scope] += 1
        by_domain[domain] += 1

        if scope == "workspace":
            ws_by_entrypoint[entry] += 1
            if not requires_ws:
                ws_missing_requires.append(cid)

        if scope == "global" and entry in {"ws", "gov", "run", "inspect", "verify", "bundle"}:
            ws_global_like.append(cid)

    lines = []
    lines.append("# Workspace Model Report")
    lines.append("")
    lines.append("## Scope Distribution")
    for key, val in sorted(by_scope.items()):
        lines.append(f"- {key}: {val}")
    lines.append("")
    lines.append("## Domain Distribution")
    for key, val in sorted(by_domain.items()):
        lines.append(f"- {key}: {val}")
    lines.append("")
    lines.append("## Workspace-Scoped Coverage by Entrypoint")
    for key, val in sorted(ws_by_entrypoint.items()):
        lines.append(f"- {key}: {val}")
    lines.append("")
    lines.append("## Invariant Checks")
    lines.append(f"- workspace commands missing requires_workspace=true: {len(ws_missing_requires)}")
    lines.append(f"- global commands under workspace-centric entrypoints: {len(ws_global_like)}")
    lines.append("")
    if ws_missing_requires:
        lines.append("### Missing requires_workspace")
        lines.extend([f"- {cid}" for cid in ws_missing_requires[:30]])
        lines.append("")
    if ws_global_like:
        lines.append("### Global under workspace-centric entrypoints")
        lines.extend([f"- {cid}" for cid in ws_global_like[:30]])
        lines.append("")

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[ok] wrote {REPORT_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
