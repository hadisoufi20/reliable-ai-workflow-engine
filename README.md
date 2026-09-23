# reliable-ai-workflow-engine

[![tests](https://github.com/hadisoufi20/reliable-ai-workflow-engine/actions/workflows/tests.yml/badge.svg)](https://github.com/hadisoufi20/reliable-ai-workflow-engine/actions/workflows/tests.yml)

Inspired by deterministic system design principles explored in the NEXUS architecture research.

## Technical Philosophy
In enterprise-grade automation, non-determinism is a liability. This system follows a **"Deterministic-First"** architecture: core business logic and state transitions are strictly rule-based, while AI agents are confined to non-critical advisory roles. This ensures 100% auditability and system predictability in high-risk environments.

## Problem Statement
AI systems in enterprise environments often fail due to non-deterministic behavior in high-risk workflows. Traditional black-box AI approaches lack the audit trails required for compliance and risk management.

## System Objective
To build a reliable, rule-based autonomous workflow system that ensures auditability and bounded autonomy.

## Architecture Overview
- **Core Engine:** Deterministic rule-based validation and risk assessment.
- **State Machine:** Explicit lifecycle management (RECEIVED -> VALIDATING -> RISK_ANALYSIS -> APPROVED/ESCALATED).
- **Observability:** Asynchronous event stream implementation for real-time monitoring and logging.
- **Agentic Layer:** Modular escalation handling designed for human-in-the-loop interventions.

## Demo Scenarios
- `clean`: Automated approval based on predefined risk thresholds.
- `suspicious`: Escalation to Agentic review due to risk violations.
- `bad`: Rejection and error reporting due to structural validation failures.

## Design Tradeoffs
- **Determinism vs. Flexibility:** Prioritizes predictability over LLM-driven unpredictability.
- **Observability vs. Overhead:** Employs a lightweight asynchronous event stream, avoiding the complexity of external message brokers while maintaining log integrity.
## Architecture and decisions

- [`architecture.md`](architecture.md) — component and lifecycle views, decision rules, failure behaviour, known limitations.
- [`docs/adr/`](docs/adr/) — architecture decision records (deterministic core, enforced transitions, event stream, dependency policy, validation order).

## Quick Start

No third-party dependencies — the standard library only.

```bash
git clone https://github.com/hadisoufi20/reliable-ai-workflow-engine.git
cd reliable-ai-workflow-engine

# run all three simulation scenarios (clean / suspicious / bad)
python3 main.py

# run the tests (no extra install needed)
python3 tests/test_workflow.py && python3 tests/test_validator.py

# or, if pytest is installed:
pytest tests/
```

Verified behaviour of `python3 main.py`: the clean invoice is auto-approved, the suspicious one is escalated
with an agent recommendation, and the malformed one is rejected with explicit validation errors.

## Repository Layout

```
core/           deterministic rules engine, state machine, validator
agents/         agentic escalation layer (bounded, advisory)
observability/  asynchronous event stream + audit logger
simulation/     sample invoices: clean, suspicious, bad
tests/          state-machine and workflow tests
```

## Related

- **Architecture overview:** [hadisoufi20.github.io](https://hadisoufi20.github.io/)
- **Research — four SSRN working papers on agentic trading systems:** [ssrn.com/author=13197688](https://ssrn.com/author=13197688)
- **ORCID:** [0009-0009-4656-5983](https://orcid.org/0009-0009-4656-5983)
- **Author:** Hadi Soufi — AI systems architect, Founder of ZVAKTHOR

## License

Proprietary - all rights reserved. See [LICENSE](LICENSE). The code is published for review and
demonstration; no reuse licence is granted.
