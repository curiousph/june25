import pytest
from math_operations import add, subtract, multiply, divide

# test_math_operations.py


# Tests for add
def test_add_positive_integers():
    assert add(2, 3) == 5

def test_add_negative_integers():
    assert add(-2, -3) == -5

def test_add_positive_and_negative():
    assert add(5, -3) == 2

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_add_floats():
    assert add(2.5, 3.1) == pytest.approx(5.6)
    assert add(-2.5, 2.5) == 0.0

def test_add_large_numbers():
    assert add(1_000_000_000, 2_000_000_000) == 3_000_000_000

# Tests for subtract
def test_subtract_positive_integers():
    assert subtract(5, 3) == 2

def test_subtract_negative_integers():
    assert subtract(-5, -3) == -2

def test_subtract_positive_and_negative():
    assert subtract(5, -3) == 8

def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5

def test_subtract_floats():
    assert subtract(5.5, 2.2) == pytest.approx(3.3)
    assert subtract(-2.5, 2.5) == -5.0

def test_subtract_large_numbers():
    assert subtract(2_000_000_000, 1_000_000_000) == 1_000_000_000

# Tests for multiply
def test_multiply_positive_integers():
    assert multiply(2, 3) == 6

def test_multiply_negative_integers():
    assert multiply(-2, -3) == 6

def test_multiply_positive_and_negative():
    assert multiply(2, -3) == -6

def test_multiply_zero():
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0

def test_multiply_floats():
    assert multiply(2.5, 4.0) == pytest.approx(10.0)
    assert multiply(-2.5, 2.0) == -5.0

def test_multiply_large_numbers():
    assert multiply(1_000_000, 2_000_000) == 2_000_000_000_000

# Tests for divide
def test_divide_positive_integers():
    assert divide(6, 3) == 2

def test_divide_negative_integers():
    assert divide(-6, -3) == 2

def test_divide_positive_and_negative():
    assert divide(6, -3) == -2

def test_divide_floats():
    assert divide(5.5, 2.2) == pytest.approx(2.5)
    assert divide(-5.5, 2.2) == pytest.approx(-2.5)

def test_divide_large_numbers():
    assert divide(2_000_000_000, 1_000_000_000) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(5, 0)