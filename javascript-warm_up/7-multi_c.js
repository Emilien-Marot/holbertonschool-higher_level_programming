#!/usr/bin/node
const args = process.argv;
let num = NaN;
if (args[2] !== undefined) {
  num = parseInt(args[2]);
}
if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun')
  }
} else {
  console.log('Missing number of occurrences');
}