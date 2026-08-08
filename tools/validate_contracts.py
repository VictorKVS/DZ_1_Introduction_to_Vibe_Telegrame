"""Validate FATHER machine-readable contracts and fixtures.

Run:
    python tools/validate_contracts.py

Dependency:
    pip install jsonschema
"""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
ARCH = ROOT / "docs" / "03_Architecture"
LEGACY = ROOT / "docs" / "20_Legacy_Intelligence"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def validate(schema_path: Path, instance_path: Path) -> list[str]:
    schema = load_json(schema_path)
    instance = load_json(instance_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [error.message for error in sorted(validator.iter_errors(instance), key=lambda e: list(e.path))]


def validate_schema_definition(schema_path: Path) -> list[str]:
    schema = load_json(schema_path)
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # jsonschema emits detailed schema exceptions
        return [str(exc)]
    return []


def main() -> int:
    graph_schema = ARCH / "GRAPH_SCHEMA_V0_1.json"
    decision_schema = ARCH / "DECISION_RECORD_SCHEMA.json"
    graph_fixture = LEGACY / "SOKRAT_TO_SOCRATES_GRAPH_V0_1.json"

    checks: list[tuple[str, list[str]]] = [
        ("GRAPH_SCHEMA definition", validate_schema_definition(graph_schema)),
        ("DECISION_RECORD_SCHEMA definition", validate_schema_definition(decision_schema)),
        ("Sokrat→SOCRATES graph fixture", validate(graph_schema, graph_fixture)),
    ]

    failed = False
    for name, errors in checks:
        if errors:
            failed = True
            print(f"[FAIL] {name}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"[PASS] {name}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
