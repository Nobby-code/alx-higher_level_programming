#!/usr/bin/node

// Script tp print the first argument passed to it

const firstArg = process.argv[2];

if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
