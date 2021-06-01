# Geometry Activity Notes

## Coordinates
- the origin is located at the top left corner
- increasing x going to the right; increasing y means going down
- each coordinate on a window plane represents a pixel

## Transformation

### Translating Objects
- a translatio is defined by moving an object, without changing its orientation or size
- we use the translate() function 
- in Processing, translate() moves the grid, not the objects on the grid
  - this means that we don't have to change the coordinates of our objects, per se
- translate(width/2, height/2) moves the origin to the center of the screen

### Rotating Objects
- a rotation is defined by turning an object about its center point, without moving or changing size
- rotate() rotates the grid around the origin (0,0)
  - rotate() takes a single argument which is the angle around the point (0,0)
  - note that the angle is defined in radians, so you may need to convert from degrees
- note that we need to translate the grid, then rotate because order matters

## Animating 
- we may define a time variable 't' in order to see the transformations of our objects
- we declare 't' as a global variable, then use it as a rotation variable
  - rotate(radians(t)), for instance, where we increment t each loop
- Processing has two functions that allow us to save orientations of the grid:
  - pushMatrix() saves the orientation
  - popMatrix() returns to the saved orientation
