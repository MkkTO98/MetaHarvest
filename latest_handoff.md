# MetaHarvest Latest Handoff

Date: 2026-06-19
Status: minimal first-class relationship index implemented and validated

## Current repository context

MetaHarvest is operating as a local-first, file-backed library for reusable non-domain knowledge.

Current bounded infrastructure surfaces:

- `retrieval/`
- `relationships/`
- `change_discovery/`
- `tools/query_knowledge.py`
- `tools/list_changes.py`
- `tools/check_coverage_health.py`
- `tools/check_relationship_health.py`
- related tests
- related decision/task/report records

## Completed recent work

Implemented task:

- `tasks/T-20260619-minimal-first-class-relationship-index.md`

Added relationship capability:

- `relationships/index.yaml` is the canonical first-class relationship index.
- Predicate vocabulary is bounded to `implements`, `contains`, `references`, `part_of`, `derived_from`, and `analyzes`.
- Records are explicit only: no inference, no graph generation, no derived edges, and no recommendation logic.
- `tools/check_relationship_health.py` validates malformed records, invalid predicates, missing source paths, and missing target paths.
- `tools/query_knowledge.py` exposes matching `explicit_relationships` descriptively for recorded relationships only.
- `indexes/relationship_index.md` documents the relationship surface.
- `tests/test_relationship_index.py` validates relationship resolution, internal consistency, malformed fixtures, and retrieval exposure.

Previous implemented task:

- `tasks/T-20260619-library-discoverability-backfill.md`

Retrieval and coverage context:

- `retrieval/problem_catalog.yaml`
- `retrieval/retrieval_index.yaml`
- `tools/check_coverage_health.py`

The taxonomy-diversity harvest is discoverable through compact problem-first routes for:

- `workflow_automation_integration` -> n8n
- `workflow_orchestration_scheduling` -> Apache Airflow
- `metadata_catalog_lineage_governance` -> OpenMetadata

## Boundaries to preserve

Do not allow retrieval, change discovery, coverage health, or relationship modeling to drift into:

- affected-project lists
- project-specific recommendations
- adoption suggestions
- target-project relevance computation
- notification routing
- task creation inside consumer projects
- automatic project modification
- ranking or prioritization of consumer work
- synthesis generation
- graph traversal over inferred or derived relationships

## Validation state

Latest validation:

- `uv run --with pytest --with pyyaml pytest tests -q` -> 16 passed
- `uv run --with pyyaml python tools/check_relationship_health.py --project . --json` -> 13 relationship records checked; 0 invalid relationships
- `uv run --with pyyaml python -m py_compile tools/query_knowledge.py tools/check_relationship_health.py tools/check_coverage_health.py tools/list_changes.py` -> passed
- YAML parse over repository `*.yaml` files -> passed
- `uv run --with pyyaml python tools/query_knowledge.py --project . --artifact-id n8n-workflow-graph --json` -> returned recorded `contains` and `part_of` explicit relationships
- `git diff --check` -> passed

Coverage-health note:

- `tools/check_coverage_health.py --project . --json` executes successfully but reports pre-existing missing coverage for older analyzed sources outside this task's narrow relationship scope.

## Resume point

If relationship work resumes, start from:

1. `relationships/index.yaml`
2. `indexes/relationship_index.md`
3. `tools/check_relationship_health.py`
4. `tests/test_relationship_index.py`
5. `tools/query_knowledge.py`

Do not add traversal, inferred relationships, recommendations, rankings, target-project relevance, or automatic task creation unless explicitly approved as a separate capability and doctrine changes first.
