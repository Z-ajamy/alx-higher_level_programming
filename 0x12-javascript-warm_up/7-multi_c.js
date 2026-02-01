#!/usr/bin/env node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('Missing number of occurrences');
  process.exit();
}

for (let i = 0; i < Number(args[0]); i++) {
  console.log('C is fun');
}
