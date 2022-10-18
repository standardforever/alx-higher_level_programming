#!/usr/bin/node
const myVar = process.argv
let max;
let min;

if (myVar.length < 4) console.log(0)

else {
  if (myVar[2] >= myVar[3]) {
    max = myVar[2]
    min = myVar[3]
  }
  else {
    min = myVar[2]
    max = myVar[3]
  }
  for (let i = 2; i < myVar.length; i++) {
    if (myVar[i] > max) {
      min = max;
      max = myVar[i];
    }
    else if (min < myVar[i]) {
      min = myVar[i]
    }
  }
  console.log(min)
}

