#!/usr/bin/node

// Script that imports an array and then multiply by its index

const list = require('./100-data').list;
console.log(list);
const newList = list.map(function (num, index) {
  return num * index;
});
console.log(newList);
