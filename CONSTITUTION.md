# MetaHarvest Constitution

MetaHarvest is an active sibling EIP project and advisory system for reusable non-domain knowledge. It is historically descended from ArchitectureHarvest, whose name remains valid only for historical provenance and compatibility paths.

MetaHarvest extracts reusable non-domain evidence and recommendation-grade judgment from projects, systems, architectures, implementations, successes, failures, concepts, methodologies, interfaces, governance structures, decision patterns, and heuristics. It does not collect projects or knowledge for their own sake. Every harvested source must be decomposed into reusable lessons, mapped to the problems or failure modes those lessons address, evaluated against target constraints, and converted into compact Hermes-usable records plus evidence-backed recommendations for project-local judgment.

## Doctrine

1. MetaHarvest is a librarian, reference system, evidence repository, and advisory system, not a passive research folder, standard-setting authority, or project controller.
2. The default output is evidence-backed recommendation: adopt, adapt, reject, retire, simplify, replace, defer, preserve vocabulary, preserve methodology, preserve decision pattern, preserve governance pattern, or preserve heuristic. Strong recommendations are acceptable, but adoption remains project-local.
3. External projects and observed ecosystem projects are evidence sources. They do not become authority over ProjectForge or generated projects.
4. Project cards are not enough. Analysis must produce the layers needed for the problem: project, component, pattern, concept/vocabulary, methodology, decision, governance, heuristic, relevance, and recommendation layers where applicable.
5. Cross-project reusable knowledge is preferred over one-off enthusiasm. If multiple projects solve or name a similar problem, compare them in compact reusable records.
6. The most valuable recommendation is often deletion, simplification, non-adoption, or preservation of negative knowledge.
7. MetaHarvest may create recommendations and candidate task proposals, but it must not decide adoption, force migration, act as controller, create tasks inside ProjectForge, MacroForge, or any target project, or directly modify those projects from research findings.
8. MetaHarvest is responsible for discoverability of change. Projects are responsible for evaluation of change. MetaHarvest may publish new, modified, retired, superseded, and stale artifact records so consumers can answer "What changed in MetaHarvest since I last looked?" without MetaHarvest deciding whether the change matters to any specific project.
9. MetaHarvest does not own project-specific relevance determination, project-specific recommendations, project prioritization, project governance, adoption decisions, implementation decisions, automatic task creation, automatic project modification, or automatic propagation workflows. Consuming projects own relevance evaluation, adoption, rejection, implementation, and local prioritization.
10. MetaHarvest remains non-domain. Domain conclusions such as GDP analysis, inflation analysis, energy-market conclusions, investment theses, company research, and macroeconomic findings belong to domain projects, not MetaHarvest. MetaHarvest may preserve reusable non-domain methods discovered while working on those projects.

## Hard constraints for v1

MetaHarvest v1 is local-first, file-based only, no paid services, no mandatory cloud dependencies, solo-developer appropriate, Ubuntu/local-machine friendly, token-budget-aware, GitHub-compatible, and Hermes-compatible.

Allowed v1 storage formats:

- Markdown
- YAML
- generated JSON audits

Forbidden v1 systems:

- database
- vector store
- dashboard
- UI
- autonomous discovery daemon
- mandatory cloud model dependency
- external service dependency

## Repository safety policy

- Raw cloned third-party repositories, when materialized for source-level analysis, live outside the ProjectForge git-tracked source tree under the configured replaceable cache root `/home/mkkto/srv/EIP/projects/ProjectForge/external_sources/` by default. Normal MetaHarvest consultation must not require this cache to exist.
- Hermes may search for candidate open-source repositories.
- Hermes may propose repositories for approval.
- Hermes must ask before moving a repository from `candidate` to `approved`.
- Once approved, Hermes may clone, pull/update, inspect, and analyze that repository without asking each time.
- Hermes must not execute code from external repositories without separate approval.
- Hermes must not run install scripts, package scripts, Docker, external project commands, package managers, or networked build commands from cloned repositories without separate approval.
- Repository URL, license, approval date, local path, last cloned commit, last analyzed commit, latest seen commit, status, and staleness must be recorded in `source_registry.yaml`.

## Source states

- `candidate`: discovered, not approved.
- `approved`: may be cloned and analyzed.
- `rejected`: intentionally excluded.
- `cloned`: local copy exists.
- `analyzed`: project/context reports exist.
- `stale`: upstream changed since last analysis.
- `retired`: no longer actively useful, but retained for future reference.

## Required analysis layers

For each analyzed external project, produce:

1. Human summary: concise Markdown summary for the user.
2. Project card: compact YAML for Hermes.
3. Component cards: YAML cards decomposing the external project into components.
4. Deep report: Markdown report with evidence, tradeoffs, limitations, and recommendations.

Do not summarize an analyzed project as a monolith. Component cards must identify failure modes addressed, failure modes introduced, required assumptions, useful patterns, local constraint mismatches, minimum useful extraction, use/do-not-use conditions, recommendation, effort, risk, evidence files, and confidence.

## Knowledge-classification doctrine

MetaHarvest may explicitly preserve reusable non-domain knowledge categories such as:

- architecture patterns;
- interface patterns;
- shared concepts;
- shared vocabulary;
- shared methodologies;
- decision patterns;
- governance patterns;
- heuristics;
- anti-patterns and failure patterns.

These categories are retrieval and reasoning aids. They are not mandatory standards for consuming projects and do not require new storage systems or artifact types by default.

Shared concepts and vocabulary should preserve observed meaning, usage, context, and discovered commonality. MetaHarvest may recommend vocabulary alignment when it improves clarity, but it must not impose terminology.

Shared methodologies should preserve repeatable workflows, validation procedures, recommendation-evaluation processes, experimentation procedures, uncertainty-handling approaches, and decision-documentation approaches as advisory patterns.

Decision patterns such as accept, reject, defer, provisional acceptance, escalation, high-impact review routing, narrow adoption, supersession, and retirement belong in MetaHarvest when they are reusable beyond a single domain.

Governance patterns such as ownership-by-purpose, advisory-only ecosystems, project autonomy, extraction-before-expansion, interface-first separation, recommendation persistence, and descriptive registries may be harvested as advisory knowledge. They do not grant MetaHarvest governance authority.

Heuristics should remain contextual. Each durable heuristic should retain applicability conditions, failure modes, evidence, and confidence where meaningful.

## Pattern library rules

Create cross-project pattern files when multiple projects solve similar problems. Pattern files must compare competing approaches where possible and include minimum useful extraction plus do-not-use conditions.

Patterns should be named by problem class, not by source project. Example: `file_backed_context_cards.yaml`, not `openhands_memory.yaml`.

## Relevance maps

Keep external-project context separate from target-project relevance context.

- ProjectForge relevance maps are mandatory in v1.
- MacroForge relevance maps may be lightweight in v1, but obvious relevance must be recorded.
- Future ProjectForge-created projects may add their own relevance map folder without changing MetaHarvest structure.

## Adoption workflow

1. Analyze external project.
2. Extract project, component, and pattern cards.
3. Compare against ProjectForge and optionally MacroForge.
4. Produce an adoption, simplification, replacement, deletion, rejection, or task recommendation proposal.
5. Create an evidence-backed, decision-grade recommendation artifact.
6. Wait for the target project's normal approval, dry-run, test, and coherence gates before implementation.

MetaHarvest must not directly modify ProjectForge, MacroForge, or target-project code, templates, architecture, permissions, model routing, tasks, or scope from research findings. It may recommend; the target project evaluates locally and decides whether to open a task, adopt, reject, defer, or supersede the recommendation.

## Recommendation priority

When evaluating recommendations, prefer:

1. Reduce unnecessary ProjectForge complexity.
2. Replace weak homemade systems with proven simpler patterns.
3. Add missing capabilities.
4. Avoid ambitious new functionality unless justified by observed failure or strong evidence.

## Audit rules

Source audits answer:

- Has the external project changed?
- Has the license changed?
- Has the architecture changed?
- Are context cards stale?
- Are previous recommendations still valid?

Target-project consultation audits answer:

- Given the current target architecture, are there MetaHarvest patterns that could simplify or improve it?
- Are there known rejected or retired patterns that prevent repeated bad decisions?
- Are there adoption candidates now relevant because the target project evolved?

Consult MetaHarvest during major architecture changes, scheduled project review, repeated failure/debug cycles, before building a new subsystem, when Hermes detects homemade infrastructure overlapping known pattern categories, or when the user explicitly asks for an improvement scan. During new project creation, consult it when architectural uncertainty or relevant pattern evidence exists; do not force simple projects into unnecessary ceremony.

Do not consult MetaHarvest during small bug fixes, minor documentation edits, simple tests, or trivial one-file utilities.

## Update policy

Update MetaHarvest context when an external repo materially changes, a target project materially changes, a new pattern is extracted, a recommendation is accepted/rejected, an adoption attempt succeeds/fails, or a scheduled review marks analysis stale.

Do not silently overwrite old conclusions. If a material conclusion changes, create a new report/audit or append a dated adoption/audit record.

## Rejected and retired sources

Do not delete rejected or retired context. Keep records so Hermes does not rediscover the same unsuitable projects later. Each rejection record must state why rejected, when rejected, what was still useful, and what future condition could justify revisiting.

## License policy

Even for private use, record license information deeply enough to decide whether code or dependencies may later be reused.

Classify possible reuse as:

- `pattern_only`
- `dependency_use`
- `code_copy`
- `redistribution`

Flag license risk for each category. If license evidence is missing, mark confidence low and reuse as `pattern_only` until verified.

## Blindspot controls

1. Context pollution: use short YAML cards, strict tags, relevance scores, indexes, confidence scores, and staleness flags.
2. Pattern duplication: create cross-project pattern files for convergent solutions.
3. No feedback loop: record adoption outcomes when a pattern is accepted, rejected, implemented, succeeds, or fails.
4. False confidence: every report/card includes confidence, evidence quality, files inspected, and analysis limitations.
5. Stale summaries: track analyzed commit, latest seen commit, analysis date, and staleness status.
6. Overengineering: every pattern includes minimum useful extraction and do-not-use conditions.
7. Wrong-fit architecture: evaluate against solo developer, local-first, low/no cost, Ubuntu desktop, 32 GB RAM, Hermes-compatible, token-budget-aware, no mandatory cloud, maintainable-by-one constraints.
8. Meta-project creep: v1 remains file-based with no database, vector search, UI, dashboard, or automated autonomous discovery beyond candidate proposal.

## Negative rules

MetaHarvest may create negative rules for Hermes, including:

- do not build custom vector memory until grep/YAML retrieval demonstrably fails
- do not add multi-agent complexity unless a real task requires it
- do not adopt enterprise/cloud-first patterns without a local minimal extraction
- do not build safeguards against purely hypothetical failure modes

## Feedback loop and recommendation staleness

MetaHarvest learns from implementation outcomes through the conceptual Evolution Interface. When a target project adopts, rejects, modifies, removes, succeeds with, fails with, later reconsiders, or repeatedly rejects a pattern under similar conditions, the target project should record local outcome history under `architecture/architectureharvest/` or its current local equivalent. Broadly useful lessons may be mirrored into `MetaHarvest/adoption_log/` or future MetaHarvest-owned learning records.

The Evolution Interface does not transfer local governance history to MetaHarvest, does not require consumers to report every outcome, does not create automatic adoption or rejection propagation, and does not turn repeated success into authority. It exists to let reusable lessons, fit conditions, confidence, priority, anti-patterns, and revisit triggers evolve while preserving consumer ownership of local decisions.

Recommendation and relevance-map statuses are:

- `active`: currently relevant and not superseded.
- `stale`: evidence or assumptions may be outdated because the source or target changed.
- `superseded`: replaced by a newer recommendation or pattern.
- `retired`: retained for historical/negative knowledge but not actively recommended.

Recommendation persistence requirements:

- reviewed recommendations remain discoverable whether accepted, rejected, deferred, superseded, or retired;
- review outcome and implementation outcome remain separate;
- rejection rationale, adoption rationale, and supersession lineage must be preserved;
- adoption by one project does not imply adoption by another project;
- confidence and priority should use decimal values when meaningful, while low/medium/high labels remain acceptable for maturity dimensions where decimals would imply false precision.

MetaHarvest must not continuously scan projects during ordinary development. It is invoked at architectural decision points and scheduled reviews.

## Decision-support retrieval doctrine

MetaHarvest must be able to answer: given a problem, which patterns should ProjectForge or a target project consider, why, how strong is the evidence, what tradeoffs exist, and what has historically worked inside this ecosystem?

Consultation starts from problem-first retrieval, not project reports:

1. `retrieval/problem_catalog.yaml`
2. `retrieval/retrieval_index.yaml`
3. synthesized pattern records under `synthesis/` and cross-project pattern cards
4. contradiction records under `contradictions/`
5. outcome models and adoption outcomes
6. target relevance maps
7. project/component/deep reports only when compact records are insufficient

Every pattern must declare problems solved, related problems, and anti-problems. Every decision-grade recommendation must include evidence strength, local fit, recommendation strength, confidence, priority when meaningful, expected benefit, implementation cost estimate, architectural impact estimate, maintenance cost, minimum useful extraction, do-not-use conditions, limitations, lineage, and the reminder that adoption is decided by the target project.

## Pattern maturity model

Maturity scores are explainable labels, not opaque calculations. Required fields are:

- `evidence_strength`: low, medium, high
- `adoption_count`: integer
- `projects_observed`: list
- `confidence`: low, medium, high
- `maintenance_cost`: low, medium, high
- `local_fit`: poor, moderate, strong
- `recommendation_strength`: weak, moderate, strong

Recommendation strength must explain why the evidence, ProjectForge constraints, and ecosystem outcomes justify the label. Popularity in external projects is not enough if local fit is poor or maintenance cost is high.

## Contradictions and tradeoffs

When architectural approaches conflict, create records under `contradictions/`. A contradiction record must list competing approaches, assumptions, where each wins, where each loses, failure modes introduced, confidence, and guidance. MetaHarvest should capture tradeoffs rather than force a winner.

## Outcome weighting

Adoption outcomes influence future recommendations. Recommendations must distinguish generic recommendation strength from recommendation proven successful in the ProjectForge ecosystem. Repeated local success may increase recommendation strength when current constraints still match. Repeated local failure, excessive maintenance, or recurring complexity must reduce strength and may create rejection or retirement records.

## Lifecycle tracking

Patterns, problems, contradictions, relevance records, and outcome rollups track lifecycle metadata: `first_seen`, `last_reviewed`, `last_referenced`, `last_adoption`, `adoption_frequency`, and status (`active`, `dormant`, `stale`, `superseded`, `retired`). MetaHarvest identifies heavily reused, rarely used, forgotten, obsolete, and superseded patterns, but does not automatically delete them.

## Additional negative rules

MetaHarvest may never become a mandatory dependency for implementation work, override project governance, automatically refactor projects, create tasks or implementation work inside another project, or introduce databases, vector stores, dashboards, web UIs, agent swarms, autonomous GitHub crawling, or automatic repository discovery in this v1 decision-support layer.

