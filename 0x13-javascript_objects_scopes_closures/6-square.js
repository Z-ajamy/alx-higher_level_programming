#!/usr/bin/env node

const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let x = '';
        for (let j = 0; j < this.width; j++) {
          x = x + c;
        }
        console.log(x);
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
