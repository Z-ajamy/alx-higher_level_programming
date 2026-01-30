#!/usr/bin/env node


args = process.argv.slice(2);
if(args[0] === undefined) {
  console.log("No argument");
  return;
}

console.log(args[0]);
