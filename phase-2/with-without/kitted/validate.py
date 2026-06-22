#!/usr/bin/env python3
"""Hook check: enforce this project's CLAUDE.md rules on index.html.

A PostToolUse hook runs this after every edit. If it fails (exit 1), the harness
surfaces the problem immediately — the safety net the naked build never had.
"""
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "index.html"
try:
    html = open(path, encoding="utf-8").read()
except FileNotFoundError:
    print(f"FAIL: {path} not found"); sys.exit(1)

problems = []

# Rule 1: honest disclaimer on intro AND results
if "not a clinical" not in html.lower():
    problems.append("intro disclaimer missing ('not a clinical evaluation')")
if "not a diagnosis" not in html.lower():
    problems.append("results disclaimer missing ('not a diagnosis')")

# Rule: all five subtests present
for sid in ("digitspan", "stroop", "trails", "matrices", "fluency"):
    if f'id="{sid}"' not in html:
        problems.append(f"subtest screen missing: {sid}")

# Rule 3: scoring must be centralized (single source of truth)
if "SCORING (single source of truth)" not in html:
    problems.append("no centralized SCORING block — scoring numbers must not be scattered")

if problems:
    print("FAIL — CLAUDE.md rules violated:")
    for p in problems:
        print("  -", p)
    sys.exit(1)
print(f"PASS — {path} satisfies all CLAUDE.md rules.")
