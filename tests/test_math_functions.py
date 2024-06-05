import pytest
from math_functions import plus, minus, mul, div

# Test cases for the plus function
def test_plus_integers():
    assert plus(1, 2) == 3

def test_plus_floats():
    assert plus(1.5, 2.5) == 4.0

def test_plus_negative():
    assert plus(-1, -2) == -3

# Test cases for the minus function
def test_minus_integers():
    assert minus(5, 3) == 2

def test_minus_floats():
    assert minus(5.5, 2.5) == 3.0

def test_minus_negative():
    assert minus(-1, -2) == 1

# Test cases for the mul function
def test_mul_integers():
    assert mul(3, 4) == 12

def test_mul_floats():
    assert mul(1.5, 2) == 3.0

def test_mul_negative():
    assert mul(-1, 2) == -2

# Test cases for the div function
def test_div_integers():
    assert div(8, 4) == 2

def test_div_floats():
    assert div(5.0, 2.0) == 2.5

def test_div_negative():
    assert div(-8, 2) == -4

# Test division by zero
def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)
