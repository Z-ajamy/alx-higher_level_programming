#!/usr/bin/node
exports.converter = function (base) {
  return function (A) {
    return parseInt(A, base);
  }
}
