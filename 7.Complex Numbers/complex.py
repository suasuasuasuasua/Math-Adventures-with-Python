from math import sqrt

def cAdd(a, b):
  # adds two complex numbers
  return [a[0] + b[0], a[1] + b[1]] # a + c, b + d

# u = [1,2]
# v = [3,4]
# print(cAdd(u,v))

def cMult(u, v):
  return [u[0]*v[0] - u[1]*v[1], u[0]*v[1] + u[1]*v[0]] # ac - bd, ad + bc

# print(cMult(u, v))

def magnitude(z):
  return sqrt(z[0]**2 + z[1]**2) # solves for length of complex number relative to origin
