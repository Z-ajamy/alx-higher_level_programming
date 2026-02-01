#!/usr/bin/evv node

exports.esrever = function (list) {
  const arr = [];
  let maxIndex = list.length - 1;
  for (let i = 0; i < list.length; i++) {
    arr[maxIndex] = list[i];
    maxIndex -= 1;
  }
  return arr;
};
