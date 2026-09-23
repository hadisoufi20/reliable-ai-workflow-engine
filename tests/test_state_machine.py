"""Tests for the invoice workflow state machine.

The state machine is the boundary that keeps an invoice on a defined path, so
both the permitted path and the refused transitions are asserted here.
"""
import os
import sys

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.state_machine import InvalidTransition, WorkflowStateMachine  # noqa: E402


def test_starts_in_received():
    assert WorkflowStateMachine("INV-1").get_state() == "RECEIVED"


def test_happy_path_reaches_approved():
    machine = WorkflowStateMachine("INV-2")
    machine.transition_to("VALIDATING")
    machine.transition_to("RISK_ANALYSIS")
    machine.transition_to("APPROVED")
    assert machine.get_state() == "APPROVED"


def test_validation_failure_path_reaches_escalated():
    machine = WorkflowStateMachine("INV-3")
    machine.transition_to("VALIDATING")
    machine.transition_to("ESCALATED")
    assert machine.get_state() == "ESCALATED"


def test_high_risk_path_reaches_escalated():
    machine = WorkflowStateMachine("INV-4")
    machine.transition_to("VALIDATING")
    machine.transition_to("RISK_ANALYSIS")
    machine.transition_to("ESCALATED")
    assert machine.get_state() == "ESCALATED"


@pytest.mark.parametrize("sequence,illegal", [
    (["RISK_ANALYSIS"], "RISK_ANALYSIS"),          # cannot skip validation
    (["VALIDATING", "APPROVED"], "APPROVED"),      # cannot approve before risk analysis
    (["VALIDATING", "RISK_ANALYSIS", "APPROVED", "ESCALATED"], "ESCALATED"),  # terminal state
    (["VALIDATING", "ESCALATED", "APPROVED"], "APPROVED"),                    # terminal state
])
def test_illegal_transitions_are_refused(sequence, illegal):
    machine = WorkflowStateMachine("INV-5")
    for step in sequence[:-1]:
        machine.transition_to(step)
    with pytest.raises(InvalidTransition):
        machine.transition_to(illegal)


def test_state_is_unchanged_after_a_refused_transition():
    machine = WorkflowStateMachine("INV-6")
    machine.transition_to("VALIDATING")
    with pytest.raises(InvalidTransition):
        machine.transition_to("APPROVED")
    assert machine.get_state() == "VALIDATING"
