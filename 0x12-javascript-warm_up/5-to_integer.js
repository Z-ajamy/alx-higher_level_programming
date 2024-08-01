#!/usr/bin/node

const args = process.argv;
const num = parseInt(args[2], 10);

// Check if parseInt returns NaN
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
