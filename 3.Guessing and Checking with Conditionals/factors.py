## Define a function that shows even factors of a given number
# def factors(num):
  # factors = []
  # for i in range(1, num + 1):
    # if (num % i == 0):
      # factors.append(i)
  # return factors
# print(factors(120))

#---
### 3-1 Finding the Factor
def GCF(a, b):
  factorsA = []
  factorsB = []
  gcf = []
  for i in range(1, a):
    if (a % i == 0):
      factorsA.append(i)
  for i in range(1, b):
    if (b % i == 0):
      factorsB.append(i)
  for i in factorsA:
    for j in factorsB:
      if (i == j) and (i not in gcf) and (j not in gcf):
        gcf.append(i)
  return gcf[-1]

print(GCF(324,756))
