# Architecture Overview
- Core: Deterministic engines for rules and validation.
- State Machine: Explicit transitions (RECEIVED -> VALIDATING -> RISK_ANALYSIS -> APPROVED/ESCALATED).
- Observability: Asynchronous event streaming via `event_stream.py`.
- Agents: Rule-based escalation handling (not LLM-dependent).