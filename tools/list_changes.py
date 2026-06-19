#!/usr/bin/env python3
"""List project-neutral MetaHarvest changes since a caller's last checkpoint."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except Exception:  # pragma: no cover - exercised only when dependency missing
    yaml = None


QUESTION_ANSWERED = "What changed in MetaHarvest since I last looked?"
DOES_NOT_ANSWER = "Does this matter to my project, and what should I do?"
CONSUMER_RESPONSIBILITY = (
    "Evaluate relevance, adoption, rejection, implementation, and local priority "
    "inside the consuming project."
)


class UsageError(Exception):
    pass


def load_index(root: Path) -> dict[str, Any]:
    if yaml is None:
        raise UsageError(
            "PyYAML is required to read change_discovery/index.yaml. "
            "Run with `uvx --with pyyaml python tools/list_changes.py ...`."
        )
    path = root / "change_discovery" / "index.yaml"
    if not path.exists():
        raise UsageError(f"change discovery index not found: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if data.get("kind") != "metaharvest_change_discovery_index":
        raise UsageError(f"unexpected change discovery index kind in {path}")
    return data


def parse_date(value: str | None) -> dt.date | None:
    if not value:
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise UsageError(f"invalid --since-date {value!r}; expected YYYY-MM-DD") from exc


def changed_since(index: dict[str, Any], since_sequence: int, since_date: dt.date | None) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    for entry in index.get("changes", []):
        sequence = int(entry.get("sequence", 0))
        if sequence <= since_sequence:
            continue
        if since_date is not None:
            entry_date = dt.date.fromisoformat(str(entry.get("date")))
            if entry_date <= since_date:
                continue
        selected.append(entry)
    return selected


def build_payload(index: dict[str, Any], since_sequence: int, since_date: dt.date | None) -> dict[str, Any]:
    return {
        "kind": "metaharvest_change_discovery_result",
        "question_answered": QUESTION_ANSWERED,
        "does_not_answer": DOES_NOT_ANSWER,
        "since_sequence": since_sequence,
        "since_date": since_date.isoformat() if since_date else None,
        "latest_sequence": max((int(e.get("sequence", 0)) for e in index.get("changes", [])), default=0),
        "consumer_responsibility": CONSUMER_RESPONSIBILITY,
        "changes": changed_since(index, since_sequence, since_date),
    }


def render_text(payload: dict[str, Any]) -> str:
    lines = [
        payload["question_answered"],
        f"Does not answer: {payload['does_not_answer']}",
        f"Consumer responsibility: {payload['consumer_responsibility']}",
        f"Checkpoint: since_sequence={payload['since_sequence']}, since_date={payload['since_date']}",
        f"Latest sequence: {payload['latest_sequence']}",
        "",
        "Changes:",
    ]
    if not payload["changes"]:
        lines.append("- None.")
        return "\n".join(lines) + "\n"
    for entry in payload["changes"]:
        lines.append(
            f"- {entry['sequence']} | {entry['date']} | {entry['change_type']} | "
            f"{entry['artifact_status']}: {entry['summary']}"
        )
        for path in entry.get("paths", []):
            lines.append(f"  - {path}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=".", help="MetaHarvest root. Defaults to current directory.")
    parser.add_argument("--since-sequence", type=int, default=0, help="Return records with sequence greater than this value.")
    parser.add_argument("--since-date", default=None, help="Optionally return records newer than YYYY-MM-DD.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    args = parser.parse_args()

    try:
        root = Path(args.project).resolve()
        since_date = parse_date(args.since_date)
        index = load_index(root)
        payload = build_payload(index, args.since_sequence, since_date)
    except UsageError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(render_text(payload), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
