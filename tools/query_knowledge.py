#!/usr/bin/env python3
"""Descriptively retrieve MetaHarvest-owned reusable knowledge."""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import yaml
except Exception:  # pragma: no cover - exercised only when dependency missing
    yaml = None

DOES_NOT_ANSWER = [
    "Does this matter to Project X?",
    "What should Project X do?",
    "Which project is affected?",
    "What should be prioritized?",
]

FORBIDDEN_KEYS = {
    "affected_projects",
    "target_projects",
    "project_recommendations",
    "recommended_actions",
    "adoption_suggestions",
    "priority_by_project",
    "relevance_by_project",
}

SCAN_DIRS = {
    "synthesis": "synthesis",
    "contradictions": "contradictions",
    "adoption_outcomes": "adoption_log",
    "adoption_candidates": "adoption_candidates",
    "pattern_library": "pattern_library",
}


class UsageError(Exception):
    pass


@dataclass(frozen=True)
class Query:
    problem_id: str | None = None
    keyword: str | None = None
    pattern_id: str | None = None
    artifact_id: str | None = None

    def terms(self) -> list[str]:
        return [term for term in [self.problem_id, self.keyword, self.pattern_id, self.artifact_id] if term]

    def as_dict(self) -> dict[str, str | None]:
        return {
            "problem_id": self.problem_id,
            "keyword": self.keyword,
            "pattern_id": self.pattern_id,
            "artifact_id": self.artifact_id,
        }


def load_yaml(path: Path) -> Any:
    if yaml is None:
        raise UsageError("PyYAML is required. Run with `uvx --with pyyaml python tools/query_knowledge.py ...`.")
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception as exc:  # pragma: no cover - defensive CLI boundary
        raise UsageError(f"failed to parse {path}: {exc}") from exc


def rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def text_blob(value: Any) -> str:
    if isinstance(value, str):
        return value
    return json.dumps(value, sort_keys=True, ensure_ascii=False, default=str)


def nested_values(value: Any, key: str) -> list[Any]:
    found: list[Any] = []
    if isinstance(value, dict):
        for current_key, current_value in value.items():
            if current_key == key:
                found.append(current_value)
            found.extend(nested_values(current_value, key))
    elif isinstance(value, list):
        for item in value:
            found.extend(nested_values(item, key))
    return found


def flatten_paths(value: Any) -> list[str]:
    paths: list[str] = []
    if isinstance(value, str):
        paths.append(value)
    elif isinstance(value, list):
        for item in value:
            paths.extend(flatten_paths(item))
    return paths


def sanitize_record_data(data: Any) -> dict[str, Any]:
    if not isinstance(data, dict):
        return {}
    summary: dict[str, Any] = {}
    for key in ["id", "name", "title", "kind", "status", "problem_statement", "summary", "evidence_summary", "lifecycle", "tags"]:
        if key in data and key not in FORBIDDEN_KEYS:
            summary[key] = data[key]
    return summary


def make_record(root: Path, path: Path, section: str, data: Any, match_reasons: list[str]) -> dict[str, Any]:
    return {
        "path": rel(root, path),
        "section": section,
        "match_reasons": sorted(set(match_reasons)),
        "descriptive_fields": sanitize_record_data(data),
    }


def query_matches_path(query: Query, path: str) -> bool:
    stem = Path(path).stem.lower()
    normalized_path = path.lower()
    return any(term.lower() in normalized_path or term.lower() == stem for term in query.terms())


def query_matches_data(query: Query, data: Any) -> list[str]:
    reasons: list[str] = []
    blob = text_blob(data).lower()
    if query.keyword and query.keyword.lower() in blob:
        reasons.append("keyword")
    if query.problem_id:
        problem = query.problem_id.lower()
        ids = [str(value).lower() for value in nested_values(data, "id") + nested_values(data, "problem_id")]
        if problem in ids or problem in blob:
            reasons.append("problem_id")
    if query.pattern_id:
        pattern = query.pattern_id.lower()
        ids = [str(value).lower() for value in nested_values(data, "id")]
        pattern_lists = flatten_paths(nested_values(data, "pattern_ids") + nested_values(data, "related_patterns"))
        if pattern in ids or pattern in [str(value).lower() for value in pattern_lists] or pattern in blob:
            reasons.append("pattern_id")
    if query.artifact_id:
        artifact = query.artifact_id.lower()
        if artifact in blob:
            reasons.append("artifact_id")
    return reasons


def append_unique(target: list[dict[str, Any]], item: dict[str, Any]) -> None:
    key = (item.get("path"), item.get("section"), json.dumps(item.get("descriptive_fields", {}), sort_keys=True, default=str))
    existing = {
        (entry.get("path"), entry.get("section"), json.dumps(entry.get("descriptive_fields", {}), sort_keys=True, default=str))
        for entry in target
    }
    if key not in existing:
        target.append(item)


def load_problem_catalog(root: Path, query: Query) -> list[dict[str, Any]]:
    path = root / "retrieval" / "problem_catalog.yaml"
    data = load_yaml(path)
    records: list[dict[str, Any]] = []
    if query_matches_path(query, rel(root, path)):
        records.append(make_record(root, path, "problem_catalog", data, ["artifact_path"]))
    for problem in data.get("problems", []):
        reasons = query_matches_data(query, problem)
        if reasons:
            records.append(make_record(root, path, "problem_catalog", problem, reasons))
    return records


def load_retrieval_index(root: Path, query: Query) -> tuple[list[dict[str, Any]], list[dict[str, Any]], set[str]]:
    path = root / "retrieval" / "retrieval_index.yaml"
    data = load_yaml(path)
    records: list[dict[str, Any]] = []
    evidence: list[dict[str, Any]] = []
    referenced_paths: set[str] = set()
    if query_matches_path(query, rel(root, path)):
        records.append(make_record(root, path, "retrieval_index", data, ["artifact_path"]))
    for entry in data.get("entries", []):
        reasons = query_matches_data(query, entry)
        if not reasons:
            continue
        records.append(make_record(root, path, "retrieval_index", entry, reasons))
        for field in ["synthesized_patterns", "pattern_cards", "component_cards", "project_cards", "contradiction_records", "adoption_outcomes", "recommendation_records"]:
            for artifact_path in flatten_paths(entry.get(field, [])):
                if artifact_path.endswith("/"):
                    continue
                referenced_paths.add(artifact_path)
                evidence.append({"path": artifact_path, "source_field": field, "relation": "referenced_by_retrieval_index"})
    return records, evidence, referenced_paths


def scan_yaml_dir(root: Path, section: str, directory: str, query: Query, referenced_paths: set[str]) -> list[dict[str, Any]]:
    base = root / directory
    if not base.exists():
        return []
    records: list[dict[str, Any]] = []
    for path in sorted(base.glob("*.yaml")):
        data = load_yaml(path)
        relative = rel(root, path)
        reasons = query_matches_data(query, data)
        if relative in referenced_paths:
            reasons.append("retrieval_index_reference")
        if query_matches_path(query, relative):
            reasons.append("artifact_path")
        if reasons:
            records.append(make_record(root, path, section, data, reasons))
    return records


def change_discovery_refs(root: Path, query: Query, matched_paths: set[str]) -> list[dict[str, Any]]:
    path = root / "change_discovery" / "index.yaml"
    if not path.exists():
        return []
    data = load_yaml(path)
    refs: list[dict[str, Any]] = []
    for entry in data.get("changes", []):
        paths = set(entry.get("paths", []))
        reasons = []
        if paths & matched_paths:
            reasons.append("matched_artifact_path")
        if query_matches_data(query, entry):
            reasons.append("query_term")
        if reasons:
            refs.append(
                {
                    "sequence": entry.get("sequence"),
                    "date": entry.get("date"),
                    "change_type": entry.get("change_type"),
                    "artifact_status": entry.get("artifact_status"),
                    "summary": entry.get("summary"),
                    "paths": sorted(paths & matched_paths) or entry.get("paths", []),
                    "match_reasons": sorted(set(reasons)),
                }
            )
    return refs


def build_payload(root: Path, query: Query) -> dict[str, Any]:
    matching_records: list[dict[str, Any]] = []
    for record in load_problem_catalog(root, query):
        append_unique(matching_records, record)
    retrieval_records, evidence_sources, referenced_paths = load_retrieval_index(root, query)
    for record in retrieval_records:
        append_unique(matching_records, record)

    sections: dict[str, list[dict[str, Any]]] = {}
    for section, directory in SCAN_DIRS.items():
        section_records = scan_yaml_dir(root, section, directory, query, referenced_paths)
        sections[section] = section_records
        for record in section_records:
            append_unique(matching_records, record)

    # Markdown index files are included as discoverability surfaces, not as advice.
    for index_path in sorted((root / "indexes").glob("*.md")) if (root / "indexes").exists() else []:
        relative = rel(root, index_path)
        text = index_path.read_text(encoding="utf-8")
        reasons = []
        if query.keyword and query.keyword.lower() in text.lower():
            reasons.append("keyword")
        if query.artifact_id and query.artifact_id.lower() in relative.lower():
            reasons.append("artifact_id")
        if reasons:
            append_unique(matching_records, make_record(root, index_path, "indexes", {"kind": "markdown_index", "summary": text.splitlines()[0] if text.splitlines() else relative}, reasons))

    matched_paths = {record["path"] for record in matching_records}
    return {
        "kind": "metaharvest_knowledge_retrieval_result",
        "question_answered": "What does MetaHarvest know about the requested reusable non-domain problem or artifact?",
        "does_not_answer": DOES_NOT_ANSWER,
        "project_identity_required": False,
        "query": query.as_dict(),
        "doctrine_boundary": {
            "mode": "descriptive_only",
            "project_relevance_evaluation": "not_performed",
            "project_specific_recommendations": "not_emitted",
            "prioritization": "not_emitted",
        },
        "matching_records": matching_records,
        "evidence_sources": evidence_sources,
        "contradictions": sections.get("contradictions", []),
        "synthesis_records": sections.get("synthesis", []),
        "adoption_outcomes": sections.get("adoption_outcomes", []),
        "adoption_candidates": sections.get("adoption_candidates", []),
        "pattern_records": sections.get("pattern_library", []),
        "change_discovery_references": change_discovery_refs(root, query, matched_paths),
    }


def render_text(payload: dict[str, Any]) -> str:
    lines = [
        payload["question_answered"],
        f"Project identity required: {payload['project_identity_required']}",
        "Does not answer:",
    ]
    lines.extend(f"- {item}" for item in payload["does_not_answer"])
    lines.append("")
    for section in ["matching_records", "evidence_sources", "contradictions", "synthesis_records", "adoption_outcomes", "change_discovery_references"]:
        lines.append(f"{section}:")
        items = payload.get(section, [])
        if not items:
            lines.append("- None")
        else:
            for item in items:
                label = item.get("path") or f"sequence {item.get('sequence')}"
                lines.append(f"- {label}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=".", help="MetaHarvest root. Defaults to current directory.")
    parser.add_argument("--problem-id")
    parser.add_argument("--keyword")
    parser.add_argument("--pattern-id")
    parser.add_argument("--artifact-id")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    args = parser.parse_args()

    query = Query(problem_id=args.problem_id, keyword=args.keyword, pattern_id=args.pattern_id, artifact_id=args.artifact_id)
    if not query.terms():
        print("ERROR: provide at least one query input: --problem-id, --keyword, --pattern-id, or --artifact-id", file=sys.stderr)
        return 2

    try:
        payload = build_payload(Path(args.project).resolve(), query)
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
