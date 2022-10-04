#!/usr/bin/node
const data = require('./100-data.js').list;
let index = -1;
function compute (num) {
  index++;
  return (num * index);
}

const map1 = data.map(compute);
console.log(data);
console.log(map1);
