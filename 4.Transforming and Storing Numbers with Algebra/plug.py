"""
this is a brute force method of solving this equation.

we make an educated guess that x is between -100 and 100, then check every integer between
"""
def plug():
  x = -100
  while x < 100:
    if 2*x + 5 == 13:
      print("x =", x)
      break
    x += 1

plug()
