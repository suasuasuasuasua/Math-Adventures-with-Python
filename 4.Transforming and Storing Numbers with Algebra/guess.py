def f(x):
  # return 6*x**3 + 31*x**2 + 3*x - 10 # x = -5, -2/3, 1/2
  return 2*x**2 + 7*x - 15 # x = -5, 1.5

def average(a, b): # used to get average between two points
  return (a + b) / 2.0
  
def guess(): # solves for when f(x) is closest to 0
  # lower = -1.0 # we are trying to solve for the x between -1.0 and 0.0
  # upper = 0.0
  lower = 1.0
  upper = 2.0
  for i in range(20): 
    midpoint = average(lower, upper) # gets the midpoints between the bounds
    if f(midpoint) == 0:
      return midpoint
    elif f(midpoint) > 0:
      lower = midpoint
    else:
      upper = midpoint
  return midpoint

x = guess()
print(x, f(x))
