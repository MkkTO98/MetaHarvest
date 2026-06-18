# First ArchitectureHarvest adoption outcome proposal

Created UTC: 2026-06-06T10:24:07Z

Status: proposed only. No implementation was performed.

Purpose: select the single recommendation from the first ArchitectureHarvest-guided ProjectForge review with the highest expected benefit-to-effort ratio, then propose a small reversible implementation that can generate the first ArchitectureHarvest adoption outcome and begin validating the ecosystem-weighted recommendation model.

Source review:
- `ArchitectureHarvest/reviews/R-20260606-projectforge-architectureharvest-guided-review.yaml`

Companion machine-readable artifact:
- `ArchitectureHarvest/adoption_proposals/P-20260606-architectureharvest-first-adoption-outcome.yaml`

## Selected recommendation

Selected recommendation: PF-AH-REC-007

Title: Delete or retire ArchitectureHarvest source-derived candidates that remain unused after scheduled reviews or never gain local adoption outcomes.

Classification from first review: A. Immediate candidate

Category: deletion candidate

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

## Why this has the highest expected benefit-to-effort ratio

PF-AH-REC-007 has the strongest combination of:

- Implementation effort: low
- Expected maintenance reduction: high
- Expected complexity reduction: high
- Risk: low
- Direct relevance to ArchitectureHarvest's own maintenance burden

It is also the safest first adoption-outcome candidate because it changes only ArchitectureHarvest governance/schema expectations, not ProjectForge runtime behavior, task execution, approvals, or generated-project behavior.

Compared with other high-ratio candidates:

- PF-AH-REC-001 is also high-value and low-effort, but it mostly reinforces an existing ProjectForge principle: file-backed governance remains default. It is valuable, but its marginal implementation path is less concrete because much of the behavior already exists.
- PF-AH-REC-005 also validates an existing ProjectForge principle: raw logs stay out of normal context. Again valuable, but less useful as a first adoption outcome because it mostly confirms existing design.
- PF-AH-REC-007 creates a new and measurable ArchitectureHarvest capability: retiring stale or unused recommendations instead of letting them accumulate.

That makes PF-AH-REC-007 the best first implementation proposal for validating whether ArchitectureHarvest can improve its own recommendation quality over time.

## Why not "minimal lifecycle/checkpoint vocabulary"?

The chosen recommendation is not "minimal lifecycle/checkpoint vocabulary."

Reason:

Minimal lifecycle/checkpoint vocabulary is important, but it is not the highest benefit-to-effort first adoption candidate.

The first review classified the lifecycle/checkpoint recommendation as a future or evidence-gated candidate with:

- Implementation effort: medium
- Maintenance reduction: medium or unknown depending on scope
- Complexity reduction: medium or unknown
- Risk: medium for standardization before a real long-running task proves the need

Its value depends on measuring whether it actually reduces handoff ambiguity in a real long-running ProjectForge task. Implementing it first would risk standardizing vocabulary before there is local outcome evidence.

PF-AH-REC-007 is better as the first adoption outcome because it is smaller, safer, and directly strengthens the ArchitectureHarvest feedback loop. It also sets up the ecosystem-weighted model so later lifecycle/checkpoint adoption can be evaluated more rigorously.

## Small reversible implementation proposal

### Implementation scope

Add a compact retirement discipline for ArchitectureHarvest recommendation/candidate records.

The implementation should define:

1. Review triggers for source-derived candidates.
2. Criteria for keeping, retiring, superseding, or evidence-gating candidates.
3. How retirement/rejection outcomes are recorded as useful ecosystem evidence.
4. Tests proving the new fields/rules remain parseable and linked.

No source records should be deleted in the first implementation. The first implementation should only add policy/schema support and a first adoption outcome record after validation.

### Exact files affected if implemented

1. `ArchitectureHarvest/retrieval/recommendation_rules.yaml`
   - Add a compact `candidate_retirement_rules` section.
   - Define when stale/unused source-derived candidates must be reviewed, retired, superseded, or kept active.

2. `ArchitectureHarvest/templates/adoption_candidate.template.yaml`
   - Add optional lifecycle/review metadata fields:
     - `last_reviewed`
     - `next_review_due`
     - `retirement_condition`
     - `superseded_by`

3. `ArchitectureHarvest/templates/adoption_outcome.template.yaml`
   - Add optional links:
     - `proposal_id`
     - `review_cycle_id`
   - Purpose: future outcome records can trace back to this adoption proposal and the originating ArchitectureHarvest review.

4. `ArchitectureHarvest/outcome_models/ecosystem_outcome_model.yaml`
   - Add a rule that retirement/rejection outcomes are positive ecosystem evidence when they reduce maintenance burden or avoid complexity.

5. `tests/test_architectureharvest_integration.py`
   - Add tests that parse the updated retirement metadata/rules.
   - Verify outcome records can link to proposal/review identifiers.

6. If implementation succeeds, create one adoption outcome record:
   - `ArchitectureHarvest/adoption_log/O-20260606-source-candidate-retirement-discipline.yaml`

### Explicit non-scope

Do not:

- Delete OpenHands or LangGraph analysis records.
- Retire any source, pattern, contradiction, or candidate without a separate review record.
- Modify ProjectForge runtime behavior.
- Modify ProjectForge task/state/handoff behavior.
- Add a database, dashboard, scheduler, vector store, or autonomous cleanup job.
- Inspect external repositories.
- Perform new harvesting.

## Expected benefits

1. Converts ArchitectureHarvest from an accumulating analysis folder into a governed feedback system with an exit path for low-value evidence.
2. Produces a first local adoption outcome without requiring a risky runtime or workflow change.
3. Reduces future review noise by requiring old candidates to prove continuing usefulness.
4. Improves trust in ArchitectureHarvest recommendations by making retirement/rejection first-class signals.
5. Starts validating ecosystem-weighted recommendation logic using an outcome that directly targets maintenance burden and complexity.

## Risks

1. Criteria may over-retire useful but not-yet-needed candidates if written too aggressively.
2. Lifecycle fields could add YAML/template ceremony if they are not optional and compact.
3. The first adoption outcome may be too meta to validate implementation-value predictions for user-facing ProjectForge work.
4. Tests may accidentally hard-code policy wording that should remain advisory.

## Rollback plan

If implemented and rejected, revert only these changes:

- Remove the `candidate_retirement_rules` section from `ArchitectureHarvest/retrieval/recommendation_rules.yaml`.
- Remove lifecycle/review metadata additions from `ArchitectureHarvest/templates/adoption_candidate.template.yaml`.
- Remove proposal/review-cycle link additions from `ArchitectureHarvest/templates/adoption_outcome.template.yaml`.
- Remove the retirement/rejection outcome rule from `ArchitectureHarvest/outcome_models/ecosystem_outcome_model.yaml`.
- Remove corresponding tests from `tests/test_architectureharvest_integration.py`.
- Remove `ArchitectureHarvest/adoption_log/O-20260606-source-candidate-retirement-discipline.yaml` if the adoption outcome is abandoned before acceptance.

No harvested source records, source clones, ProjectForge state files, or runtime behavior should need rollback.

## How success will be measured

Qualitative success:

- A future ArchitectureHarvest review can classify at least one candidate as keep, retire, supersede, or needs-evidence using explicit rules.
- The first adoption outcome record can be parsed and linked back to this proposal and the original review recommendation.
- Recommendation-strength updates can cite retirement/rejection outcomes as ecosystem evidence, not only successful adoptions.
- Reviewers do not need to inspect external repositories or deep reports to apply the retirement rule.

Quantitative success:

- All ArchitectureHarvest YAML files parse successfully.
- ArchitectureHarvest integration tests pass.
- Full ProjectForge tests pass.
- ProjectForge context health reports no new blocks/warnings caused by the implementation.
- ProjectForge coherence reports no new blocks/warnings caused by the implementation.
- Architecture-to-Reality audit reports no new blocks/warnings caused by the implementation.

## How failure will be measured

Qualitative failure:

- The new fields make candidate records harder to read or maintain.
- Reviewers cannot decide whether a candidate should be retired without re-reading deep reports or external repositories.
- Outcome weighting remains unchanged because retirement/rejection outcomes are not actionable.
- The change encourages premature deletion instead of evidence-based retirement.

Quantitative failure:

- YAML parse fails.
- ArchitectureHarvest integration tests fail.
- Full ProjectForge tests fail.
- Context health, coherence, or architecture audit adds blocks/warnings attributable to the change.
- The implementation touches files outside the exact scope listed above.

## Expected adoption outcome if implemented

Expected future outcome record:
- `ArchitectureHarvest/adoption_log/O-20260606-source-candidate-retirement-discipline.yaml`

Expected outcome class:
- `proven_successful_in_ecosystem`, if the implementation remains compact, parseable, tested, and reduces future recommendation noise.

Expected weighting delta:
- increase

Rationale:
- A successful implementation would show that ArchitectureHarvest can use its own review output to reduce future maintenance burden and improve recommendation quality without adding runtime complexity.

## Validation for this proposal artifact

Required checks:

- Validate dry-run report.
- Parse proposal YAML.
- Run full ProjectForge tests.
- Run context health.
- Run ProjectForge coherence.
- Run Architecture-to-Reality audit in JSON mode.
