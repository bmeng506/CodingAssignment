from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import Optional
from src.functions import *

app = FastAPI(
    title="MathPath API", 
    description="Explore math functions with FastAPI"
)

app.mount("/static", StaticFiles(directory="app/static", 
                                 html=True), 
                                 name="static")

@app.get("/")
def read_index():
    return FileResponse("app/static/index.html")

@app.get("/api")
def root():
    return {"message": "Welcome to the MathPath API! Explore math functions."}

@app.get("/factorial")
def get_factorial(n: int, recursive: bool = False):
    try:
        result = factorial_rec(n) if recursive else factorial_iter(n)
        return {"number": n, "factorial": result, "recursive": recursive}
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/fibonacci")
def get_fibonacci(n: int, recursive: bool = False):
    try:
        result = fibonacci_rec(n) if recursive else fibonacci_iter(n)
        return {"number": n, "fibonacci": result, "recursive": recursive}
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/gcd")
def get_gcd(a: str = None, b: str = None, recursive: bool = False):
    if not a or not b:
        raise HTTPException(status_code=400,
                             detail="Both numbers must be provided!")

    try:
        a_int = int(a)
        b_int = int(b)
    except ValueError:
        raise HTTPException(status_code=400, 
                            detail="Inputs must be valid integers!")

    try:
        result = gcd_rec(a_int, b_int) if recursive else gcd_iter(a_int, b_int)
        return {"a": a_int, "b": b_int, "gcd": result, "recursive": recursive}
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=str(e))

    
