import pytest

def validate_login_response(response):
    if response["status_code"] != 200:
        return False
    body = response["body"]
    if "token" not in body or not body["token"]:
        return False
    if "user_id" not in body or body["user_id"] <=0:
        return False
    if body["role"] not in ["admin", "user"]:
        return False
    return True

@pytest.mark.parametrize(
    "response, expected",
    [
        ({"status_code": 200, "body": {"token": "abc123","user_id": 101, "role": "admin"}}, True),
        ({"status_code": 200, "body": {"token": "abc123","user_id": 101, "role": "user"}}, True),
        ({"status_code": 200, "body": {"user_id": 101, "role": "admin"}}, False),
        ({"status_code": 200, "body": {"token": "","user_id": 101, "role": "admin"}}, False),
        ({"status_code": 401, "body": {"token": "abc123","user_id": 101, "role": "admin"}}, False),
        ({"status_code": 200, "body": {"token": "abc123", "role": "admin"}}, False),
        ({"status_code": 200, "body": {"token": "abc123","user_id": -101, "role": "admin"}}, False),
        ({"status_code": 200, "body": {"token": "abc123","user_id": 101, "role": "guest"}}, False),
        ({"status_code": 404, "body": {"token": "abc123","user_id": -1, "role": "admin"}}, False),
    ],
    ids=[
        "Valid admin login",
        "Valid regular user login",
        "Missing token",
        "Empty token",
        "Invalid status code",
        "Missing user_id",
        "Negative user_id",
        "invalid role",
        "Multiple invalid fields",
    ]
)
def test_validate_withdrawal(response, expected):
    assert validate_login_response(response) == expected