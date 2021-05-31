from turtle import * # imports all functions from the turtle module

speed(0) # changes the speed of the animation

### note that the turtle object may only move in the direction that it faces
# forward(100)
# right(45)
# forward(150)

#---
### 1-1 Square Dance
## using loops to draw a square

# for i in range(4): # the turtle moves in a square in this loop
  # forward(200)
  # right(90)

# def square(sideLength = 200): 
  # for i in range(4):
    # forward(sideLength)
    # right(90)

# square() 

#---
### 1-2 A Circle of Squares
## creates a pretty cool shape of 72 squares, rotating 5 degrees each time

# for i in range(72): 
  # square()
  # right(5)

#---
### 1-3 Tri and Tri Again
## write a triangle() function to draw a triangle

# def triangle(sideLength):
 # for i in range(3):
  # forward(sideLength)
  # right(180 - 60) # note that this angle is with respect to the direction of motion. we would need to use the external angle

# triangle(200)

#---
### 1-4 Polygon Functions
## write a function called polygon() that draws an arbitrary polygon based on number of sides

# def polygon(numSides): 
  # for i in range(numSides): # draws a line for each side, rotating depending on the number of sides
    # forward(100)
    # right(360  - (360.0 / numSides)) # the interior side depends on the number of sides

# polygon(10)

#---
### 1-5 Turtle Spiral
## write a function to draw 60 squres, turning 5 degrees, making each square larger

# def spiralSquares():
  # sideLength = 5 # initial side length of 5
  # for i in range(60): # iterates 60 times
    # for i in range(4): # draws a square of sideLength
      # forward(sideLength)
      # right(90)
    # sideLength += 5 # sideLength increases by 5 each time a square is drawn
    # right(5) # rotates by 5 deg as well

# spiralSquares()

#---
### 1-6 A Star is Born
## write a function that will draw a spiral of stars

def spiralStars():
  sideLength = 5 # initial side length of 5
  for i in range(60): # iterates 60 times
    for i in range(5): # draws a star of sideLength
      forward(sideLength)
      right(180 - (180 / 5.0)) # 5 pointed stars have an internal angle of 180 / 5.0
    sideLength += 5
    right(5)

spiralStars()
input() # lets the image stay longer
