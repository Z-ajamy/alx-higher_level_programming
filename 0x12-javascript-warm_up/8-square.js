#!/usr/bin/node
const x = +process.argv[2];
if (x) {
  let str = 'X';
  for (let i = 1; i < x; i++) {
    str += 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(str);
  }
} else {
  console.log('Missing size');
}
