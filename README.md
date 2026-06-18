# MetaHarvest (conceptual name: MetaHarvest)

MetaHarvest is currently hosted within ProjectForge as an advisory subsystem. Its conceptual long-term name is MetaHarvest: a file-backed system for discovering, preserving, organizing, analyzing, and recommending reusable non-domain knowledge.

The current physical directory remains `MetaHarvest/`. This conceptual rename does not split the subsystem, create a new project, relocate files, or change governance authority.

MetaHarvest's purpose is broader than architecture patterns alone. It preserves reusable non-domain knowledge from projects, systems, architectures, implementations, successes, failures, concepts, methodologies, interfaces, governance structures, decision patterns, and heuristics. It helps ProjectForge, MacroForge, and future projects avoid reinventing infrastructure, reduce unnecessary complexity, preserve lessons, and selectively consider proven patterns through project-local governance.

MetaHarvest is not a research archive and not a domain-knowledge repository. It is a file-based advisory knowledge system for Hermes.

## Purpose boundaries

MetaHarvest is advisory only. It may provide evidence, patterns, concepts, vocabulary, methodologies, decision lessons, governance lessons, heuristics, recommendations, candidate task proposals, and decision inputs. It must not govern projects, enforce standards, create tasks inside other projects, automatically adopt recommendations, automatically implement changes, or directly modify target projects.

Projects remain autonomous. MetaHarvest recommendations are inputs to project-local review.

MetaHarvest remains non-domain. It may preserve reusable non-domain methods discovered while working on domain projects, but it must not store domain conclusions such as GDP analysis, inflation analysis, energy-market knowledge, macroeconomic conclusions, investment theses, or company research. Those belong to domain projects.

## Knowledge categories

MetaHarvest may explicitly reason about reusable non-domain knowledge categories including:

- architecture patterns;
- interface patterns;
- shared concepts;
- shared vocabulary;
- shared methodologies;
- decision patterns;
- governance patterns;
- heuristics;
- anti-patterns and failure patterns.

These categories guide retrieval and recommendations. They do not create mandatory standards and do not require new storage systems or artifact types by default.

## v1 scope

MetaHarvest / MetaHarvest v1 is local-first and file-only:

- YAML source registry and cards
- Markdown summaries, reports, decisions, and indexes
- generated JSON audit outputs when tools are added later
- no database
- no vector store
- no dashboard or UI
- no mandatory cloud dependency
- no execution of third-party code without separate approval

## Storage

Subsystem files live in this ProjectForge repository at:

```text
MetaHarvest/
```

Raw cloned third-party repositories must live outside the git-tracked source tree, normally at:

```text
/home/mkkto/srv/EIP/projects/ProjectForge/external_sources/
```

## How Hermes should use this subsystem

Use MetaHarvest when:

- creating a new ProjectForge-managed project
- planning a major architecture change
- doing a scheduled architecture/project review
- encountering repeated failure/debug cycles
- before building a new subsystem
- detecting homemade infrastructure that overlaps a known pattern category
- the user asks for an improvement scan

Do not use MetaHarvest for small bug fixes, minor documentation edits, simple tests, or trivial one-file utilities.

## Normal workflow

1. Check `source_registry.yaml` for approved, analyzed, stale, rejected, and retired sources.
2. If a repository is only a candidate, ask the user before approving or cloning it.
3. Clone approved repositories only under `/home/mkkto/srv/EIP/projects/ProjectForge/external_sources/`.
4. Inspect source/docs/issues without executing third-party code.
5. Produce the four analysis layers:
   - human summary in `projects/`
   - project card in `project_cards/`
   - component cards in `component_cards/`
   - deep report in `reports/`
6. Extract or update cross-project patterns in `pattern_library/`.
7. Update target relevance maps under `relevance_maps/<target>/`.
8. Create adoption, simplification, replacement, deletion, rejection, or task recommendation proposals as appropriate.
9. Route implementation through normal ProjectForge decision/dry-run/test/coherence gates.

## Key files

- `CONSTITUTION.md`: doctrine, governance, safety, audit rules, and blindspot controls.
- `source_registry.yaml`: machine-readable source list and state/staleness metadata.
- `indexes/`: human-readable navigation and retrieval hints.
- `templates/`: canonical YAML template shapes for cards and records.
- `projects/`: human summaries for analyzed projects.
- `project_cards/`: compact Hermes-readable project cards.
- `component_cards/`: component-level cards; do not treat projects as monoliths.
- `pattern_library/`: cross-project reusable patterns.
- `relevance_maps/`: target-specific fit maps.
- `adoption_candidates/`: decision-grade recommendation artifacts awaiting target-project review.
- `adoption_log/`: outcomes after recommendations are accepted/rejected/implemented.
- `rejected/` and `retired/`: preserved negative knowledge.
- `audits/` and `reports/`: source audits, target consultations, and deep reports.

## Retrieval discipline

Prefer compact files first:

1. relevant index
2. source registry entry
3. project card
4. component cards
5. pattern card
6. relevance map
7. deep report only when needed

Avoid loading cloned repository trees or large reports into normal context unless a specific audit or analysis task requires it.

## v1 initial candidates

The initial candidate batch is:

- OpenHands
- LangGraph
- Aider
- SWE-agent
- AutoGen

They are candidates only. They are not approved for cloning until the user explicitly approves them.

## Project feedback loop

Generated ProjectForge projects maintain lightweight local MetaHarvest files under `architecture/architectureharvest/`:

- `relevance_map.yaml`: target-specific active/stale/superseded/retired recommendations.
- `adoption_candidates.md`: advisory recommendation proposals that still require normal governance.
- `rejected_candidates.md`: negative knowledge for the project.
- `review_history.md`: periodic architecture review history.
- adoption outcome records: optional YAML entries that can be mirrored to `MetaHarvest/adoption_log/` when generally useful.

Architecture reviews answer whether the project architecture changed, new patterns became relevant, recommendations became obsolete, simplification/replacement/deletion opportunities exist, recurring failures are already solved elsewhere, or adopted patterns should be reported back.

Reviews generate recommendations, candidate task proposals, and decision inputs. MetaHarvest may recommend that a project consider opening a task, but it may not create tasks inside another project and must not trigger automatic adoption or implementation.

## Decision-support retrieval layer

MetaHarvest now starts from problems, not source-project enthusiasm. For architecture consultation, use:

```text
Problem -> Relevant Patterns -> Relevant Components -> Relevant Projects -> Prior Adoption Outcomes -> Recommendation
```

Canonical retrieval files live under `retrieval/`:

- `problem_catalog.yaml`: problem-first catalog with related patterns, anti-problems, lifecycle metadata, and evidence notes.
- `retrieval_index.yaml`: compact routing index from problems to patterns, synthesis records, contradictions, outcomes, and relevance maps.
- `recommendation_rules.yaml`: explainable maturity and recommendation-strength rules.
- `retrieval_policy.md`: Hermes consultation workflow and context discipline.

Hermes should consult these files before reading project/component/deep reports. Deep reports are evidence, not the first retrieval layer.

## Maturity, contradictions, outcomes, and synthesis

Pattern recommendations must distinguish generic evidence from ProjectForge ecosystem evidence. Cards and recommendations use explicit fields for `evidence_strength`, `adoption_count`, `projects_observed`, `confidence`, `maintenance_cost`, `local_fit`, and `recommendation_strength`.

- `synthesis/`: cross-project synthesized pattern records. These become the preferred recommendation source once multiple projects independently solve the same problem.
- `contradictions/`: competing architectural approaches with contexts where each wins or loses. Do not force a winner when assumptions differ.
- `outcome_models/`: file-based rules for weighting ProjectForge/MacroForge/generated-project adoption outcomes.

Lifecycle metadata (`first_seen`, `last_reviewed`, `last_referenced`, `last_adoption`, `adoption_frequency`, and status) helps identify heavily reused, forgotten, stale, superseded, or retired patterns without deleting historical context.
