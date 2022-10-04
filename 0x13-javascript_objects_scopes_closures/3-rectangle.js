#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1 || isNaN(w) || isNaN(h)) {
      return (this);
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let chara = '';
      for (let j = 0; j < this.width; j++) {
        chara += 'X';
      }
      console.log(chara);
    }
  }
};
