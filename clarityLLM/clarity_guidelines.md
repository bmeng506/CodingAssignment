# Style Guide - Clarity Coding Standards

Welcome to the Python style guide that Clarity, your friendly code reviewer, will use. 
These important guidelines will help ensure that your code is readable, effective, and neat. 

## 1. Proper, Readable Logic and Naming
- Use relevant and meaningful names for variables and functions ex: `final_answer`, not `fa`
- Whenever possible, avoid deeply nested logic (nested for or if loops)
- Break longer logic and expressions into smaller steps. 

## 2. Organization
- Group related functions / ideas and keep them in separate files.
- Reduce use of global state.
- Use whitespace to separate logical chunks of code.
- Programs should have a clearly marked starting point (ex: `def main():`)

## 3. Iteration and Recursion
- Use iteration instead of recursion, unless recursion produces more clear code.
- Clearly define base cases and use proper comments if using recursion.

## 4. Testing and Robustness
- Include meaningful and unique test cases; don't be testing the same thing over and over.
- Functions should validate all user inputs (of any form) and return proper error messages.
- Failing early and clearly is preferred (ex: `raise ValueError`)

## 5. Documentation and Comments
- Use docstrings to explain functions, inline comments to explain tricky or complex lines.
- Follow this format for docstrings: 
```python
    def sum(n: int):
        """
        (Description of function) This function sums all numbers...

        Parameters:
        - (parameter name and type) n (int): (explain its usage, why its used, where its used) Sums from 1 to n...

        Returns:
        - (type) int: (Explain what the function returns) Returns sum of numbers...
        """
        sum = 0

        for i in range(1, n+1):
            sum += i

        return sum


## 6. Style and Formatting
- Follow PEP8.
- Use 4 spaces per indent.
- Limit lines to 79 characters.
- Use f-strings for embedding and formatting.

---

Clarity uses this guide to provide warm, constructive feedback to allow you to write beautiful Python!
