#!/usr/bin/node
function add (a, b) {
  if (isNaN(a)) console.log('NaN');
  else if (isNaN(b)) console.log('NaN');
  else console.log(Number(a) + Number(b));
}

add(process.argv[2], process.argv[3]);
