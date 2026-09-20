---
type: Reference
status: draft
---

# Architecture

Template: populate from actual code and accepted requirements. Read this page when an area is unfamiliar or a change touches boundaries or invariants; otherwise start from the known implementation and related tests.

## Purpose and boundaries

Describe the actual responsibility and external boundaries in a few sentences; link the source of each non-obvious constraint.

## Components and flow

Describe only real components and critical data paths. Add relative links to their implementation and relevant tests. A short diagram is useful only when it reveals relationships more clearly than prose.

## Invariants

Record hard-to-discover behavior, safety boundaries and operating constraints. Distinguish intended requirements from observed implementation and unverified assumptions.

## Decisions

Link relevant [decision records](decisions/README.md); do not restate their rationale here.

Do not create a domains folder by default. If this page becomes too large to navigate, split actual domain knowledge into targeted pages and link them here.
