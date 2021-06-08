"""
there are two things that we want to pay attention to when we write the gaussian elimination algorithm function.

  1. dividing all elements in a row by a constant
  2. adding one row(multiplied by an appropriate constant) to another row
...such that we work toward the identity matrix

we can do this efficiently by using python's built-in enumerate() function
"""

# # task 1. dividing all elements in a row
# divisor = 2
# row = [1,2,3,4,5]
# for i, term in enumerate(row): # this loop will iterate through the list, dividing and reassigning each element
# # we keep track of both the index and the value so that we can update the rows accordingly
  # row[i] = term / divisor
# print(row)

# # task 2. adding one row to another row
# # the tricky part is that we need to add respective elements 

# my_matrix = [ [2,-4,6,-8],
              # [-3,6,-9,12] ]

# # note that this loop iterates for how ever many entries there are in the row
# # the loop does not have to be complicated because we are only working with two rows at a time
# for i in range(len(my_matrix[1])): # this loop will iterate through the list, then add elements from the first row to the other row
  # my_matrix[1][i] += my_matrix[0][i] # this is where the respective elements are updated
# print(my_matrix)

#---------

## now that the basic ideas are out of the way, we need to work on repeating the process so long that we don't have a identity matrix

def gauss(A):

  m = len(A) # number of rows
  n = len(A[0]) # numbers of columns in the matrix

  for j, row in enumerate(A):
    # print(A)
    # set pivot term to equal 1
    if row[j] != 0: # row[j] will be defined as the diagonal entries of the matrix
      # moreover, the diagonal entry is when the row and column indices are equal
      divisor = row[j] # sets the divisor equal to the pivot element
      for i, term in enumerate(row): # iterates over the row for column number of times
        row[i] = term / divisor # reassigns the row by dividing the original term by the pivot element
        # note that any negative pivot values will automatically be assigned 1 

  # now we need to calculate the additive inverse such that we can work toward the identity matrix

    for i in range(m):
      # print(A)
      # print(i,j)
      # print(A[i][j])
      if i != j:
        # calculate the additive inverse
        addInv = A[i][j] * -1
        # print(addInv)
        for ind in range(n):
          # add corresponding term in jth row to the term in the ith row
          A[i][ind] += A[j][ind] * addInv

  return A # the solution will be the last indices of the rows put together

# A = [ [2,1,-1,8], # this is the matrix that we will be working with
      # [-3,-1,2,-1],
      # [-2,1,2,-3] ]

# print(gauss(A))

C = [ [ 2, -1, 5, 1, -3],
      [ 3, 2, 2, -6, -32],
      [ 1, 3, 3, -1, -47 ],
      [5,-2, -3, 3 , 49] ]

solutionC = gauss(C)
x = []

for row in solutionC:
  x.append(row[-1])

print(x)
