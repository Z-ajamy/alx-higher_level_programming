#!/usr/bin/env node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log(NaN);
  process.exit();
}

function factorial (x) {
  if (x === 1 || x === 0) return 1;
  return x * factorial(x - 1);
}

console.log(factorial(args[0]));
