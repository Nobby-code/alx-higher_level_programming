#!/usr/bin/node

// Second biggest integer in the list of argumens

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const sortedList = process.argv.sort();
  console.log(sortedList.reverse()[1]);
}
