def factorial(n):
  if n == 0:
    return 1 # default case because 0! is defined as 1
  else:
    return n * factorial(n - 1) # returns the argument number multiplied by the factorial of itself minus 1

print(factorial(5))
