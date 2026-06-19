# MetaHarvest taxonomy harvest: Apache Airflow taxonomy harvest

Boundary: static source inspection only. No external code was installed, imported, built, tested, or executed. This report is descriptive evidence only; it introduces no synthesis, recommendation, ranking, or target-project decision logic.

Analyzed commit: `9c4908019a3f8d386eaed56c0552adfde241e952`

## Evidence inspected
- `README.md`
- `task-sdk/src/airflow/sdk/definitions/dag.py`
- `task-sdk/src/airflow/sdk/definitions/timetables/_cron.py`
- `task-sdk/src/airflow/sdk/definitions/asset/__init__.py`
- `airflow-core/src/airflow/jobs/scheduler_job_runner.py`

## Categories added or strengthened
- workflow orchestration
- scheduling system
- executor boundary
- asset-aware orchestration

## Discovered concepts
- DAG
- task dependency
- DagRun
- TaskInstance
- timetable
- asset event
- executor boundary

## Discovered methodologies
- static inspection of definition layer and scheduler layer separately
- schedule/timetable contract extraction
- asset-aware scheduling vocabulary extraction

## Discovered patterns
- workflow as code DAG
- validated timetable contract
- bounded scheduler loop
- asset-event scheduling

## Discovered interfaces
- DAG authoring API
- timetable interface
- scheduler/executor boundary
- asset URI normalization interface

## Component cards produced
- `MetaHarvest/component_cards/airflow-dag-definition.yaml`
- `MetaHarvest/component_cards/airflow-scheduler-loop.yaml`
- `MetaHarvest/component_cards/airflow-timetable-contract.yaml`
- `MetaHarvest/component_cards/airflow-asset-aware-scheduling.yaml`

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
