import pytest
from access_json_data import get_correct_answer

@pytest.mark.parametrize(
    "question_id, expected",
    [
        (1, "Paris"),
        (2, "Tokyo"),
        (3, "Ottawa"),
        (999, None),
        (-1, None),
    ],
)
def test_get_correct_answer(question_id, expected):
    assert get_correct_answer(question_id) == expected