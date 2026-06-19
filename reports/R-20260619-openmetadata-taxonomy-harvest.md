# MetaHarvest taxonomy harvest: OpenMetadata taxonomy harvest

Boundary: static source inspection only. No external code was installed, imported, built, tested, or executed. This report is descriptive evidence only; it introduces no synthesis, recommendation, ranking, or target-project decision logic.

Analyzed commit: `b953555301bcb85094ce8c06f570a7f32c5699f8`

## Evidence inspected
- `README.md`
- `openmetadata-spec/src/main/resources/json/schema/entity/data/table.json`
- `openmetadata-spec/src/main/resources/json/schema/type/entityLineage.json`
- `openmetadata-service/src/main/java/org/openmetadata/service/resources/lineage/LineageResource.java`
- `openmetadata-mcp/README.md`

## Categories added or strengthened
- metadata catalog
- lineage system
- governance infrastructure
- context activation interface

## Discovered concepts
- metadata entity
- entity reference
- lineage edge
- column lineage
- domain
- classification
- glossary term
- data contract
- governed context

## Discovered methodologies
- schema-first metadata extraction
- lineage API/interface inspection
- governance taxonomy decomposition
- AI/tool access boundary extraction

## Discovered patterns
- schema-first metadata graph
- lineage edge with details
- governance taxonomy attached to assets
- governed MCP/API context activation

## Discovered interfaces
- JSON schema entity definitions
- lineage REST resource
- classification/glossary/domain/data-contract schemas
- OAuth-backed MCP interface

## Component cards produced
- `MetaHarvest/component_cards/openmetadata-schema-first-entity-model.yaml`
- `MetaHarvest/component_cards/openmetadata-lineage-resource.yaml`
- `MetaHarvest/component_cards/openmetadata-governance-taxonomy.yaml`
- `MetaHarvest/component_cards/openmetadata-mcp-context-interface.yaml`

## Doctrine preservation

- The harvest is non-domain and descriptive.
- It does not introduce recommendations, ranking, target-project relevance logic, or implementation tasks.
- It does not modify retrieval architecture.
- It does not modify other EIP projects.
- Source code is used only as evidence and not copied into local implementation.

## Limitations

- Static inspection was bounded to representative architecture, interface, and schema files.
- The project was not executed, installed, built, imported, or tested.
- License classification is for MetaHarvest evidence handling only; dependency adoption would require a separate decision.
