# sets the range of x-values
xmin = -10
xmax = 10

# sets the range of y-values
ymin = -10
ymax = 10

# calculates the respective ranges
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
  global xscl, yscl
  size(600,600)
  # sets the scale factors for drawing on the grid
  xscl = width/rangex
  yscl = -height/rangey
  
  noFill()

def draw():
  global xscl,yscl
  background(255) # set background to white
  translate(width/2, height/2)
  grid(xscl, yscl)

  strokeWeight(2) # a slightly thicker line
  stroke(0) # sets line color to black

  # rotatedMatrix = multMatrix(fmatrix, rotation_matrix) # incorrect way of doing it
  # note that we have to transpose the the matrix product back into coordinate form so that we can plot it on our graph
  # the problem becomes obvious when we print the list

  # print(multMatrix( rotation_matrix, transpose(fmatrix) ) )
  rotatedMatrix = transpose(multMatrix( rotation_matrix, transpose(fmatrix) ) ) 
  # print(rotatedMatrix)
  graphPoints(fmatrix)

  stroke(255,0,0) # changes the color of the transformed matrix for clarity
  graphPoints(rotatedMatrix) # draws the transformed matrix

# coordinates of vertices of a 'f' shape
fmatrix = [ [0,0],
            [1,0],
            [1,2],
            [2,2],
            [2,3],
            [1,3],
            [1,4],
            [3,4],
            [3,5],
            [0,5] ]
# note that vector notation is different than coordinate notation
# for example, the vector (1,2) would be represented as [ 1 ] like as 2x1 matrix, rather than a 1x2 matrix                                               [ 2 ]
# this means that we need to transpose our fmatrix so that we can properly multiply properly


# rotation_matrix = [ [1,0],
                     # [0,1]  ]
# rotation_matrix = [ [0,-1],
                    #  [1,0]  ]

### 8-1 More Transformation Matrices
## Check out what happens if you change the transformation matrix to these
rotation_matrix = [ [1,0],
                    [1,-1]  ]
# rotation_matrix = [ [0,-1],
                    # [-1,0]  ]
# rotation_matrix = [ [-1,1],
                    # [1,1]  ]

def graphPoints(matrix): # function to graph points, given a matrix of points
  beginShape()
  for pt in matrix: # each row of a given matrix becomes the vertices
    vertex(pt[0]*xscl, pt[1]*yscl) # graphs the vertices of the matrix
  endShape(CLOSE)

def multMatrix(A, B): # function for multiplying two matrices
  
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

def transpose(a):
  aT = [] # resultant matrix is transposed
  m = len(a)    # number of rows
  n = len(a[0]) # number of elements in each row
  
  # defines an nxm matrix, since we are going to flip an mxn matrix 
  for i in range(n): # iterates n times as the go across the columns of a
    aT.append([]) # an empty list
    for j in range(m): # iterates m times, as we go down the rows of a
      aT[i].append(a[j][i]) # fills up the empty list with elements 
      # this is the line that switches the rows and columns of a
  return aT

def grid(xscl, yscl):
  strokeWeight(1)
  stroke(0,255,255)
  for x in range(xmin, xmax+1): # draws the grid lines
    line(x*xscl, ymin*yscl, x*xscl, ymax*yscl)
  for y in range(ymin, ymax+1):
    line(xmin*xscl, y*yscl, xmax*xscl, y*yscl)
  stroke(0) # black axes
  line(0, ymin*yscl, 0, ymax*yscl)
  line(xmin*xscl, 0, xmax*xscl, 0)
