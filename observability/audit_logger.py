# observability/audit_logger.py
from datetime import datetime
from observability.event_stream import EventStream

class AuditLogger:
    """
    Logs workflow transitions and sends events to the asynchronous stream.
    """
    
    @staticmethod
    def log(invoice_id, from_state, to_state, decision, reason):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] ID: {invoice_id} | Transition: {from_state} -> {to_state} | Decision: {decision} | Reason: {reason}"
        
        # 1. Print to console for real-time visibility
        print(f"[AUDIT] {log_message}")
        
        # 2. Emit to Event Stream for asynchronous processing
        EventStream.emit("WORKFLOW_STATE_CHANGE", {
            "invoice_id": invoice_id,
            "from_state": from_state,
            "to_state": to_state,
            "decision": decision,
            "reason": reason,
            "timestamp": timestamp
        })
        
        # 3. Persistent log (Optional: could be a file append)
        with open("workflow.log", "a") as f:
            f.write(log_message + "\n")