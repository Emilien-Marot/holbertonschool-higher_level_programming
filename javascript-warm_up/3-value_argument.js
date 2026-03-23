#!/usr/bin/node
const args = process.argv;
if (args[2] === undefined) {
  console.log('No argument');
} else {
  args.forEach((val, index) => {
    if (index > 1) {
      console.log(val);
    }
  });
}
