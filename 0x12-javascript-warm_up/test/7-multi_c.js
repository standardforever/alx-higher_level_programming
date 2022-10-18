#!/usr/bin/node
const myVar = process.argv
if (!isNaN(myVar[2])) {
  for (let i = 0; i < myVar[2]; i++) {
    console.log('C is fun')
  }
}
else console.log('Missing number of occurrences')
