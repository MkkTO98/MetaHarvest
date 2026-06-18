# ArchitectureHarvest: dbt + Dagster MacroForge comparison

Boundary: ArchitectureHarvest analysis only. No MacroForge changes and no recommendation implementation. External source code was cloned and statically inspected only; it was not installed, imported, built, tested, or executed.

## Reinforcing evidence

- MacroForge's canonical-domain direction is strongly reinforced. dbt separates source/model metadata and contracts; Dagster separates source/external assets from materialized assets. Both support DEC-010/011: provider representations belong in evidence, staging, metadata, and mapping layers, not as curated identities.
- Source-specific loaders remain defensible. dbt/Dagster prove strong definition/validation patterns, but both also show the maintenance cost of generalized transformation/orchestration systems. This reinforces DEC-013's framework deferral.
- Accepted/provisional mapping state as a gate gained confidence. dbt contracts/tests and Dagster asset checks/data versions align with DEC-018's proposal -> review -> accepted mapping state flow.
- Lineage should be explicit and artifact-backed. dbt manifest dependencies and Dagster asset graphs both argue for compact lineage edge artifacts.

## Contradictory evidence

- dbt and Dagster both show that mature data platforms centralize transformations/assets in formal frameworks; this contradicts any permanent commitment to purely ad hoc scripts. It does not contradict MacroForge's current deferral because MacroForge has not yet hit the operational pressure threshold.
- Strict contracts/checks are mature best practice, but MacroForge source spikes need lighter evidence reports until a source/mapping is accepted.
- Complete lineage/metadata can become context bloat; ProjectForge/MacroForge should keep summaries and pointers as normal context.

## New high-confidence patterns

1. typed_canonical_manifest
2. asset_key_lineage_graph
3. data_contract_check_gate
4. provider_evidence_not_canonical_truth
5. definition_execution_boundary
6. schema_evolution_policy_surface
7. metadata_first_lineage_evidence

## Existing MacroForge decisions that gained confidence

- DEC-010: canonical-domain schema evolution over provider-centric identities.
- DEC-011: provider period/territory/code mappings and source-agnostic facts.
- DEC-013: defer generalized ingestion/framework/orchestration while accepting bounded shared validation.
- DEC-018: proposals, confidence/reasoning/evidence/version, review routing, accepted/provisional mapping state, and supersession lineage.
- DEC-019: next step should reduce uncertainty with tiny deterministic proposal workflow before model dependence or persistence complexity.

## Existing MacroForge decisions that lost confidence

No accepted decision lost net confidence. The strongest pressure is that future MacroForge should not remain permanently script-only if repeated assets, checks, lineage, and refreshes accumulate. This is a future trigger, not current implementation approval.

## Potential overengineering risks

- Adopting dbt/Dagster runtime/platform before MacroForge has repeated operational refresh/scheduling pressure.
- Hiding source-specific macroeconomic semantics behind generic loader interfaces.
- Turning every source spike into contract/asset ceremony.
- Loading full metadata/lineage graphs into normal context instead of compact summaries/pointers.
- Creating provider-shaped canonical models because framework abstractions make source columns easy to propagate.

## Potential missing capabilities

- Static canonical asset/manifest registry for raw evidence, staging tables, canonical dimensions/facts, mappings, reports, and checks.
- Explicit lineage edge artifacts with source path/checksum/run references.
- Contract/check representation for accepted canonical mappings and schema evolution.
- Data/code/ruleset/proposal versioning with staleness causes.
- Loadable-definition validation: duplicate keys, missing dependencies, unresolved mappings, partition/frequency mapping errors.
- Owner/group/access/review status metadata for canonical concepts and mappings.

## Recommendation boundary

Do not implement these recommendations from this report. If the user later approves MacroForge work, start with the smallest file-backed static definition/check artifact over existing fixtures; do not adopt dbt or Dagster runtime by default.
