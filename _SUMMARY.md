# Folder Summary: MetaHarvest

## Purpose
This folder is part of the ProjectForge file-backed operating system for `MetaHarvest`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `CONSTITUTION.md`
- `INTEGRATION.md`
- `README.md`
- `latest_handoff.md`
- `adoption_candidates/`
- `adoption_log/`
- `adoption_proposals/`
- `anti_patterns/`
- `audits/`
- `component_cards/`
- `contradictions/`
- `decisions/`
- `change_discovery/`
- `experiments/`
- `indexes/`
- `outcome_models/`
- `pattern_library/`
- `project_cards/`
- `projects/`
- `rejected/`
- `relevance_maps/`
- `reports/`
- `relationships/`
- `retired/`
- `retrieval/`
- `reviews/`
- `source_registry.yaml`
- `synthesis/`
- `tasks/`
- `templates/`
- `tests/`
- `tools/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `CONSTITUTION.md`, `README.md`, and `INTEGRATION.md` frame MetaHarvest as an active sibling EIP advisory project with historical ArchitectureHarvest provenance preserved only where it is evidence or compatibility language.
- Recommendation language uses candidate task proposals/task recommendations and forbids task creation inside target projects.
- `templates/recommendation.template.yaml` defines recommendation schema v2 while historical artifacts remain unmigrated.
- `source_registry.yaml` keeps local source paths as optional replaceable cache hints; normal consultation does not require local clones to exist.
- `change_discovery/index.yaml` publishes project-neutral MetaHarvest change records; consuming projects evaluate relevance locally.
- `tools/query_knowledge.py` provides the smallest descriptive retrieval helper for asking what MetaHarvest knows about a problem, keyword, pattern, or artifact.
- `reports/R-20260619-infrastructure-status-audit.md` records the bounded status of retrieval, change discovery, query/list tools, tests, and related decisions.
- `tasks/T-20260619-library-discoverability-backfill.md` is completed; n8n, Apache Airflow, and OpenMetadata are discoverable through compact retrieval and change-discovery surfaces.
- `tools/check_coverage_health.py` reports missing analyzed-source coverage across registry, cards, reports, retrieval, and change discovery.
- `reports/R-20260619-relationship-capability-audit.md` records that MetaHarvest has deterministic relationship-like metadata but not first-class typed artifact relationships.
- `tasks/T-20260619-minimal-first-class-relationship-index.md` is completed; `relationships/index.yaml`, `tools/check_relationship_health.py`, and query output now expose only explicit descriptive relationship records.
- `indexes/relationship_index.md` documents the relationship surface and bounded predicate vocabulary.

## Needs Attention
- Do not let MetaHarvest govern, directly modify, or create tasks inside consumer projects without separate project-local approval.
- Do not let retrieval or change discovery drift into affected-project lists, project-specific advice, recommendation engines, ecosystem coordination, task suggestions, notification routing, prioritization, or EII-style functionality.
- Historical v1 adoption candidates remain as-is; use the v2 recommendation template for new recommendation artifacts when appropriate.
