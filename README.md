# MetaHarvest

MetaHarvest is a file-backed advisory subsystem for reusable, non-domain knowledge.

It collects and curates evidence from architectures, implementations, and tooling ecosystems so AI-assisted projects can reuse proven practices quickly without re-running full research each time.

It is designed as an **operating support system** for projects in the ProjectForge ecosystem, not as a runtime part of those projects.

---

## What MetaHarvest is

MetaHarvest is:

- a **non-domain knowledge library** for reusable architecture, process, governance, and design lessons;
- a **decision-support system** that helps with problem-first retrieval and recommendations;
- a **governance-aware evidence layer** that preserves context, uncertainty, lifecycle, and outcomes;
- a **Framework-adjacent consumer** for ProjectForge and MacroForge that stays decoupled from any one domain workload.

It is explicit about boundaries: MetaHarvest owns reusable knowledge artifacts; consuming projects own local adoption decisions.

---

## Core principles

1. **Autonomy-first consumption**
   - Consumers decide what to adopt, defer, reject, replace, retire, or preserve.
   - MetaHarvest does not execute, modify, or govern other projects.
2. **Evidence over opinion**
   - New knowledge enters through explicit source registration, artifact generation, and validation.
   - Confidence, lineage, and limitations are stored with recommendations.
3. **Problem-first retrieval**
   - Retrieval starts from problem statements and evidence-backed patterns, then drills into reports only when needed.
4. **Reuse over reinvention**
   - The goal is preserving reusable lessons (including negative outcomes), not copying ecosystems or replacing domain products.
5. **Governed evolution**
   - Architecture grows only when stable project evidence shows value and pressure points.

---

## Operating systems inside MetaHarvest

MetaHarvest is organized into five practical systems:

1. **Source governance and lifecycle**
   - `source_registry.yaml`, candidate/approved/rejected states, freshness and lineage tracking.

2. **Structured ingestion and analysis**
   - Standardized record-driven workflow that produces summaries, cards, components, and reports before conclusions are claimed.

3. **Retrieval and problem mapping**
   - `problem_catalog.yaml`, retrieval indexes, and recommendation policy files for fast problem-to-pattern lookup.

4. **Knowledge modeling**
   - Projects, components, patterns, contradictions, relevance maps, and outcome records encoded in compact files for reuse.

5. **Evolution and outcome feedback**
   - Adoption, rejection, supersession, and staleness metadata ensure decisions are traceable without becoming a controller.

---

## Design philosophy

- **Lightweight**: Minimal fixed surface area, no mandatory external infrastructure.
- **Local-first**: Works from local files and local tool runs.
- **Deterministic**: Artifact-first and reproducible for replay.
- **Evidence-driven**: Canonical outputs are derived from inspected sources, comparisons, and recorded limits.
- **Project-owned**: Consumers own outcomes and implementation choices.
- **Minimal architectural growth**: New abstractions only when clear pressure appears in repeated evidence.

### What MetaHarvest is not

MetaHarvest is intentionally not:

- an orchestration platform;
- a CI/CD framework;
- a project-management system;
- a runtime agent platform;
- a knowledge graph database.

---

## Current status

**Project:** MetaHarvest Stable v1

**Status:** Architecturally stable

**Architecture:** Frozen, subject to constitutional evidence-based evolution.

---

## Getting started

1. Clone and inspect:

```bash
git clone git@github.com:MkkTO98/MetaHarvest.git
cd MetaHarvest
```

2. Read the governing documents first:

- `CONSTITUTION.md`
- `INTEGRATION.md`
- `ingestion/workflow.md` (ingestion and analysis methodology)

3. Start from retrieval interfaces for new consultation tasks:

- `retrieval/problem_catalog.yaml`
- `retrieval/retrieval_index.yaml`
- `templates/` and `source_registry.yaml`

4. Optional validation (no project modification required):

```bash
python3 tools/check_ingestion_workflow.py --project .
```

5. For project onboarding and adoption workflows, use existing compatibility paths:

- `architecture/architectureharvest/` in generated/consuming projects.

---

## Repository structure (high level)

- `projects/` and `projects/*.md` — project-level human summaries.
- `project_cards/` and `component_cards/` — compact machine-oriented records.
- `pattern_library/`, `contradictions/`, `synthesis/`, and `outcome_models/` — reusable cross-project learning (where present).
- `retrieval/` — problem-first discovery and routing.
- `adoption_candidates/` and `adoption_log/` — recommendation hypotheses and outcomes.
- `reports/` — deep analysis artifacts and historical evidence.
- `source_registry.yaml`, `templates/` and `tools/` — source registry and workflow support tooling.

---

## Notes for first-time contributors

MetaHarvest intentionally preserves historical evidence, including rejected or retired artifacts, so the repo remains a long-lived memory for architectural learning.

The compatibility name **ArchitectureHarvest** is retained for historical/provenance context only; new active references should use **MetaHarvest**.