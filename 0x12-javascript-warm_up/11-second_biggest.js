#!/usr/bin/node

// Extract and convert arguments to integers
const args = process.argv.slice(2).map(arg => parseInt(arg, 10));

// Remove duplicates and sort in descending order
const uniqueArgs = [...new Set(args)].sort((a, b) => b - a);

// Print the second largest number if available, otherwise print 0
console.log(uniqueArgs.length >= 2 ? uniqueArgs[1] : 0);
