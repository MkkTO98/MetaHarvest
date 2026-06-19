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

MetaHarvest is advisory only. Ecosystem-wide capability ownership is recorded in `/home/mkkto/srv/EIP/governance/CAPABILITY_OWNERSHIP.md`; that artifact preserves the same boundary: MetaHarvest stores and publishes reusable non-domain knowledge, while consuming projects evaluate relevance and act locally.

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
- treat domain conclusions as MetaHarvest-owned knowledge;
- perform project-specific relevance determination;
- prioritize consumer-project work;
- automatically propagate adoption, rejection, or implementation decisions.

## Change-discoverability boundary

MetaHarvest is responsible for discoverability of change. Projects are responsible for evaluation of change.

MetaHarvest owns publication of:

- new artifacts;
- modified artifacts;
- retired artifacts;
- superseded artifacts;
- staleness information.

Consuming projects own:

- relevance evaluation;
- adoption;
- rejection;
- implementation;
- local prioritization.

The provider interface may expose a project-neutral change-discovery index that answers: "What changed in MetaHarvest since I last looked?" It must not answer: "Does this matter to my project, and what should I do?"

The provider interface may also expose a project-neutral retrieval helper that answers: "What does MetaHarvest know about problem Y?" It must return descriptive records, evidence sources, contradictions, synthesis records, adoption outcomes, and change references without target-project identity, affected-project computation, local-fit judgment, task suggestions, notification routing, or priority ranking.

This boundary exists because MetaHarvest is an advisory knowledge provider, not an ecosystem coordinator. Change discoverability prevents stale consumer context while preserving local governance, local prioritization, and project autonomy.

Future agents must not turn change discovery into recommendation engines, ecosystem coordinators, project-ranking systems, automatic propagation systems, automatic task creation, automatic project modification, or EII-style functionality inside MetaHarvest.

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
change_discovery/index.yaml
tools/query_knowledge.py
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

When MetaHarvest is consulted for reusable non-domain knowledge retrieval, Hermes should answer through compact retrieval first:

1. Interpret the problem, keyword, pattern id, or artifact id.
2. Find matching entries in `retrieval/problem_catalog.yaml` and `retrieval/retrieval_index.yaml`.
3. Return related synthesis records, pattern records, contradictions, generalized adoption outcomes, evidence-source paths, and change-discovery references.
4. Drill down into project cards, component cards, or deep reports only when compact records are insufficient.
5. Leave relevance evaluation, adoption, rejection, implementation, task creation, and prioritization to the consuming project.

A retrieval result should state:

- interpreted query;
- matching records;
- evidence sources;
- synthesis records;
- contradictions;
- generalized adoption outcomes;
- change-discovery references;
- source-record confidence or limitations when present.

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
