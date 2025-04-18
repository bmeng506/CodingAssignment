"""
This file contains implementation of the factorial, fibonacci, and greatest 
common divisor (GCD) functions using both iterative and recursive approaches. 
"""

def factorial_iter(n: int):
    """
    Function that returns the factorial of a number n using an iterative 
    approach. 

    Parameters: 
    - n (int): The integer that the function finds the factorial of. It iterates
    from 1 to n, multiplying the result (initially 1) by each number in the range.

    Returns:
    - int: If n is 0, it returns 1. Otherwise, it returns the factorial of n.

    Raises:
    - TypeError if n is not an integer 
    - ValueError if n is a negative integer.
    
    NOTE: The factorial of 0 is defined to be 1, so the function returns 1 in 
    this case.
    """
    if n is None:
        raise ValueError('Number must be provided!')
    if not isinstance(n, int):
        raise TypeError('Input must be an integer!')  
    if n < 0:
        raise ValueError('Input must be a non-negative integer!')
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    
def factorial_rec(n: int):
    """
    A function that returns the factorial of a number n using a recursive 
    approach. 
    
    Parameters: 
    - n (int): The integer that the function finds the factorial of. It calls 
    itself with n-1 until n is 0, multiplying the current value n with the value 
    of the factorial of n-1. Once it reaches n is 0, it returns 1. 

    Returns:
    - int: If n is 0, it returns 1. Otherwise, it returns the factorial of n.

    Raises:
    - TypeError if n is not an integer 
    - ValueError if n is a negative integer.
    """
    if n is None:
        raise ValueError('Number must be provided!')
    if not isinstance(n, int):
        raise TypeError('Input must be an integer!')  
    if n < 0:
        raise ValueError('Input must be a non-negative integer!')
    
    # Base case
    if n == 0:
        return 1
    else: 
        return n * factorial_rec(n-1) # Recursion for n-1.
    
def fibonacci_iter(n: int):
    """
    A function that returns the nth number in the Fibonacci sequence using an 
    iterative approach.

    Parameters:
    - n (int): The index (non-negative) of the Fibonacci sequence to retrieve.

    Returns:
    - int: The nth Fibonacci number. 0 when n=0, 1 when n=1.

    Raises:
    - TypeError: If n is not an integer.
    - ValueError: If n is negative.

    NOTE: The fibonacci sequence starts with 0 and 1, so the zeroth (n=0) number
    is 0, the first (n=1) number is 1, and so on.
    """
    if n is None:
        raise ValueError('Number must be provided!')
    if not isinstance(n, int):
        raise TypeError('Input must be an integer!')
    if n < 0:
        raise ValueError('Must be not be negative!')
    
    # 0th Fib num is 0, 1st Fib num is 1
    if n == 0 or n == 1:
        return n
    else: 
        # Creates a, b to 0, 1.
        a, b = 0, 1
        for i in range(2, n+1):
            # For each loop, swaps b to a and (a + b) to b. 
            a, b = b, a + b
        return b # Returns b, the nth fibonacci number. 

# Dictionary to store previously calculated fibonacci numbers.
# Must be global to properly store the numbers and reaccess them. 
memo_fib_rec = {} 

def fibonacci_rec(n: int, memo: bool = False): 
    """
    Returns the nth Fibonacci number using a recursive approach, with optional 
    memoization. It calls itself using n-1 and n-2, adding the two 
    results together until the function reaches a base case of n <= 1. In this
    case, it returns n.

    Parameters:
    - n (int): The index (non-negative) of the Fibonacci sequence to retrieve.
    - memo (bool): Whether to use memoization for optimization. Default is False.

    Returns:
    - int: The nth Fibonacci number. 0 when n=0, 1 when n=1.

    Raises:
    - TypeError: If n is not an integer.
    - ValueError: If n is negative.
    
    NOTE: Includes a memoization feature to store previously calculated values. 
    This is mostly used in the application to show the effectiveness of
    memoization in shrinking down time.      
    """
    if n is None:
        raise ValueError('Number must be provided!')
    if not isinstance(n, int):
        raise TypeError('Input must be an integer!')
    if n < 0:
        raise ValueError('Must be not be negative!')
    
    # If the nth fib num is in the dict, return that number without calculating.
    if memo and n in memo_fib_rec: 
        return memo_fib_rec[n]
    elif n <= 1:
        return n
    else: # Recursion for both n-1 and n-2.
        result = fibonacci_rec(n-1, memo) + fibonacci_rec(n-2, memo)
   
    memo_fib_rec[n] = result  # Add the nth fibonacci number to the dict.

    return result 

def gcd_iter(a: int, b: int):
    """
    A function that returns the greatest common divisor of two integers a and b 
    using an iterative version of Euclid's algorithm. a and b are both made 
    positive. The function iteratively updates a to b and b to the remainder of 
    a divided by b (a % b) until b becomes 0.

    Parameters:
    - a (int): first number
    - b (int): second number

    Returns:
    - int: The GCD of the two numbers. If either a or b is 0, it returns the 
    other number. 
    
    Raises: 
    - TypeError if a or b is not an integer
    - ValueError if either a or b is None. 
    
    NOTE: This function allows for negative numbers, but turns the inputs into 
    positive numbers. 
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
    
def gcd_rec(a: int, b: int): 
    """
    A function that returns the greatest common divisor of two numbers a and b
    using a recursive approach of Euclid's algorithm, similar to the function 
    above. A and b are firstly made positive. It calls itself with b and the 
    remainder of a divided by b (a % b) until either value is 0.  

    Parameters:
    - a (int): The first number.
    - b (int): The second number.

    Returns:
    - int: The GCD of a and b. If either a or b is 0, it returns the other
    number.

    Raises: 
    - TypeError if either a or b is not an integer.
    - ValueError if either a or b is None. 

    NOTE: See previous function.
    """
    
    if a is None or b is None:
        raise ValueError('Both numbers must be provided!')
    
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Inputs must be integers!')
    
    a, b = abs(a), abs(b) # Make sure a and b are positive
    
    if a == 0 or b == 0: # If a or b is zero, return the other value. 
        return a or b
    
    return gcd_rec(b, a % b) # Recursion of b, remainder of a divided by b.