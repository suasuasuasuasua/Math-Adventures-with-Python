# color grid activity notes

## drawing a grid of objects

- we will want to create a grid that is 20x20, having 25x25 pixel squares
- to do this, we will define two for-loops, drawing a rectangle every 30 pixels (30 x 20 = 600)

## adding the rainbow color

- Processing defines a function called colorMode() that allows us to add colors to our sketches
- colorMode() uses HSB, which is hue, saturation, and brightness
  - we will be working with hue
- dist() is another function that calculates the distance between two 2D coordinates
  - we will use it to calculate the distance between a square and the mouse cursor
