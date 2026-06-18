# SWE-agent ArchitectureHarvest deep analysis

Date: 2026-06-06
Source: https://github.com/SWE-agent/SWE-agent
Commit: 10e3e76e629ad47331af562f367b9df6501cc55c
License observed: MIT (`LICENSE`)
Boundary: static source inspection only. No external code was installed, imported, built, tested, or executed.

## Focused evidence inspected

- `sweagent/run/run_single.py`: run configuration, output directory, hooks, environment start/close, predictions.
- `sweagent/agent/agents.py`: main agent loop, retry agent, trajectory persistence, setup, model query/action handling, autosubmission after errors.
- `sweagent/environment/swe_env.py`: deployment/session startup, repository copy/reset, command execution, timeout interruption, environment close.
- `sweagent/agent/history_processors.py`: history elision and cache-control-aware context processors.
- `sweagent/agent/reviewer.py`: retry loop, reviewer, chooser, preselector, score/acceptance mechanics.
- `tools/submit/bin/submit`: patch submission boundary.
- `sweagent/run/hooks/apply_patch.py` and `open_pr.py`: patch saving/local application and optional draft PR creation.

## Repository workflow

SWE-agent treats repository setup as part of the environment boundary. `SWEEnv` starts a deployment, copies a repository into it, resets to a base commit, and can hard-reset between attempts. This is stronger than Aider for repeatable evaluation, but heavier than ProjectForge should adopt by default.

## Code modification workflow

The model changes code through actions in the environment. Final output becomes `/root/model.patch`, saved by a submission command and optionally saved/applied locally by a hook. Optional draft PR creation is gated by configuration and multiple checks. This strongly reinforces patch-as-submission and publication-as-separate-step.

## Planning/execution separation

SWE-agent separates problem statement, templates, environment, tools, model, agent, run hooks, and output trajectory. Planning is encoded in templates/problem statements rather than interactive architect mode. This supports ProjectForge's file-backed task artifacts and explicit task definitions.

## Task completion lifecycle

`RunSingle` starts the environment, runs the agent, invokes hooks, saves predictions, and closes the environment. The agent saves trajectory data repeatedly. Retry agents can run multiple attempts, submit to reviewer/chooser logic, select the best attempt, and persist aggregate stats.

## Human oversight

SWE-agent includes human model variants and a reviewer loop, but its default architecture is more autonomous and benchmark-oriented than ProjectForge. Open PR behavior creates draft PRs and instructs humans to review carefully, but ProjectForge should preserve its stronger dry-run/human-approval gates.

## Context management

History processors elide older observations while preserving trajectory evidence. This mirrors ProjectForge's separation between compact active context and raw evidence artifacts. The key pattern is not the exact processor, but the split between prompt history, trajectory evidence, and final patch.

## Recovery after interruption

SWE-agent persists `.traj` files during execution, includes replay configuration, and can autosubmit a patch after certain failures. This is strong evidence for trajectory/checkpoint artifacts, but autosubmission is contradictory to ProjectForge if it bypasses approval.

## Simplification opportunities

- For ProjectForge, extract patch-as-submission and trajectory-as-evidence without adopting the full environment/retry framework.
- Use environment reset boundaries only for tasks that truly need isolated reproducible execution.
- Keep reviewer/retry loops reserved for high-value or benchmark-like tasks.

## Deletion opportunities

- Delete/retire recommendations that imply benchmark-agent autonomy for ordinary ProjectForge work.
- Avoid implementing automatic PR creation or autosubmission without a new explicit approval design.

## Confidence

High for task lifecycle, patch submission, trajectory persistence, retry/reviewer loop, and environment reset patterns. Medium for human oversight fit because ProjectForge's governance assumptions are stricter than SWE-agent's benchmark assumptions.
