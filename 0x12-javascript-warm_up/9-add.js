#!/usr/bin/node

// Script that prints the addition of two integers

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const result = add(process.argv[2], process.argv[3]);

console.log(result);
