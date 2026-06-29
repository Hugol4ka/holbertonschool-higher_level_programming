#!/usr/bin/node

const numberFactorial = parseInt(process.argv[2]);

function factorial (n) {
  if (n === 0 || n === 1 || Number.isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(numberFactorial));
