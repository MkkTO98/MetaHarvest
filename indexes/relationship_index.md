# Relationship Index

Status: active
Updated: 2026-06-19

## Purpose

This index points to MetaHarvest's first-class relationship metadata surface.

Canonical relationship file:

- `relationships/index.yaml`

Validation command:

- `uv run --with pyyaml python tools/check_relationship_health.py --project . --json`

## Predicate vocabulary

The bounded vocabulary is intentionally small:

- `implements`
- `contains`
- `references`
- `part_of`
- `derived_from`
- `analyzes`

## Doctrine boundary

Relationship records are descriptive metadata only. They must not be used to emit recommendations, rankings, adoption suggestions, project-specific advice, target-project relevance, governance decisions, or automatic task creation.

## Current relationship coverage

Initial explicit records cover a narrow, evidence-backed subset:

- source registry references to selected project cards
- selected project-card containment of component cards
- selected component-card `part_of` links back to project cards
- selected project-card references to taxonomy harvest reports
- relationship audit analysis of the relationship-index task

This is intentionally not a graph traversal system and does not imply unrecorded relationships.
