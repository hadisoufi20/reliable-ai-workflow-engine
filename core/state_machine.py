# core/state_machine.py

class WorkflowStateMachine:
    """
    Manages the lifecycle of an invoice processing workflow.
    Ensures deterministic transitions between states.
    """
    
    def __init__(self, invoice_id):
        self.invoice_id = invoice_id
        self.current_state = "RECEIVED"
        self._log_transition(None, "RECEIVED")

    def transition_to(self, new_state):
        old_state = self.current_state
        self.current_state = new_state
        self._log_transition(old_state, new_state)

    def _log_transition(self, old, new):
        # This will be connected to audit_logger later
        print(f"[AUDIT] Invoice {self.invoice_id}: {old} -> {new}")

    def get_state(self):
        return self.current_state