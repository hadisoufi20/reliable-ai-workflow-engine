# main.py
"""
Main entry point for the Reliable AI Workflow Engine.
Orchestrates the invoice validation and risk assessment workflow.
Integrates InvoiceAgent and asynchronous EventStream for observability.
"""

import sys
import os
import json

# Ensure the root directory is in the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.validator import validate_invoice
from core.rules_engine import RulesEngine
from core.state_machine import WorkflowStateMachine
from observability.audit_logger import AuditLogger
from observability.event_stream import EventStream
from agents.invoice_agent import InvoiceAgent

def run_workflow(invoice: dict):
    """
    Executes the deterministic invoice processing workflow with Agentic support.
    """
    invoice_id = invoice.get("invoice_id", "UNKNOWN")
    workflow = WorkflowStateMachine(invoice_id)
    agent = InvoiceAgent(agent_name="Analysis-Agent-01")
    
    # 1. Validation Phase
    workflow.transition_to("VALIDATING")
    validation_result = validate_invoice(invoice)
    
    if not validation_result["valid"]:
        workflow.transition_to("ESCALATED")
        reason = f"Validation Errors: {', '.join(validation_result['errors'])}"
        AuditLogger.log(invoice_id, "VALIDATING", "ESCALATED", "REJECTED", reason)
        
        # Agentic Intervention
        recommendation = agent.analyze_escalation(invoice, reason)
        print(f"[AGENT RECOMMENDATION] {recommendation}")
        return

    # 2. Risk Analysis Phase
    workflow.transition_to("RISK_ANALYSIS")
    risk_level = RulesEngine.analyze_risk(invoice)
    
    if risk_level == "HIGH_RISK":
        workflow.transition_to("ESCALATED")
        reason = "Risk threshold exceeded"
        AuditLogger.log(invoice_id, "RISK_ANALYSIS", "ESCALATED", "MANUAL_REVIEW", reason)
        
        # Agentic Intervention
        recommendation = agent.analyze_escalation(invoice, reason)
        print(f"[AGENT RECOMMENDATION] {recommendation}")
    else:
        workflow.transition_to("APPROVED")
        AuditLogger.log(invoice_id, "RISK_ANALYSIS", "APPROVED", "AUTO_APPROVED", "Risk level acceptable")

if __name__ == "__main__":
    # Start the background event consumer
    EventStream.start_consumer()
    
    test_files = [
        "simulation/clean_invoice.json",
        "simulation/suspicious_invoice.json",
        "simulation/bad_invoice.json"
    ]
    
    for file_path in test_files:
        print(f"\n--- Processing: {file_path} ---")
        try:
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    invoice_data = json.load(f)
                    run_workflow(invoice_data)
            else:
                print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            
    print("\n[WORKFLOW COMPLETE]")