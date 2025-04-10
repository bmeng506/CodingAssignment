
class functions:
    def factorial_iterative(n):
        result = 1
        if n == 0:
            return result
        else:
            for i in range(1, n + 1):
                result *= i
            return result

    def factorial_recursive(n):
        if n == 0:
            return 1
        else: 
            return n * functions.factorial(n-1)
        
    def fibonacci_iterative(n):
        if n <= 0:
            return 'Must be greater than 0!'
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else: 
            a, b = 0, 1
            for i in range(2, n):
                a, b = b, a + b
            return b

    def fibonacci_recursive(n): # Function that returns nth number in the fibonacci sequence
        if n <= 1:
            return n
        else:
            return functions.fibonacci(n-1) + functions.fibonacci(n-2)
        
    def gcd_iterative(a, b):
        if a == 0:
            return b
        elif b == 0:
            return a
        else: 
            while b != 0:
                a, b = b, a % b
            return a
        
    print(gcd_iterative(15, 10))
        
    def gcd_recursive(a, b): # Function that returns the greatest common divisor of two numbers
        if a == 0:
            return b
        elif b == 0:
            return a
        else:
            return functions.gcd(b, a % b)
        