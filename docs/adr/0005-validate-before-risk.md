# ADR-0005: Validate structure before assessing risk

- **Status:** accepted

## Context

Risk classification depends on the invoice amount. A missing or malformed amount would make any risk
judgement meaningless, and a partially readable invoice could still be scored by accident.

## Decision

Run structural validation first. If it fails, transition to `ESCALATED` and stop; risk analysis is never
reached for a malformed invoice.

## Consequences

- A risk score always corresponds to a structurally complete invoice.
- The escalation reason distinguishes "could not read it" from "read it, it is high risk".
- Validation errors are reported as a list, so a reviewer sees every problem at once.

## Alternatives considered

- **Risk first, validate later** — rejected: produces scores for invoices that are not readable.
- **Default missing amounts to zero and continue** — rejected: silently turns a data error into a low-risk classification.
