#!/usr/bin/node
function factorial(x) {
  if (x === 0 || x === undefined || isNaN(x)) return 1;

  else {
    return (x * factorial(x - 1));
  }
}

console.log(factorial(process.argv[2]))
