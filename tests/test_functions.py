import pytest
from src.functions import *

"""
To run, use the command: python -m pytest tests/test_functions.py
"""

def test_factorial_iter():
    assert factorial_iter(5) == 120
    assert factorial_iter(0) == 1
    with pytest.raises(ValueError, match="Input must be a non-negative integer!"):
        factorial_iter(-1)
    with pytest.raises(TypeError, match="Input must be an integer!"):
        factorial_iter('x')
    assert factorial_iter(1) == 1

def test_factorial_rec():
    assert factorial_rec(5) == 120
    assert factorial_rec(0) == 1
    with pytest.raises(ValueError, match="Input must be a non-negative integer!"):
        factorial_iter(-1)
    with pytest.raises(TypeError, match="Input must be an integer!"):
        factorial_iter('x')
    assert factorial_rec(1) == 1

def test_fibonacci_iter():
    assert fibonacci_iter(5) == 5
    assert fibonacci_iter(0) == 0
    assert fibonacci_iter(1) == 1
    with pytest.raises(ValueError, match="Must be not be negative!"):
        fibonacci_iter(-1)
    with pytest.raises(TypeError, match="Input must be an integer!"):
        fibonacci_iter('x')

def test_fibonacci_rec():
    assert fibonacci_rec(5) == 5
    assert fibonacci_rec(0) == 0
    assert fibonacci_rec(1) == 1
    with pytest.raises(ValueError, match="Must be not be negative!"):
        fibonacci_iter(-1)
    with pytest.raises(TypeError, match="Input must be an integer!"):
        fibonacci_iter('x')

def test_gcd_iter():
    assert gcd_iter(12, 8) == 4
    assert gcd_iter(0, 0) == 0
    assert gcd_iter(0, 1) == 1
    assert gcd_iter(1, 0) == 1
    assert gcd_iter(-1, -1) == 1
    with pytest.raises(TypeError, match="Inputs must integers!"):
        gcd_iter('x', 'y')
    with pytest.raises(ValueError, match="Both numbers must be provided!"):
        gcd_iter(4, None)
    with pytest.raises(ValueError, match="Both numbers must be provided!"):
        gcd_iter(None, 4)
    with pytest.raises(ValueError, match="Both numbers must be provided!"):
        gcd_iter(None, None)

def test_gcd_rec():
    assert gcd_rec(12, 8) == 4
    assert gcd_rec(0, 0) == 0
    assert gcd_rec(0, 1) == 1
    assert gcd_rec(1, 0) == 1
    assert gcd_rec(-1, -1) == 1
    with pytest.raises(TypeError, match="Inputs must integers!"):
        gcd_iter('x', 'y')
    with pytest.raises(ValueError, match="Both numbers must be provided!"):
        gcd_iter(4, None)
    with pytest.raises(ValueError, match="Both numbers must be provided!"):
        gcd_iter(None, 4)
    with pytest.raises(ValueError, match="Both numbers must be provided!"):
        gcd_iter(None, None)
