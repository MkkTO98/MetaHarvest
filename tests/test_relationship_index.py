import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
RELATIONSHIP_INDEX = ROOT / "relationships" / "index.yaml"
RELATIONSHIP_TOOL = ROOT / "tools" / "check_relationship_health.py"
QUERY_TOOL = ROOT / "tools" / "query_knowledge.py"

FORBIDDEN_OUTPUT_FRAGMENTS = [
    "affected_projects",
    "target_projects",
    "project_recommendations",
    "recommended_actions",
    "adoption_suggestions",
    "priority_by_project",
    "relevance_by_project",
]


def run_json(command):
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def assert_descriptive_only(payload):
    output_dump = json.dumps(payload).lower()
    for forbidden in FORBIDDEN_OUTPUT_FRAGMENTS:
        assert forbidden not in output_dump


def load_relationship_tool():
    spec = importlib.util.spec_from_file_location("check_relationship_health", RELATIONSHIP_TOOL)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_relationship_index_validation_accepts_explicit_resolving_records():
    payload = run_json([
        sys.executable,
        str(RELATIONSHIP_TOOL),
        "--project",
        str(ROOT),
        "--json",
    ])

    assert payload["kind"] == "metaharvest_relationship_health_result"
    assert payload["question_answered"] == "Which recorded relationship records are malformed or unresolved?"
    assert payload["does_not_answer"] == "What should any consuming project do?"
    assert payload["predicate_vocabulary"] == [
        "implements",
        "contains",
        "references",
        "part_of",
        "derived_from",
        "analyzes",
    ]
    assert payload["relationship_count"] > 0
    assert payload["invalid_relationships"] == []
    assert any(
        relationship["predicate"] == "contains"
        and relationship["source"] == "project_cards/n8n.yaml"
        and relationship["target"] == "component_cards/n8n-workflow-graph.yaml"
        for relationship in payload["relationships"]
    )
    assert_descriptive_only(payload)


def test_relationship_validation_reports_invalid_predicates_missing_paths_and_malformed_records(tmp_path):
    module = load_relationship_tool()
    project = tmp_path / "project"
    project.mkdir()
    (project / "existing.yaml").write_text("kind: fixture\n", encoding="utf-8")
    index = project / "relationships" / "index.yaml"
    index.parent.mkdir()
    index.write_text(
        yaml.safe_dump(
            {
                "schema_version": 1,
                "kind": "relationship_index",
                "predicate_vocabulary": ["contains"],
                "relationships": [
                    {
                        "id": "bad-predicate",
                        "source": "existing.yaml",
                        "predicate": "recommends",
                        "target": "existing.yaml",
                    },
                    {
                        "id": "missing-source",
                        "source": "missing-source.yaml",
                        "predicate": "contains",
                        "target": "existing.yaml",
                    },
                    {
                        "id": "missing-target",
                        "source": "existing.yaml",
                        "predicate": "contains",
                        "target": "missing-target.yaml",
                    },
                    {
                        "id": "malformed",
                        "source": "existing.yaml",
                        "predicate": "contains",
                    },
                    "not-a-record",
                ],
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )

    payload = module.build_payload(project)
    messages = [issue["issue"] for issue in payload["invalid_relationships"]]

    assert "invalid predicate: recommends" in messages
    assert "source path does not exist: missing-source.yaml" in messages
    assert "target path does not exist: missing-target.yaml" in messages
    assert "missing required field: target" in messages
    assert "relationship record is not a mapping" in messages
    assert payload["relationship_count"] == 5
    assert_descriptive_only(payload)


def test_query_exposes_only_recorded_relationships_for_matching_artifacts():
    payload = run_json([
        sys.executable,
        str(QUERY_TOOL),
        "--project",
        str(ROOT),
        "--artifact-id",
        "n8n-workflow-graph",
        "--json",
    ])

    relationships = payload["explicit_relationships"]
    assert relationships
    assert any(
        relationship["predicate"] == "contains"
        and relationship["source"] == "project_cards/n8n.yaml"
        and relationship["target"] == "component_cards/n8n-workflow-graph.yaml"
        for relationship in relationships
    )
    assert any(
        relationship["predicate"] == "part_of"
        and relationship["source"] == "component_cards/n8n-workflow-graph.yaml"
        and relationship["target"] == "project_cards/n8n.yaml"
        for relationship in relationships
    )
    assert "relationship_records" not in payload
    assert_descriptive_only(payload)
