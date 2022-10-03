#!/usr/bin/node

// Script that prints x time "C is fun"

const myVar = 'C is fun';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log(myVar);
  }
}
