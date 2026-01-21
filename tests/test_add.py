import pytest
from src.math_operations import add

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, -2, -3),
        (-1, 1, 0),
        (1.5, 2.5, 4.0),
        (1e10, 1e10, 2e10),
        (0, 5, 5),
        (5, 0, 5),
        (-100, 100, 0),
    ]
)
def test_add(a, b, expected):
    assert add(a, b) == expected

def test_add_type_error():
    with pytest.raises(TypeError):
        add('a', 1)
    with pytest.raises(TypeError):
        add(1, None)
