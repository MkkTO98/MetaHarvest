# Folder Summary: MetaHarvest

## Purpose
This folder is part of the ProjectForge file-backed operating system for `MetaHarvest`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `CONSTITUTION.md`
- `INTEGRATION.md`
- `README.md`
- `adoption_candidates/`
- `adoption_log/`
- `adoption_proposals/`
- `anti_patterns/`
- `audits/`
- `component_cards/`
- `contradictions/`
- `decisions/`
- `experiments/`
- `indexes/`
- `outcome_models/`
- `pattern_library/`
- `project_cards/`
- `projects/`
- `rejected/`
- `relevance_maps/`
- `reports/`
- `retired/`
- `retrieval/`
- `reviews/`
- `source_registry.yaml`
- `synthesis/`
- `templates/`
- `tools/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `CONSTITUTION.md`, `README.md`, and `INTEGRATION.md` now frame MetaHarvest as currently hosted within ProjectForge as an advisory subsystem, conceptually separable but not split.
- Recommendation language now uses candidate task proposals/task recommendations and forbids task creation inside target projects.
- `templates/recommendation.template.yaml` defines recommendation schema v2 while historical artifacts remain unmigrated.

## Needs Attention
- Do not split MetaHarvest, create a separate MetaHarvest project, add automation, or implement future-project functionality without a separate approved architecture review.
- Historical v1 adoption candidates remain as-is; use the v2 recommendation template for new recommendation artifacts when appropriate.
