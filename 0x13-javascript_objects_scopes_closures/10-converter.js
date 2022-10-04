#!/usr/bin/node

// pass a number from base 10 to base passed as an argument

exports.converter = function (base) {
  return function (argv) {
    return argv.toString(base);
  };
};
