# Task: Minimal First-Class Relationship Index

Date created: 2026-06-19
Status: completed
Owner: MetaHarvest

## Purpose

Add the smallest useful file-backed relationship capability for MetaHarvest library artifacts.

This task exists because `reports/R-20260619-relationship-capability-audit.md` found that MetaHarvest has deterministic relationship-like fields and retrieval co-indexing, but no first-class typed relationship surface.

## Scope

Artifacts in scope:

- sources
- project cards
- component cards
- concepts
- methodologies
- patterns
- interfaces
- reports

## Objective

Represent existing library relationships as deterministic, descriptive metadata so MetaHarvest can answer relationship-discovery questions without creating recommendations, rankings, synthesis, or consumer-project advice.

## Requirements

1. Use existing artifacts as source of truth.

Do not invent relationships unsupported by current files.

2. Stay file-backed.

Allowed outputs are YAML, Markdown, and deterministic validation output. Do not add a database, vector store, UI, dashboard, daemon, or external service.

3. Define a small bounded predicate vocabulary.

Candidate predicates to consider:

- contains
- references
- part_of
- derived_from
- related_to
- implements
- depends_on

The final predicate set should be minimal and documented.

4. Preserve doctrine boundaries.

The relationship surface must not emit:

- recommendations
- rankings
- adoption suggestions
- target-project relevance
- affected-project lists
- project-specific advice
- automatic task generation
- automatic project modification
- synthesis

5. Add deterministic validation.

Validation should report missing or stale relationship coverage only. It should not advise what to do with the relationship.

6. Keep retrieval bounded.

If retrieval support is added, it should traverse explicit relationship records descriptively only. It must not infer project-specific relevance or rank paths.

## Candidate implementation surfaces

These are candidate surfaces for the future task, not approved implementation details:

- `relationships/index.yaml`
- `tools/check_relationship_health.py`
- optional read-only relationship query support in `tools/query_knowledge.py`
- tests proving descriptive-only output and absence of forbidden keys

Use fewer surfaces if possible.

## Acceptance criteria

- A first-class relationship index exists or this task explicitly documents why a smaller surface was sufficient.
- Relationships are deterministic and typed.
- Existing links from source registry, project cards, component cards, retrieval index, and reports are represented or intentionally excluded with rationale.
- A validation command reports missing/stale relationship coverage only.
- Existing retrieval/change-discovery doctrine boundaries remain intact.
- Full tests pass.

## Completion record

Completed: 2026-06-19

Implemented surfaces:

- `relationships/index.yaml` as the canonical file-backed relationship index.
- `tools/check_relationship_health.py` for deterministic validation of malformed records, invalid predicates, missing sources, and missing targets.
- `tools/query_knowledge.py` now exposes matching `explicit_relationships` for recorded relationships only.
- `tests/test_relationship_index.py` proves valid relationship resolution, malformed fixture detection, and retrieval exposure.
- `indexes/relationship_index.md` documents the bounded relationship surface.

Predicate vocabulary used:

- `implements`
- `contains`
- `references`
- `part_of`
- `derived_from`
- `analyzes`

Doctrine boundary preserved:

- no recommendations
- no rankings
- no adoption suggestions
- no target-project relevance
- no project-specific advice
- no governance decisions
- no automatic task creation
- no graph traversal or derived edges

Validation runs:

- `uv run --with pytest --with pyyaml pytest tests/test_relationship_index.py -q` -> passed
- `uv run --with pytest --with pyyaml pytest tests -q` -> 16 passed

## Non-goals

- no recommendations
- no ranking systems
- no adoption suggestions
- no synthesis
- no architectural advice
- no consumer-project changes
- no new storage architecture
- no database
- no vector store
