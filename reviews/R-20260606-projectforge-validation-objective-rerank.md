# ArchitectureHarvest validation-objective re-rank

Created UTC: 2026-06-06T10:32:08Z

Status: recommendation artifact only. No implementation was performed.

Source review:
- `ArchitectureHarvest/reviews/R-20260606-projectforge-architectureharvest-guided-review.yaml`

Companion machine-readable artifact:
- `ArchitectureHarvest/reviews/R-20260606-projectforge-validation-objective-rerank.yaml`

## Objective

Re-evaluate the first ArchitectureHarvest review using a different objective.

Do not optimize for highest benefit-to-effort ratio.

Optimize for:

> Strongest validation of ArchitectureHarvest's ability to improve ProjectForge.

Ranking criteria, in order:

1. Ability to generate measurable local evidence.
2. Ability to validate ArchitectureHarvest recommendations.
3. Reversibility.
4. Risk.
5. Implementation effort.

## Result

Selected recommendation: PF-AH-REC-010

Title: Test whether the lifecycle/checkpoint vocabulary actually reduces handoff ambiguity in one real long-running ProjectForge task before standardizing it.

This recommendation is the best validation candidate because it directly tests whether harvested architectural knowledge can improve ProjectForge's own operating model.

PF-AH-REC-007 remains the best benefit-to-effort candidate, but it mostly validates ArchitectureHarvest self-governance. PF-AH-REC-010 validates whether source-derived architecture patterns can improve ProjectForge task lifecycle, context recovery, and handoff clarity.

## Ranked recommendations

### 1. PF-AH-REC-010 — Test lifecycle/checkpoint vocabulary in one real long-running ProjectForge task

Selected: yes

Originating pattern(s):
- `thread_checkpoint_contract`
- `observable_task_stream`
- `interrupt_as_approval_gate`

Originating project(s):
- LangGraph

Scores:
- Measurable local evidence: 5/5
- Validates ArchitectureHarvest recommendations: 5/5
- Reversibility: 5/5
- Low risk: 4/5
- Low effort: 3/5

Rationale:
- This is explicitly an evidence-generating experiment.
- It tests a harvested LangGraph-derived idea against a real ProjectForge weakness: ambiguity after interruption, compaction, or handoff.
- It can be isolated to one task before any durable standardization.
- It can produce measurable before/after evidence.

### 2. PF-AH-REC-002 — Replace ad-hoc long-running status notes with minimal lifecycle/checkpoint vocabulary only where needed

Scores:
- Measurable local evidence: 4/5
- Validates ArchitectureHarvest recommendations: 5/5
- Reversibility: 4/5
- Low risk: 3/5
- Low effort: 3/5

Rationale:
- This is the underlying improvement likely to help ProjectForge.
- It ranks below PF-AH-REC-010 only because PF-AH-REC-010 tests it before standardizing it.

### 3. PF-AH-REC-003 — Add a file-backed approval-interrupt record for high-risk actions

Scores:
- Measurable local evidence: 4/5
- Validates ArchitectureHarvest recommendations: 4/5
- Reversibility: 4/5
- Low risk: 3/5
- Low effort: 3/5

Rationale:
- Strong evidence potential around approval durability.
- Should follow lifecycle/checkpoint experimentation because it touches human approval semantics and high-risk workflows.

### 4. PF-AH-REC-004 — Add optional checkpoint pointer schema for resumable architecture/governance work

Scores:
- Measurable local evidence: 4/5
- Validates ArchitectureHarvest recommendations: 4/5
- Reversibility: 4/5
- Low risk: 3/5
- Low effort: 3/5

Rationale:
- Closely related to the selected recommendation.
- More schema-specific and therefore less useful as a first proof that harvested lifecycle vocabulary improves real work.

### 5. PF-AH-REC-007 — Retire unused ArchitectureHarvest source-derived candidates

Scores:
- Measurable local evidence: 3/5
- Validates ArchitectureHarvest recommendations: 3/5
- Reversibility: 5/5
- Low risk: 5/5
- Low effort: 5/5

Rationale:
- Excellent maintenance hygiene.
- Best benefit-to-effort ratio.
- But it validates ArchitectureHarvest self-governance more than ProjectForge operational improvement.

### 6. PF-AH-REC-001 — Keep file-backed governance as default; reject runtime/framework adoption by default

Scores:
- Measurable local evidence: 2/5
- Validates ArchitectureHarvest recommendations: 3/5
- Reversibility: 5/5
- Low risk: 5/5
- Low effort: 5/5

Rationale:
- Important, but largely confirms an existing ProjectForge design principle.
- Hard to separate ArchitectureHarvest-caused improvement from ProjectForge already working as intended.

### 7. PF-AH-REC-005 — Treat observable task streams as derived summaries/events, not raw logs loaded into normal context

Scores:
- Measurable local evidence: 2/5
- Validates ArchitectureHarvest recommendations: 3/5
- Reversibility: 5/5
- Low risk: 5/5
- Low effort: 5/5

Rationale:
- Also confirms an existing ProjectForge principle: raw logs are audit/debug artifacts only.
- Useful validation, but weak as proof that harvested knowledge caused improvement.

### 8. PF-AH-REC-009 — Gather local outcome evidence before expanding ArchitectureHarvest

Scores:
- Measurable local evidence: 3/5
- Validates ArchitectureHarvest recommendations: 2/5
- Reversibility: 5/5
- Low risk: 5/5
- Low effort: 5/5

Rationale:
- Good meta-governance constraint.
- It limits premature harvesting but does not itself test a harvested pattern against ProjectForge work.

### 9. PF-AH-REC-006 — Add readiness gates only for future persistent workers/services

Scores:
- Measurable local evidence: 2/5
- Validates ArchitectureHarvest recommendations: 3/5
- Reversibility: 3/5
- Low risk: 3/5
- Low effort: 3/5

Rationale:
- Could validate OpenHands-derived knowledge if ProjectForge grows persistent services.
- Current ProjectForge does not appear to have enough runtime pressure for a near-term validation experiment.

### 10. PF-AH-REC-008 — Reject product-level sandbox/tool-proxy adoption for current ProjectForge

Scores:
- Measurable local evidence: 1/5
- Validates ArchitectureHarvest recommendations: 2/5
- Reversibility: 4/5
- Low risk: 2/5
- Low effort: 1/5

Rationale:
- The rejection is likely correct.
- It does not produce much positive evidence that harvested knowledge improves ProjectForge.
- Implementing the rejected machinery would be high effort and high risk.

## Why PF-AH-REC-010 is stronger than PF-AH-REC-007

PF-AH-REC-007 validates that ArchitectureHarvest can manage its own maintenance burden. That is useful, but it is meta-evidence.

PF-AH-REC-010 validates the harder claim:

> Harvested architectural knowledge can improve ProjectForge itself.

If PF-AH-REC-010 succeeds, the evidence would show that a LangGraph-derived pattern family can improve ProjectForge's real operating model without importing LangGraph as a dependency.

Specifically, it would test whether the ideas behind thread checkpoints, interrupt/resume transitions, and observable task progress can reduce ambiguity in:

- long-running ProjectForge task lifecycle management
- compact handoff creation
- post-compaction resume quality
- failure recovery
- context selection
- approval/interrupt boundaries, if present in the selected task

PF-AH-REC-007 cannot show that. It can only show that ArchitectureHarvest can avoid becoming noisy.

## Success criteria for PF-AH-REC-010

A future implementation experiment succeeds if:

1. A real long-running ProjectForge task can be resumed from a compact checkpoint without broad unrelated context reads.
2. The checkpoint/lifecycle vocabulary reduces ambiguity in handoff, active-goal, and task-status records compared with prior ad-hoc notes.
3. The vocabulary remains minimal and optional.
4. No runtime dependency, graph framework, database, dashboard, scheduler, or autonomous cleanup loop is introduced.
5. Tests, context health, coherence, and architecture audit pass after the experiment.
6. A reviewer can decide whether to adopt, modify, or reject the vocabulary using local evidence rather than generic source evidence.

## Failure criteria for PF-AH-REC-010

The experiment fails if:

1. The vocabulary adds ceremony without reducing resume or handoff ambiguity.
2. Agents still need broad manual reconstruction or session search to resume the task.
3. The experiment expands into a runtime framework, graph engine, or persistent service.
4. The vocabulary duplicates existing task/state/handoff artifacts without a clear improvement.
5. Context-health, coherence, tests, or architecture audit produce new blocks or warnings caused by the experiment.
6. The evidence cannot support a clear adopt, modify, reject, or retire outcome.

## Measurable outcomes

A future experiment should measure:

1. Number of resume decisions answered from checkpoint/handoff without broader context.
2. Number of files needed to resume before and after the experiment.
3. Time or step count needed to identify current task phase after interruption.
4. Count of ambiguous or conflicting status fields before and after the experiment.
5. Context-health handoff size before and after the experiment.
6. Reviewer rating of handoff clarity before and after the experiment.
7. Whether the final adoption outcome is adopt, modify, reject, or retire.

## Estimated evidence generated for the ecosystem-weighted recommendation model

Estimated evidence amount: high.

Why:

PF-AH-REC-010 would generate direct ProjectForge outcome evidence for a harvested pattern family. It would measure fit, maintenance cost, operational impact, and boundaries.

That evidence could update future recommendation strength for:

- `thread_checkpoint_contract`
- `observable_task_stream`
- `interrupt_as_approval_gate`
- minimal lifecycle/checkpoint vocabulary in ProjectForge and generated projects

It would also help distinguish:

- useful minimal extraction
- premature lifecycle ceremony
- runtime/framework machinery that should remain rejected

## Explicit answer

If this recommendation succeeds, what new confidence would we gain that we do not gain from implementing PF-AH-REC-007?

We would gain confidence that harvested external architecture patterns can improve ProjectForge's core operating model.

Specifically, we would learn whether source-derived lifecycle/checkpoint ideas improve real ProjectForge work by reducing handoff ambiguity, improving recovery after interruption, and making context selection more reliable.

Implementing PF-AH-REC-007 would not give us that confidence. It would show that ArchitectureHarvest can prune or retire its own stale recommendations, which is useful maintenance evidence. But it would not show that ArchitectureHarvest-derived patterns make ProjectForge tasks, governance, or recovery better.

PF-AH-REC-010 is therefore the stronger validation candidate, even though PF-AH-REC-007 remains the stronger benefit-to-effort candidate.

## Future experiment boundary

Do not implement now.

If approved later, the smallest experiment should:

- apply a tiny optional lifecycle/checkpoint vocabulary to one real long-running ProjectForge architecture/governance task;
- record before/after resume evidence;
- avoid any graph runtime or external dependency;
- create an adoption outcome deciding whether to adopt, modify, reject, or retire the vocabulary.

Non-scope:

- No LangGraph dependency.
- No OpenHands dependency.
- No graph runtime.
- No scheduler.
- No database.
- No broad template rollout before local evidence.

## Validation for this artifact

Dry-run report:
- `simulation/dry_runs/20260606_123202-dry-run.md`

Required checks:
- validate dry-run
- parse YAML artifact
- run full ProjectForge tests
- run context health
- run coherence
- run architecture audit JSON mode
