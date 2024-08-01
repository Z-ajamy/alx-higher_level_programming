#!/usr/bin/node

const args = process.argv;

const arg1 = args[2] !== undefined ? args[2] : 'undefined';
const arg2 = args[3] !== undefined ? args[3] : 'undefined';

console.log(`${arg1} is ${arg2}`);
