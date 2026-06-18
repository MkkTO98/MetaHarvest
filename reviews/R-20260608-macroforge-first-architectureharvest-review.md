# First MacroForge ArchitectureHarvest Review

Date: 2026-06-08

Scope: recommendation artifacts only. No MacroForge files were modified, no recommendations were implemented, and external repositories were not inspected.

Allowed evidence used:

- dbt analyses
- Dagster analyses
- synthesized patterns
- contradiction records
- MacroForge relevance maps
- adoption candidates

Ranking method: 1=low, 2=low-medium, 3=medium, 4=high, 5=very high. Benefit-to-effort score = expected_benefit / implementation_effort.

## Executive conclusion

ArchitectureHarvest has identified improvements valuable enough to justify a future MacroForge change request, but only in a narrow file-backed form. The evidence does not justify dbt/Dagster runtime adoption, generalized ingestion-framework extraction, automated materialization, or broad orchestration changes.

## Single highest expected benefit-to-effort recommendation

MF-AH-REV-001: Create a tiny file-backed canonical asset/manifest registry for accepted/provisional canonicalization artifacts.

Why this wins: it captures the strongest shared dbt/Dagster evidence with the smallest MacroForge-native implementation surface. It creates stable keys and compact definitions for source evidence, staging, canonical concepts, mappings, reports, checks, owners/status, and artifact pointers. It also unlocks the next useful improvements — lineage edges, checks, schema evolution, and governance metadata — without adopting a runtime platform or replacing source-specific loaders.

Important nuance: deletion guardrails have a numerically high benefit/effort score because they are cheap, but they mostly prevent overengineering. MF-AH-REV-001 has the best positive capability gain for modest effort.

## Ranked findings

- MF-AH-REV-001: Create a tiny file-backed canonical asset/manifest registry for accepted/provisional canonicalization artifacts
  - Scores: benefit 5, effort 2, maintenance 2, confidence 5, benefit/effort 2.5
  - Disposition: highest_benefit_to_effort
  - Rationale: Unifies dbt typed manifest and Dagster asset-key evidence into the smallest MacroForge-native artifact: stable keys plus source/raw/staging/canonical/report roles, status, owner, and pointers. It simplifies scattered evidence without introducing runtime orchestration.

- MF-AH-REV-002: Add explicit lineage edge artifacts for raw -> staging -> canonical -> report paths
  - Scores: benefit 5, effort 3, maintenance 3, confidence 5, benefit/effort 1.67
  - Disposition: valuable_after_manifest
  - Rationale: Lineage evidence is high confidence, but a standalone lineage artifact is more useful after a tiny manifest/key vocabulary exists. Keep compact summaries and pointers to avoid context bloat.

- MF-AH-REV-003: Represent accepted canonicalization checks as reusable contract/check artifacts
  - Scores: benefit 5, effort 3, maintenance 3, confidence 5, benefit/effort 1.67
  - Disposition: valuable_for_accepted_state
  - Rationale: dbt contracts/tests and Dagster asset checks strongly support checks as gates, but MacroForge should scope strict checks to accepted canonical state and use lighter reports during source spikes.

- MF-AH-REV-004: Replace ad hoc validation/lineage report shapes with explicit manifest/check/lineage records once repeated pressure exists
  - Scores: benefit 4, effort 3, maintenance 3, confidence 4, benefit/effort 1.33
  - Disposition: defer_until_repetition
  - Rationale: Replacement is likely valuable, but not first: MacroForge should first prove the tiny manifest/check format on one existing canonicalization path.

- MF-AH-REV-005: Add schema/mapping/proposal version and deprecation/staleness fields
  - Scores: benefit 4, effort 3, maintenance 3, confidence 5, benefit/effort 1.33
  - Disposition: defer_or_bundle_lightly
  - Rationale: Schema evolution policy is high-confidence, but the first implementation can include only minimal version/status fields; full deprecation/staleness model needs more local evidence.

- MF-AH-REV-006: Use typed definitions to reduce scattered report/lineage evidence while preserving source-specific loaders
  - Scores: benefit 4, effort 2, maintenance 3, confidence 4, benefit/effort 2.0
  - Disposition: second_best
  - Rationale: Simplification candidate is strong but depends on the same tiny manifest registry; it should be framed as the outcome of MF-AH-REV-001 rather than a separate system.

- MF-AH-REV-007: Retire broad dbt/Dagster runtime adoption as a near-term MacroForge candidate
  - Scores: benefit 3, effort 1, maintenance 1, confidence 5, benefit/effort 3.0
  - Disposition: cheap_guardrail_not_highest_benefit
  - Rationale: Very cheap and high-confidence as a governance guardrail, but expected positive capability benefit is lower than manifest creation. Keep runtime adoption dormant until refresh/scheduling/materialization pressure appears.

- MF-AH-REV-008: Reject generalized ingestion-framework extraction from dbt/Dagster evidence
  - Scores: benefit 3, effort 1, maintenance 1, confidence 5, benefit/effort 3.0
  - Disposition: cheap_guardrail_not_highest_benefit
  - Rationale: Contradictions strongly favor source-specific loaders for now; deleting/retiring generic ingestion ambitions prevents framework creep.

- MF-AH-REV-009: Measure repeated validation/report boilerplate across MacroForge sources before replacing current reports
  - Scores: benefit 3, effort 2, maintenance 1, confidence 4, benefit/effort 1.5
  - Disposition: needs_local_measurement
  - Rationale: External evidence is strong, but replacement should wait for local evidence of repeated shape drift or maintenance overhead.

- MF-AH-REV-010: Measure operational refresh/scheduling/materialization pressure before adopting orchestration runtime concepts
  - Scores: benefit 2, effort 2, maintenance 1, confidence 5, benefit/effort 1.0
  - Disposition: needs_local_measurement
  - Rationale: dbt/Dagster runtimes solve real orchestration pressure, but MacroForge evidence currently supports deferral.

## Simplification candidates

- MF-AH-REV-001: Create a tiny file-backed canonical asset/manifest registry for accepted/provisional canonicalization artifacts
  - Scores: benefit 5, effort 2, maintenance 2, confidence 5, benefit/effort 2.5
  - Disposition: highest_benefit_to_effort
  - Rationale: Unifies dbt typed manifest and Dagster asset-key evidence into the smallest MacroForge-native artifact: stable keys plus source/raw/staging/canonical/report roles, status, owner, and pointers. It simplifies scattered evidence without introducing runtime orchestration.

- MF-AH-REV-006: Use typed definitions to reduce scattered report/lineage evidence while preserving source-specific loaders
  - Scores: benefit 4, effort 2, maintenance 3, confidence 4, benefit/effort 2.0
  - Disposition: second_best
  - Rationale: Simplification candidate is strong but depends on the same tiny manifest registry; it should be framed as the outcome of MF-AH-REV-001 rather than a separate system.

## Replacement candidates

- MF-AH-REV-004: Replace ad hoc validation/lineage report shapes with explicit manifest/check/lineage records once repeated pressure exists
  - Scores: benefit 4, effort 3, maintenance 3, confidence 4, benefit/effort 1.33
  - Disposition: defer_until_repetition
  - Rationale: Replacement is likely valuable, but not first: MacroForge should first prove the tiny manifest/check format on one existing canonicalization path.

## Missing capability candidates

- MF-AH-REV-002: Add explicit lineage edge artifacts for raw -> staging -> canonical -> report paths
  - Scores: benefit 5, effort 3, maintenance 3, confidence 5, benefit/effort 1.67
  - Disposition: valuable_after_manifest
  - Rationale: Lineage evidence is high confidence, but a standalone lineage artifact is more useful after a tiny manifest/key vocabulary exists. Keep compact summaries and pointers to avoid context bloat.

- MF-AH-REV-003: Represent accepted canonicalization checks as reusable contract/check artifacts
  - Scores: benefit 5, effort 3, maintenance 3, confidence 5, benefit/effort 1.67
  - Disposition: valuable_for_accepted_state
  - Rationale: dbt contracts/tests and Dagster asset checks strongly support checks as gates, but MacroForge should scope strict checks to accepted canonical state and use lighter reports during source spikes.

- MF-AH-REV-005: Add schema/mapping/proposal version and deprecation/staleness fields
  - Scores: benefit 4, effort 3, maintenance 3, confidence 5, benefit/effort 1.33
  - Disposition: defer_or_bundle_lightly
  - Rationale: Schema evolution policy is high-confidence, but the first implementation can include only minimal version/status fields; full deprecation/staleness model needs more local evidence.

## Deletion candidates

- MF-AH-REV-007: Retire broad dbt/Dagster runtime adoption as a near-term MacroForge candidate
  - Scores: benefit 3, effort 1, maintenance 1, confidence 5, benefit/effort 3.0
  - Disposition: cheap_guardrail_not_highest_benefit
  - Rationale: Very cheap and high-confidence as a governance guardrail, but expected positive capability benefit is lower than manifest creation. Keep runtime adoption dormant until refresh/scheduling/materialization pressure appears.

- MF-AH-REV-008: Reject generalized ingestion-framework extraction from dbt/Dagster evidence
  - Scores: benefit 3, effort 1, maintenance 1, confidence 5, benefit/effort 3.0
  - Disposition: cheap_guardrail_not_highest_benefit
  - Rationale: Contradictions strongly favor source-specific loaders for now; deleting/retiring generic ingestion ambitions prevents framework creep.

## Recommendations requiring more evidence

- MF-AH-REV-009: Measure repeated validation/report boilerplate across MacroForge sources before replacing current reports
  - Scores: benefit 3, effort 2, maintenance 1, confidence 4, benefit/effort 1.5
  - Disposition: needs_local_measurement
  - Rationale: External evidence is strong, but replacement should wait for local evidence of repeated shape drift or maintenance overhead.

- MF-AH-REV-010: Measure operational refresh/scheduling/materialization pressure before adopting orchestration runtime concepts
  - Scores: benefit 2, effort 2, maintenance 1, confidence 5, benefit/effort 1.0
  - Disposition: needs_local_measurement
  - Rationale: dbt/Dagster runtimes solve real orchestration pressure, but MacroForge evidence currently supports deferral.

## Recommendation boundary

Do not implement these recommendations from this review. If the user later approves MacroForge work, start with MF-AH-REV-001 as a narrow design/implementation task inside MacroForge, with its own dry-run, tests, coherence, and audit.

## Evidence interpretation

Reinforcing evidence: dbt manifests/contracts and Dagster assets/checks/versions both support typed definitions, explicit lineage, and validation gates.

Contradictory evidence: mature data systems eventually centralize transformations and assets in frameworks, but MacroForge has not shown enough operational pressure to justify runtime adoption. Strict contracts are useful for accepted canonical state, not early exploratory source spikes.

Net result: ArchitectureHarvest justifies a future small MacroForge-native file-backed metadata/check/lineage improvement, not a framework adoption.
