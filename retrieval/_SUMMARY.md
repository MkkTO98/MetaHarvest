# Folder Summary: MetaHarvest/retrieval

## Purpose
This folder is part of the ProjectForge file-backed operating system for `MetaHarvest/retrieval`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `problem_catalog.yaml`
- `recommendation_rules.yaml`
- `retrieval_index.yaml`
- `retrieval_policy.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `tools/query_knowledge.py` provides a descriptive search surface over existing MetaHarvest-owned knowledge by problem id, keyword, pattern id, or artifact id.
- OpenHands/LangGraph and Aider/SWE-agent ArchitectureHarvest analysis cycles completed on 2026-06-06; recommendations are advisory only and not implemented.

## Needs Attention
- Keep retrieval outputs descriptive: no affected-project computation, local-fit judgment, project-specific recommendations, task suggestions, notification routing, or priority ranking.
- Backfill retrieval index coverage for the 2026-06-19 taxonomy-diversity harvest before considering n8n, Apache Airflow, and OpenMetadata fully discoverable through the compact retrieval surface.
- Refresh source-derived records before using them for implementation decisions; upstream repositories may change.
