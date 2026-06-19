# MetaHarvest Retrieval Policy

MetaHarvest answers reusable non-domain knowledge and architecture-pattern questions through a problem-first, compact-context workflow.

The retrieval surface answers:

- What does MetaHarvest know about this reusable non-domain problem, pattern, artifact, or keyword?
- Which MetaHarvest records contain matching evidence?
- Which synthesis records, contradictions, adoption outcomes, and change records are connected?

It does not answer:

- Does this matter to a specific project?
- What should a specific project do?
- Which project is affected?
- What should be prioritized?

## Query shape

Use this descriptive chain:

Problem or keyword -> Matching MetaHarvest records -> Evidence sources -> Synthesis records -> Contradictions -> Adoption outcomes -> Change-discovery references

The purpose is to expose MetaHarvest-owned knowledge without manually scanning every record and without performing project-specific relevance evaluation.

## Consultation order

For a descriptive knowledge query, use this order:

1. `retrieval/problem_catalog.yaml`
2. `retrieval/retrieval_index.yaml`
3. synthesized pattern records under `synthesis/` and `pattern_library/`
4. contradiction records under `contradictions/`
5. adoption outcomes under `adoption_log/`
6. adoption candidate artifacts only as evidence records, not as action instructions
7. change records under `change_discovery/`
8. project, component, and deep reports only when compact records are insufficient

Do not require a target project or consult project-specific relevance maps for the basic MetaHarvest-owned knowledge query.

## Output discipline

A retrieval answer should include:

- interpreted query
- matching records
- evidence sources
- synthesis records
- contradictions
- prior generalized adoption outcomes
- change-discovery references
- confidence and limitations when present in the source records

A retrieval answer must remain descriptive. It must not emit local-fit judgments, affected-project lists, project-specific recommendations, task suggestions, notification routing, or priority rankings.

## Context controls

Use tags, relevance scores, maturity fields, lifecycle status, concise YAML cards, and explicit links. Do not load cloned repositories or long reports unless the compact retrieval layer cannot answer the question.

## Validation sources

Validate retrieval against existing analyzed harvested knowledge before adding synthetic examples. Current analyzed sources include OpenHands, LangGraph, Aider, SWE-agent, dbt Core, and Dagster, with project cards, component cards, reports, synthesis records, contradictions, and adoption outcomes already present. These records are sufficient for current retrieval validation. Validation assertions should target analyzed-project records and mature synthesis records rather than legacy `.example.yaml` scaffolds when real harvested evidence exists.

Only document future ingestion needs if existing harvested material becomes insufficient for retrieval validation, taxonomy validation, discovery workflow validation, or methodology extraction validation. Do not clone or add external sources solely to increase collection size; add sources only when they provide meaningful validation value or novel reusable non-domain knowledge.

## Safety limits

MetaHarvest may store, publish, and descriptively retrieve reusable non-domain knowledge. It may not override project governance, evaluate relevance for a specific project, create implementation work, route notifications, automatically refactor projects, or introduce databases/vector stores/UI systems for this minimal retrieval capability.
