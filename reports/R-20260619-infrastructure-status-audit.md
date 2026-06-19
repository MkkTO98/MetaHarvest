# MetaHarvest Infrastructure Status Audit

Date: 2026-06-19
Status: bounded audit
Scope:
- `retrieval/`
- `change_discovery/`
- `tools/query_knowledge.py`
- `tools/list_changes.py`
- related tests
- related decisions

Non-scope:
- new architecture
- synthesis
- recommendation systems
- governance systems
- functionality or source-harvest quality outside the bounded infrastructure surface

## Executive assessment

MetaHarvest has a working file-backed v1 infrastructure surface for descriptive library use:

1. `tools/list_changes.py` answers what changed since a sequence/date checkpoint.
2. `tools/query_knowledge.py` answers descriptive problem/keyword/pattern/artifact queries without requiring target-project identity.
3. `retrieval/problem_catalog.yaml` and `retrieval/retrieval_index.yaml` provide compact problem-first routing for the original analyzed knowledge set.
4. `change_discovery/index.yaml` records project-neutral infrastructure changes.
5. Tests enforce the key boundary: MetaHarvest may publish reusable knowledge and change records, but must not compute affected projects, emit project-specific advice, create tasks for consumers, rank consumer priorities, or modify other projects.

The infrastructure is sufficient for MetaHarvest's intended role as a small file-backed library, provided consumers understand that retrieval coverage depends on explicitly indexed records. It is not yet sufficient as a complete library discovery layer for all currently harvested sources, because recent taxonomy-diversity harvest artifacts are not yet represented in the retrieval index or change-discovery stream.

## Existing capabilities

### Retrieval policy and doctrine

Existing:
- `retrieval/retrieval_policy.md` defines descriptive retrieval boundaries and context discipline.
- `INTEGRATION.md` states the provider interface and explicitly separates MetaHarvest-owned retrieval from consumer-owned relevance evaluation.
- `CONSTITUTION.md` preserves the larger decision-support doctrine while also forbidding automatic project modification and project-specific relevance determination.

Capability:
- Consumers can use MetaHarvest as a descriptive knowledge library without requiring databases, vector stores, dashboards, or cloud services.

### Problem-first retrieval records

Existing:
- `retrieval/problem_catalog.yaml`
- `retrieval/retrieval_index.yaml`
- `retrieval/recommendation_rules.yaml`

Capability:
- Problem IDs can route to related patterns, components, project cards, contradictions, outcomes, and related records.
- The current indexed retrieval set is strongest for long-running agent state, checkpointing, state/event consistency, code-editing agents, and workflow/asset orchestration records that were explicitly indexed.

### Query tool

Existing:
- `tools/query_knowledge.py`

Capability:
- Supports `--problem-id`, `--keyword`, `--pattern-id`, and `--artifact-id`.
- Emits JSON or text.
- Scans compact retrieval records and selected YAML knowledge directories.
- Includes change-discovery references when matched records overlap recorded changes.
- Sanitizes output to avoid forbidden project-specific keys.

Observed working commands:
- `uvx --with pyyaml python tools/query_knowledge.py --project . --problem-id long_running_agent_state --json`
- `uvx --with pyyaml python tools/query_knowledge.py --project . --keyword metadata --json`

### Change discovery

Existing:
- `change_discovery/index.yaml`
- `tools/list_changes.py`
- `decisions/D-20260618-change-discoverability-boundary.md`

Capability:
- Consumers can ask what changed since a sequence or date.
- Output is project-neutral and status-oriented.
- Records distinguish new, modified, retired, superseded, and staleness updates.

Observed working command:
- `uvx --with pyyaml python tools/list_changes.py --project . --since-sequence 0 --json`

### Tests

Existing:
- `tests/test_change_discovery.py`
- `tests/test_query_knowledge.py`

Capability:
- Tests validate doctrine text, output boundaries, usage errors, descriptive-only retrieval, and use of existing analyzed harvested sources for validation.

## Partially implemented capabilities

### Library-wide retrieval coverage

Partially implemented:
- Retrieval works for records represented in `retrieval/retrieval_index.yaml` and selected scanned directories.
- It does not yet cover all current library artifacts equally.
- `query_knowledge.py` scans selected directories: `synthesis`, `contradictions`, `adoption_log`, `adoption_candidates`, and `pattern_library`.
- Project cards, component cards, reports, and source registrations are primarily discoverable when linked through `retrieval/retrieval_index.yaml` or markdown indexes.

Impact:
- Newer taxonomy-diversity harvest artifacts for n8n, Apache Airflow, and OpenMetadata exist as project cards, component cards, reports, source registrations, and index entries, but are not yet first-class retrieval-index entries.

### Change-discovery coverage

Partially implemented:
- The change-discovery mechanism exists and is tested.
- The index currently records the creation of the change-discovery and retrieval surfaces through sequence 5.
- It does not yet record the 2026-06-19 taxonomy-diversity harvest or this audit/task-context work.

Impact:
- Consumers using `list_changes.py` would miss recent library expansion unless the change index is backfilled.

### Doctrine consistency

Partially implemented:
- Bounded retrieval/change-discovery doctrine is coherent and tested.
- Broader MetaHarvest doctrine still contains recommendation and decision-support language, which is historically valid for MetaHarvest, but the current bounded library infrastructure must continue to avoid crossing into project-specific relevance or action.

Impact:
- Tests currently guard the critical boundary for the infrastructure surface. Future edits should preserve the distinction between descriptive library retrieval and advisory recommendation artifacts.

## Incomplete capabilities

1. Retrieval index coverage for newly harvested categories.
   - Missing first-class routing entries for workflow automation, integration platforms, scheduling systems, metadata catalogs, lineage systems, and governance-related infrastructure introduced by n8n, Apache Airflow, and OpenMetadata.

2. Change-discovery entries for recent library expansion.
   - Missing project-neutral change records for the taxonomy-diversity harvest and any subsequent infrastructure audit/task artifacts.

3. Library coverage health check.
   - No deterministic check currently verifies that analyzed sources have at least source registration, project card, component cards, report, index coverage, retrieval coverage where intended, and change-discovery coverage.
   - This is a validation gap, not a request for a new system architecture.

4. Explicit future-task queue.
   - No task artifact folder existed before this audit. This audit creates a single explicit future task artifact rather than implementing the task.

## Active infrastructure work disposition

### Should commit

The current bounded infrastructure work should be committed after validation because it is coherent and useful:
- retrieval policy hardening
- change-discovery index and doctrine
- `tools/query_knowledge.py`
- `tools/list_changes.py`
- related tests
- related decision artifact
- this audit report and explicit next-task artifact

Rationale:
- The tools execute successfully.
- Tests cover the main doctrine boundaries.
- The work strengthens MetaHarvest as a library without adding prohibited architecture.

### Should not reject

No inspected infrastructure artifact should be rejected outright. The existing implementation is modest, file-backed, and aligned with v1 constraints.

### Should convert to explicit future task

The incomplete part should be converted into one explicit task:
- backfill library discoverability coverage for recently harvested taxonomy-diversity sources.

This task should update retrieval/change-discovery coverage and validation, but should not introduce synthesis, recommendations, rankings, or new architecture.

## Sufficiency for intended library role

Current state is sufficient for a bounded v1 library if the user asks about already indexed problems or known compact records.

Current state is not yet fully sufficient for complete library discovery across all harvested sources because retrieval and change-discovery coverage lag behind the latest harvest artifacts.

The correct next move is not new architecture. It is a narrow coverage backfill and validation task using the existing file-backed mechanisms.

## Active bottlenecks

1. Retrieval-index lag.
   - New harvested categories exist but are not yet represented as problem-first retrieval routes.

2. Change-discovery lag.
   - Recent library expansion is not visible through `list_changes.py`.

3. Coverage validation gap.
   - Tests validate doctrine and selected retrieval behavior, but not analyzed-source-to-library-discoverability completeness.

4. Ambiguous status of broader uncommitted infrastructure work until committed.
   - The infrastructure is valid, but a dirty tree makes future audits and handoffs harder.

## Ranked next tasks

1. Backfill library discoverability coverage for taxonomy-diversity harvests.
   - Update retrieval index entries and change-discovery records for n8n, Apache Airflow, and OpenMetadata.
   - Add bounded tests proving descriptive retrieval and change listing see these artifacts.
   - Do not add synthesis, recommendations, rankings, target-project relevance, or new architecture.

2. Add a narrow analyzed-source coverage check.
   - Validate that analyzed sources have required library artifacts and, where applicable, retrieval/change-discovery visibility.
   - Keep it as a deterministic test or script; no new storage system.

3. Review `recommendation_rules.yaml` naming in the provider interface.
   - Determine whether the filename remains appropriate for a library mode that forbids project-specific recommendation output.
   - If retained, document that it is historical/explainability support, not an active recommendation emitter.

4. Keep summaries synchronized after infrastructure commits.
   - Refresh only affected folder summaries when bounded infrastructure changes land.

## Single recommended next task

Backfill library discoverability coverage for the taxonomy-diversity harvest.

Reason:
- It fixes the only material library-readiness bottleneck found in this bounded audit.
- It uses existing infrastructure.
- It improves MetaHarvest's role as a library without expanding scope.
- It avoids architecture, synthesis, recommendation, ranking, and governance drift.
