#!/usr/bin/env node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('Missing size');
  process.exit();
}

const size = Number(args[0]);
for (let i = 0; i < size; i++) {
  console.log('X'.repeat(size));
}
