import pytest
from src.math_operations import subtract

def test_subtract_positive_integers():
    assert subtract(5, 3) == 2

def test_subtract_negative_integers():
    assert subtract(-5, -3) == -2

def test_subtract_mixed_sign_integers():
    assert subtract(-5, 3) == -8

def test_subtract_zero():
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5
    assert subtract(0, 0) == 0

def test_subtract_floats():
    assert subtract(5.5, 2.1) == pytest.approx(3.4)

def test_subtract_large_numbers():
    assert subtract(10**10, 10**9) == 9 * 10**9
