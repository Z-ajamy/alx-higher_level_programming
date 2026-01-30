#!/usr/bin/env node


args = process.argv.slice(2);
if(args.length === 0) {
  console.log("No argument");
  return;
}

console.log(args[0]);
