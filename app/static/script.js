
async function getFactorial() {
    const n = document.getElementById("factorial-input").value;
    const recursive = document.getElementById("factorial-rec").checked;
    const resultElement = document.getElementById("factorial-result");
    
    try {
        const response = await fetch(`/factorial?n=${n}&recursive=${recursive}`);
        const data = await response.json();
        
        if (!response.ok) {
            resultElement.innerText = `Error: ${data.detail}`;
        } else {
            resultElement.innerText = `Factorial of ${n} is ${data.factorial}`;
        }
    } catch (error) {
        resultElement.innerText = `Error: ${error.message}`;
    }
}

async function getFibonacci() {
    const n = document.getElementById("fibonacci-input").value;
    const recursive = document.getElementById("fibonacci-rec").checked;
    const resultElement = document.getElementById("fibonacci-result");

    try {
        const response = await fetch(`/fibonacci?n=${n}&recursive=${recursive}`);
        const data = await response.json();
        
        if (!response.ok) {
            resultElement.innerText = `Error: ${data.detail}`;
        } else {
            resultElement.innerText = `The ${n}th Fibonacci Number is ${data.fibonacci}`;
        }
    } catch (error) {
        resultElement.innerText = `Error: ${error.message}`;
    }
}

document.getElementById("gcd-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const a = document.getElementById("gcd-a").value;
    const b = document.getElementById("gcd-b").value;
    const recursive = document.getElementById("gcd-rec").checked;
    const resultElement = document.getElementById("gcd-result");

    try {
        const response = await fetch(`/gcd?a=${a}&b=${b}&recursive=${recursive}`);
        const data = await response.json();

        if (!response.ok) {
            const errorMessage =
                typeof data.detail === "string"
                    ? data.detail
                    : JSON.stringify(data.detail);
            resultElement.innerText = `Error: ${errorMessage}`;
        } else {
            resultElement.innerText = `The GCD of ${a} and ${b} is ${data.gcd}`;
        }
    } catch (error) {
        resultElement.innerText = `Error: ${error.toString()}`;
    }
});