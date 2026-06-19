import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUERY_TOOL = ROOT / "tools" / "query_knowledge.py"
CHANGES_TOOL = ROOT / "tools" / "list_changes.py"
COVERAGE_TOOL = ROOT / "tools" / "check_coverage_health.py"

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


def query(*args):
    return run_json([sys.executable, str(QUERY_TOOL), "--project", str(ROOT), *args, "--json"])


def test_taxonomy_harvest_sources_are_retrievable_through_existing_retrieval_surface():
    cases = [
        (
            "workflow_automation_integration",
            "workflow automation",
            "project_cards/n8n.yaml",
            {
                "component_cards/n8n-workflow-graph.yaml",
                "component_cards/n8n-trigger-webhook-registration.yaml",
                "component_cards/n8n-execution-persistence.yaml",
                "component_cards/n8n-credential-node-interface.yaml",
            },
            ["workflow_graph", "trigger_registration", "webhook_interface", "credential_boundary"],
        ),
        (
            "workflow_orchestration_scheduling",
            "timetable",
            "project_cards/airflow.yaml",
            {
                "component_cards/airflow-dag-definition.yaml",
                "component_cards/airflow-scheduler-loop.yaml",
                "component_cards/airflow-timetable-contract.yaml",
                "component_cards/airflow-asset-aware-scheduling.yaml",
            },
            ["dag_definition", "scheduler_loop", "timetable_contract", "asset_aware_scheduling"],
        ),
        (
            "metadata_catalog_lineage_governance",
            "metadata catalog lineage governance",
            "project_cards/openmetadata.yaml",
            {
                "component_cards/openmetadata-schema-first-entity-model.yaml",
                "component_cards/openmetadata-lineage-resource.yaml",
                "component_cards/openmetadata-governance-taxonomy.yaml",
                "component_cards/openmetadata-mcp-context-interface.yaml",
            },
            ["schema_first_entity_model", "lineage_graph", "governance_taxonomy", "mcp_context_interface"],
        ),
    ]

    for problem_id, keyword, project_card, component_cards, expected_patterns in cases:
        payload = query("--problem-id", problem_id, "--keyword", keyword)
        assert payload["project_identity_required"] is False
        assert payload["doctrine_boundary"]["mode"] == "descriptive_only"

        evidence_paths = {record["path"] for record in payload["evidence_sources"]}
        matching_paths = {record["path"] for record in payload["matching_records"]}
        assert project_card in evidence_paths
        assert component_cards.issubset(evidence_paths)
        assert "retrieval/problem_catalog.yaml" in matching_paths
        assert "retrieval/retrieval_index.yaml" in matching_paths

        output_dump = json.dumps(payload).lower()
        for pattern in expected_patterns:
            assert pattern in output_dump
        assert_descriptive_only(payload)


def test_taxonomy_harvest_change_is_project_neutral_and_discoverable_since_previous_checkpoint():
    payload = run_json([
        sys.executable,
        str(CHANGES_TOOL),
        "--project",
        str(ROOT),
        "--since-sequence",
        "6",
        "--json",
    ])

    summaries = [change["summary"] for change in payload["changes"]]
    assert any("taxonomy-diversity harvest" in summary for summary in summaries)
    taxonomy_change = next(change for change in payload["changes"] if "taxonomy-diversity harvest" in change["summary"])
    paths = set(taxonomy_change["paths"])
    assert "project_cards/n8n.yaml" in paths
    assert "project_cards/airflow.yaml" in paths
    assert "project_cards/openmetadata.yaml" in paths
    assert "reports/R-20260619-taxonomy-coverage-n8n-airflow-openmetadata.md" in paths
    assert payload["does_not_answer"] == "Does this matter to my project, and what should I do?"
    assert_descriptive_only(payload)


def test_coverage_health_check_reports_no_missing_coverage_for_taxonomy_harvest_sources():
    payload = run_json([
        sys.executable,
        str(COVERAGE_TOOL),
        "--project",
        str(ROOT),
        "--source-id",
        "n8n",
        "--source-id",
        "airflow",
        "--source-id",
        "openmetadata",
        "--json",
    ])

    assert payload["kind"] == "metaharvest_coverage_health_result"
    assert payload["question_answered"] == "Which analyzed sources are missing required library coverage?"
    assert payload["does_not_answer"] == "What should any consuming project do?"
    assert payload["missing_coverage"] == []
    assert {source["source_id"] for source in payload["checked_sources"]} == {"n8n", "airflow", "openmetadata"}
    assert_descriptive_only(payload)
