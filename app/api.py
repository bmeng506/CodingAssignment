from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from src.functions import *

app = FastAPI(
    title="MathPath API", 
    description="Explore math functions with FastAPI"
)

app.mount("/static", StaticFiles(directory="app/static", html=True),name="static")

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
def get_gcd(a: int, b: int, recursive: bool = False):
    try:
        result = gcd_rec(a, b) if recursive else gcd_iter(a, b)
        return {"a": a, "b": b, "gcd": result, "recursive": recursive}
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    
