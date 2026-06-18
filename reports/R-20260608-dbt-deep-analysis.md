# dbt Core deep ArchitectureHarvest analysis

Boundary: static source analysis only; dbt code was not executed.

## Highest-confidence observations

- dbt compiles file-backed source inputs into a typed manifest graph: `crates/dbt-compilation/src/core.rs`, `crates/dbt-parser/src/resolver.rs`, `crates/dbt-schemas/src/schemas/manifest/manifest.rs`.
- Lineage/dependency metadata is explicit through `depends_on`, refs, sources, macro dependencies, scheduler dependency derivation, and optional column-lineage metadata.
- Contracts and validation are first-class: enforced contracts, contract checksums, breaking-change detection, model/data/unit tests, and store-failures behavior.
- Schema evolution policy is explicit through `OnSchemaChange`, incremental schema-change macros, model versions, latest-version pointers, and deprecation fields.
- Governance boundaries appear through `private/protected/public` access, groups, restrict-access, selectors, and access-denied validation.

## MacroForge comparison

Reinforces DEC-010/011: provider codes and metadata should remain evidence/mappings while canonical facts stay source-agnostic. Reinforces DEC-013: parse/resolve/schedule/run boundaries can be useful without approving a generalized framework. Reinforces DEC-018: proposals/accepted mapping state need checksums, versions, and evidence references.

## Contradictions and risks

- dbt runtime/model abstraction would overfit MacroForge before repeated transformation pressure appears.
- Strict contracts are valuable for accepted canonical state but too heavy for early source spikes.
- Column-lineage/metadata completeness can become context bloat unless loaded by pointer.
