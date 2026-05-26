# core/validator.py

def validate_invoice(invoice: dict) -> dict:
    """
    Validates the structural integrity of the invoice.
    Returns a dictionary with validation status and error list.
    """
    errors = []
    
    if not invoice.get("invoice_id"):
        errors.append("MISSING_INVOICE_ID")
    if not invoice.get("vendor"):
        errors.append("MISSING_VENDOR")
    if not invoice.get("currency"):
        errors.append("MISSING_CURRENCY")
    
    amount = invoice.get("amount")
    if amount is None or not isinstance(amount, (int, float)) or amount <= 0:
        errors.append("INVALID_AMOUNT")
        
    return {
        "valid": len(errors) == 0,
        "errors": errors
    }