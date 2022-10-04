#!/usr/bin/node

// Rectangle class with a constructor having 2 arguments
// if w or h is 0, create an empty object

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
