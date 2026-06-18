# ArchitectureHarvest analysis cycle: Aider + SWE-agent compared with OpenHands/LangGraph

Date: 2026-06-06
Approved sources: Aider, SWE-agent
External clone locations:
- `/home/mkkto/srv/projectforge/external_sources/aider` @ 5dc9490bb35f9729ef2c95d00a19ccd30c26339c
- `/home/mkkto/srv/projectforge/external_sources/swe-agent` @ 10e3e76e629ad47331af562f367b9df6501cc55c

Boundary: ArchitectureHarvest analysis only. No recommendations were implemented. No external repository code was installed, imported, built, tested, or executed. ProjectForge runtime/governance/templates/state were not changed by this analysis, except for the required dry-run evidence outside ArchitectureHarvest.

## Highest-confidence patterns

1. Git/patch anchored coding workflow.
   - Evidence: Aider `GitRepo` diffs/commits/dirty-file tracking; SWE-agent `/root/model.patch`, patch save/apply hook, draft PR hook.
   - Confidence: high.
   - ProjectForge implication: final code changes should remain inspectable as diffs/patches/commits with tests before claims of completion.

2. Bounded context selection with durable evidence split.
   - Evidence: Aider editable/read-only files + repo map + summarization; SWE-agent history processors + persisted trajectories; LangGraph checkpoints; OpenHands event/lifecycle records.
   - Confidence: high.
   - ProjectForge implication: keep compact current-state/context bundles for active work and raw trajectories/logs for audit/debug.

3. Patch/submission boundary before publication.
   - Evidence: SWE-agent submit tool and apply/open-PR hooks; Aider diffs/commits; OpenHands source-control tool boundary.
   - Confidence: high.
   - ProjectForge implication: publication/push/PR remains a separate approval-gated step.

4. Planning/execution separation.
   - Evidence: Aider ask/code/architect/context modes; SWE-agent problem statement/templates vs agent action loop; LangGraph graph/state separation; OpenHands conversation/runtime lifecycle.
   - Confidence: high.
   - ProjectForge implication: planning/recommendations should remain decision inputs until separately approved for implementation.

5. Trajectory/checkpoint artifacts for recovery.
   - Evidence: SWE-agent repeated `.traj` saves and replay config; LangGraph checkpoint contract; OpenHands event stream; PF-AH-REC-010 narrow local checkpoint outcome.
   - Confidence: high for long-running/high-risk workflows; medium for ordinary tasks.

## Strongest simplification opportunities

1. Use git diff/patch/checkpoint files before adding any orchestration runtime.
   - Reinforced by Aider, SWE-agent, LangGraph, OpenHands, and the PF-AH-REC-010 outcome.

2. Keep reviewer/retry/sandbox machinery optional.
   - SWE-agent and OpenHands show the value of heavy machinery for product/benchmark contexts, but ProjectForge's file-first Hermes workflow usually needs only the smallest evidence artifact.

3. Replace dynamic or full replay context with compact summaries plus pointers.
   - Aider repo map and SWE-agent history processors both support the principle that active prompt context is not the same as complete audit evidence.

4. Treat automatic commit/apply/PR features as anti-defaults.
   - They are useful in external tools, but for ProjectForge they should remain disabled unless an explicit approval workflow is designed.

## Strongest replacement opportunities

1. Replace raw-log/chat-memory recovery with checkpoint/current-state + diff/patch/trajectory pointers.
2. Replace implicit file scope with explicit editable/read-only/in-scope file records for complex repository-changing work.
3. Replace out-of-band task completion notes with structured final artifacts: changed files, diff/patch pointer, tests, coherence result, and rollback handle.
4. Replace generic multi-agent retry loops with a reviewer/retry loop only for high-value tasks where multiple attempts and best-submission selection are explicitly approved.

## Strongest contradictions

1. Autocommit/apply/PR convenience vs ProjectForge dry-run/human approval.
   - Aider and SWE-agent support fast code publication workflows; ProjectForge constitution requires dry-run and approval gates.
   - Guidance: preserve ProjectForge gates.

2. Full trajectory/event replay vs compact current-state context.
   - SWE-agent/OpenHands/LangGraph value complete replay; ProjectForge normal context must stay compact.
   - Guidance: store replay evidence, but load compact summaries by default.

3. Benchmark autonomous loops vs human-governed project lifecycle.
   - SWE-agent retry/reviewer/autosubmission loops optimize issue solving; ProjectForge must not create autonomous refactoring campaigns.
   - Guidance: use as optional high-value pattern only.

4. Automatic repo-map context vs explicit context bundles/audits.
   - Aider dynamically builds repo maps; ProjectForge values explicit context manifests.
   - Guidance: if adapted, make repo-map-like summaries explicit and auditable.

## Comparison against OpenHands findings

Reinforcing evidence:
- OpenHands sandbox/runtime lifecycle is reinforced by SWE-agent environment start/reset/close and timeout interruption.
- OpenHands source-control/tool-boundary evidence is reinforced by Aider git boundaries and SWE-agent patch/PR hooks.
- OpenHands pending/lifecycle state aligns with Aider explicit editable context and SWE-agent persisted trajectories.

Contradictory evidence:
- OpenHands product/runtime orientation and SWE-agent benchmark autonomy are heavier than Aider's interactive git workflow and ProjectForge's file-first governance.
- Aider supports direct autocommit ergonomics; ProjectForge should not adopt that default.

## Comparison against LangGraph findings

Reinforcing evidence:
- LangGraph checkpoint contract is reinforced by SWE-agent trajectory persistence and PF-AH-REC-010 local checkpoint validation.
- LangGraph interrupt/resume approval concept is reinforced by Aider's explicit user confirmations and SWE-agent's patch-before-publication boundary, but not by SWE-agent autosubmission.

Contradictory evidence:
- LangGraph suggests a graph/checkpointer dependency is available; Aider/SWE-agent show many benefits can be captured with git, patch, history, and trajectory files without adding a graph runtime.

## Existing ecosystem-weighted recommendations

Gained confidence:
- Minimal file-backed checkpoint/recovery artifacts: increased by SWE-agent trajectories, LangGraph checkpoints, OpenHands events, and the PF-AH-REC-010 adoption outcome.
- File-backed context summaries instead of raw logs: increased by Aider repo-map/summarization and SWE-agent history processors.
- Patch/diff as review boundary: increased by Aider and SWE-agent independent evidence.
- Separate planning/recommendation from execution: increased by Aider architect/code modes and SWE-agent problem/template/action separation.

Lost confidence:
- Adopting an external orchestration/runtime dependency by default lost confidence. Aider/SWE-agent show effective workflows can remain file/git/patch-based.
- Broad automatic retry/autosubmit/publish workflows lost confidence for ProjectForge default use because they conflict with dry-run and approval rules.
- Full trajectory/event replay as normal startup context lost confidence; it remains useful for audit/debug only.

## Recommendations requiring further evidence

1. Whether ProjectForge should standardize explicit editable/read-only file-scope fields for complex code tasks needs one or two local validation experiments.
2. Whether a repo-map-like generated summary belongs in ProjectForge should be tested against `tools/build_context.py` and folder summaries rather than assumed from Aider.
3. Whether reviewer/retry loops fit ProjectForge needs a concrete high-value task with a preapproved budget, success threshold, and human review gate.
4. Whether environment reset boundaries belong in ProjectForge core or only generated projects requires a real sandboxed/reproducible workflow.
5. Whether patch-as-submission should become a required artifact for all code changes or only high-risk repository workflows needs local outcome data.

## Artifact index

- Project cards: `ArchitectureHarvest/project_cards/aider.yaml`, `ArchitectureHarvest/project_cards/swe-agent.yaml`
- Component cards: `ArchitectureHarvest/component_cards/aider-*.yaml`, `ArchitectureHarvest/component_cards/swe-agent-*.yaml`
- Deep reports: `ArchitectureHarvest/reports/R-20260606-aider-deep-analysis.md`, `ArchitectureHarvest/reports/R-20260606-swe-agent-deep-analysis.md`
- Contradictions: `ArchitectureHarvest/contradictions/autocommit-vs-dry-run-approval.yaml`, `trajectory-replay-vs-compact-state.yaml`, `benchmark-agent-loop-vs-human-governance.yaml`, `repo-map-vs-explicit-context-bundles.yaml`
- Synthesis: `ArchitectureHarvest/synthesis/git_anchored_coding_workflow.yaml`, `bounded_context_selection.yaml`, `plan_execute_split.yaml`, `trajectory_artifact_recovery.yaml`, `patch_submission_boundary.yaml`, `reviewer_retry_loop.yaml`, `environment_reset_boundary.yaml`
- Relevance maps: `ArchitectureHarvest/relevance_maps/projectforge/aider-relevance-map.yaml`, `swe-agent-relevance-map.yaml`
- Candidates: `ArchitectureHarvest/adoption_candidates/aider-*-candidate.yaml`, `swe-agent-*-candidate.yaml`
