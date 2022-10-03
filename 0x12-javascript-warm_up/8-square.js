#!/usr/bin/node

// Script that prints a square

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (i = 0; i < Number(process.argv[2]); i++) {
    console.log('X'.repeat(Number(process.argv[2])));
  }
}
