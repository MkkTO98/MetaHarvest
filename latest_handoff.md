# MetaHarvest Latest Handoff

Date: 2026-06-19
Status: stable library v1 cleanup complete; active development should pause unless new evidence creates a bounded corpus-maintenance task

## Current repository context

MetaHarvest is operating as a local-first, file-backed descriptive library for reusable non-domain knowledge.

Stable-v1 bounded infrastructure surfaces:

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

Implemented stable-v1 cleanup:

- `reports/R-20260619-stable-v1-cleanup.md`

Coverage-health baseline before cleanup:

- analyzed sources checked: 9
- missing coverage records: 71
- gaps were limited to older analyzed sources: OpenHands, LangGraph, Aider, SWE-agent, dbt, and Dagster

Coverage-health cleanup completed:

- Added missing deep-report references for OpenHands, LangGraph, Aider, and SWE-agent in `retrieval/retrieval_index.yaml`.
- Added compact problem/retrieval route for dbt and Dagster in `retrieval/problem_catalog.yaml` and `retrieval/retrieval_index.yaml`.
- Backfilled project-neutral change-discovery entries for older analyzed-source cards, components, reports, and retrieval updates.
- Normalized active dbt/Dagster project-card links from `ArchitectureHarvest/` compatibility paths to `MetaHarvest/` paths.
- Updated active README/retrieval wording to clarify stable-v1 descriptive library doctrine and preserve historical advisory artifacts only as corpus evidence.

Relationship capability already completed:

- `relationships/index.yaml` is the canonical first-class relationship index.
- Predicate vocabulary is bounded to `implements`, `contains`, `references`, `part_of`, `derived_from`, and `analyzes`.
- Records are explicit only: no inference, no graph generation, no derived edges, and no recommendation logic.
- `tools/check_relationship_health.py` validates malformed records, invalid predicates, missing source paths, and missing target paths.
- `tools/query_knowledge.py` exposes matching `explicit_relationships` descriptively for recorded relationships only.

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

Historical `adoption_*`, `relevance_maps/`, `synthesis/`, and ArchitectureHarvest-named provenance artifacts remain preserved corpus evidence unless a future explicitly approved cleanup task says otherwise.

## Validation state

Latest validation:

- `uv run --with pytest --with pyyaml pytest tests -q` -> 16 passed
- `uv run --with pyyaml python tools/check_relationship_health.py --project . --json` -> 13 relationship records checked; 0 invalid relationships
- `uv run --with pyyaml python tools/check_coverage_health.py --project . --json` -> 9 analyzed sources checked; 0 missing coverage records
- YAML parse over repository `*.yaml` files -> passed
- `git diff --check` -> passed

## Resume point

If MetaHarvest work resumes, start from:

1. `reports/R-20260619-stable-v1-cleanup.md`
2. `tools/check_coverage_health.py`
3. `retrieval/problem_catalog.yaml`
4. `retrieval/retrieval_index.yaml`
5. `change_discovery/index.yaml`
6. `relationships/index.yaml`

Recommendation: pause active MetaHarvest infrastructure development. Future work should be limited to source-corpus maintenance, stale-source refresh, or explicitly requested cleanup. Do not add capabilities unless a bounded audit proves a real missing library need.
