# Folder Summary: MetaHarvest/tools

## Purpose
This folder is part of the ProjectForge file-backed operating system for `MetaHarvest/tools`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `check_coverage_health.py`
- `check_relationship_health.py`
- `list_changes.py`
- `query_knowledge.py`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `check_coverage_health.py` reports missing analyzed-source library coverage across registry, project cards, component cards, reports, retrieval, and change discovery; it emits missing coverage only.
- `check_relationship_health.py` validates explicit relationship records for bounded predicates, required source/target fields, and endpoint path resolution; it emits malformed or unresolved records only.
- `list_changes.py` reads `change_discovery/index.yaml` and lists project-neutral MetaHarvest changes since a caller-supplied sequence/date checkpoint.
- `query_knowledge.py` answers descriptive MetaHarvest-owned knowledge queries by problem id, keyword, pattern id, or artifact id and includes matching explicit relationship records without project-specific relevance evaluation or advice.

## Needs Attention
- No folder-specific issues recorded.
