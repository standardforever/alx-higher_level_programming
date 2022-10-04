#!/usr/bin/node
const Squar = require('./5-square.js');

module.exports = class Square extends Squar {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let chara = '';
      for (let j = 0; j < this.width; j++) {
        chara += c;
      }
      console.log(chara);
    }
  }
};
