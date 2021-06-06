 # def addMatrices(A, B):

  # C = [ [A[0][0]+B[0][0], A[0][1]+B[0][1]],
        # [A[1][0]+B[1][0], A[1][1]+B[1][1]] ]

  # return C
      
def addMatrices(A,B): # general form of adding matrices
  C = []
  for i in range(len(A)): # iterates m times (equal to the number of rows)
    placeHold = [] # contains new rows of added entries
    for j in range(len(A[0])): # iterates n times (equal to the number of columns or entries in each row)
      placeHold.append(A[i][j] + B[i][j]) # adds the respective entries

    C.append(placeHold) # appends the placeholder list containing the added entries to the new matrix

  return C

def multMatrix(A, B):
  
  m = len(A) # number of rows in the first matrix
  n = len(B[0]) # number of columns in the second matrix

  C = []

  # iterates over every row in A
  for i in range(m):
    row = [] # row of 'dotted' numbers
    # iterates over every column in B
    for j in range(n):
      entry = 0 # entry that will be summed
      # iterates over every element in the column
      for k in range(len(B)):
        entry += A[i][k]*B[k][j]
      row.append(entry)
    C.append(row)
  return C

  print(C)
#  [2  3]  [1 -4]
#  [5 -8]  [8 -6]

A = [[2,3],
     [5,-8]]
B = [[1,-4],
     [8,-6]]
C = [[1,2,-3,-1]]
D = [[4,-1],
     [-2,3],
     [6,-3],
     [1, 0]]

print(addMatrices(A,B))
print(multMatrix(C,D))
