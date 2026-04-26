import pytest

def validate_withdrawal(account):
    errors = set()

    if account["status"] != "active":
        errors.add("inactive")

    if account["balance"] <= account["amount"]:
        errors.add("balance is less than amount")

    if account["amount"] <= 0:
        errors.add("amount is negative")

    if account["amount"] > 1000:
        errors.add("amount is greater than 1000")
    return len(errors) == 0

@pytest.mark.parametrize(
    "input_data, expected",
    [
        ({"status": "active", "balance": 5000, "amount": 300}, True),
        ({"status": "inactive", "balance": 5000, "amount": 300}, False),
        ({"status": "active", "balance": 100, "amount": 300}, False),
        ({"status": "active", "balance": 5000, "amount": 0}, False),
        ({"status": "active", "balance": 5000, "amount": -100}, False),
        ({"status": "active", "balance": 5000, "amount": 1002}, False),
    ],
    ids=[
        "valid_withdrawal",
        "inactive_account",
        "insufficient_balance",
        "zero_amount",
        "negative_amount",
        "exceeds_limit",
    ]
)
def test_withdrawal(input_data, expected):
    assert validate_withdrawal(input_data) == expected