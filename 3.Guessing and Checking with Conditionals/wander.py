from turtle import *
from random import randint # generates random integers

speed(0)

def wander(): # function to let the turtle wander between some boundaries
  while True:
    forward(3)
    if xcor() >= 200 or xcor() <= -200 or ycor() <= -200 or ycor() >= 200: # if the turtle exceeds the boundaries, turn
      left(randint(90,180)) # turn left some degrees between 90 and 180 

wander()
      
