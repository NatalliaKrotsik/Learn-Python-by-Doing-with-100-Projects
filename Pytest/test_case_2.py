import pytest


def validate_registration(data):
    errors = set()

    if len(data["username"]) < 4:
        errors.add("username too short")

    if len(data["password"]) < 8:
        errors.add("password too short")

    if data["age"] < 18:
        errors.add("underage")

    return len(errors) == 0


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ({"username": "Jonatan", "password": "12345678", "age": 20}, True),
        ({"username": "Jon", "password": "12345678", "age": 20}, False),
        ({"username": "Jonatan", "password": "1234567", "age": 20}, False),
        ({"username": "Jonatan", "password": "12345678", "age": 17}, False),
        ({"username": "Jo", "password": "123", "age": 15}, False),
    ],
)
def test_validate_registration(input_data, expected):
    assert validate_registration(input_data) == expected