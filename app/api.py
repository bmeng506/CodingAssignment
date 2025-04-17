from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import time
from src.functions import *

"""
This file creates a FastAPI application for the MathPath webapp. 
"""


# This creates the FastAPI app with the title and description. 
app = FastAPI(
    title="MathPath API", 
    description="Explore math functions with FastAPI"
)


# Mounts the static files directory to serve frontend files.
app.mount("/static", StaticFiles(directory="app/static", html=True))

@app.get("/")
def read_index():

    """
    This endpoint serves the index.html file when the root URL (/) is accessed.
    """

    return FileResponse("app/static/index.html")

@app.get("/api")
def root():

    """
    This is the root endpoint of the API. It returns a welcome message.
    It is a GET request and does not take any parameters.
    """

    return {"message": "Welcome to the MathPath API. Explore math functions."}

@app.get("/factorial")
def get_factorial(n: str, recursive: bool = False):

    """
    This endpoint calculates the factorial of a number n using an iterative or
    recursive method. 

    Parameters:
    - n: The non-negative integer that we want to calculate the factorial of. 
    - recursive: A boolean that indicates whether to use the recursive method.

    Returns:
    - A JSON object containing the number, factorial, whether the recursive
    method was used, and the runtime of the function in milliseconds.

    NOTE: The input n is a string that is converted to an integer due to errors
    that occur when passing in 'NONE' into the function. Replacing the input as
    a string and then recasting it to an integer allows the function to properly
    throw an error when the input is null.
    """

    # Get the start time    
    start_time = time.time() 

    if not n:
        # Throw error if user does not provide a number.
        raise HTTPException(status_code=400, detail="Number must be provided!")
    try:
        n_int = int(n)
        result = factorial_rec(n_int) if recursive else factorial_iter(n_int)
    except (ValueError, TypeError) as e:
        # Handle errors for invalid input
        raise HTTPException(status_code=400, detail=str(e))
    
    # Calculate ending time in milliseconds
    runtime = round((time.time() - start_time) * 1000, 4) 

    return {"number": n, 
            "factorial": result, 
            "recursive": recursive,
            "runtime": runtime}

    
@app.get("/fibonacci")
def get_fibonacci(n: str, recursive: bool = False, memo: bool = False):

    """
    This endpoint calculates the nth Fibonacci number using either an iterative
    or recursive method. 

    Parameters:
    - n: The nth number in the Fibonacci sequence to calculate.
    - recursive: A boolean that indicates whether to use the recursive method.
    - memo: A boolean that indicates whether to use memoization in the recursive
    method.

    Returns:
    - A JSON object containing the number, Fibonacci number, whether the
    recursive method was used, and the runtime of the function in milliseconds.
    
    NOTE: The input n is a string that is converted to an integer due to errors
    similar to issues with the functions above. In addition, memoization was
    used to optimize the recursive function and to show its effectiveness in
    reducing time (seen through the runtime). 
    """

    # Get the start time
    start_time = time.time()

    if not n:
        raise HTTPException(status_code=400, detail="Number must be provided!")
    try:
        # Cast n into an int.
        n_int = int(n)
        result = fibonacci_rec(n_int, memo) if recursive else fibonacci_iter(n_int)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    # Calculate ending time in milliseconds
    runtime = round((time.time() - start_time) * 1000, 4)
    
    return {"number": n, 
            "fibonacci": result, 
            "recursive": recursive,
            "runtime": runtime}

    
@app.get("/gcd")
def get_gcd(a: str, b: str, recursive: bool = False):
    """
    This endpoint calculates the GCD of two numbers a and b using either an
    iterative or recursive method.

    Parameters:
    - a: The first number.
    - b: The second number.
    - recursive: A boolean that indicates whether to use the recursive method.

    Returns:
    - A JSON object containing the two numbers, GCD, whether the recursive
    method was used, and the runtime of the function in milliseconds.
    
    NOTE: The inputs a and b are strings that are converted to integers due to
    errors similar to issues with the functions above.
    """

    # Get the start time
    start_time = time.time()
    
    if not a or not b:
        raise HTTPException(status_code=400,
                             detail="Both numbers must be provided!")
    try:
        a_int = int(a)
        b_int = int(b)
        result = gcd_rec(a_int, b_int) if recursive else gcd_iter(a_int, b_int)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=str(e))
            
     # Calculate ending time in milliseconds
    runtime = round((time.time() - start_time) * 1000, 4)

    return {"a": a_int, 
            "b": b_int, 
            "gcd": result, 
            "recursive": recursive, 
            "runtime": runtime}
   



    
