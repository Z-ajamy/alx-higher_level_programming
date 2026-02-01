#!/usr/bin/env node

const args = process.argv.slice(2);
if (args[0] === undefined) {
  console.log('No argument');
  process.exit();
}

console.log(args[0]);
