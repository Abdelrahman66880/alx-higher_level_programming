#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const uniqueArgs = Array.from(new Set(args));

if (uniqueArgs.length < 2) {
  console.log(0);
} else {
  uniqueArgs.sort((a, b) => b - a);
  console.log(uniqueArgs[1]);
}
