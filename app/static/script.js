
function getOrdinal(n) {
    /*
    Function to get the ordinal suffix for a number. It takes a number as input
    and returns it with its ordinal suffix (th, st, nd, rd).
    */

    const s = ["th", "st", "nd", "rd"];
    const v = n % 100;

    /* 
    Handles special cases for 11, 12, and 13. First section of the OR blocks 
    is limited to values of v greater than 20. If the value is under 20, the 
    function moves to the next block (s[v]). The only values that work here are
    0, 1, 2, and 3. The rest are handled by the last block (values 4-19, which
    all need "th"). This is the default block. 
    */ 

    return n + (s[(v - 20) % 10] || s[v] || s[0])
}

console.log(getOrdinal(5))

async function getFactorial() {

    /*
    Asynchronous function to fetch the factorial of a number from the server. 
    It retrieves the value of the number from the input field, checks if the recursive 
    option is selected, and sends a GET request to the server with the number and 
    the recursive option as query parameters.

    Errors are caught and displayed properly, so that the UI also displays them.
    The resulting text will either be an error or the factorial of the number and
    its runtime, structured as:

    Factorial of <number> is <factorial> (calculated in <runtime> ms)

    NOTE: This function is asynchronous so that the UI remains responsive while waiting
    for the server to respond and send the result back to the client.
    */

    const n = document.getElementById("factorial-input").value;
    const recursive = document.getElementById("factorial-rec").checked;
    const resultElement = document.getElementById("factorial-result");
        
    const response = await fetch(`/factorial?n=${n}&recursive=${recursive}`);
    const data = await response.json();

    if (!response.ok) {
        resultElement.innerText = `${data.detail}`;
        resultElement.classList.remove('result-success');
        resultElement.classList.add('result-fail');
    } else {
        resultElement.innerText = 
        `Factorial of ${n} is ${data.factorial} (calculated in ${data.runtime} ms)`;
        resultElement.classList.remove('result-fail');
        resultElement.classList.add('result-success');

    }
}

async function getFibonacci() {

    /*
    Asynchronous function to fetch the nth fibonacci number from the server. 
    Very similar structure and purpose as the function above. It takes a value
    from the input field and checks for recursive and memoization options, and 
    properly returns the value. Errors are also properly handled. 

    NOTE: Same above.
    */

    const n = document.getElementById("fibonacci-input").value;
    const recursive = document.getElementById("fibonacci-rec").checked;
    const memo = document.getElementById("fibonacci-memo").checked;
    const resultElement = document.getElementById("fibonacci-result");

    const response = await fetch(`/fibonacci?n=${n}&recursive=${recursive}&memo=${memo}`);
    const data = await response.json();
    if (!response.ok) {
        resultElement.innerText = `${data.detail}`;
        resultElement.classList.remove('result-success');
        resultElement.classList.add('result-fail');
    } else {
        resultElement.innerText = 
        `The ${getOrdinal(parseInt(n))} Fibonacci Number is ${data.fibonacci} (calculated in ${data.runtime} ms)`;
        resultElement.classList.remove('result-fail');
        resultElement.classList.add('result-success');
    }
}

async function getGCD() {

    /*
    Asynchronous function to fetch the GCD of two numbers from the server. 
    Similar to the functions above. It takes two values from the input field and
    checks for the recursive option properly returns the value. 

    NOTE: Same above.
    */

    const a = document.getElementById("gcd-a").value;
    const b = document.getElementById("gcd-b").value;
    const recursive = document.getElementById("gcd-rec").checked;
    const resultElement = document.getElementById("gcd-result");

    const response = await fetch(`/gcd?a=${a}&b=${b}&recursive=${recursive}`);
    const data = await response.json();
    if (!response.ok) {
        resultElement.innerText = `${data.detail}`;
        resultElement.classList.remove('result-success');
        resultElement.classList.add('result-fail');
    } else {
        resultElement.innerText = 
        `The GCD of ${a} and ${b} is ${data.gcd} (calculated in ${data.runtime} ms)`;
        resultElement.classList.remove('result-fail');
        resultElement.classList.add('result-success');
    }
}

// Exposes the functions to the global scope so they can be called from HTML.
window.getFactorial = getFactorial;
window.getFibonacci = getFibonacci;
window.getGCD = getGCD;

