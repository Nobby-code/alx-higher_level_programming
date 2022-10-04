#!/usr/bin/node

// printing the number of arguments already printed and the new arg value

let i = 0;
exports.logMe = function (item) {
  console.log(i + ': ' + item);
  i++;
};
