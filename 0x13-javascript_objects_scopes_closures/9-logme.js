#!/usr/bin/node
let counter_of_logMe = 0;
exports.logMe = function (item) {
  console.log(`${counter_of_logMe} : ${item}`);
  counter_of_logMe++;
}
