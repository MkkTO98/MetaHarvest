# MetaHarvest Stable v1 Cleanup Report

Date: 2026-06-19
Status: completed
Scope: bounded corpus/data hygiene after stable library v1 infrastructure

## Objective

Clean up remaining corpus metadata needed for stable-v1 consistency without adding capabilities, redesigning retrieval/change discovery/relationships, adding harvested projects, or changing consumer-project governance.

## Coverage-health baseline

Initial command:

```bash
uv run --with pyyaml python tools/check_coverage_health.py --project . --json
```

Initial result:

- analyzed sources checked: 9
- missing coverage records: 71

Missing coverage was limited to older analyzed sources:

- OpenHands
- LangGraph
- Aider
- SWE-agent
- dbt
- Dagster

The 2026-06-19 taxonomy-diversity sources already had coverage-health consistency:

- n8n
- Apache Airflow
- OpenMetadata

## Fixed coverage gaps

### OpenHands, LangGraph, Aider, SWE-agent

Fixed gaps:

- Added missing deep-report references to `retrieval/retrieval_index.yaml`.
- Added project-neutral change-discovery coverage for project cards, component cards, reports, and retrieval-index update.

No new source analysis, recommendation logic, ranking, or target-project advice was added.

### dbt and Dagster

Fixed gaps:

- Added `transformation_lineage_asset_orchestration` problem route to `retrieval/problem_catalog.yaml`.
- Added compact retrieval route to `retrieval/retrieval_index.yaml` covering:
  - dbt project card
  - Dagster project card
  - dbt component cards
  - Dagster component cards
  - dbt/Dagster deep reports
  - dbt/Dagster comparative report
  - existing MacroForge relevance-map artifacts as historical records
- Added project-neutral change-discovery coverage for dbt and Dagster cards, components, reports, and retrieval updates.
- Normalized active dbt/Dagster project-card links from `ArchitectureHarvest/` compatibility paths to `MetaHarvest/` paths.

No new harvested projects were added.

## Stale wording cleanup

Updated active library-facing wording in:

- `README.md`
- `retrieval/problem_catalog.yaml`
- `retrieval/retrieval_index.yaml`
- affected summaries and handoff files

The cleanup narrows active wording toward descriptive library use and treats recommendation/adoption/relevance artifacts as historical advisory records where they still exist.

Historical ArchitectureHarvest/adoption/recommendation artifacts were not mass-migrated. They remain preserved as provenance or compatibility records.

## Remaining intentional gaps

None for coverage-health consistency.

Intentional preserved residue:

- Historical ArchitectureHarvest names in provenance artifacts and generated-project compatibility language.
- Historical adoption/recommendation/relevance artifacts that predate stable library-v1 doctrine.
- Existing `adoption_*`, `relevance_maps/`, and `synthesis/` folders as preserved historical library corpus, not active recommendation engines.

## Validation

Final validation:

- `uv run --with pytest --with pyyaml pytest tests -q` -> 16 passed
- `uv run --with pyyaml python tools/check_coverage_health.py --project . --json` -> 9 analyzed sources checked; 0 missing coverage records
- `uv run --with pyyaml python tools/check_relationship_health.py --project . --json` -> 13 relationship records checked; 0 invalid relationships
- YAML parse over repository `*.yaml` files -> passed
- `git diff --check` -> passed
