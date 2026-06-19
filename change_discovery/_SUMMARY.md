# Folder Summary: MetaHarvest/change_discovery

## Purpose
This folder publishes project-neutral MetaHarvest change-discovery records.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `index.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `index.yaml` lets consumers answer "What changed in MetaHarvest since I last looked?" without MetaHarvest determining project-specific relevance or recommending action.

## Needs Attention
- Keep entries project-neutral: no affected-project lists, project-specific recommendations, adoption suggestions, automatic review generation, task creation, or project modification.
- Backfill change records for the 2026-06-19 taxonomy-diversity harvest before consumers rely on `list_changes.py` for complete post-harvest awareness.
