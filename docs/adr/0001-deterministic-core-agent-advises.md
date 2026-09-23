# ADR-0001: The rules engine decides; the agent only advises

- **Status:** accepted

## Context

In an approval workflow, a wrong decision creates a financial and compliance obligation that must be
explainable after the fact. Language models produce different answers for identical inputs and cannot
guarantee the same outcome twice.

## Decision

All decisions (validity, risk class, final state) are made by deterministic Python. The agent layer receives
the decision plus its reason and returns advisory text for a human reviewer. It has no write path to the
workflow state.

## Consequences

- The same invoice always produces the same decision, which is what makes the audit trail meaningful.
- The decision logic is unit-testable without a model.
- A model can be added later without giving it authority.

## Alternatives considered

- **Model decides, code logs** — rejected: unauditable and non-reproducible.
- **Model proposes, human approves, no code rules** — rejected: removes the deterministic baseline that makes exceptions visible.
