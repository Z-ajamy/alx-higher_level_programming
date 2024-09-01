#!/usr/bin/node
function factorial (a) {
  let res = 1;
  for (let i = 1; i <= a; i++) {
    res *= i;
  }
  console.log(res);
}

let x = +process.argv[2];
if (!x) {
  x = 1;
}
factorial(x);
