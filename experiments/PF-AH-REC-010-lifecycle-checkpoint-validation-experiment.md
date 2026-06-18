# PF-AH-REC-010 lifecycle/checkpoint validation experiment design

Created UTC: 2026-06-06T11:51:40Z

Status: proposal only. No implementation was performed.

Recommendation under test:
- PF-AH-REC-010 — Test whether the lifecycle/checkpoint vocabulary actually reduces handoff ambiguity in one real long-running ProjectForge task before standardizing it.

Supported recommendation:
- PF-AH-REC-002 — Replace ad-hoc long-running status notes with minimal lifecycle/checkpoint vocabulary only where needed.

Companion machine-readable artifact:
- `ArchitectureHarvest/experiments/PF-AH-REC-010-lifecycle-checkpoint-validation-experiment.yaml`

Dry-run:
- `simulation/dry_runs/20260606_135136-dry-run.md`

## Goal

Determine whether a minimal lifecycle/checkpoint vocabulary improves ProjectForge task handoff, interruption recovery, and resume clarity.

The experiment is designed to be:

- small
- reversible
- low-risk
- measurable
- capable of failing

It is explicitly not optimized to prove the recommendation correct. It is optimized to generate trustworthy local evidence for the ArchitectureHarvest ecosystem-weighted recommendation model.

## Selected real ProjectForge task type

Selected task type:

ProjectForge architecture/governance review closeout task.

Examples:

- ArchitectureHarvest-guided ProjectForge review.
- Architecture-to-Reality Audit remediation planning.
- Architecture/governance design task that writes recommendation, decision, state, handoff, and verification artifacts.

Why this task type is suitable:

- It is long enough to be interrupted.
- It often produces several durable artifacts.
- It requires summary-first context loading.
- It commonly crosses handoff or compaction boundaries.
- It is important enough that resume ambiguity matters.
- It can be tested without production data, secrets, billing risk, or external source inspection.
- It directly exercises ProjectForge task handoff, interruption recovery, and resume clarity.

Why not an ordinary bug fix:

- Ordinary bug fixes are often too short and implementation-specific to measure lifecycle/checkpoint value.

Why not a persistent worker/service task:

- Persistent services would confound the experiment with runtime readiness and operational lifecycle concerns, increasing risk.

## 1. Exact vocabulary to test

The experiment should test only the following vocabulary.

No graph/runtime terms should be introduced.

### lifecycle_status

Allowed values:

- `not_started`
- `active`
- `interrupted`
- `awaiting_approval`
- `verifying`
- `complete`
- `failed`

Meaning:

Current phase of the experiment task. This is not a global ProjectForge task status replacement.

### checkpoint_id

Format:

- `CKPT-YYYYMMDD-short-slug-NN`

Meaning:

Stable identifier for one resumable point in the task.

### parent_checkpoint_id

Format:

- another checkpoint id, or `null`

Meaning:

Previous checkpoint this one advances from. `null` for the first checkpoint.

### resume_pointer

Meaning:

The exact smallest file/section a future agent should read first to resume.

### next_action

Meaning:

One concrete next action that can be performed without re-planning the whole task.

### completed_since_parent

Meaning:

Compact bullet list of completed work since the parent checkpoint.

### decisions_since_parent

Meaning:

Durable choices made since the parent checkpoint, with artifact links when available.

### blockers_or_interrupts

Meaning:

Active pause reason, approval need, failure, or interruption cause. Empty when none.

### verification_state

Allowed values:

- `not_started`
- `partial`
- `passed`
- `failed`

Meaning:

Whether verification has been run for the current checkpoint.

### context_budget_hint

Meaning:

Smallest intended context set for resume. Must not include raw logs or broad repository dumps.

### measurement_notes

Meaning:

Before/after observations for resume clarity, files read, ambiguity, and overhead.

### Prohibited terms

Do not introduce:

- `graph_node`
- `edge`
- `runtime_state_machine`
- `durable_executor`
- `scheduler`
- `queue`

These terms are prohibited to prevent drift into a LangGraph-like runtime abstraction.

## 2. Exact files affected

### Proposal artifacts created now

- `ArchitectureHarvest/experiments/PF-AH-REC-010-lifecycle-checkpoint-validation-experiment.md`
- `ArchitectureHarvest/experiments/PF-AH-REC-010-lifecycle-checkpoint-validation-experiment.yaml`

### Future experiment files if approved

1. `artifacts/tasks/T-YYYYMMDD-lifecycle-checkpoint-validation.md`
   - Defines the real test task, baseline assumptions, experiment rules, and final outcome.

2. `artifacts/tasks/T-YYYYMMDD-lifecycle-checkpoint-validation.checkpoints.yaml`
   - Stores checkpoint records using the exact vocabulary above for this one experiment only.

3. `context/latest_handoff.md`
   - During the experiment only, may include one compact checkpoint pointer and next action.

4. `state/active_goal.md`
   - During the experiment only, may point to the active task and current checkpoint id.

5. `ArchitectureHarvest/adoption_log/O-YYYYMMDD-lifecycle-checkpoint-vocabulary.yaml`
   - Records adopt/modify/reject/retire outcome after experiment completion.

6. `artifacts/reports/R-YYYYMMDD-lifecycle-checkpoint-validation-results.md`
   - Stores measurement results and evidence interpretation.

### Explicitly not affected

- `AGENTS.md`
- `CONSTITUTION.md`
- `context/context_policy.yaml`
- templates
- tools
- generated project scaffolds
- `external_sources/`

## 3. Before-state workflow

Existing ProjectForge task closeout workflow without lifecycle/checkpoint vocabulary:

1. Read startup context and relevant task/review files.
2. Work through the task using normal notes, state files, handoff, and summaries.
3. If interrupted, rely on `context/latest_handoff.md`, `state/active_goal.md`, task artifacts, and possibly session search to reconstruct progress.
4. Resume by manually identifying current phase, next action, verification state, and changed artifacts.

Baseline measurements to capture:

- files read to resume
- minutes or steps to identify current phase
- ambiguous status questions count
- whether session search or broad context was needed
- handoff character count
- resume confidence rating from 1 to 5

## 4. After-state workflow

Same task type with one optional sidecar checkpoint file and compact checkpoint pointer:

1. Create the task artifact as usual.
2. Capture baseline resume measurements before using the new vocabulary.
3. Add the sidecar checkpoint YAML for the experiment task only.
4. At each natural interruption boundary, add or update a checkpoint record.
5. Put only the current checkpoint id and resume pointer in `state/active_goal.md` or `context/latest_handoff.md` when needed.
6. Simulate or use a real interruption by resuming from the checkpoint sidecar plus normal Priority 1 context only.
7. Record after-state measurements.
8. Decide adopt, modify, reject, or retire using the evidence thresholds below.

## 5. Success criteria

The experiment succeeds if:

- Resume requires fewer or equal files than baseline and no broad unrelated context.
- Current phase and next action are identifiable from Priority 1 context plus checkpoint sidecar within the target threshold.
- At least 80% of predefined resume questions are answerable from checkpoint evidence.
- Handoff ambiguity decreases by at least two questions or reaches zero/one ambiguity questions.
- Added checkpoint overhead remains below 10 minutes total or below 15% of task closeout time, whichever is smaller.
- Vocabulary remains optional and isolated to the experiment task.
- Full tests, context health, coherence, and architecture audit pass after the experiment.

## 6. Failure criteria

The experiment fails if:

- Resume clarity is unchanged or worse than baseline.
- The experiment requires reading more files than baseline without a corresponding ambiguity reduction.
- Agents still need session search, raw logs, broad repository exploration, or external source reports to resume.
- Checkpoint maintenance exceeds 15% of task closeout time or feels like duplicate ceremony.
- Vocabulary expands beyond the exact approved terms.
- The sidecar creates contradictory state relative to `state/active_goal.md`, `context/latest_handoff.md`, or the task artifact.
- Verification produces new blocks or warnings attributable to the experiment.

## 7. Measurement methodology

Design:

Within-task before/after measurement.

Baseline window:

First resume attempt for the selected task using normal ProjectForge artifacts before the checkpoint sidecar is introduced.

Treatment window:

Second resume attempt, or simulated resume, using Priority 1 context plus checkpoint sidecar after checkpoint vocabulary is used.

Resume questions to score:

1. What is the current lifecycle status?
2. What work has completed since the previous checkpoint?
3. What is the exact next action?
4. What verification remains?
5. What decisions or approvals changed the plan?
6. What files are in scope?
7. What should not be touched?
8. What would make the task complete?

Metrics:

- `files_read_to_resume`: lower or same is better.
- `resume_steps_to_current_phase`: lower is better.
- `ambiguous_questions_count`: lower is better.
- `answerable_resume_questions_percent`: higher is better.
- `checkpoint_update_overhead_minutes`: lower is better.
- `handoff_chars`: lower or same is better unless clarity materially improves.
- `contradiction_count`: must be zero for adoption.
- `reviewer_confidence_rating`: higher is better.

Anti-bias rules:

- Record failure and friction explicitly.
- Do not reinterpret overhead as success.
- Do not add fields mid-experiment unless the likely outcome is Modify, not Adopt.
- Do not use external repositories or deep harvested reports to rescue the experiment.
- Treat no measurable improvement as rejection or retirement evidence, not as neutral.

## 8. Rollback procedure

If the future experiment is implemented and needs rollback:

1. Delete the experiment-only checkpoint sidecar file.
2. Remove checkpoint id/pointer lines from `state/active_goal.md` and `context/latest_handoff.md` if they were added.
3. Keep the task artifact and measurement report only if useful as historical evidence; otherwise move the final outcome into ArchitectureHarvest adoption log and remove the experiment report.
4. Do not alter tools, templates, `AGENTS.md`, `CONSTITUTION.md`, or generated projects.
5. Rerun tests, context health, coherence, and architecture audit after rollback.

## 9. Expected maintenance burden

During experiment:

- Low to medium.

Steady state if adopted:

- Low, only if optional and sidecar-only.

Expected overhead:

- 5–10 minutes per checkpointed long-running task.

Burden warning:

- If every ordinary task starts requiring checkpoints, the recommendation should be modified or rejected.

## 10. Expected benefits

Expected benefits:

- Better resume clarity after context compaction or session interruption.
- More explicit next action and verification state.
- Less reliance on hidden chat continuity or broad session search.
- Local evidence for ArchitectureHarvest lifecycle/checkpoint pattern fit.
- Clear basis for adopt/modify/reject/retire outcome.

## 11. Potential negative side effects

Potential negative side effects:

- Duplicate state across `active_goal`, `latest_handoff`, task artifact, and checkpoint sidecar.
- Added ceremony for tasks that do not need pause/resume support.
- False confidence if the checkpoint sidecar becomes stale.
- Vocabulary creep into a hidden runtime/state-machine design.
- Context bloat if checkpoints become verbose history rather than compact current-state pointers.

## 12. Conditions under which the recommendation should be rejected

Reject the recommendation if:

- There is no measurable resume clarity improvement in the selected task.
- Overhead exceeds benefit or agents resist maintaining the sidecar.
- Any contradiction is introduced between checkpoint and canonical ProjectForge state artifacts.
- The vocabulary cannot remain small and optional.
- The experiment requires broad workflow/template/tool changes to appear useful.

## Evidence thresholds

### A. Adopt

Evidence sufficient to adopt:

- At least 80% of resume questions are answerable from checkpoint evidence.
- Ambiguous questions after experiment are less than or equal to 1.
- Files read to resume after experiment are fewer than or equal to baseline.
- Checkpoint update overhead is less than or equal to 10 minutes.
- Contradiction count is zero.
- Verification passes.

Interpretation:

Minimal vocabulary clearly improves resume clarity with low overhead and no state contradiction.

### B. Modify

Evidence sufficient to modify:

Any of the following:

- 60–79% of resume questions are answerable from checkpoint evidence.
- Ambiguous questions improve but remain above 1.
- Overhead is useful but above 10 minutes and below 20 minutes.
- One or more vocabulary fields are unused or confusing while the general sidecar concept helps.

Interpretation:

The pattern family is promising, but the exact vocabulary or scope should be narrowed before adoption.

### C. Reject

Evidence sufficient to reject:

Any of the following:

- Fewer than 60% of resume questions are answerable from checkpoint evidence.
- Ambiguous questions after experiment are greater than or equal to baseline.
- Files read to resume increase and clarity does not materially improve.
- Contradiction count is greater than zero.
- Checkpoint update overhead is 20 minutes or more.
- Verification fails due to experiment artifacts.

Interpretation:

The proposed vocabulary does not improve ProjectForge enough to justify adoption.

### D. Retire

Evidence sufficient to retire:

Any of the following:

- The selected task type proves unsuitable and no near-term ProjectForge task type needs lifecycle/checkpoint support.
- The recommendation only solves hypothetical failure modes under current ProjectForge workflows.
- Maintaining the recommendation creates ongoing review noise after rejection.

Interpretation:

Keep the harvested pattern as historical evidence, but stop carrying it as an active ProjectForge candidate.

## Future outcome record

If this experiment is later approved and run, the future outcome record should be:

- `ArchitectureHarvest/adoption_log/O-YYYYMMDD-lifecycle-checkpoint-vocabulary.yaml`

Possible actions:

- adopted
- rejected
- modified
- failed

Expected ecosystem evidence generated:

- medium to high

Expected confidence after completion:

- medium

Reason:

A single-task experiment is not universal proof, but it is direct ProjectForge evidence about local fit, overhead, and operational impact.

## Validation for this proposal

Required checks:

- validate dry-run
- parse YAML proposal
- run full ProjectForge tests
- run context health
- run coherence
- run Architecture-to-Reality audit in JSON mode
