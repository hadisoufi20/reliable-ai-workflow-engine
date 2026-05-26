import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.validator import validate_invoice

def test_validator():
    bad_inv = {"invoice_id": "", "vendor": None, "amount": -500}
    result = validate_invoice(bad_inv)
    assert result["valid"] == False
    print("Validator Test Passed: Detected invalid invoice.")

if __name__ == "__main__":
    test_validator()