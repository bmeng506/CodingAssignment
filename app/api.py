from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import time
from src.functions import *

"""
This file uses FastAPI to create APIs that connect the Python backend code to an
HTML/CSS webpage for full functionality.
"""

"""
This creates the FastAPI app with the title and description. 
"""
app = FastAPI(
    title="MathPath API", 
    description="Explore math functions with FastAPI"
)


app.mount("/static", StaticFiles(directory="app/static", 
                                 html=True))

@app.get("/")
def read_index():
    return FileResponse("app/static/index.html")

@app.get("/api")
def root():
    return {"message": "Welcome to the MathPath API. Explore math functions."}

@app.get("/factorial")
def get_factorial(n: str, recursive: bool = False):
    start_time = time.time()
    if not n:
        raise HTTPException(status_code=400, detail="Number must be provided!")
    try:
        n_int = int(n)
        result = factorial_rec(n_int) if recursive else factorial_iter(n_int)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    runtime = round((time.time() - start_time) * 1000, 4)

    return {"number": n, 
            "factorial": result, 
            "recursive": recursive,
            "runtime": runtime}

    
@app.get("/fibonacci")
def get_fibonacci(n: str, recursive: bool = False, memo: bool = False):
    start_time = time.time()
    if not n:
        raise HTTPException(status_code=400, detail="Number must be provided!")
    try:
        n_int = int(n)
        result = fibonacci_rec(n_int, memo) if recursive else fibonacci_iter(n_int)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    runtime = round((time.time() - start_time) * 1000, 4)
    return {"number": n, "fibonacci": result, "recursive": recursive, "runtime": runtime}

    
@app.get("/gcd")
def get_gcd(a: str = None, b: str = None, recursive: bool = False):
    start_time = time.time()
    if not a or not b:
        raise HTTPException(status_code=400,
                             detail="Both numbers must be provided!")
    try:
        a_int = int(a)
        b_int = int(b)
    except ValueError:
        raise HTTPException(status_code=400, 
                            detail="Inputs must be integers!")
    try:
        result = gcd_rec(a_int, b_int) if recursive else gcd_iter(a_int, b_int)
        runtime = round((time.time() - start_time) * 1000, 4)
        return {"a": a_int, "b": b_int, "gcd": result, "recursive": recursive, "runtime": runtime}
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=str(e))

    
