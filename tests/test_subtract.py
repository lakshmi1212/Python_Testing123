import pytest
from src.math_operations import subtract

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 2, 1),
        (0, 0, 0),
        (-1, -2, 1),
        (-1, 1, -2),
        (2.5, 1.5, 1.0),
        (1e10, 1e9, 9e9),
        (0, 5, -5),
        (5, 0, 5),
        (-100, 100, -200),
    ]
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract('a', 1)
    with pytest.raises(TypeError):
        subtract(1, None)
