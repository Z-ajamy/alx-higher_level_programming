#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let shap = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        shap += c;
      }
      if (i < this.height - 1) {
        shap += '\n';
      }
    }
    console.log(shap);
  }
}
module.exports = Square;
