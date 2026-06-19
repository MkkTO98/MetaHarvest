#!/usr/bin/env python3
"""Report missing MetaHarvest library coverage for analyzed sources."""
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

QUESTION_ANSWERED = "Which analyzed sources are missing required library coverage?"
DOES_NOT_ANSWER = "What should any consuming project do?"

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
        raise UsageError("PyYAML is required. Run with `uvx --with pyyaml python tools/check_coverage_health.py ...`.")
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception as exc:  # pragma: no cover - defensive CLI boundary
        raise UsageError(f"failed to parse {path}: {exc}") from exc


def normalize_path(value: str | None) -> str | None:
    if not value:
        return value
    for prefix in ("MetaHarvest/", "ArchitectureHarvest/"):
        if value.startswith(prefix):
            return value[len(prefix):]
    return value


def flatten_paths(value: Any) -> list[str]:
    paths: list[str] = []
    if isinstance(value, str):
        paths.append(normalize_path(value) or value)
    elif isinstance(value, list):
        for item in value:
            paths.extend(flatten_paths(item))
    return paths


def text_blob(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, default=str).lower()


def analyzed_sources(root: Path, source_ids: list[str]) -> list[dict[str, Any]]:
    registry = load_yaml(root / "source_registry.yaml")
    sources = [source for source in registry.get("sources", []) if source.get("status") == "analyzed"]
    if source_ids:
        wanted = set(source_ids)
        sources = [source for source in sources if source.get("id") in wanted]
        found = {source.get("id") for source in sources}
        missing = sorted(wanted - found)
        if missing:
            raise UsageError(f"requested analyzed source ids not found: {', '.join(missing)}")
    return sources


def project_card_path(source_id: str) -> str:
    return f"project_cards/{source_id}.yaml"


def load_project_card(root: Path, source_id: str) -> tuple[dict[str, Any] | None, list[str]]:
    path = root / project_card_path(source_id)
    if not path.exists():
        return None, [f"project card missing: {project_card_path(source_id)}"]
    return load_yaml(path), []


def expected_artifact_paths(source_id: str, card: dict[str, Any] | None) -> dict[str, list[str]]:
    paths: dict[str, list[str]] = {
        "project_cards": [project_card_path(source_id)],
        "component_cards": [],
        "reports": [],
        "projects": [],
    }
    if not card:
        return paths
    links = card.get("links", {})
    paths["component_cards"] = flatten_paths(links.get("component_cards", []))
    deep_report = normalize_path(links.get("deep_report"))
    human_summary = normalize_path(links.get("human_summary"))
    if deep_report:
        paths["reports"].append(deep_report)
    if human_summary:
        paths["projects"].append(human_summary)
    return paths


def existing_path_missing(root: Path, paths: dict[str, list[str]]) -> list[str]:
    missing: list[str] = []
    for category, category_paths in paths.items():
        for relative in category_paths:
            if not (root / relative).exists():
                missing.append(f"{category} artifact missing: {relative}")
    return missing


def retrieval_missing(root: Path, source_id: str, paths: dict[str, list[str]]) -> list[str]:
    problem_catalog = load_yaml(root / "retrieval" / "problem_catalog.yaml")
    retrieval_index = load_yaml(root / "retrieval" / "retrieval_index.yaml")
    problem_blob = text_blob(problem_catalog)
    index_blob = text_blob(retrieval_index)
    missing: list[str] = []

    if source_id.lower() not in problem_blob:
        missing.append("problem_catalog does not reference source id")
    if source_id.lower() not in index_blob:
        missing.append("retrieval_index does not reference source id")

    for project_path in paths["project_cards"]:
        if project_path.lower() not in index_blob:
            missing.append(f"retrieval_index missing project card reference: {project_path}")
    for component_path in paths["component_cards"]:
        if component_path.lower() not in index_blob:
            missing.append(f"retrieval_index missing component card reference: {component_path}")
    for report_path in paths["reports"]:
        if report_path.lower() not in index_blob:
            missing.append(f"retrieval_index missing report reference: {report_path}")
    return missing


def change_discovery_missing(root: Path, source_id: str, paths: dict[str, list[str]]) -> list[str]:
    index = load_yaml(root / "change_discovery" / "index.yaml")
    change_blob = text_blob(index)
    missing: list[str] = []
    if source_id.lower() not in change_blob:
        missing.append("change_discovery does not reference source id")
    required_paths = paths["project_cards"] + paths["component_cards"] + paths["reports"]
    for relative in required_paths:
        if relative.lower() not in change_blob:
            missing.append(f"change_discovery missing artifact reference: {relative}")
    return missing


def check_source(root: Path, source: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    source_id = source["id"]
    card, card_missing = load_project_card(root, source_id)
    paths = expected_artifact_paths(source_id, card)
    missing_messages = []
    missing_messages.extend(card_missing)
    missing_messages.extend(existing_path_missing(root, paths))
    missing_messages.extend(retrieval_missing(root, source_id, paths))
    missing_messages.extend(change_discovery_missing(root, source_id, paths))

    checked = {
        "source_id": source_id,
        "status": source.get("status"),
        "checked_paths": paths,
    }
    missing_records = [
        {
            "source_id": source_id,
            "missing": message,
        }
        for message in sorted(set(missing_messages))
    ]
    return checked, missing_records


def build_payload(root: Path, source_ids: list[str]) -> dict[str, Any]:
    checked_sources = []
    missing_coverage = []
    for source in analyzed_sources(root, source_ids):
        checked, missing = check_source(root, source)
        checked_sources.append(checked)
        missing_coverage.extend(missing)
    return {
        "kind": "metaharvest_coverage_health_result",
        "question_answered": QUESTION_ANSWERED,
        "does_not_answer": DOES_NOT_ANSWER,
        "project_identity_required": False,
        "scope": "analyzed_sources",
        "checked_sources": checked_sources,
        "missing_coverage": missing_coverage,
    }


def render_text(payload: dict[str, Any]) -> str:
    lines = [
        payload["question_answered"],
        f"Does not answer: {payload['does_not_answer']}",
        f"Checked sources: {len(payload['checked_sources'])}",
        "Missing coverage:",
    ]
    if not payload["missing_coverage"]:
        lines.append("- None")
    else:
        for item in payload["missing_coverage"]:
            lines.append(f"- {item['source_id']}: {item['missing']}")
    return "\n".join(lines) + "\n"


def assert_no_forbidden_keys(payload: dict[str, Any]) -> None:
    dump = json.dumps(payload, sort_keys=True, default=str).lower()
    found = sorted(key for key in FORBIDDEN_KEYS if key in dump)
    if found:  # pragma: no cover - defensive guard
        raise UsageError(f"coverage output included forbidden project-specific keys: {', '.join(found)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=".", help="MetaHarvest root. Defaults to current directory.")
    parser.add_argument("--source-id", action="append", default=[], help="Limit check to one analyzed source id. Repeatable.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    args = parser.parse_args()

    try:
        payload = build_payload(Path(args.project).resolve(), args.source_id)
        assert_no_forbidden_keys(payload)
    except UsageError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, default=str))
    else:
        print(render_text(payload), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
