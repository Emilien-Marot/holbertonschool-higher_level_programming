#!/usr/bin/node
function factorial (n) {
  if (n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

const args = process.argv;
const a = parseInt(args[2]);
console.log(factorial(a));
