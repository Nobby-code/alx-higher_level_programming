#!/usr/bin/node

// Rectangle class with a constructor having 2 arguments
// if w or h is 0, create an empty object
// adding a method called print(), rotate(), double()

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // swapping height and width
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // doubling height and width
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
