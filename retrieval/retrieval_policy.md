# ArchitectureHarvest Retrieval Policy

ArchitectureHarvest answers architectural questions through a problem-first, compact-context workflow.

## Query shape

Use this chain:

Problem -> Relevant Patterns -> Relevant Components -> Relevant Projects -> Prior Adoption Outcomes -> Recommendation

The purpose is to answer:

- What patterns solve this problem?
- Which projects contain those patterns?
- Which implementations have succeeded?
- Which implementations have failed?
- Which recommendations are strongest?

without reading every project report.

## Consultation order

When consulted during project creation, architecture review, architecture redesign, or subsystem creation, Hermes must query in this order:

1. `retrieval/problem_catalog.yaml`
2. `retrieval/retrieval_index.yaml`
3. synthesized pattern records under `synthesis/` and `pattern_library/`
4. contradiction records under `contradictions/`
5. outcome models and adoption outcomes under `outcome_models/` and `adoption_log/`
6. project-specific relevance maps under `relevance_maps/<target>/`
7. project, component, and deep reports only when the compact records are insufficient

## Output discipline

A consultation answer should include:

- problem interpreted
- relevant patterns
- evidence strength
- local fit
- tradeoffs and contradictions
- prior ecosystem outcomes
- generic recommendation
- ecosystem-weighted recommendation
- confidence and limitations
- next ProjectForge governance gate if implementation is considered

## Context controls

Use tags, relevance scores, maturity fields, lifecycle status, concise YAML cards, and explicit links. Do not load cloned repositories or long reports unless the compact retrieval layer cannot answer the question.

## Safety limits

ArchitectureHarvest may recommend, reject, simplify, replace, defer, or retire. It may not override project governance, create implementation work without a recommendation record, automatically refactor projects, or introduce databases/vector stores/UI systems for v1.
