#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!(w === 0 || h === 0 || (h * w) <= 0 || isNaN(h * w))) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let shap = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        shap += 'X';
      }
      if (i < this.height - 1) {
        shap += '\n';
      }
    }
    console.log(shap);
  }
}
module.exports = Rectangle;
