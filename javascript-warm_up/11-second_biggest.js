#!/usr/bin/node
const args = process.argv;
let n;
let n1 = 0;
let n2 = 0;
for (let i = 2; i < args.length; i++) {
  n = parseInt(args[i]);
  if (n1 < n) {
    n2 = n1;
    n1 = n;
  } else if (n2 < n) {
    n2 = n;
  }
}
console.log(n2);
