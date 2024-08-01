#!/usr/bin/node

const args = process.argv;

// Check if there is at least one argument after the script name
if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
