"""
This file contains implementation of the factorial, fibonacci, and greatest 
common divisor (GCD) functions using both iterative and recursive approaches. 
"""

def factorial_iter(n):
    """
    Function that returns the factorial of a number n using an iterative 
    approach. It iterates from 1 to n, multiplying the result (initially 1) by
    each number in the range. If n is 0, it returns 0. Otherwise, it returns 
    the factorial of n.

    NOTE: The function throws a TypeError if n is not an integer and a ValueError
    if n is a negative integer.
    The factorial of 0 is defined to be 1, so the function returns 1 in this
    case.
    """
    if not isinstance(n, int):
        raise TypeError('Input must be an integer!')  
    if n < 0:
        raise ValueError('Input must be a non-negative integer!')
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    
def factorial_rec(n):
    """
    A function that returns the factorial of a number n using a recursive 
    approach. It calls itself with n-1 until n is 0, multiplying the current 
    value n with the value of the factorial of n-1. Once it reaches n is 0,
    it returns 1. 

    NOTE: See previous function.
    """
    if not isinstance(n, int):
        raise TypeError('Input must be an integer!')  
    if n < 0:
        raise ValueError('Input must be a non-negative integer!')
    
    # Base case
    if n == 0:
        return 1
    else: 
        return n * factorial_rec(n-1)
    
# fibonacci functions
def fibonacci_iter(n):
    """
    A function that returns the nth number in the fibonacci sequence using an 
    iterative approach. It creates two variables a and b, intialized to 0 and 1.
    It then iterates from 2 to n, updating the value of a to b and b to a+b. 
    Once it reaches n, it returns b. If n <= 0, it returns an error message. 
    If n is 1, 0 is returned, and if n is 2, 1 is returned. 

    NOTE: The fibonacci sequence starts with 0 and 1, so the zeroth (n=0) number
    is 0, the first (n=1) number is 1, and so on.
    The function throws a TypeError if n is not an integer and a ValueError if 
    n is a negative integer.
    """
    if n is None:
        raise ValueError('Number must be provided!')
    if not isinstance(n, int):
        raise TypeError('Input must be an integer!')
    if n < 0:
        raise ValueError('Must be not be negative!')
    
    if n == 0 or n == 1:
        return n
    else: 
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a + b
        return b

memo_fib_rec = {} # Dictionary to store previously calculated fibonacci numbers

def fibonacci_rec(n, memo = False): 
    """
    A function that returns the nth number in the fibonacci sequence using a 
    recursive approach. It calls itself using n-1 and n-2, adding the two 
    results together until the function reaches a base case of n <= 1. In this
    case, it returns n, which is either 0 or 1. The function throws an error 
    message when n < 0.

    NOTE: See previous function.
    
    Includes a memoization feature to store previously calculated 
    values. This is mostly used in the application to show the effectiveness of
    memoization in shrinking down time.      
    """
    if n is None:
        raise ValueError('Number must be provided!')
    if not isinstance(n, int):
        raise TypeError('Input must be an integer!')
    if n < 0:
        raise ValueError('Must be not be negative!')
    
    if memo and n in memo_fib_rec:
        return memo_fib_rec[n]
    elif n <= 1:
        return n
    else:
        result = fibonacci_rec(n-1, memo) + fibonacci_rec(n-2, memo)
    memo_fib_rec[n] = result 
    return result 

# gcd functions
def gcd_iter(a, b):
    """
    A function that returns the greatest common divisor of two integers a and b 
    using an iterative version of Euclid's algorithm. A and b are both made 
    positive. If either a or b is 0, it returns the other number. If not, the 
    function iteratively updates a to b and b to the remainder of a divided by b
    (a % b) until b becomes 0, and returns a.

    NOTE: The function throws a TypeError if a or b is not an integer, and a 
    ValueError if either a or b is None. This function allows for negative 
    numbers, but turns the inputs into positive numbers. 
    """

    if a is None or b is None:
        raise ValueError('Both numbers must be provided!')
    
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Inputs must be integers!')

    a, b = abs(a), abs(b) # Make sure a and b are positive    

    if a == 0 or b == 0:
        return a or b
    while b != 0:
        a, b = b, a % b
    return a
    
def gcd_rec(a, b): # Function that returns the greatest common divisor of two numbers
    """
    A function that returns the greatest common divisor of two numbers a and b
    using a recursive approach of Euclid's algorithm, similar to the function 
    above. A and b are firstly made positive. If either a or b is 0, it returns 
    the other number. It calls itself with b and the remainder of a divided by b 
    (a % b) until either value is 0.  

    NOTE: See previous function.
    """
    
    if a is None or b is None:
        raise ValueError('Both numbers must be provided!')
    
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Inputs must be integers!')
    
    a, b = abs(a), abs(b) # Make sure a and b are positive
    if a == 0 or b == 0:
        return a or b
    return gcd_rec(b, a % b)
