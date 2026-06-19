import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "change_discovery" / "index.yaml"
TOOL = ROOT / "tools" / "list_changes.py"

FORBIDDEN_PROJECT_SPECIFIC_KEYS = {
    "affected_projects",
    "target_projects",
    "project_recommendations",
    "recommended_actions",
    "adoption_suggestions",
    "priority_by_project",
    "relevance_by_project",
}


def load_index():
    return yaml.safe_load(INDEX.read_text(encoding="utf-8"))


def test_change_discovery_doctrine_is_recorded_in_provider_interface():
    constitution = (ROOT / "CONSTITUTION.md").read_text(encoding="utf-8")
    integration = (ROOT / "INTEGRATION.md").read_text(encoding="utf-8")
    decision = (ROOT / "decisions" / "D-20260618-change-discoverability-boundary.md").read_text(encoding="utf-8")

    for text in [constitution, integration, decision]:
        assert "MetaHarvest is responsible for discoverability of change" in text
        assert "Projects are responsible for evaluation of change" in text
        assert "project-specific relevance determination" in text
        assert "automatic project modification" in text


def test_change_discovery_index_is_project_neutral_and_status_oriented():
    index = load_index()

    assert index["kind"] == "metaharvest_change_discovery_index"
    assert index["doctrine"]["metaharvest_owns"] == "discoverability_of_change"
    assert index["doctrine"]["consuming_projects_own"] == "evaluation_of_change"
    assert index["consumer_contract"]["question_answered"] == "What changed in MetaHarvest since I last looked?"
    assert index["consumer_contract"]["does_not_answer"] == "Does this matter to my project, and what should I do?"

    changes = index["changes"]
    assert changes
    sequences = [entry["sequence"] for entry in changes]
    assert sequences == sorted(sequences)

    forbidden_dump = json.dumps(index).lower()
    for key in FORBIDDEN_PROJECT_SPECIFIC_KEYS:
        assert key not in forbidden_dump

    for entry in changes:
        assert entry["change_type"] in {"new_artifact", "modified_artifact", "retired_artifact", "superseded_artifact", "staleness_update"}
        assert entry["artifact_status"] in {"active", "stale", "superseded", "retired"}
        assert entry["paths"]
        assert "project" not in entry
        assert "recommendation" not in json.dumps(entry.get("consumer_action", "")).lower()


def test_list_changes_reports_changes_since_sequence_without_relevance_or_recommendations():
    result = subprocess.run(
        [sys.executable, str(TOOL), "--project", str(ROOT), "--since-sequence", "0", "--json"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["question_answered"] == "What changed in MetaHarvest since I last looked?"
    assert payload["does_not_answer"] == "Does this matter to my project, and what should I do?"
    assert payload["since_sequence"] == 0
    assert payload["changes"]

    output_dump = result.stdout.lower()
    for forbidden in ["affected_projects", "recommended_actions", "adoption_suggestions", "relevance_by_project"]:
        assert forbidden not in output_dump


def test_list_changes_empty_result_is_still_project_neutral():
    index = load_index()
    latest = max(entry["sequence"] for entry in index["changes"])
    result = subprocess.run(
        [sys.executable, str(TOOL), "--project", str(ROOT), "--since-sequence", str(latest), "--json"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["changes"] == []
    assert payload["consumer_responsibility"] == "Evaluate relevance, adoption, rejection, implementation, and local priority inside the consuming project."
