# Coding Assignment
# Part I: Math Path
A creative Python project that implements the factorial, Fibonacci, and GCD math algorithms, using both iterative and recursive approaches.

---

## Features

- Factorial (iterative & recursive)
- Fibonacci (iterative & recursive)
- Greatest Common Divisor using Euclid's  (iterative & recursive)
- Proper error handling with exceptions
- Comprehensive & edge testing with `pytest`

---

## How to Use

### Installation

1. Clone the repository:
```bash
git clone https://github.com/bmeng506/MathPath.git
cd MathPath
```

2. (Optional) Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
- If `python -m venv venv` does not work, try:
```bash
python3 -m venv venv
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Tests
To run all unit tests on functions:
```bash
pytest
```
or
```bash
python -m pytest tests/test_functions.py
```
**NOTE**: Look in test_functions.py for more information on how to run unit tests.


### Running Web App
To run and launch the web app locally:
```bash
uvicorn app.api:app --reload
```
or run the `main.py` file.

# Part II: Clarity

Look into the ClarityLLM folder for more information, where you will find the `clarity_guidelines.md`, `clarity_prompt.md`, `bad_example.py`, and `clarity_response.md` files.

Clarity is a friendly and helpful LLM-powered Python style checker!

## About the Creator
Hi! I'm Brian, a first-year university student studying Computer Science and Mathematical Economics. I am passionate about computer science, math, and building new things :)

The Web App reflects my love for programming and math. I had a lot of fun building this project and hope it is just as fun to use!

### Inspiration 

This project sprung out of a coding challenge and demonstrates not only how I code, but also how I think, design, and make my work unique!

### Contact
Feel free to reach out or connect with me!\
Email: bmeng@sas.upenn.edu\
Github: @bmeng506\
LinkedIn: https://www.linkedin.com/in/bmeng506/
