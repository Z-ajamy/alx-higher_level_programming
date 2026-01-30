#!/usr/bin/env node


args = process.argv.slice(2);
const x = Number(args[0])
if(isNaN(x)) {
  console.log("Not a number");
  return;
}

console.log("My number: " + args[0]);
