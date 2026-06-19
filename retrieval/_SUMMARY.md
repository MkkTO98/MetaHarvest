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
- `tools/query_knowledge.py` provides a descriptive search surface over existing MetaHarvest-owned knowledge by problem id, keyword, pattern id, or artifact id, including matching explicit relationships from `relationships/index.yaml`.
- OpenHands/LangGraph and Aider/SWE-agent ArchitectureHarvest analysis cycles completed on 2026-06-06; recommendations are advisory only and not implemented.
- n8n, Apache Airflow, and OpenMetadata taxonomy-diversity harvest artifacts are discoverable through compact problem-first retrieval routes added on 2026-06-19.

## Needs Attention
- Keep retrieval outputs descriptive: no affected-project computation, local-fit judgment, project-specific recommendations, task suggestions, notification routing, or priority ranking.
- Refresh source-derived records before using them for implementation decisions; upstream repositories may change.
