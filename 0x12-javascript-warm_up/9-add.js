#!/usr/bin/node

const arg = process.argv.slice(2);

if (arg.length !== 2) {
  console.log('NaN');
} else {
  const num1 = Number(arg[0]);
  const num2 = Number(arg[1]);
  console.log(num1 + num2);
}
