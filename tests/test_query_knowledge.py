import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "query_knowledge.py"
SOURCE_REGISTRY = ROOT / "source_registry.yaml"

FORBIDDEN_OUTPUT_FRAGMENTS = [
    "affected_projects",
    "target_projects",
    "project_recommendations",
    "recommended_actions",
    "adoption_suggestions",
    "priority_by_project",
    "relevance_by_project",
]


def run_query(*args):
    result = subprocess.run(
        [sys.executable, str(TOOL), "--project", str(ROOT), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def test_problem_id_query_returns_descriptive_knowledge_sections_without_project_identity():
    payload = run_query("--problem-id", "long_running_agent_state", "--json")

    assert payload["kind"] == "metaharvest_knowledge_retrieval_result"
    assert payload["project_identity_required"] is False
    assert payload["query"]["problem_id"] == "long_running_agent_state"
    assert payload["does_not_answer"] == [
        "Does this matter to Project X?",
        "What should Project X do?",
        "Which project is affected?",
        "What should be prioritized?",
    ]

    assert any(record["path"] == "retrieval/problem_catalog.yaml" for record in payload["matching_records"])
    assert any(record["path"] == "retrieval/retrieval_index.yaml" for record in payload["matching_records"])
    assert payload["evidence_sources"]
    assert payload["contradictions"]
    assert payload["synthesis_records"]
    assert payload["adoption_outcomes"]

    output_dump = json.dumps(payload).lower()
    for forbidden in FORBIDDEN_OUTPUT_FRAGMENTS:
        assert forbidden not in output_dump


def test_pattern_id_query_finds_synthesis_records_and_change_discovery_references_descriptively():
    payload = run_query("--pattern-id", "checkpointing", "--json")

    synthesis_paths = {record["path"] for record in payload["synthesis_records"]}
    assert "synthesis/thread_checkpoint_contract.yaml" in synthesis_paths
    assert payload["matching_records"]
    assert payload["change_discovery_references"] is not None
    assert payload["doctrine_boundary"]["mode"] == "descriptive_only"

    output_dump = json.dumps(payload).lower()
    assert "generic_recommendation" not in output_dump
    assert "ecosystem_weighted_recommendation" not in output_dump
    for forbidden in FORBIDDEN_OUTPUT_FRAGMENTS:
        assert forbidden not in output_dump


def test_keyword_query_finds_contradictions_without_project_specific_advice():
    payload = run_query("--keyword", "checkpoint", "--json")

    assert payload["query"]["keyword"] == "checkpoint"
    assert payload["matching_records"]
    assert any(record["section"] == "contradictions" for record in payload["matching_records"])

    output_dump = json.dumps(payload).lower()
    for forbidden in FORBIDDEN_OUTPUT_FRAGMENTS:
        assert forbidden not in output_dump


def test_artifact_id_query_finds_interface_artifact_without_project_identity():
    payload = run_query("--artifact-id", "retrieval_index", "--json")

    assert payload["query"]["artifact_id"] == "retrieval_index"
    assert any(record["path"] == "retrieval/retrieval_index.yaml" for record in payload["matching_records"])
    assert payload["project_identity_required"] is False

    output_dump = json.dumps(payload).lower()
    for forbidden in FORBIDDEN_OUTPUT_FRAGMENTS:
        assert forbidden not in output_dump


def test_retrieval_validation_uses_existing_analyzed_harvested_sources():
    registry = yaml.safe_load(SOURCE_REGISTRY.read_text(encoding="utf-8"))
    analyzed_sources = {source["id"] for source in registry["sources"] if source["status"] == "analyzed"}

    assert {"openhands", "langgraph", "aider", "swe-agent"}.issubset(analyzed_sources)

    payload = run_query("--problem-id", "long_running_agent_state", "--json")
    evidence_paths = {record["path"] for record in payload["evidence_sources"]}
    matched_paths = {record["path"] for record in payload["matching_records"]}

    assert "project_cards/openhands.yaml" in evidence_paths
    assert "project_cards/langgraph.yaml" in evidence_paths
    assert "component_cards/openhands-conversation-lifecycle.yaml" in evidence_paths
    assert "component_cards/langgraph-checkpoint-saver.yaml" in evidence_paths
    assert "synthesis/thread_checkpoint_contract.yaml" in matched_paths
    assert "contradictions/event-log-vs-state-snapshot.yaml" in matched_paths


def test_missing_query_is_usage_error():
    result = subprocess.run(
        [sys.executable, str(TOOL), "--project", str(ROOT), "--json"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 2
    assert "provide at least one query input" in result.stderr.lower()
