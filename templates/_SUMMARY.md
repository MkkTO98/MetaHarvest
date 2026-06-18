# Folder Summary: MetaHarvest/templates

## Purpose
This folder is part of the ProjectForge file-backed operating system for `MetaHarvest/templates`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `adoption_candidate.template.yaml`
- `adoption_outcome.template.yaml`
- `audit_record.template.yaml`
- `component_card.template.yaml`
- `contradiction_record.template.yaml`
- `lifecycle_metadata.template.yaml`
- `pattern_card.template.yaml`
- `problem_record.template.yaml`
- `project_card.template.yaml`
- `rejection_record.template.yaml`
- `recommendation.template.yaml`
- `relevance_map.template.yaml`
- `retrieval_query.template.yaml`
- `synthesized_pattern.template.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `recommendation.template.yaml` defines backward-compatible recommendation schema v2 for new recommendation artifacts; historical v1 artifacts were not mass-migrated.

## Needs Attention
- Use decimal confidence/priority values when meaningful, but retain low/medium/high labels where decimal precision would be false.
