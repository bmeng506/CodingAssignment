import pytest
from src.functions import *

"""
To run, use the command: python -m pytest tests/test_functions.py
"""

def test_factorial_iter():
    """
    This and below are tests for the iterative and recursive factorial 
    functions. The tests in order are: ordinary case, 0th case (edge case), 
    ValueError case, TypeError case, and 1st case (edge case). 
    """
    assert factorial_iter(5) == 120
    assert factorial_iter(0) == 1
    with pytest.raises(ValueError, match="Input must be a non-negative integer!"):
        factorial_iter(-1)
    with pytest.raises(TypeError, match="Input must be an integer!"):
        factorial_iter('x')
    assert factorial_iter(1) == 1

def test_factorial_rec():
    """
    See above for test information.
    """
    assert factorial_rec(5) == 120
    assert factorial_rec(0) == 1
    with pytest.raises(ValueError, match="Input must be a non-negative integer!"):
        factorial_iter(-1)
    with pytest.raises(TypeError, match="Input must be an integer!"):
        factorial_iter('x')
    assert factorial_rec(1) == 1

def test_fibonacci_iter():
    """
    This function and below are tests for the iterative and recursive fibonacci 
    functions. The tests in order are: ordinary case, 0th case (edge case), 1st 
    case (edge case), ValueError case, and TypeError case.
    """
    assert fibonacci_iter(5) == 5
    assert fibonacci_iter(0) == 0
    assert fibonacci_iter(1) == 1
    with pytest.raises(ValueError, match="Must be not be negative!"):
        fibonacci_iter(-1)
    with pytest.raises(TypeError, match="Input must be an integer!"):
        fibonacci_iter('x')

def test_fibonacci_rec():
    """
    See above for test information.
    """
    assert fibonacci_rec(5) == 5
    assert fibonacci_rec(0) == 0
    assert fibonacci_rec(1) == 1
    with pytest.raises(ValueError, match="Must be not be negative!"):
        fibonacci_iter(-1)
    with pytest.raises(TypeError, match="Input must be an integer!"):
        fibonacci_iter('x')

def test_gcd_iter():
    """
    This function and below are tests for the iterative and recursive gcd
    functions. The tests in order are: ordinary case, 0-0 case (edge case),
    0-1 case (edge case), 1-0 case (edge case), TypeError case, and ValueError
    cases for 4-None, None-4, and None-None.

    NOTE: Swaps of the values are both tested (i.e. 0-1 and 1-0) to see if the
    function's ability to calculate GCD properly for all forms of the same
    input. None values are also tested to see if the function can throw the 
    right error and catch them.
    """
    assert gcd_iter(12, 8) == 4
    assert gcd_iter(0, 0) == 0
    assert gcd_iter(0, 1) == 1
    assert gcd_iter(1, 0) == 1
    assert gcd_iter(-1, -1) == 1
    with pytest.raises(TypeError, match="Inputs must be integers!"):
        gcd_iter('x', 'y')
    with pytest.raises(ValueError, match="Both numbers must be provided!"):
        gcd_iter(4, None)
    with pytest.raises(ValueError, match="Both numbers must be provided!"):
        gcd_iter(None, 4)
    with pytest.raises(ValueError, match="Both numbers must be provided!"):
        gcd_iter(None, None)

def test_gcd_rec():
    """
    See above for test information.
    """
    assert gcd_rec(12, 8) == 4
    assert gcd_rec(0, 0) == 0
    assert gcd_rec(0, 1) == 1
    assert gcd_rec(1, 0) == 1
    assert gcd_rec(-1, -1) == 1
    with pytest.raises(TypeError, match="Inputs must be integers!"):
        gcd_iter('x', 'y')
    with pytest.raises(ValueError, match="Both numbers must be provided!"):
        gcd_iter(4, None)
    with pytest.raises(ValueError, match="Both numbers must be provided!"):
        gcd_iter(None, 4)
    with pytest.raises(ValueError, match="Both numbers must be provided!"):
        gcd_iter(None, None)
