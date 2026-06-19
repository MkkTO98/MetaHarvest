# Component Index

Use this index to route from an architectural concern to the compact component card before loading deep reports.

## First-cycle component cards

### OpenHands
- Conversation lifecycle: `../component_cards/openhands-conversation-lifecycle.yaml`
- Event service: `../component_cards/openhands-event-service.yaml`
- Pending message queue: `../component_cards/openhands-pending-message-queue.yaml`
- Sandbox boundary/readiness: `../component_cards/openhands-sandbox-boundary.yaml`
- MCP/source-control tool surface: `../component_cards/openhands-mcp-source-control-tools.yaml`

### LangGraph
- StateGraph builder: `../component_cards/langgraph-stategraph.yaml`
- Pregel execution loop: `../component_cards/langgraph-pregel-loop.yaml`
- Checkpoint saver contract: `../component_cards/langgraph-checkpoint-saver.yaml`
- Interrupt/Command types: `../component_cards/langgraph-interrupt-command.yaml`
- Streaming task/checkpoint events: `../component_cards/langgraph-streaming-task-events.yaml`

## 2026-06-19 taxonomy-diversity component cards

### n8n
- Workflow graph and expression model: `../component_cards/n8n-workflow-graph.yaml`
- Trigger and webhook registration lifecycle: `../component_cards/n8n-trigger-webhook-registration.yaml`
- Execution persistence and data storage boundary: `../component_cards/n8n-execution-persistence.yaml`
- Credential-aware node interface: `../component_cards/n8n-credential-node-interface.yaml`

### Apache Airflow
- DAG definition and task dependency contract: `../component_cards/airflow-dag-definition.yaml`
- Scheduler loop and run-state coordination: `../component_cards/airflow-scheduler-loop.yaml`
- Timetable and cron schedule contract: `../component_cards/airflow-timetable-contract.yaml`
- Asset-aware scheduling and lineage hooks: `../component_cards/airflow-asset-aware-scheduling.yaml`

### OpenMetadata
- Schema-first metadata entity model: `../component_cards/openmetadata-schema-first-entity-model.yaml`
- Lineage API and edge detail model: `../component_cards/openmetadata-lineage-resource.yaml`
- Governance taxonomy: domains, classifications, glossaries, contracts: `../component_cards/openmetadata-governance-taxonomy.yaml`
- Governed MCP/API activation interface: `../component_cards/openmetadata-mcp-context-interface.yaml`
