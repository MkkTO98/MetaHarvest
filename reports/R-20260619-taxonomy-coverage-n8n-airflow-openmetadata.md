# MetaHarvest taxonomy coverage summary: n8n, Apache Airflow, OpenMetadata

Boundary: coverage summary for the 2026-06-19 taxonomy harvest. This artifact summarizes descriptive evidence only. It does not synthesize recommendations, rank projects, or create decision logic.

## Sources added

| Source | Category | Commit | Evidence role |
| --- | --- | --- | --- |
| n8n | workflow automation / integration platform | `31f718f8f8ad6575fd049a2bb10aa597049604b1` | connector-rich workflow graph, webhook/trigger lifecycle, credential boundary, execution persistence |
| Apache Airflow | workflow orchestration / scheduling system | `9c4908019a3f8d386eaed56c0552adfde241e952` | DAGs, scheduler state machine, timetables, executor boundary, asset-aware scheduling |
| OpenMetadata | metadata catalog / lineage / governance infrastructure | `b953555301bcb85094ce8c06f570a7f32c5699f8` | schema-first metadata graph, lineage edges, governance taxonomy, governed MCP/API context interface |

## Categories added or materially strengthened

Previously strong: agent runtime/orchestration, coding agents, analytics transformation, asset orchestration.

New or weakly represented before this harvest:

- workflow automation
- integration platforms
- webhook-triggered automation
- credential-aware connector interfaces
- workflow orchestration systems
- scheduling systems
- timetable/schedule validation
- asset/event-aware scheduling
- metadata catalogs
- lineage systems
- column lineage interfaces
- governance-related infrastructure
- semantic metadata and glossary systems
- data contract metadata
- governed AI/context activation interfaces

## Concepts added

- workflow graph
- integration node
- trigger registration
- webhook endpoint
- credential boundary
- execution snapshot
- DAG
- task dependency
- DagRun
- TaskInstance
- timetable
- asset event
- executor boundary
- metadata entity
- entity reference
- lineage edge
- column lineage
- domain
- classification
- glossary term
- data contract
- governed context

## Methodologies added

- Decompose workflow automation platforms by definition graph, activation lifecycle, credential boundary, and execution evidence.
- Decompose schedulers by authoring contract, timetable normalization, run-state machine, executor boundary, and asset/event inputs.
- Decompose metadata catalogs by schema-first entity model, lineage interface, governance taxonomy, and activation/API boundary.
- Use static representative source files and schemas to broaden taxonomy coverage without executing third-party code.

## Patterns added

- Declarative node-and-connection workflow graph.
- Desired-vs-actual trigger reconciliation.
- Execution evidence stored outside workflow definition.
- Credential references separated from workflow graph.
- Workflow-as-code DAG.
- Validated timetable contract.
- Bounded scheduler loop.
- Asset-event scheduling.
- Schema-first metadata graph.
- Lineage edge with details.
- Governance taxonomy attached to assets.
- Governed MCP/API context activation.

## Interfaces added

- n8n node type interface.
- n8n credential access interface.
- n8n webhook registration surface.
- n8n execution persistence store.
- Airflow DAG authoring API.
- Airflow timetable interface.
- Airflow scheduler/executor boundary.
- Airflow asset URI normalization interface.
- OpenMetadata JSON schema entity definitions.
- OpenMetadata lineage REST resource.
- OpenMetadata classification/glossary/domain/data-contract schemas.
- OpenMetadata OAuth-backed MCP interface.

## Coverage conclusion

The harvest broadens MetaHarvest beyond the existing agent, coding-agent, transformation, and asset-orchestration sources. It adds category diversity specifically in workflow automation, integration platforms, orchestration/scheduling systems, metadata catalogs, lineage systems, and governance infrastructure. The added material is sufficient for future taxonomy and retrieval validation across these categories without maximizing source count.
