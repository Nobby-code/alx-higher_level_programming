#!/usr/bin/node

// Script tp print the first argument passed to it

const first_arg = process.argv[2];

if (first_arg === undefined) {
  console.log('No argument');
} else {
  console.log(first_arg);
}
