# OpenHands ArchitectureHarvest Deep Analysis

Analysis date: 2026-06-06
Analyzed commit: 03aab93625079c24d6f43655c9506931cf43bc17
Repository: https://github.com/All-Hands-AI/OpenHands
Local clone: /home/mkkto/srv/projectforge/external_sources/openhands
Execution boundary: static inspection only; no external repository code was installed, imported, built, or executed.

## Scope focus

This cycle inspected OpenHands for agent orchestration, agent state management, checkpointing/resume analogs, execution loops, tool permission systems, approval workflows, context management, failure recovery, and task lifecycle management.

## Evidence inspected

- README.md lines 32-83: OpenHands separates Software Agent SDK, CLI, Local GUI, Cloud, and Enterprise; license is MIT outside enterprise/.
- LICENSE lines 1-3: enterprise/ has separate terms; content outside enterprise/ is MIT.
- openhands/app_server/app_conversation/app_conversation_service.py: abstract conversation lifecycle service with start status progression WORKING -> WAITING_FOR_SANDBOX -> PREPARING_REPOSITORY -> RUNNING_SETUP_SCRIPT -> SETTING_UP_GIT_HOOKS -> SETTING_UP_SKILLS -> STARTING_CONVERSATION -> READY/ERROR; export_conversation writes events and metadata to a zip.
- openhands/app_server/event/event_service.py: event get/search/count/save abstraction.
- openhands/app_server/pending_messages/pending_message_service.py: SQL pending message queue, ordered by created_at, including old-conversation-id to real-conversation-id migration.
- openhands/app_server/sandbox/sandbox_service.py: sandbox start/resume/pause/delete boundary, RUNNING/ERROR polling, alive health check, timeout failure path, and oldest-sandbox pause cleanup.
- openhands/app_server/mcp/mcp_router.py: MCP/source-control tool proxy that binds provider tokens, user id, conversation id, and PR metadata.

## Findings

1. OpenHands product architecture treats agent work as a conversation running inside a sandbox, not as a single tool call. This is useful evidence for ProjectForge when future workflows need runtime readiness, delayed messages, and explicit lifecycle status.
2. Its strongest transferable pattern is not the full app runtime; it is the combination of lifecycle task status, event retrieval, pending input queue, sandbox readiness gate, and credential-scoped tool proxy.
3. Its failure recovery stance is operational: wait for alive runtime, detect ERROR, timeout if readiness never arrives, export event trajectories, and preserve pending messages during identity transitions.
4. Its permission/tooling evidence is product-integrated: MCP tools receive request context and provider tokens. ProjectForge should borrow scoped metadata and explicit side-effect records, not import OpenHands tool proxy architecture wholesale.
5. Checkpointing is less directly visible in this approved repository than in LangGraph. OpenHands offers event/conversation/sandbox lifecycle evidence; its README points core agentic SDK code to a separate repository that was not cloned in this cycle.

## ProjectForge fit

High for future orchestration design and permission-system design, moderate for current file-backed governance. ProjectForge should adapt small patterns: task lifecycle status enum, pending input record for async workers, sandbox/readiness gate for risky side effects, and tool metadata records. Do not implement these recommendations in this task.
