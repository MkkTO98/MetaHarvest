# First ArchitectureHarvest confidence consolidation review

Created UTC: 2026-06-08T15:30:53Z

Boundary: recommendation artifacts only. No ProjectForge doctrine, runtime code, templates, governance files, or operating procedures were changed.

## Executive conclusion

Seven patterns have enough accumulated evidence to become explicit ProjectForge doctrine if the user later approves a doctrine update. The rest should remain recommendations, emerging patterns, or insufficient-evidence references. This review does not implement those doctrine changes.

## Patterns recommended for explicit doctrine

- `bounded_context_selection` — Bounded context selection / evidence split: Add to doctrine as an explicit principle: active context is bounded, while durable evidence remains file-backed and available by pointer.
- `git_anchored_coding_workflow` — Git/diff anchored coding workflow: Add to doctrine for repository-changing work: final claims require inspectable diff/patch/commit evidence plus validation; publication remains separate.
- `patch_submission_boundary` — Patch/submission boundary before publication: Add doctrine that publication/push/PR is separate from generation and must pass approval/validation; do not require heavyweight patch workflow for every small edit yet.
- `thread_checkpoint_contract` — Minimal file-backed checkpoint/current-state contract: Add to doctrine narrowly: long-running or interruption-prone governance/architecture work should use compact file-backed checkpoints/current-state pointers; ordinary tasks are exempt.
- `trajectory_artifact_recovery` — Trajectory/evidence artifact for recovery: Add doctrine: recovery evidence may be stored, but normal context loads compact state and pointers, not raw trajectories.
- `plan_execute_split` — Planning/recommendation vs execution split: Add to doctrine: ArchitectureHarvest outputs are decision inputs; implementation requires a separate approval/dry-run/test cycle.
- `problem_first_decision_support` — Problem-first ArchitectureHarvest retrieval: Keep/add as doctrine: ArchitectureHarvest consultation starts problem-first and compact-first, then expands only when needed.

## Patterns that should remain recommendations

- `observable_task_stream` — Strong Recommendation: Remain a strong recommendation: use derived task/lifecycle event summaries where needed, not a core doctrine requiring streams everywhere.
- `environment_reset_boundary` — Strong Recommendation: Remain a strong recommendation for future sandboxed workers/services, not ProjectForge doctrine today.
- `interrupt_as_approval_gate` — Strong Recommendation: Remain a strong recommendation until a concrete high-risk approval workflow is tested.
- `typed_state_graph` — Emerging Pattern: Keep as emerging; do not add to doctrine except as a negative/default rule: prefer file-backed extraction before graph runtime adoption.
- `reviewer_retry_loop` — Emerging Pattern: Keep emerging; only test under explicit human-approved high-value workflow.
- `sandboxed_conversation_runtime` — Emerging Pattern: Keep emerging/optional for future generated projects or workers; do not add to ProjectForge doctrine now.
- `pending_input_queue` — Emerging Pattern: Keep emerging for future async workers/gateways only.
- `credential_scoped_tool_proxy` — Insufficient Evidence: Do not add to doctrine now; retain as cautionary reference for future permission-system design.
- `checkpointing` — Insufficient Evidence: Do not promote; prefer specific checkpoint/trajectory/current-state patterns.

## Full classification table

### Architectural Principle

#### bounded_context_selection: Bounded context selection / evidence split

Confidence: high

Supporting evidence:
- Aider editable/read-only file sets, repo map, chat summarization
- SWE-agent history processors plus persisted trajectories
- LangGraph checkpoints and OpenHands event/lifecycle records reinforce active-context vs evidence split
- Matches ProjectForge raw-log exclusion and summary-first context policy

Contradictory evidence:
- Aider dynamic repo map is less explicit than ProjectForge context manifests
- Full trajectory/event replay can tempt agents to load too much context

Local outcome evidence: Indirectly supported by ProjectForge context policy and coherence behavior; no single local A/B experiment for repo-map-like context yet.

Maintenance implications: Low-to-medium if framed as doctrine; medium if it creates new generated repo-map artifacts. Prefer existing context bundles/summaries before new machinery.

Doctrine guidance: Add to doctrine as an explicit principle: active context is bounded, while durable evidence remains file-backed and available by pointer.

#### git_anchored_coding_workflow: Git/diff anchored coding workflow

Confidence: high

Supporting evidence:
- Aider GitRepo centralizes dirty-file detection, tracked files, diffs, commits, attribution, and undo handles
- SWE-agent finalizes changes as model.patch and patch/apply/PR hook artifacts
- OpenHands source-control tooling reinforces explicit side-effect records

Contradictory evidence:
- Aider autocommit ergonomics conflict with ProjectForge dry-run and approval discipline
- Git is not sufficient for non-code architecture recommendations or generated evidence

Local outcome evidence: ProjectForge already requires tests before code-change summary and human approval before pushes; no local patch-as-submission experiment yet.

Maintenance implications: Low if expressed as doctrine around diff/patch evidence; medium if every small edit requires extra patch artifacts. Keep proportional to risk.

Doctrine guidance: Add to doctrine for repository-changing work: final claims require inspectable diff/patch/commit evidence plus validation; publication remains separate.

#### patch_submission_boundary: Patch/submission boundary before publication

Confidence: high

Supporting evidence:
- SWE-agent submit tool stores git diff as /root/model.patch
- SWE-agent apply_patch/open_pr hooks separate patch capture from local apply and draft PR publication
- Aider diffs/commits and OpenHands source-control tool boundary reinforce inspect-before-publish

Contradictory evidence:
- Automatic apply/open-PR is useful externally but would bypass ProjectForge governance if made default
- For tiny docs edits, mandatory patch artifacts can be ceremony

Local outcome evidence: ProjectForge constitution already separates local validation and human-approved push; no local universal patch requirement exists.

Maintenance implications: Low if principle remains publication-boundary doctrine; medium/high if required for every file change.

Doctrine guidance: Add doctrine that publication/push/PR is separate from generation and must pass approval/validation; do not require heavyweight patch workflow for every small edit yet.

#### thread_checkpoint_contract: Minimal file-backed checkpoint/current-state contract

Confidence: high

Supporting evidence:
- LangGraph checkpoint contract provides stable thread/checkpoint/parent/step semantics
- SWE-agent trajectories and OpenHands event streams reinforce reconstructable state
- PF-AH-REC-010 showed a minimal sidecar improved resume coverage from 62.5% to 87.5% and ambiguity from 3 to 1

Contradictory evidence:
- Full graph/checkpointer dependency is not justified
- Checkpoint sidecars can duplicate state and add overhead
- PF-AH-REC-010 found file-scope ambiguity remained partly unresolved

Local outcome evidence: Strongest local evidence: PF-AH-REC-010 met Adopt threshold narrowly with 8 minute overhead and no contradictions.

Maintenance implications: Low-to-medium if limited to long-running architecture/governance tasks; high if required for ordinary tasks.

Doctrine guidance: Add to doctrine narrowly: long-running or interruption-prone governance/architecture work should use compact file-backed checkpoints/current-state pointers; ordinary tasks are exempt.

#### trajectory_artifact_recovery: Trajectory/evidence artifact for recovery

Confidence: high

Supporting evidence:
- SWE-agent repeatedly persists .traj/history/info/replay_config
- Aider persists practical recovery through git commits/diffs and summarized history
- OpenHands event stream and LangGraph checkpoint stream reinforce durable evidence

Contradictory evidence:
- Normal ProjectForge startup must not load raw trajectories/logs
- Trajectory capture can become storage/context bloat

Local outcome evidence: PF-AH-REC-010 supports pointer-style recovery, not full trajectory replay. ProjectForge raw-log policy already aligns.

Maintenance implications: Low if implemented as pointers to evidence; high if agents maintain verbose replay records for ordinary work.

Doctrine guidance: Add doctrine: recovery evidence may be stored, but normal context loads compact state and pointers, not raw trajectories.

#### plan_execute_split: Planning/recommendation vs execution split

Confidence: high_for_doctrine_medium_in_synthesis

Supporting evidence:
- Aider ask/code/architect/context modes separate discussion/planning from editing
- SWE-agent separates problem statement/templates from action loop
- LangGraph graph/state and OpenHands runtime lifecycle reinforce explicit phase boundaries
- Current user task explicitly forbids implementation while requesting recommendations

Contradictory evidence:
- Aider mode switching is product-specific
- Over-formal phase boundaries can slow tiny tasks

Local outcome evidence: ProjectForge already requires ArchitectureHarvest recommendations not force implementation; this task itself validates recommendation-only workflow.

Maintenance implications: Low as doctrine; medium if every task must create separate planning artifacts.

Doctrine guidance: Add to doctrine: ArchitectureHarvest outputs are decision inputs; implementation requires a separate approval/dry-run/test cycle.

#### problem_first_decision_support: Problem-first ArchitectureHarvest retrieval

Confidence: medium_high_local

Supporting evidence:
- ProjectForge ArchitectureHarvest integration already starts from problem catalog and retrieval index
- OpenHands/LangGraph/Aider/SWE-agent artifacts became useful through compact synthesis/relevance/contradiction records rather than raw reports first

Contradictory evidence:
- Can hide useful source nuance if compact records are stale
- Not directly proven by external projects

Local outcome evidence: Direct ProjectForge usage in this and prior ArchitectureHarvest cycles; no quantitative retrieval experiment yet.

Maintenance implications: Low if compact indexes stay current; medium if every source cycle requires broad index churn.

Doctrine guidance: Keep/add as doctrine: ArchitectureHarvest consultation starts problem-first and compact-first, then expands only when needed.

### Strong Recommendation

#### observable_task_stream: Observable task/checkpoint stream

Confidence: high

Supporting evidence:
- LangGraph exposes task/checkpoint start/result/error/interrupt stream modes
- OpenHands event service reinforces observable lifecycle evidence
- PF-AH-REC-010 supports compact lifecycle state

Contradictory evidence:
- Event streams are too verbose for normal ProjectForge context
- ProjectForge already has logs and summaries; duplicative event streams risk bloat

Local outcome evidence: PF-AH-REC-010 validates compact checkpoint/lifecycle fields, not full task streams.

Maintenance implications: Low if derived summaries; medium/high if full event stream schema becomes mandatory.

Doctrine guidance: Remain a strong recommendation: use derived task/lifecycle event summaries where needed, not a core doctrine requiring streams everywhere.

#### environment_reset_boundary: Environment reset boundary

Confidence: high

Supporting evidence:
- SWE-agent environment starts deployment/session, copies repo, resets to base commit, interrupts timeouts, closes deployment
- OpenHands sandbox lifecycle and readiness states reinforce resettable execution boundaries

Contradictory evidence:
- ProjectForge is mostly file-first/Hermes-native, not a persistent sandbox product
- Heavy sandbox/reset machinery is unnecessary for ordinary docs/code tasks

Local outcome evidence: No direct ProjectForge sandbox/reset adoption outcome yet.

Maintenance implications: Medium/high; requires lifecycle hooks, cleanup, timeout states, tests, and safety policy.

Doctrine guidance: Remain a strong recommendation for future sandboxed workers/services, not ProjectForge doctrine today.

#### interrupt_as_approval_gate: Interrupt/resume as approval gate

Confidence: high_source_medium_local

Supporting evidence:
- LangGraph interrupt/resume shows approval as durable interrupted state
- Aider confirmations and SWE-agent patch-before-publication reinforce explicit human gates
- ProjectForge constitution already requires human approval for high-risk actions

Contradictory evidence:
- SWE-agent autosubmission and Aider autocommit show external tools can bypass approvals when configured
- ProjectForge already has Hermes approval semantics; adding interrupt records may duplicate them

Local outcome evidence: PF-AH-REC-010 supports checkpoint vocabulary but did not test high-risk approval interruption.

Maintenance implications: Medium; needs clear schema and refusal/resume semantics to avoid confusing approvals.

Doctrine guidance: Remain a strong recommendation until a concrete high-risk approval workflow is tested.

### Emerging Pattern

#### typed_state_graph: Typed state graph orchestration

Confidence: high_source_low_local

Supporting evidence:
- LangGraph StateGraph provides mature typed state-machine orchestration
- Planning/execution and checkpoint patterns can be expressed cleanly with graph semantics

Contradictory evidence:
- Aider/SWE-agent show many benefits can be captured with git/patch/files without graph dependency
- ProjectForge architecture is explicitly file-first and local-execution/cloud-governance

Local outcome evidence: No ProjectForge adoption outcome for graph runtime; PF-AH-REC-010 intentionally avoided graph/runtime vocabulary.

Maintenance implications: Medium/high if adopted; adds dependency, schema, runtime concepts, and debugging burden.

Doctrine guidance: Keep as emerging; do not add to doctrine except as a negative/default rule: prefer file-backed extraction before graph runtime adoption.

#### reviewer_retry_loop: Reviewer/retry loop for high-value attempts

Confidence: medium

Supporting evidence:
- SWE-agent RetryAgent/reviewer/chooser preserves multiple attempts and best submission
- Potentially useful for high-value architecture/coding tasks with explicit budgets

Contradictory evidence:
- Benchmark autonomy conflicts with ProjectForge human-governed lifecycle if generalized
- Can create autonomous refactoring campaigns or token/tool waste

Local outcome evidence: No local reviewer/retry experiment. User constraints repeatedly emphasize not implementing recommendations automatically.

Maintenance implications: Medium/high; requires budget, stop conditions, reviewer criteria, and audit records.

Doctrine guidance: Keep emerging; only test under explicit human-approved high-value workflow.

#### sandboxed_conversation_runtime: Sandboxed conversation runtime

Confidence: medium

Supporting evidence:
- OpenHands provides concrete conversation/sandbox lifecycle, readiness, timeout, and exportable trajectory patterns
- SWE-agent environment reset partially reinforces sandbox isolation

Contradictory evidence:
- Product-level runtime is heavier than ProjectForge needs
- Hermes-native tools already provide controlled local execution

Local outcome evidence: No local sandbox runtime outcome.

Maintenance implications: High if adopted; requires lifecycle management, cleanup, permissions, and observability.

Doctrine guidance: Keep emerging/optional for future generated projects or workers; do not add to ProjectForge doctrine now.

#### pending_input_queue: Pending input queue during lifecycle transitions

Confidence: medium

Supporting evidence:
- OpenHands pending message queue preserves ordered input during readiness/identity transitions

Contradictory evidence:
- No current ProjectForge async/gateway worker pressure requiring this
- Could add queue semantics before needed

Local outcome evidence: No local outcome.

Maintenance implications: Medium; needs ordering, dedupe, identity, retry, and stale-message rules.

Doctrine guidance: Keep emerging for future async workers/gateways only.

### Insufficient Evidence

#### credential_scoped_tool_proxy: Credential-scoped tool proxy

Confidence: medium_source_low_fit

Supporting evidence:
- OpenHands demonstrates provider/user-aware tool proxy boundaries

Contradictory evidence:
- ProjectForge must not bypass Hermes approval or dry-run gates
- Credential handling is high-risk and not needed for current ArchitectureHarvest use

Local outcome evidence: No local outcome; ProjectForge already has permissions/approval policies.

Maintenance implications: High security and policy burden.

Doctrine guidance: Do not add to doctrine now; retain as cautionary reference for future permission-system design.

#### checkpointing: Generic checkpointing example

Confidence: low

Supporting evidence:
- Conceptually related to LangGraph/PF-AH-REC-010

Contradictory evidence:
- Example record had no analyzed projects and has been superseded by thread_checkpoint_contract and trajectory_artifact_recovery

Local outcome evidence: PF-AH-REC-010 supports a specific minimal checkpoint vocabulary, not this generic example.

Maintenance implications: Low but noisy if retained as decision input.

Doctrine guidance: Do not promote; prefer specific checkpoint/trajectory/current-state patterns.

## Consolidated doctrine guidance

Should be explicitly added to ProjectForge doctrine after a separate approved doctrine-change task:

- Bounded active context with durable file-backed evidence pointers.
- Git/diff/patch evidence for repository-changing work.
- Publication/push/PR as a separate approval-gated boundary.
- Narrow checkpoint/current-state pointers for long-running or interruption-prone governance/architecture tasks.
- Store recovery evidence, but load compact summaries/pointers by default.
- Separate ArchitectureHarvest recommendations from implementation.
- Problem-first, compact-first ArchitectureHarvest consultation.

Should remain recommendations rather than doctrine:

- Observable task streams as derived summaries/events.
- Environment reset boundaries for future sandboxed services/workers.
- Interrupt-as-approval records until a concrete high-risk workflow is tested.
- Typed state graph orchestration and graph runtime adoption.
- Reviewer/retry loops for high-value attempts.
- Sandboxed conversation runtime and pending input queues.
- Credential-scoped tool proxy patterns.

## Recommendations requiring further evidence

- Run one more long-running ProjectForge governance task with checkpoint/current-state pointers before broadening checkpoint doctrine beyond narrow architecture/governance work.
- Test explicit editable/read-only/in-scope file fields on a real complex code task before making them mandatory.
- Test approval-interrupt records on a concrete high-risk action before adding new approval schema.
- Validate environment reset boundaries only when ProjectForge or a generated project has a real persistent worker/sandbox need.
- Keep external runtime/framework adoption behind a separate spike comparing file-backed extraction vs dependency adoption.
