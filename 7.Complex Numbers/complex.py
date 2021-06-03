def cAdd(a, b):
  # adds two complex numbers
  return [a[0] + b[0], a[1] + b[1]] # looks similar to vector addition

u = [1,2]
v = [3,4]
print(cAdd(u,v))
