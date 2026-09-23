# ADR-0002: Enforce the lifecycle with an explicit transition allow-list

- **Status:** accepted
- **Supersedes:** "set the state and log it" behaviour

## Context

The state machine originally assigned `current_state` directly. The class documented deterministic
transitions, but nothing prevented an invoice from jumping from `RECEIVED` straight to `APPROVED`, or
leaving a terminal state. Documentation claimed a guarantee the code did not provide.

## Decision

Declare `ALLOWED_TRANSITIONS` explicitly and raise `InvalidTransition` for anything outside it. A refused
transition must leave the state unchanged.

## Consequences

- The documented lifecycle is the enforced lifecycle; the claim and the code now match.
- Paths such as *approve before risk analysis* and *reopen an escalated invoice* fail loudly instead of being recorded.
- New states must be added to the allow-list deliberately.

## Alternatives considered

- **Documentation only** — rejected: the guarantee would remain unverified and untestable.
- **Warn on illegal transitions** — rejected: a warning in an approval path is not a control.
