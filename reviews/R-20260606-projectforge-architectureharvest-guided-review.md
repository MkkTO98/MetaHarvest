# First ArchitectureHarvest-guided ProjectForge review

Created UTC: 2026-06-06T10:14:50Z

Goal: determine whether ArchitectureHarvest has identified improvements sufficiently valuable to justify its continued existence.

Boundary:
- Used only synthesized patterns, contradiction records, ProjectForge relevance maps, and adoption candidates.
- Did not inspect external repositories again.
- Did not perform new harvesting.
- Did not implement recommendations.
- Created recommendation artifacts only.

Companion machine-readable artifact:
- `ArchitectureHarvest/reviews/R-20260606-projectforge-architectureharvest-guided-review.yaml`

## Executive judgment

ArchitectureHarvest conditionally justifies its maintenance burden.

The first harvested cycle produced genuinely useful decision constraints, not just interesting notes:

1. ProjectForge should keep file-backed governance as the default and resist embedding a runtime/framework unless ordinary task/state/handoff artifacts fail.
2. A minimal lifecycle/checkpoint vocabulary may be valuable for long-running architecture/governance work.
3. Human approval can be treated as an interrupt/resume transition with durable evidence, not just an ad-hoc chat moment.
4. ArchitectureHarvest itself needs deletion/retirement discipline so source-derived candidates do not become permanent noise.

However, the evidence is still first-cycle, static, and has no ProjectForge adoption outcomes. Continued harvesting should be constrained until at least one local adoption/rejection outcome is recorded.

## Classification legend

A. Immediate candidate
B. Future candidate
C. Insufficient evidence
D. Reject

## 1. Simplification candidates

### PF-AH-REC-001 — Keep file-backed governance as default; reject runtime/framework adoption by default

Classification: A. Immediate candidate

Originating pattern(s):
- `thread_checkpoint_contract`
- `observable_task_stream`
- `typed_state_graph`
- `sandboxed_conversation_runtime`

Originating project(s):
- LangGraph
- OpenHands

Originating contradiction:
- `runtime-orchestration-vs-file-backed-governance`

Problem solved:
- Prevents ArchitectureHarvest from turning ProjectForge into a runtime orchestration framework when current task/state/handoff/decision artifacts are sufficient.

Estimates:
- Implementation effort: low
- Maintenance reduction: high
- Complexity reduction: high
- Risk: low

Would this recommendation likely have been discovered without ArchitectureHarvest?
- Partly. ProjectForge already prefers file-backed governance, but ArchitectureHarvest made the external pressure explicit by contrasting runtime-oriented evidence with ProjectForge defaults. Without ArchitectureHarvest, this likely remains a preference rather than a reusable decision constraint backed by contradiction evidence.

### PF-AH-REC-005 — Treat observable task streams as derived summaries/events, not raw logs loaded into normal context

Classification: A. Immediate candidate

Originating pattern(s):
- `observable_task_stream`
- `thread_checkpoint_contract`

Originating project(s):
- LangGraph

Originating contradiction:
- `event-log-vs-state-snapshot`

Problem solved:
- Preserves ProjectForge context discipline while allowing better audit and recovery records for long-running work.

Estimates:
- Implementation effort: low
- Maintenance reduction: medium
- Complexity reduction: medium
- Risk: low

Would this recommendation likely have been discovered without ArchitectureHarvest?
- Likely. ProjectForge already excludes raw logs and uses compact summaries. ArchitectureHarvest mostly validates this existing design rather than discovering it.

## 2. Replacement candidates

### PF-AH-REC-002 — Replace ad-hoc long-running status notes with minimal lifecycle/checkpoint vocabulary only where needed

Classification: B. Future candidate

Originating pattern(s):
- `thread_checkpoint_contract`
- `interrupt_as_approval_gate`
- `observable_task_stream`
- `typed_state_graph`

Originating project(s):
- LangGraph

Problem solved:
- Reduces ambiguity when long-running ProjectForge work is interrupted, resumed, compacted, or handed off.

Estimates:
- Implementation effort: medium
- Maintenance reduction: medium
- Complexity reduction: medium
- Risk: medium

Would this recommendation likely have been discovered without ArchitectureHarvest?
- Maybe, but less precisely. ProjectForge already has task/state/handoff artifacts, but the specific combination of stable thread identity, parent checkpoint, interrupt/resume, and observable task events is unlikely to appear as a coherent vocabulary without the LangGraph-derived patterns.

### PF-AH-REC-006 — Replace implicit runtime readiness assumptions with readiness gates only for persistent sandboxes/workers/services

Classification: B. Future candidate

Originating pattern(s):
- `sandboxed_conversation_runtime`
- `pending_input_queue`
- `observable_task_stream`

Originating project(s):
- OpenHands

Problem solved:
- Prevents agents from proceeding while an execution environment is not ready and provides a recovery path for inputs arriving during lifecycle transitions.

Estimates:
- Implementation effort: medium
- Maintenance reduction: medium
- Complexity reduction: low
- Risk: medium

Would this recommendation likely have been discovered without ArchitectureHarvest?
- Maybe. Readiness checks are common, but the combination of readiness, pending input, and conversation/runtime separation is more specific to OpenHands-derived evidence. It becomes valuable only if ProjectForge grows persistent worker/service workflows.

## 3. Deletion candidates

### PF-AH-REC-007 — Delete or retire unused ArchitectureHarvest source-derived candidates after scheduled reviews

Classification: A. Immediate candidate

Originating pattern(s):
- `typed_state_graph`
- `sandboxed_conversation_runtime`
- `pending_input_queue`
- `credential_scoped_tool_proxy`

Originating project(s):
- LangGraph
- OpenHands

Problem solved:
- Prevents ArchitectureHarvest from becoming a permanent graveyard of interesting but unused architecture notes.

Estimates:
- Implementation effort: low
- Maintenance reduction: high
- Complexity reduction: high
- Risk: low

Would this recommendation likely have been discovered without ArchitectureHarvest?
- No. This recommendation exists because ArchitectureHarvest creates a new maintenance surface. The need for retirement discipline would not exist without the subsystem.

### PF-AH-REC-008 — Reject product-level sandbox/tool-proxy adoption for current ProjectForge

Classification: D. Reject

Originating pattern(s):
- `credential_scoped_tool_proxy`
- `sandboxed_conversation_runtime`

Originating project(s):
- OpenHands

Originating contradiction:
- `sandbox-tool-proxy-vs-hermes-tool-approval`

Problem solved:
- Avoids duplicating Hermes tool approval and credential boundaries with a heavier product-runtime integration layer.

Estimates:
- Implementation effort if adopted: high
- Maintenance reduction from rejecting: high
- Complexity reduction from rejecting: high
- Risk if adopted: high

Would this recommendation likely have been discovered without ArchitectureHarvest?
- Likely. ProjectForge already has Hermes-native approval boundaries. ArchitectureHarvest adds value by distinguishing the useful extractable idea, scoped identity/metadata, from the rejected product-level tool proxy.

## 4. Missing capability candidates

### PF-AH-REC-003 — Add a file-backed approval-interrupt record for high-risk actions

Classification: B. Future candidate

Originating pattern(s):
- `interrupt_as_approval_gate`
- `credential_scoped_tool_proxy`

Originating project(s):
- LangGraph
- OpenHands

Originating contradiction:
- `sandbox-tool-proxy-vs-hermes-tool-approval`

Problem solved:
- Makes human approval workflows durable across context compaction, session interruption, and multi-step risky actions without bypassing Hermes approval boundaries.

Estimates:
- Implementation effort: medium
- Maintenance reduction: medium
- Complexity reduction: low
- Risk: medium

Would this recommendation likely have been discovered without ArchitectureHarvest?
- Maybe. ProjectForge already requires human approval for dangerous actions. ArchitectureHarvest adds value by framing approval as an interruptible lifecycle transition rather than a chat-only confirmation.

### PF-AH-REC-004 — Add an optional checkpoint pointer schema for resumable architecture/governance work

Classification: C. Insufficient evidence

Originating pattern(s):
- `thread_checkpoint_contract`
- `observable_task_stream`

Originating project(s):
- LangGraph

Originating contradiction:
- `event-log-vs-state-snapshot`

Problem solved:
- Could make long reviews and architecture audits easier to resume from a known checkpoint while preserving compact current-state startup context.

Estimates:
- Implementation effort: medium
- Maintenance reduction: unknown
- Complexity reduction: unknown
- Risk: medium

Would this recommendation likely have been discovered without ArchitectureHarvest?
- Unlikely in this shape. The checkpoint fields and event-log/current-state tradeoff came from ArchitectureHarvest. But this remains evidence-gated because there is no ProjectForge adoption outcome.

## 5. Recommendations requiring additional evidence

### PF-AH-REC-009 — Gather local outcome evidence before expanding ArchitectureHarvest

Classification: C. Insufficient evidence

Originating pattern(s):
- `thread_checkpoint_contract`
- `interrupt_as_approval_gate`
- `observable_task_stream`
- `sandboxed_conversation_runtime`

Originating project(s):
- LangGraph
- OpenHands

Problem solved:
- Prevents over-investment in a source-harvesting subsystem before it demonstrates local adoption value.

Estimates:
- Implementation effort: low
- Maintenance reduction: unknown
- Complexity reduction: unknown
- Risk: low

Would this recommendation likely have been discovered without ArchitectureHarvest?
- No. This is a meta-governance finding about ArchitectureHarvest's own burden and comes directly from evaluating harvested evidence against ProjectForge fit.

### PF-AH-REC-010 — Test lifecycle/checkpoint vocabulary in one real long-running ProjectForge task before standardizing it

Classification: C. Insufficient evidence

Originating pattern(s):
- `thread_checkpoint_contract`
- `observable_task_stream`
- `interrupt_as_approval_gate`

Originating project(s):
- LangGraph

Problem solved:
- Converts promising static evidence into local ProjectForge outcome evidence.

Estimates:
- Implementation effort: medium
- Maintenance reduction: unknown
- Complexity reduction: unknown
- Risk: low

Would this recommendation likely have been discovered without ArchitectureHarvest?
- Unlikely. The proposed experiment follows from the ArchitectureHarvest maturity gap: high generic evidence but insufficient ProjectForge outcome history.

## Would this recommendation likely have been discovered without ArchitectureHarvest?

Overall answer: mixed, and that is important.

Findings that ProjectForge probably would have discovered anyway:
- Raw logs should stay out of normal context.
- Runtime/framework adoption should be resisted unless there is a concrete need.
- Product-level tool proxies are a poor fit while Hermes remains the controlling tool boundary.

Findings that ArchitectureHarvest made substantially sharper:
- The runtime-vs-file-backed contradiction is now explicit and reusable.
- Checkpointing is no longer a vague recovery idea; it has a concrete vocabulary: stable thread identity, checkpoint identity, parent relation, step, state values/versions, and pending writes.
- Approval can be modeled as an interrupt/resume state transition with durable evidence.
- Runtime readiness and pending input are only useful under a specific future condition: persistent workers/services, not ordinary ProjectForge tasks.

Findings that likely would not exist without ArchitectureHarvest:
- Retirement discipline for source-derived candidates.
- The meta-recommendation to require local adoption outcomes before expanding future harvesting.

So ArchitectureHarvest did not merely invent generic architecture advice. It created a structured way to separate:
- external evidence worth extracting,
- external mechanisms worth rejecting,
- contradictions that should remain visible,
- and evidence gaps that must be closed before implementation.

## Direct answers

### 1. Which findings appear genuinely valuable?

Genuinely valuable:
- Keep file-backed governance as the default despite runtime-oriented source evidence.
- Consider minimal lifecycle/checkpoint vocabulary for long-running governance work.
- Consider durable approval-interrupt records for high-risk actions.
- Add retirement/deletion pressure for stale ArchitectureHarvest records.

### 2. Which findings are merely interesting?

Merely interesting for ProjectForge now:
- Full typed state graph orchestration.
- Pending input queues.
- Product sandbox lifecycle separation.
- Observable live streaming as a runtime feature rather than file-backed summaries/events.

These may matter later if ProjectForge grows persistent services or workers, but they are not immediate implementation drivers.

### 3. Which findings are likely noise?

Likely noise for current ProjectForge:
- Any implication that ProjectForge should embed LangGraph or OpenHands as a runtime dependency.
- Product-level tool proxy adoption.
- Broad source-harvesting expansion before local outcomes exist.
- Lifecycle machinery for ordinary one-shot implementation tasks.

### 4. Did ArchitectureHarvest justify its maintenance burden?

Conditionally yes.

It justified a small, file-backed, compact-first ArchitectureHarvest because it produced practical constraints and evidence-gated candidates from only two sources. It did not justify a larger subsystem, continuous harvesting, additional infrastructure, embeddings, dashboards, or mandatory consultation for ordinary work.

The maintenance burden remains justified only if future reviews:
- record adoption/rejection outcomes,
- retire stale or unused candidates,
- keep recommendations compact and problem-first,
- and avoid deep reports unless compact evidence is insufficient.

### 5. Should future harvesting continue?

Yes, but constrained.

Continue future harvesting only when one of these is true:
- scheduled architecture review,
- new subsystem design,
- orchestration/context/permission/workflow redesign,
- repeated implementation failure,
- explicit user-requested improvement scan.

Do not harvest more sources merely because they are interesting. Before expanding to more sources, ProjectForge should record at least one local adoption or rejection outcome from this first cycle.

## Validation plan

Required checks after creating this recommendation artifact:
- Validate dry-run report.
- Parse the review YAML.
- Run ProjectForge tests.
- Run context health.
- Run ProjectForge coherence.
- Run Architecture-to-Reality audit.
