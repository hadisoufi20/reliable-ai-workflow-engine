# ADR-0004: Standard library only (no runtime dependencies)

- **Status:** accepted

## Context

The system is meant to be reviewable by someone who has to trust its decisions. Every third-party package
is a supply-chain surface and a reviewer's question.

## Decision

Use only the Python standard library at runtime. `requirements.txt` states this explicitly.
`pytest` is a test-time dependency only.

## Consequences

- A clean checkout runs with no network access and no install step.
- The dependency audit for diligence purposes reduces to "there are none".
- Some conveniences (schema validation libraries, structured logging) are implemented by hand or deferred.

## Alternatives considered

- **Add pydantic for schema validation** — rejected for now: the validation surface is four fields.
- **Add a structured logging library** — rejected: one-line audit records do not need it.
