# Decision: Change Discoverability Boundary

Date: 2026-06-18
Status: Accepted

## Decision

MetaHarvest is responsible for discoverability of change.

Projects are responsible for evaluation of change.

## Doctrine

MetaHarvest owns publication of project-neutral change information:

- new artifacts;
- modified artifacts;
- retired artifacts;
- superseded artifacts;
- staleness information.

MetaHarvest does not own:

- project-specific relevance determination;
- project-specific recommendations;
- project prioritization;
- project governance;
- adoption decisions;
- implementation decisions;
- automatic project modification;
- automatic task creation.

Consuming projects own:

- relevance evaluation;
- adoption;
- rejection;
- implementation;
- local prioritization.

## Rationale

The EIP ecosystem needs a durable way for autonomous projects to answer, "What changed in MetaHarvest since I last looked?" without turning MetaHarvest into a controller, recommendation engine, project-ranking system, or governance authority.

Change discoverability prevents stale consumer context. Evaluation remains local because only the consuming project can judge its current goals, constraints, risk tolerance, priorities, governance gates, and implementation timing.

## Implementation boundary

The smallest acceptable capability is a file-backed, deterministic, project-neutral change-discovery index plus a read-only listing tool.

The capability must not emit:

- affected project lists;
- project recommendations;
- project-specific advice;
- adoption suggestions;
- automated review generation;
- project-specific relevance scoring.

Future agents should not drift toward recommendation engines, ecosystem coordinators, project-ranking systems, automatic propagation systems, automatic project modification, or EII-style functionality inside MetaHarvest.
