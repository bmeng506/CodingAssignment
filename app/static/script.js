console.log("loaded");
async function getFactorial() {
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
        resultElement.innerText = `Factorial of ${n} is ${data.factorial} (calculated in ${data.runtime} ms)`;
        resultElement.classList.remove('result-fail');
        resultElement.classList.add('result-success');

    }
}

async function getFibonacci() {
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
        resultElement.innerText = `The ${n}th Fibonacci Number is ${data.fibonacci} (calculated in ${data.runtime} ms)`;
        resultElement.classList.remove('result-fail');
        resultElement.classList.add('result-success');
    }
}

async function getGCD() {
    const a = document.getElementById("gcd-a").value;
    const b = document.getElementById("gcd-b").value;
    const recursive = document.getElementById("gcd-rec").checked;
    const resultElement = document.getElementById("gcd-result");

    try{
        const response = await fetch(`/gcd?a=${a}&b=${b}&recursive=${recursive}`);
        const data = await response.json();

        if (!response.ok) {
            resultElement.innerText = `${data.detail}`;
            resultElement.classList.remove('result-success');
            resultElement.classList.add('result-fail');
        } else {
            resultElement.innerText = `The GCD of ${a} and ${b} is ${data.gcd} (calculated in ${data.runtime} ms)`;
            resultElement.classList.remove('result-fail');
            resultElement.classList.add('result-success');
        }
    } catch (error) {
        resultElement.innerText = `Error: ${error.message}`;
    }
}

window.getFactorial = getFactorial;
