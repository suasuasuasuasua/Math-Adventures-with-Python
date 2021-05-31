### 3-2 Finding the Square Root
## Find the square root of 200, 1000, 50000
def average(a, b):
  return (a + b) / 2

def squareRoot(num, lower, upper):
  for i in range(200):
    guess = average(lower, upper)
    if guess ** 2 == num:
      print(guess)
      break
    elif guess ** 2 > num:
      upper = guess
    else:
      lower = guess
  print(guess)

squareRoot(60, 7, 8)
squareRoot(200, 14, 15)
squareRoot(1000, 100, 101)
squareRoot(50000, 1, 500)
