import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.state_machine import WorkflowStateMachine

def test_transition():
    sm = WorkflowStateMachine("TEST-001")
    sm.transition_to("VALIDATING")
    assert sm.current_state == "VALIDATING"
    print("Workflow Test Passed: Transition successful.")

if __name__ == "__main__":
    test_transition()