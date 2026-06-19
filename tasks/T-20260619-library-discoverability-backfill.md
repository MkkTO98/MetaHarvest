# Task: Backfill Library Discoverability Coverage for Taxonomy-Diversity Harvest

Date created: 2026-06-19
Status: future_task
Owner: MetaHarvest

## Purpose

Make the recently harvested n8n, Apache Airflow, and OpenMetadata knowledge discoverable through the existing MetaHarvest retrieval and change-discovery surfaces.

This is a coverage backfill task, not a new architecture task.

## Background

The 2026-06-19 taxonomy-diversity harvest added descriptive library artifacts for:

- n8n
- Apache Airflow
- OpenMetadata

These artifacts broaden MetaHarvest category coverage into:

- workflow automation
- integration platforms
- orchestration systems
- scheduling systems
- metadata catalogs
- lineage systems
- governance-related infrastructure

The bounded infrastructure audit found that the artifacts exist, but the library discovery surface lags behind the harvest:

- `retrieval/retrieval_index.yaml` does not yet provide first-class problem/category routes for the new harvest.
- `change_discovery/index.yaml` does not yet publish project-neutral change records for the harvest.
- tests do not yet prove descriptive retrieval/change discovery for these categories.

## Scope

Update existing file-backed infrastructure only:

- `retrieval/retrieval_index.yaml`
- `retrieval/problem_catalog.yaml`, only if new problem IDs are needed for category routing
- `change_discovery/index.yaml`
- `tests/test_query_knowledge.py`
- `tests/test_change_discovery.py`
- affected folder summaries

## Non-goals

Do not:

- create synthesis records
- create recommendations
- create rankings
- create target-project relevance logic
- create adoption proposals
- modify retrieval architecture
- introduce databases, vector stores, dashboards, services, daemons, or new tools unless a narrow test helper is unavoidable
- modify ProjectForge, MacroForge, or any other EIP project

## Required outcome

A consumer should be able to use the existing library surfaces to discover the new categories descriptively.

Expected examples:

- query by workflow automation and find n8n records
- query by scheduling or timetable and find Airflow records
- query by metadata catalog or lineage and find OpenMetadata records
- list changes since the previous checkpoint and see project-neutral records for the taxonomy-diversity harvest

## Validation requirements

Run and pass:

```text
uvx --with pyyaml --with pytest pytest tests -q
python3 -m py_compile tools/query_knowledge.py tools/list_changes.py
git diff --check
```

Add tests proving:

1. New taxonomy-diversity categories are retrievable descriptively.
2. Retrieval output remains project-neutral and contains no forbidden affected-project/recommendation keys.
3. Change discovery reports the taxonomy harvest as a project-neutral library change.
4. Existing retrieval/change-discovery tests continue to pass.

## Acceptance criteria

- Retrieval coverage includes n8n, Apache Airflow, and OpenMetadata through existing mechanisms.
- Change discovery includes recent harvest/library-expansion records.
- No synthesis, recommendations, ranking, governance, or target-project action logic is introduced.
- All validations pass.
