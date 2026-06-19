# MetaHarvest Relationship Capability Audit

Date: 2026-06-19
Status: bounded audit
Scope: current MetaHarvest artifact relationships among sources, project cards, component cards, concepts, methodologies, patterns, interfaces, and reports.

## Objective

Determine whether MetaHarvest currently supports first-class artifact relationships, whether current relationships are explicit/implicit/absent, whether retrieval can traverse them, whether they are deterministic, and whether current doctrine permits relationship modeling.

Non-goals honored:

- no recommendations about adopting external sources
- no rankings
- no adoption suggestions
- no synthesis
- no architectural advice for consumer projects

## Executive assessment

MetaHarvest already contains many relationship-like fields, but it does not currently have first-class artifact relationships.

Current state:

- Relationship data exists as file paths, source IDs, problem IDs, pattern IDs, link lists, evidence lists, and change-discovery path lists.
- These relationships are deterministic because they are file-backed YAML/Markdown records.
- Most relationships are implicit or typed only by container field name, not by stable relationship predicates such as `implements`, `contains`, `references`, `depends_on`, `related_to`, `part_of`, or `derived_from`.
- Retrieval can surface co-indexed related artifacts and change references, but it cannot perform general relationship traversal.
- Current doctrine permits project-neutral relationship modeling as a legitimate library capability if it remains descriptive and file-backed.

Conclusion:

MetaHarvest has relationship ingredients and partial relationship discovery, but not a sufficient first-class relationship model.

## Evidence inspected

Primary files inspected:

- `CONSTITUTION.md`
- `INTEGRATION.md`
- `latest_handoff.md`
- `source_registry.yaml`
- `retrieval/problem_catalog.yaml`
- `retrieval/retrieval_index.yaml`
- `tools/query_knowledge.py`
- `tools/check_coverage_health.py`
- `change_discovery/index.yaml`
- `templates/project_card.template.yaml`
- `templates/component_card.template.yaml`
- sample project cards, component cards, synthesis records, and indexes

Deterministic corpus scan found relationship-like keys including:

- `source_project_id`
- `component_cards`
- `project_cards`
- `reports`
- `pattern_ids`
- `related_problems`
- `problems_solved`
- `useful_patterns`
- `observed_in`
- `links`
- `evidence_files_inspected`
- `contradiction_records`
- `adoption_outcomes`
- `synthesized_patterns`
- `pattern_cards`

The same scan found zero uses of these explicit relationship predicate keys:

- `implements`
- `contains`
- `references`
- `depends_on`
- `related_to`
- `part_of`
- `derived_from`

## Current relationship mechanisms

### 1. Source to project card

Mechanism:

- `source_registry.yaml` records sources and their lifecycle.
- `project_cards/<source_id>.yaml` conventionally mirrors analyzed sources.
- `tools/check_coverage_health.py` assumes analyzed source `id` maps to `project_cards/<id>.yaml`.

Classification:

- deterministic: yes
- explicit: partly
- first-class relationship: no

The relationship is deterministic by naming convention, but no artifact states `source X has_project_card Y` as a typed edge.

### 2. Project card to component cards/reports

Mechanism:

- project cards contain `links.human_summary`, `links.deep_report`, and `links.component_cards`.
- `templates/project_card.template.yaml` includes those fields.

Classification:

- deterministic: yes
- explicit: yes as link fields
- first-class relationship: partial

These are the strongest current relationships. They encode direct links, but the relationship type is implied by the field name rather than represented as reusable relationship records.

### 3. Component card to source/project

Mechanism:

- component cards contain `component.source_project_id`.
- component cards also preserve source evidence in `analysis.evidence_files_inspected`.

Classification:

- deterministic: yes
- explicit: yes for component -> source project ID
- first-class relationship: partial

The source-project relationship exists but is not generally traversable as a relationship graph. Evidence file references are descriptive pointers, not typed artifact relationships.

### 4. Component card to concepts, methodologies, patterns, and interfaces

Mechanism:

- component cards contain `architecture.problems_solved`, `architecture.related_problems`, `architecture.useful_patterns`, and category/name fields.
- retrieval entries may include `concept_terms`, `methodology_terms`, `interface_terms`, and `pattern_ids`.

Classification:

- deterministic: yes
- explicit: partial
- first-class relationship: no

Concepts, methodologies, and interfaces are mostly terms, not first-class artifacts. They can be found textually or through retrieval-index terms, but they are not independently addressable nodes with typed relationships.

### 5. Retrieval index relationships

Mechanism:

- `retrieval/retrieval_index.yaml` groups artifacts under `problem_id` entries.
- Each entry lists `pattern_ids`, `synthesized_patterns`, `pattern_cards`, `component_cards`, `project_cards`, `reports`, `concept_terms`, `methodology_terms`, `interface_terms`, contradictions, outcomes, relevance maps, and recommendation records.
- `tools/query_knowledge.py` emits `evidence_sources` with `relation: referenced_by_retrieval_index`.

Classification:

- deterministic: yes
- explicit: partial
- first-class relationship: partial but narrow

The retrieval index gives deterministic co-location by problem. It can answer “what artifacts are connected to this problem?” It does not model general artifact-to-artifact relationships or support arbitrary traversal such as source -> project card -> component card -> pattern -> report.

### 6. Change-discovery path relationships

Mechanism:

- `change_discovery/index.yaml` groups changed artifact paths in sequence records.
- `tools/list_changes.py` lists those changes.
- `tools/query_knowledge.py` can include change-discovery references when matched records overlap change paths.

Classification:

- deterministic: yes
- explicit: partial
- first-class relationship: no

Change records relate artifacts by co-change event, not by semantic relation. This is useful but not first-class relationship modeling.

### 7. Synthesis/pattern relationships

Mechanism:

- synthesis records include `observed_in.analyzed_projects`, `problems_solved`, `related_problems`, `anti_problems`, `contradictions`, and sometimes recommendation/evidence fields.

Classification:

- deterministic: yes
- explicit: partial
- first-class relationship: partial inside synthesis only

Synthesis records have richer internal relationships, but they are not normalized across the whole library and do not cover all artifacts.

## Explicit, implicit, absent

| Relationship type | Current support | Notes |
| --- | --- | --- |
| source -> project card | implicit/partial | Naming convention plus coverage-health assumption. |
| project card -> component cards | explicit/partial | `links.component_cards`; field-typed but not edge-typed. |
| project card -> report | explicit/partial | `links.human_summary`, `links.deep_report`. |
| component card -> source | explicit/partial | `component.source_project_id`. |
| component card -> evidence file | explicit/partial | `analysis.evidence_files_inspected`; source-relative evidence, not MetaHarvest artifact edge. |
| artifact -> problem | explicit/partial | Retrieval index groups artifacts by `problem_id`; component cards also list problems. |
| artifact -> concept/methodology/interface | implicit/partial | Terms exist, but many are not first-class artifact IDs. |
| pattern -> observed source | explicit/partial | Synthesis `observed_in.analyzed_projects`. |
| report -> component/project/source | mostly implicit | Markdown content and naming conventions, not typed edges. |
| change -> artifacts | explicit/partial | Path list in change-discovery records. |
| implements | absent | No current predicate key. |
| contains | absent | No current predicate key. |
| references | absent as predicate | Path lists reference artifacts, but no stable `references` edge. |
| depends_on | absent as MetaHarvest relationship | Appears in source-analysis prose/evidence only. |
| related_to | absent as predicate | `related_problems` exists, not generic `related_to`. |
| part_of | absent | No current predicate key. |
| derived_from | absent | No current predicate key. |

## Retrieval traversal assessment

Current retrieval can:

- query by problem ID;
- query by keyword;
- query by pattern ID;
- query by artifact ID/path;
- return retrieval-index evidence sources;
- return matching synthesis, contradiction, adoption outcome, adoption candidate, pattern-library, index, and change-discovery records;
- show that evidence is `referenced_by_retrieval_index`.

Current retrieval cannot:

- traverse arbitrary relationships by predicate;
- answer “what does this artifact contain?” as a typed edge query;
- answer “what artifacts are derived from this source?” except through conventions and coverage-health assumptions;
- distinguish semantic `references` from mere file-path inclusion;
- traverse from a concept term to all component cards unless the term is textually/indexed matched;
- validate relationship directionality or cardinality.

Therefore retrieval supports deterministic co-index lookup, not first-class relationship traversal.

## Determinism assessment

Existing relationship-like data is deterministic where it exists:

- YAML fields are stable and file-backed.
- Paths are explicit strings.
- `query_knowledge.py`, `list_changes.py`, and `check_coverage_health.py` operate deterministically over files.
- No database, vector store, UI, or external service is required.

Weakness:

- Because many relationships are conventions or terms, determinism does not imply completeness or typed meaning.
- Path references can be checked for existence, but semantic relationship intent is often inferred from field names.

## Doctrine fit

Current doctrine permits relationship modeling if bounded correctly.

Supporting doctrine:

- `CONSTITUTION.md` states MetaHarvest may preserve architecture patterns, interface patterns, shared concepts, vocabulary, methodologies, decision patterns, governance patterns, heuristics, anti-patterns, and failure patterns.
- `CONSTITUTION.md` requires analyzed projects to produce project cards, component cards, and reports.
- `CONSTITUTION.md` says patterns should declare problems solved, related problems, and anti-problems.
- `INTEGRATION.md` permits project-neutral retrieval helpers that return descriptive records, evidence sources, contradictions, synthesis records, adoption outcomes, and change references.
- v1 storage constraints allow Markdown, YAML, and generated JSON audits; no new database or vector store is permitted.

Boundary conditions:

- Relationship modeling must remain project-neutral and descriptive.
- It must not emit recommendations, rankings, adoption suggestions, target-project relevance, affected-project lists, automatic task creation, or automatic project modification.
- It must not become synthesis generation or architectural advice.

Conclusion:

A file-backed deterministic relationship index would be a legitimate library capability under current doctrine. It would be library metadata, not governance or recommendation logic.

## Gaps

1. No first-class relationship artifact or index.

There is no canonical file that records typed edges such as:

- source contains project card
- project card references component card
- component card derived_from source evidence file
- problem related_to pattern
- report references component card

2. No stable relationship predicate vocabulary.

Existing field names imply relations, but MetaHarvest does not have a bounded predicate set or edge schema.

3. Concepts, methodologies, and interfaces are not uniformly addressable artifacts.

Recent retrieval backfill stores them as terms. That is sufficient for discoverability, but insufficient for first-class relationships.

4. Retrieval lacks relationship traversal.

`query_knowledge.py` can surface indexed evidence, but it cannot traverse relationship edges because no edge index exists.

5. Coverage-health checks do not validate relationship consistency.

`tools/check_coverage_health.py` verifies analyzed-source coverage across registry/cards/reports/retrieval/change discovery. It does not verify relationship edge completeness because no first-class relationship surface exists.

## Risks

1. Hidden coupling through path lists.

As the library grows, path lists in project cards, retrieval indexes, and change records may drift without a single relationship consistency check.

2. Concept ambiguity.

Concepts such as `workflow graph`, `lineage edge`, and `credential boundary` can be retrieved as terms, but not disambiguated as stable relationship nodes.

3. Traversal overreach.

Adding traversal without a strict doctrine boundary could drift into recommendation, ranking, or target-project advice. Any future relationship capability must report descriptive edges only.

4. Premature abstraction.

A relationship system could become an unnecessary graph platform. Current v1 doctrine forbids databases/vector stores and favors file-backed YAML/Markdown.

5. Historical compatibility paths.

Some older artifacts still use `ArchitectureHarvest/` paths. A relationship task would need to preserve historical truth and compatibility aliases rather than rewriting history.

## Recommendation

Relationships are not currently sufficient as a first-class capability.

Recommendation: create a future task for a minimal, file-backed, deterministic relationship index and validation check.

The task should be bounded to:

- describe existing relationships only;
- use existing artifacts as source of truth;
- define a small predicate vocabulary;
- avoid new storage architecture;
- avoid recommendations, rankings, adoption suggestions, synthesis, or project-specific advice;
- add validation that reports missing or stale relationship coverage only.

Do not implement this task during this audit.
