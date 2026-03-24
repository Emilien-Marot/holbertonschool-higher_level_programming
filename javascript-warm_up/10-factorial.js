#!/usr/bin/node
function factorial (n) {
  if (n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

const args = process.argv;
let a = parseInt(args[2]);
if (isNaN(a)) {
  a = 1;
}
console.log(factorial(a));
