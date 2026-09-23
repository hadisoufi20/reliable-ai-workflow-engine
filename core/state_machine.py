# core/state_machine.py


class InvalidTransition(Exception):
    """Raised when a transition is not permitted by the workflow definition."""


class WorkflowStateMachine:
    """
    Manages the lifecycle of an invoice processing workflow.

    Every transition is checked against ALLOWED_TRANSITIONS, so an invoice can
    never reach a state the workflow does not define a path to.
    """

    RECEIVED = "RECEIVED"
    VALIDATING = "VALIDATING"
    RISK_ANALYSIS = "RISK_ANALYSIS"
    APPROVED = "APPROVED"
    ESCALATED = "ESCALATED"

    ALLOWED_TRANSITIONS = {
        RECEIVED: {VALIDATING},
        VALIDATING: {RISK_ANALYSIS, ESCALATED},
        RISK_ANALYSIS: {APPROVED, ESCALATED},
        APPROVED: set(),
        ESCALATED: set(),
    }

    def __init__(self, invoice_id):
        self.invoice_id = invoice_id
        self.current_state = self.RECEIVED
        self._log_transition(None, self.RECEIVED)

    def transition_to(self, new_state):
        allowed = self.ALLOWED_TRANSITIONS.get(self.current_state, set())
        if new_state not in allowed:
            raise InvalidTransition(
                "invoice %s: %s -> %s is not an allowed transition (allowed: %s)"
                % (self.invoice_id, self.current_state, new_state, sorted(allowed) or "none")
            )
        old_state = self.current_state
        self.current_state = new_state
        self._log_transition(old_state, new_state)
        return self.current_state

    def _log_transition(self, old, new):
        print(f"[AUDIT] Invoice {self.invoice_id}: {old} -> {new}")

    def get_state(self):
        return self.current_state
