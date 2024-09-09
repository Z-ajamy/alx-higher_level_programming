#!/usr/bin/node
exports.esrever = function (list) {
  const l = [];
  for (const i of list) {
    l.unshift(i);
  }
  return l;
};
