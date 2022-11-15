#!/usr/bin/node

/* script to write scring to a file */

const fs = require('fs');
const fileName = process.argv[2];
const fileContent = process.argv[3];

fs.writeFile(fileName, fileContent, 'utf8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log('write success');
  }
});
