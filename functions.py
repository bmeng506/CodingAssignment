"""
This file contains implementation of the factorial, fibonacci, and greatest 
common divisor (GCD) functions using both iterative and recursive approaches. 
"""

def factorial_iterative(n):
    """
    Function that returns the factorial of a number n using an iterative 
    approach. It iterates from 1 to n, multiplying the result (initially 1) by
    each number in the range. If n is 0, it returns 0. Otherwise, it returns 
    the factorial of n.
    """
    result = 1
    if n == 0:
        return 0
    else:
        for i in range(1, n + 1):
            result *= i
        return result
    
def factorial_recursive(n):
    """
    A function that returns the factorial of a number n using a recursive 
    approach. It calls itself with n-1 until n is 0, multiplying the current 
    value n with the value of the factorial of n-1. Once it reaches n is 0,
    it returns 1. 
    """
    if n == 0:
        return 1
    else: 
        return n * factorial_recursive(n-1)
    
# fibonacci functions
def fibonacci_iterative(n):
    """
    A function that returns the nth number in the fibonacci sequence using an 
    iterative approach. It creates two variables a and b, intialized to 0 and 1.
    It then iterates from 2 to n, updating the value of a to b and b to a+b. 
    Once it reaches n, it returns b. If n <= 0, it returns an error message. 
    If n is 1, 0 is returned, and if n is 2, 1 is returned.
    """
    if n < 0:
        return 'Must be not be negative!'
    elif n == 0 or n == 1:
        return n
    else: 
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b

def fibonacci_recursive(n): # Function that returns nth number in the fibonacci sequence
    """
    A function that returns the nth number in the fibonacci sequence using a 
    recursive approach. It calls itself using n-1 and n-2, adding the two 
    results together until the function reaches a base case of n <= 1. In this
    case, it returns n, which is either 0 or 1. The function throws an error 
    message when n < 0.
    """
    if n < 0:
        return 'Must be not be negative!'
    elif n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
# gcd functions
def gcd_iterative(a, b):
    """
    A function that returns the greatest common divisor of two integers a and b 
    using an iterative version of Euler's algorithm. If either a or b is 0, it 
    returns the other number. If not, the function iteratively updates a to b 
    and b to the remainder of a divided by b (a % b) until b becomes 0, and 
    returns a.
    """
    if a == 0 or b == 0:
        return a or b
    while b != 0:
        a, b = b, a % b
    return a
    
def gcd_recursive(a, b): # Function that returns the greatest common divisor of two numbers
    """
    A function that returns the greatest common divisor of two numbers a and b
    using a recursive approach, similar to the function above. If either a or b 
    is 0, it returns the other number. It calls itself with b and the remainder 
    of a divided by b (a % b) until either value is 0.  
    """
    if a == 0 or b == 0:
        return a or b
    return gcd_recursive(b, a % b)

print(gcd_recursive(-5, 5))