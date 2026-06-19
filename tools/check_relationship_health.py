#!/usr/bin/env python3
"""Validate explicit MetaHarvest relationship records descriptively."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except Exception:  # pragma: no cover - dependency boundary
    yaml = None

QUESTION_ANSWERED = "Which recorded relationship records are malformed or unresolved?"
DOES_NOT_ANSWER = "What should any consuming project do?"
ALLOWED_PREDICATES = ["implements", "contains", "references", "part_of", "derived_from", "analyzes"]
REQUIRED_FIELDS = ["id", "source", "predicate", "target"]
FORBIDDEN_KEYS = {
    "affected_projects",
    "target_projects",
    "project_recommendations",
    "recommended_actions",
    "adoption_suggestions",
    "priority_by_project",
    "relevance_by_project",
}


class UsageError(Exception):
    pass


def load_yaml(path: Path) -> Any:
    if yaml is None:
        raise UsageError("PyYAML is required. Run with `uvx --with pyyaml python tools/check_relationship_health.py ...`.")
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception as exc:  # pragma: no cover - defensive CLI boundary
        raise UsageError(f"failed to parse {path}: {exc}") from exc


def normalize_path(value: str) -> str:
    for prefix in ("MetaHarvest/", "ArchitectureHarvest/"):
        if value.startswith(prefix):
            return value[len(prefix):]
    return value


def issue(record_id: str | None, relationship: Any, message: str) -> dict[str, Any]:
    return {
        "id": record_id,
        "issue": message,
        "record": relationship if isinstance(relationship, dict) else str(relationship),
    }


def validate_record(root: Path, relationship: Any, seen_ids: set[str]) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
    if not isinstance(relationship, dict):
        return None, [issue(None, relationship, "relationship record is not a mapping")]

    record_id = relationship.get("id")
    issues: list[dict[str, Any]] = []
    for field in REQUIRED_FIELDS:
        if not isinstance(relationship.get(field), str) or not relationship.get(field):
            issues.append(issue(record_id if isinstance(record_id, str) else None, relationship, f"missing required field: {field}"))

    if isinstance(record_id, str) and record_id in seen_ids:
        issues.append(issue(record_id, relationship, f"duplicate relationship id: {record_id}"))
    if isinstance(record_id, str):
        seen_ids.add(record_id)

    predicate = relationship.get("predicate")
    if isinstance(predicate, str) and predicate not in ALLOWED_PREDICATES:
        issues.append(issue(record_id if isinstance(record_id, str) else None, relationship, f"invalid predicate: {predicate}"))

    for endpoint in ["source", "target"]:
        value = relationship.get(endpoint)
        if isinstance(value, str) and value:
            relative = normalize_path(value)
            if not (root / relative).exists():
                issues.append(issue(record_id if isinstance(record_id, str) else None, relationship, f"{endpoint} path does not exist: {relative}"))

    forbidden_present = sorted(FORBIDDEN_KEYS & set(relationship.keys()))
    for key in forbidden_present:
        issues.append(issue(record_id if isinstance(record_id, str) else None, relationship, f"forbidden key present: {key}"))

    sanitized = None
    if isinstance(record_id, str) and isinstance(predicate, str):
        source = relationship.get("source")
        target = relationship.get("target")
        if isinstance(source, str) and isinstance(target, str):
            sanitized = {
                "id": record_id,
                "source": normalize_path(source),
                "predicate": predicate,
                "target": normalize_path(target),
            }
            if isinstance(relationship.get("evidence"), str):
                sanitized["evidence"] = relationship["evidence"]
    return sanitized, issues


def build_payload(root: Path) -> dict[str, Any]:
    index_path = root / "relationships" / "index.yaml"
    if not index_path.exists():
        raise UsageError("relationship index not found: relationships/index.yaml")
    data = load_yaml(index_path)
    if not isinstance(data, dict):
        raise UsageError("relationship index must be a mapping")

    relationships_raw = data.get("relationships", [])
    if not isinstance(relationships_raw, list):
        raise UsageError("relationships must be a list")

    invalid: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for raw in relationships_raw:
        sanitized, issues = validate_record(root, raw, seen_ids)
        invalid.extend(issues)
        if sanitized is not None:
            relationships.append(sanitized)

    vocabulary = data.get("predicate_vocabulary", ALLOWED_PREDICATES)
    if vocabulary != ALLOWED_PREDICATES:
        invalid.append(issue(None, {"predicate_vocabulary": vocabulary}, "predicate vocabulary does not match bounded vocabulary"))

    return {
        "kind": "metaharvest_relationship_health_result",
        "question_answered": QUESTION_ANSWERED,
        "does_not_answer": DOES_NOT_ANSWER,
        "project_identity_required": False,
        "doctrine_boundary": {
            "mode": "descriptive_only",
            "inference": "not_performed",
            "graph_generation": "not_performed",
            "project_relevance_evaluation": "not_performed",
            "project_specific_recommendations": "not_emitted",
            "prioritization": "not_emitted",
            "automatic_task_creation": "not_emitted",
        },
        "predicate_vocabulary": ALLOWED_PREDICATES,
        "relationship_count": len(relationships_raw),
        "relationships": relationships,
        "invalid_relationships": invalid,
    }


def render_text(payload: dict[str, Any]) -> str:
    lines = [
        payload["question_answered"],
        f"Project identity required: {payload['project_identity_required']}",
        f"Relationship records checked: {payload['relationship_count']}",
        "Invalid relationships:",
    ]
    invalid = payload.get("invalid_relationships", [])
    if not invalid:
        lines.append("- None")
    else:
        for item in invalid:
            label = item.get("id") or "<unknown>"
            lines.append(f"- {label}: {item.get('issue')}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=".", help="MetaHarvest root. Defaults to current directory.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    args = parser.parse_args()

    try:
        payload = build_payload(Path(args.project).resolve())
    except UsageError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, default=str))
    else:
        print(render_text(payload), end="")
    return 1 if payload["invalid_relationships"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
