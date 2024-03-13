#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(Number(arg))) {
  console.log(1);
} else {
  console.log(factorial(Number(arg)));
}

function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return (n * factorial(n - 1));
}
