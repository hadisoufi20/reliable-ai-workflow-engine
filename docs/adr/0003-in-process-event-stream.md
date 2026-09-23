# ADR-0003: In-process event stream instead of an external message broker

- **Status:** accepted

## Context

Observability is required, but the system must run from a clean checkout with no infrastructure.

## Decision

Implement a class-level queue with a background consumer thread (`observability/event_stream.py`).
Producers call `emit()`; the consumer currently prints and is the single place where an external sink would
be attached.

## Consequences

- No broker, no credentials, no connection handling to test.
- Events are processed off the decision path, so logging cannot delay or block a transition.
- Durability is not provided: an event is lost if the process dies before the consumer drains it.

## Alternatives considered

- **Kafka / RabbitMQ** — rejected: operational weight disproportionate to the requirement at this stage.
- **Synchronous logging on the decision path** — rejected: couples decision latency to a sink that may be slow or unavailable.
