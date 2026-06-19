# MetaHarvest Latest Handoff

Date: 2026-06-19
Status: relationship capability audit complete; relationship modeling task created but not implemented

## Current repository context

MetaHarvest is operating as a local-first, file-backed library for reusable non-domain knowledge.

Current bounded infrastructure surfaces:

- `retrieval/`
- `change_discovery/`
- `tools/query_knowledge.py`
- `tools/list_changes.py`
- `tools/check_coverage_health.py`
- related tests
- related decision/task records

## Completed recent work

Implemented task:

- `tasks/T-20260619-library-discoverability-backfill.md`

Updated retrieval coverage:

- `retrieval/problem_catalog.yaml`
- `retrieval/retrieval_index.yaml`

The taxonomy-diversity harvest is discoverable through compact problem-first routes for:

- `workflow_automation_integration` -> n8n
- `workflow_orchestration_scheduling` -> Apache Airflow
- `metadata_catalog_lineage_governance` -> OpenMetadata

Updated change discovery:

- `change_discovery/index.yaml` sequence 7 records the taxonomy-diversity harvest backfill as a project-neutral library change.

Added coverage-health check:

- `tools/check_coverage_health.py`

It reports missing analyzed-source coverage across source registry, project cards, component cards, reports, retrieval surfaces, and change-discovery surfaces. The check reports missing coverage only and does not emit recommendations, project-specific advice, rankings, synthesis, or automatic tasks.

## Latest bounded audit

Created:

- `reports/R-20260619-relationship-capability-audit.md`
- `tasks/T-20260619-minimal-first-class-relationship-index.md`

Audit conclusion:

- MetaHarvest has deterministic relationship-like metadata through source IDs, project-card links, component-card source IDs, retrieval-index co-location, synthesis fields, and change-discovery path lists.
- These are not sufficient as first-class artifact relationships.
- Explicit predicate keys such as `implements`, `contains`, `references`, `depends_on`, `related_to`, `part_of`, and `derived_from` are absent as canonical relationship fields.
- Retrieval can surface co-indexed evidence and change references, but cannot traverse arbitrary typed relationships.
- Current doctrine permits project-neutral file-backed relationship modeling as a legitimate library capability, if descriptive-only boundaries are preserved.

Recommended future task:

- `tasks/T-20260619-minimal-first-class-relationship-index.md`

Do not implement it unless explicitly asked.

## Boundaries to preserve

Do not allow retrieval, change discovery, coverage health, or future relationship modeling to drift into:

- affected-project lists
- project-specific recommendations
- adoption suggestions
- target-project relevance computation
- notification routing
- task creation inside consumer projects
- automatic project modification
- ranking or prioritization of consumer work
- synthesis generation

## Resume point

If relationship work is explicitly requested later, start from:

1. `reports/R-20260619-relationship-capability-audit.md`
2. `tasks/T-20260619-minimal-first-class-relationship-index.md`
3. `retrieval/retrieval_index.yaml`
4. `tools/query_knowledge.py`
5. `tools/check_coverage_health.py`
