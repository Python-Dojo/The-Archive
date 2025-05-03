import pytest

from main import longest_diverse_string

@pytest.mark.parametrize("a, b, c, expected_length", [
    (1, 1, 1, 3),
    (2, 2, 2, 6),
    (3, 0, 0, 2),
    (7, 1, 0, 5),
    (7, 1, 1, 8),
    (0, 0, 0, 0)
])

def test_main(a: int, b: int, c: int, expected_length: int) -> None:
    result = longest_diverse_string(a, b, c) 
    assert len(result) == expected_length