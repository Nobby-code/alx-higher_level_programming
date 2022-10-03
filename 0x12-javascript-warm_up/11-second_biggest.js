#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

/*
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.sort();
  console.log(list.reverse()[1]);
} 
*/

const mySol = process.argv;
if (mySol.length <= 3) {
  console.log(0);
} else {
  console.log(mySol.sort((x, y) => y - x).slice(3)[0]);
}
