import pytest


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ({"username": "Jonatan", "password": "12345678", "age": 20}, True),
        ({"username": "Jon", "password": "12345678", "age": 20}, False),
        ({"username": "Jonatan", "password": "1234567", "age": 20}, False),
        ({"username": "Jonatan", "password": "12345678", "age": 17}, False),
        ({"username": "Jonatan", "password": "12345678", "age": 20}, True),
    ]
)
def validation_of_registration(input_data, expected):
    assert validation_of_registration(**input_data) == expected
    errors = set()

    if len(input_data["username"]) < 4:
        errors.add("username too short")

    if len(input_data["password"]) < 8:
        errors.add("password too short")

    if len(input_data["age"]) < 18:
        errors.add("underage")

    return len(errors) == 0





