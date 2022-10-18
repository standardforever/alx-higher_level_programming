#!/usr/bin/node
const myVar = process.argv
if (!isNaN(myVar[2])) {
    let newVar = 'X'
  for (let i = 0; i < myVar[2]; i++) {
    for (let j = 1; j < myVar[2]; j++) {
      newVar += 'X' 
    }
    console.log(newVar)
    newVar = 'X'
  }
}
else console.log('Missing size')
