#!/usr/bin/node

// Script thwt imports a dictionary of occurrences by user id
// computes a dictionary of user ids by occurrences

const dict = require('./101-data').dict;

const newDict = {};

Object.keys(dict).map(function (key, index) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
  return newDict;
});

console.log(newDict);
