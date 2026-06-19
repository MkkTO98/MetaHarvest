# Folder Summary: MetaHarvest/tests

## Purpose
This folder contains deterministic validation for MetaHarvest's file-backed library infrastructure.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `test_change_discovery.py`
- `test_query_knowledge.py`
- `test_taxonomy_discoverability_backfill.py`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `test_taxonomy_discoverability_backfill.py` validates retrieval coverage, change-discovery coverage, and coverage-health output for n8n, Apache Airflow, and OpenMetadata.
- `test_query_knowledge.py` validates descriptive knowledge retrieval boundaries.
- `test_change_discovery.py` validates project-neutral change discovery boundaries.

## Needs Attention
- Tests must continue to reject affected-project lists, target-project advice, recommendation output, ranking, automatic task generation, and automatic project modification in retrieval/change-discovery surfaces.
