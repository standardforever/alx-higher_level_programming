#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (h < 1 || w < 1 || isNaN(w) || isNaN(h)) {
      return (this);
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
