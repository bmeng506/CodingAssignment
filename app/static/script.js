async function getFactorial() {
    const n = document.getElementById("factorial-input").value;
    const recursive = document.getElementById("factorial-rec").checked;
    
    const response = await fetch(`/factorial?n=${n}&recursive=${recursive}`);
    const data = await response.json();

    document.getElementById("factorial-result").innerText = 
        `Factorial of ${n} is ${data.factorial}`;
}

async function getFibonacci() {
    const n = document.getElementById("fibonacci-input").value;
    const recursive = document.getElementById("fibonacci-rec").checked;
    
    const response = await fetch(`/fibonacci?n=${n}&recursive=${recursive}`);
    const data = await response.json();

    document.getElementById("factorial-result").innerText = 
        `Fibonacci of ${n} is ${data.fibonacci}`;
}

async function getGCD() {
    const a = document.getElementById("gcd-a").value;
    const b = document.getElementById("gcd-b").value;
    const recursive = document.getElementById("gcd-rec").checked;
    
    const response = await fetch(`/gcd?a=${a}&b=${b}&recursive=${recursive}`);
    const data = await response.json();

    document.getElementById("gcd-result").innerText = 
        `GCD of ${a} and ${b} is ${data.gcd}`;
}