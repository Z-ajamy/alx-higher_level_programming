#!/usr/bin/env node


args = process.argv.slice(2);

if(args.length === 0) {
  console.log(NaN);
  return;
}

function factorial(x) {
  if (x === 1 || x === 0) return 1;
  return x * factorial(x - 1)
}

console.log(factorial(args[0]));
