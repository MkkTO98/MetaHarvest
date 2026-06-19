# MetaHarvest taxonomy harvest: n8n taxonomy harvest

Boundary: static source inspection only. No external code was installed, imported, built, tested, or executed. This report is descriptive evidence only; it introduces no synthesis, recommendation, ranking, or target-project decision logic.

Analyzed commit: `31f718f8f8ad6575fd049a2bb10aa597049604b1`

## Evidence inspected
- `README.md`
- `packages/workflow/src/workflow.ts`
- `packages/workflow/src/interfaces.ts`
- `packages/cli/src/workflows/triggers/workflow-trigger-activator.ts`
- `packages/cli/src/executions/execution-persistence.ts`

## Categories added or strengthened
- workflow automation
- integration platform
- trigger/webhook automation
- credential-aware connectors

## Discovered concepts
- workflow graph
- integration node
- trigger registration
- webhook endpoint
- credential boundary
- execution snapshot

## Discovered methodologies
- static inspection of workflow graph model
- component decomposition by runtime boundary
- separation of desired workflow publication state from actual trigger registration

## Discovered patterns
- declarative node-and-connection workflow graph
- desired-vs-actual trigger reconciliation
- execution evidence stored outside workflow definition
- credential references separated from workflow graph

## Discovered interfaces
- node type interface
- credential access interface
- webhook registration surface
- execution persistence store

## Component cards produced
- `MetaHarvest/component_cards/n8n-workflow-graph.yaml`
- `MetaHarvest/component_cards/n8n-trigger-webhook-registration.yaml`
- `MetaHarvest/component_cards/n8n-execution-persistence.yaml`
- `MetaHarvest/component_cards/n8n-credential-node-interface.yaml`

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
