### Write a function that calculates the average of two numbers

# def averageTwo(a, b):
  # return (a + b) / 2 # order of operations matters

# print(averageTwo(10,20))

#---
### 2-1 Finding the Sum
## Find the sum of all numbers from 1 to 100, 1 to 1000

# def summation(lower, upper): # this summation function sums from a lower to upper bound
  # total = 0
  # for i in range(lower, upper + 1):
   # total += i
  # return total

# print(summation(1,100))
# print(summation(1,1000))

#---
### 2-2 Finding the Average
## Find the average of the numbers in the following list

d = [53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42, 15, 96, 11, 70, 83, 97, 75]

def average(numList):
  return sum(numList) / len(numList)

print(average(d))
