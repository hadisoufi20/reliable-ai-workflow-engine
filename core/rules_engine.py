# core/rules_engine.py

class RulesEngine:
    """
    Determines the risk level of an invoice based on business rules.
    """
    
    @staticmethod
    def analyze_risk(invoice: dict) -> str:
        """
        Analyzes the invoice amount to determine risk.
        Logic: Amounts over 10,000 are considered HIGH_RISK.
        """
        amount = invoice.get("amount", 0)
        
        if amount > 10000:
            return "HIGH_RISK"
        return "LOW_RISK"