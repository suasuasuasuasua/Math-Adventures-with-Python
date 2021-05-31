# this is a general solution for all first degree polynomials
def equation(a, b, c, d):
  return (d - b) / (a - c) # we can derive this by solving ax + b = cx + d

print(equation(2 ,5 ,0 ,13))
### 4-1 Solving more Equations for X
## solve 12x + 18 = -34x + 67

print(equation(12, 18, -34, 67))

#---
### 4-2 Fractions as Coefficients
## solve 1/2x + 2/3 = 1/5x + 7/8

print(equation(1/2, 2/3, 1/5, 7/8))
