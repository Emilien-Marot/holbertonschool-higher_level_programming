#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2]);
if (!isNaN(num)) {
  let i;
  let line = '';
  for (i = 0; i < num; i++) {
    line += 'X';
  }
  for (i = 0; i < num; i++) {
    console.log(line);
  }
} else {
  console.log('Missing size');
}
