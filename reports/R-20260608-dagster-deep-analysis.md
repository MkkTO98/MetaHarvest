# Dagster deep ArchitectureHarvest analysis

Boundary: static source analysis only; Dagster code was not executed.

## Highest-confidence observations

- Dagster makes assets first-class with hierarchical keys, dependencies, metadata, owners, partitions, code versions, and graph structure: `asset_decorator.py`, `asset_spec.py`, `asset_key.py`, `asset_graph.py`, `base_asset_graph.py`.
- Asset checks are explicit, severity-aware, optionally blocking validation contracts: `asset_check_spec.py`, `asset_check_result.py`.
- Metadata and schema are typed through `MetadataValue`, `TableSchema`, `TableColumn`, `TableColumnConstraints`.
- Data/code versions and provenance/staleness causes provide a compact schema for reproducible materialization evidence.
- SourceAsset/external/unexecutable assets distinguish observed external data from owned/materialized assets.
- `Definitions.validate_loadable` shows a static validation gate before runtime execution.

## MacroForge comparison

Reinforces MacroForge's need to distinguish provider evidence from owned canonical assets. It strengthens the case for static canonical asset definitions, dependency edges, check contracts, versioned mapping/provenance, and loadability validation, while also reinforcing DEC-013's deferral of a full orchestration platform.

## Contradictions and risks

- Dagster's runtime/daemon/schedule model is too heavy for current MacroForge.
- Asset abstraction could hide source-specific semantics if introduced before carefully bounded file-backed definitions.
- Rich metadata/check definitions can become ceremony unless scoped to accepted canonical state and repeated validation pressure.
