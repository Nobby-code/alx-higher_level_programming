#!/usr/bin/node

// Script convert first argument to number if convertable

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Number(process.argv[2])}`);
}
