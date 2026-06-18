# Aider ArchitectureHarvest deep analysis

Date: 2026-06-06
Source: https://github.com/Aider-AI/aider
Commit: 5dc9490bb35f9729ef2c95d00a19ccd30c26339c
License observed: Apache-2.0 (`LICENSE.txt`)
Boundary: static source inspection only. No external code was installed, imported, built, tested, or executed.

## Focused evidence inspected

- `aider/repo.py`: git repository discovery, path normalization, ignore handling, dirty-file detection, diffs, commit generation, attribution, and tracked file listing.
- `aider/repomap.py`: tag extraction/cache and ranked repository map generation.
- `aider/coders/base_coder.py`: editable/read-only file context assembly, repo map fallback, chat history summarization, token checks, interruption handling, auto lint/test fields, commit/undo state.
- `aider/commands.py`: `/add`, `/drop`, chat modes including `ask`, `code`, `architect`, and `context`; user confirmation for file creation and editable/read-only promotion.
- `aider/models.py`: model-specific edit format, repo map, editor model, and weak model settings.

## Repository workflow

Aider is strongly git-anchored. `GitRepo` locates a single repository, rejects multi-repo file sets, normalizes paths, consults git/aiderignore, detects dirty files, computes diffs, and creates commits with explicit AI attribution options. This is high-confidence evidence for treating git diff/commit state as a durable coding-agent boundary.

ProjectForge fit: strong as pattern evidence. Do not import Aider's autocommit behavior into ProjectForge without a separate approval decision.

## Code modification workflow

Aider keeps editable files explicit in `abs_fnames`, separates read-only files, and exposes `/add` and `/drop` controls. It refuses or warns on ignored/out-of-root files and prompts before creating missing files. Modification evidence is represented through diffs, lint/test outcomes, edited-file tracking, and optional commits.

ProjectForge fit: reinforces explicit file scope and final diff/test evidence.

## Planning/execution separation

Aider exposes `ask`, `code`, `architect`, and `context` modes and can switch coder configurations. When edit format changes, incompatible previous assistant messages are summarized to avoid mode contamination. This is strong evidence for separating planning artifacts from execution artifacts rather than blending them in raw conversation history.

## Human oversight

The workflow is interactive by default: users choose files, confirm missing-file creation, decide whether to continue past context limits, and can control commits/tests/lints through configuration. However, autocommit flags and shell-command suggestions can be too permissive for ProjectForge unless constrained by ProjectForge dry-run/approval policy.

## Context management

Aider combines full editable files, read-only references, ranked repo map, mentioned filenames/identifiers, and chat-history summarization. This reinforces ProjectForge's summary-first context policy but suggests a simplification opportunity: ProjectForge should prefer explicit folder summaries/context bundles plus selected files over hidden dynamic repo-wide loading.

## Recovery after interruption

Recovery is git-anchored: commit hashes, diffs, edited-file sets, and undo mechanics provide durable handles. Chat history summarization preserves continuity when context grows. This reinforces ProjectForge's checkpoint/current-state direction but does not justify copying Aider's chat-session model.

## Simplification opportunities

- Prefer explicit editable-file scope and compact repo/context summaries over whole-repo context.
- Use git diff/patch/commit handles as the recovery substrate for code changes.
- Keep planning/execution separation as a lightweight mode/artifact boundary, not a new runtime.

## Deletion opportunities

- Delete or retire any ProjectForge candidate that would add automatic commit/publish behavior without explicit gates.
- Avoid retaining recommendations that require full Aider dependency adoption when pattern extraction is sufficient.

## Confidence

High for repository workflow, code modification workflow, context selection, and planning/execution separation. Medium for broader recovery lifecycle because behavior was inspected statically only.
