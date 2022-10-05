#!/usr/bin/node

// script that concatenates two files
// first argument is path of 1st file, 2nd argment for 2nd file
// 3rd argument for destination

const fs = require('fs');
const firstFile = fs.readFileSync(process.argv[2]).toString();
const secondFile = fs.readFileSync(process.argv[3]).toString();

fs.writeFileSync(process.argv[4], (firstFile + secondFile));
