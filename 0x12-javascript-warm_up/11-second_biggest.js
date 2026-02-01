#!/usr/bin/env node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const list = args.map(Number);

  list.sort((a, b) => b - a);
  console.log(list[1]);
}
