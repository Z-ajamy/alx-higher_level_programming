#!/usr/bin/node
exports.converter = function (base) {
  return function (A) {
    return A.toString(base);
  };
};
