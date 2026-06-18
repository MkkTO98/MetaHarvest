# ArchitectureHarvest First Analysis Cycle: OpenHands + LangGraph

Date: 2026-06-06
Approved sources: OpenHands, LangGraph
External clone locations:
- /home/mkkto/srv/projectforge/external_sources/openhands @ 03aab93625079c24d6f43655c9506931cf43bc17
- /home/mkkto/srv/projectforge/external_sources/langgraph @ 2b1abc807b282245211f5ba8f292aaf3e24f1e07

Boundary: ArchitectureHarvest analysis only. No recommendations were implemented. No external repository code was installed, imported, built, tested, or executed.

## Highest-confidence patterns

1. Thread-scoped checkpoint contract (LangGraph): stable thread id + checkpoint id + parent + step + channel values/versions + pending writes gives real resume/time-travel semantics. Highest confidence for checkpointing/failure recovery vocabulary.
2. Observable task/checkpoint stream (LangGraph): task start/result/error/interrupt/checkpoint events are first-class stream modes. Strong fit for ProjectForge audit and long-running task lifecycle records.
3. Interrupt/resume as approval gate (LangGraph): approval can be represented as a durable interrupted state rather than hidden chat state. Must remain subordinate to Hermes/user approval policy.
4. Sandboxed conversation runtime boundary (OpenHands): conversation lifecycle, sandbox lifecycle, readiness polling, timeout/error states, and exportable trajectory provide concrete evidence for risky runtime/tool work.
5. Pending input queue during lifecycle transitions (OpenHands): ordered pending messages survive readiness and identity transitions; useful for future async worker/gateway designs.

## Strongest simplification opportunities

1. Prefer file-backed checkpoint records before adopting a graph/runtime dependency. LangGraph validates the concept; ProjectForge can often implement the minimum as YAML/JSON state plus task artifacts.
2. Keep OpenHands sandbox/runtime patterns as optional high-risk workflow patterns, not default task machinery.
3. Use compact lifecycle fields instead of full event replay for normal context loading; reserve raw event/checkpoint logs for audit/debug.
4. Treat source-specific tool proxies as evidence for scoped metadata and explicit side-effect records, not as a reason to build a product integration layer.

## Strongest replacement opportunities

1. Replace ad-hoc long-running status notes with explicit task lifecycle fields only when workflows need pause/resume/recovery.
2. Replace out-of-band approval notes with interrupt/resume-style approval records for future high-risk agent actions, while preserving existing Hermes approval controls.
3. Replace raw-log-driven recovery with checkpoint/current-state plus optional replay log references.
4. Replace implicit runtime readiness assumptions with readiness gates and timeout/error states for any future sandboxed worker.

## Strongest contradictions

1. Runtime orchestration vs file-backed governance: LangGraph/OpenHands show rich runtimes; ProjectForge's accepted architecture is file-first. Guidance: adapt patterns first; do not embed a runtime without a separate approved design.
2. Event log vs compact current-state snapshot: OpenHands event service and LangGraph checkpoints both value replayability, but ProjectForge startup context must remain compact. Guidance: current-state pointers for normal work, append-only evidence for audit/debug.
3. Product sandbox/tool proxy vs Hermes native approval: OpenHands integrates tool proxies with provider tokens and product user identity; ProjectForge should not let such proxies bypass Hermes approval or ProjectForge dry-run gates.
4. Framework dependency vs vocabulary extraction: LangGraph offers mature mechanics, but adopting it as a dependency is not currently justified by ProjectForge outcomes.

## Recommendations requiring further evidence

1. Whether ProjectForge needs a tiny formal checkpoint schema beyond existing state/task/handoff artifacts requires evidence from a future long-running workflow failure or scheduled-worker use case.
2. Whether interrupt/resume approval records should be standardized requires a concrete high-risk approval workflow and tests around refusal/resume behavior.
3. Whether sandbox readiness gates belong in ProjectForge core or generated-project templates requires a future project with actual sandboxed execution.
4. Whether LangGraph should be used as a dependency requires a separate spike comparing file-backed orchestration vs LangGraph for a real ProjectForge/MacroForge workflow.
5. Whether OpenHands patterns should be augmented from the separate Software Agent SDK repository requires explicit approval to clone/analyze that additional repository.

## Artifact index

- Project cards: ArchitectureHarvest/project_cards/openhands.yaml, ArchitectureHarvest/project_cards/langgraph.yaml
- Component cards: ArchitectureHarvest/component_cards/*openhands*.yaml and *langgraph*.yaml
- Deep reports: ArchitectureHarvest/reports/R-20260606-openhands-deep-analysis.md, ArchitectureHarvest/reports/R-20260606-langgraph-deep-analysis.md
- Contradictions: ArchitectureHarvest/contradictions/runtime-orchestration-vs-file-backed-governance.yaml, event-log-vs-state-snapshot.yaml, sandbox-tool-proxy-vs-hermes-tool-approval.yaml
- Synthesis: ArchitectureHarvest/synthesis/*.yaml for typed_state_graph, thread_checkpoint_contract, interrupt_as_approval_gate, sandboxed_conversation_runtime, pending_input_queue, observable_task_stream, credential_scoped_tool_proxy
- Relevance maps: ArchitectureHarvest/relevance_maps/projectforge/openhands-relevance-map.yaml, langgraph-relevance-map.yaml
- Candidates: ArchitectureHarvest/adoption_candidates/openhands-*-candidate.yaml and langgraph-*-candidate.yaml
