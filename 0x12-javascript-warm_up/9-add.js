#!/usr/bin/env node


const args = process.argv.slice(2);

if(args.length === 0 || args.length === 1) {
  console.log(NaN);
  return;
}

console.log(Number(args[0]) + Number(args[1]));
