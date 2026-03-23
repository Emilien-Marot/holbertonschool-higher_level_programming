#!/usr/bin/node
const args = process.argv;
if (args[2] !== undefined) {
  const num = parseInt(args[2]);
  if (!isNaN(num)) {
    console.log('My number: ' + num);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
