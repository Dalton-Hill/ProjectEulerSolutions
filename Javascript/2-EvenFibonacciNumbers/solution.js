let fib_terms = new Set();

const fibonacci = (n1, n2, limit) => {
    fib_terms.add(n1);
    fib_terms.add(n2);

    let sum = n1 + n2;
    if (sum >= limit) return n2;
    return fibonacci(n2, sum, limit)
};

fibonacci(1, 2, 4000000);
fib_terms = new Array(...fib_terms);

const answer = fib_terms.reduce((sum, term) => {
    if (term % 2 === 0) return sum + term;
    return sum;
}, 0);

console.log(answer);