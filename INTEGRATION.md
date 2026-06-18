# MetaHarvest Interface Contract

MetaHarvest is an advisory project/subsystem for reusable non-domain knowledge, patterns, contradictions, source-analysis evidence, recommendation records, and ecosystem learning. This document defines the MetaHarvest-owned interface contract. ProjectForge-specific consumption behavior is owned by ProjectForge, not by this file.

## Interface status

- Interface owner: MetaHarvest
- Current physical status: active sibling EIP project at `/home/mkkto/srv/EIP/projects/MetaHarvest`
- Historical name: ArchitectureHarvest
- Historical references: preserved as historical or compatibility references
- Generated-project compatibility path: `architecture/architectureharvest/`
- Source-cache policy: local cloned repositories are optional, replaceable cache hints configured at `/home/mkkto/srv/EIP/projects/ProjectForge/external_sources`; the directory may be absent until source-level reanalysis rematerializes approved sources

## Authority boundary

MetaHarvest is advisory only.

MetaHarvest may:

- preserve reusable non-domain knowledge;
- preserve harvested source-analysis evidence;
- preserve patterns, anti-patterns, contradictions, and outcome records;
- generate recommendations;
- provide decision-support context;
- record generalized adoption or rejection lessons;
- notify or inform consuming projects through explicit artifacts or interfaces.

MetaHarvest may not:

- govern ProjectForge;
- govern consumer projects;
- directly modify consumer projects;
- create tasks inside consumer projects;
- force adoption of recommendations;
- bypass project-local approval gates;
- treat domain conclusions as MetaHarvest-owned knowledge.

## Required provider interface files

A consumer that integrates with MetaHarvest may validate only the provider interface unless it is explicitly performing a MetaHarvest-internal validation.

Minimum provider interface:

```text
README.md
CONSTITUTION.md
INTEGRATION.md
source_registry.yaml
retrieval/problem_catalog.yaml
retrieval/retrieval_index.yaml
retrieval/recommendation_rules.yaml
```

Consumers should not require direct knowledge of all MetaHarvest internal directories as a condition of normal operation.

## Recommendation contract

A MetaHarvest recommendation should preserve:

- origin project;
- recommendation identifier;
- rationale;
- expected benefit;
- implementation cost estimate;
- architectural impact estimate when relevant;
- confidence score;
- priority score;
- status;
- lineage;
- review/adoption/rejection/supersession outcomes when known.

Confidence and priority should use decimal representation where meaningful, for example `0.83`, not percentages.

## Decision-support consultation workflow

When MetaHarvest is consulted for project creation, architecture review, redesign, subsystem creation, or governance-pattern review, Hermes should answer through compact retrieval first:

1. Interpret the problem and find matching entries in `retrieval/problem_catalog.yaml`.
2. Use `retrieval/retrieval_index.yaml` to find related patterns, synthesized records, contradictions, outcomes, and relevance maps.
3. Prefer synthesized pattern records over one-off project reports when convergence exists.
4. Check contradictions before recommending a pattern.
5. Check outcome models and adoption logs to separate generic recommendations from recommendations proven or disproven in this ecosystem.
6. Check target-specific relevance maps where available.
7. Drill down into project cards, component cards, or deep reports only when compact records are insufficient.

A consultation result should state:

- interpreted problem;
- relevant patterns or reusable knowledge categories;
- evidence strength;
- local fit;
- tradeoffs;
- prior outcomes;
- generic recommendation;
- ecosystem-weighted recommendation;
- confidence;
- next project-local governance gate.

## Feedback loop

Consuming projects own their local adoption, rejection, deferral, supersession, and implementation decisions.

MetaHarvest may preserve broadly useful lessons in `adoption_log/`, but those records are generalized outcome memory, not authority over the originating project.

## Non-domain boundary

MetaHarvest may preserve reusable non-domain concepts, vocabulary, methodologies, decision patterns, governance patterns, heuristics, architecture patterns, and system-design lessons.

MetaHarvest must not preserve consumer-domain conclusions as its own knowledge base. GDP analysis, inflation analysis, energy-market knowledge, macroeconomic conclusions, investment theses, company research, and similar domain knowledge remain in the domain projects that own those purposes.

## Source-cache boundary

`source_registry.yaml` is MetaHarvest-owned source-lifecycle metadata.

Local cloned repositories are optional, replaceable caches. During EIP finalization, source-cache paths were migrated to `/home/mkkto/srv/EIP/projects/ProjectForge/external_sources` as cache hints, not canonical source identities. The cache directory may be absent during normal consultation; absence does not invalidate analyzed-source records when repository URL, commits, and MetaHarvest artifacts are present.

Canonical source identity should be represented by:

- source ID;
- repository URL;
- approved/analyzed commit;
- source-relative evidence path;
- MetaHarvest analysis artifact path;
- lifecycle/review status.

## Compatibility boundary

The historical `ArchitectureHarvest` name remains valid only as:

- historical lineage;
- generated-project compatibility path language;
- compatibility alias where needed.

New active references should use `MetaHarvest` unless preserving historical truth or compatibility paths.
