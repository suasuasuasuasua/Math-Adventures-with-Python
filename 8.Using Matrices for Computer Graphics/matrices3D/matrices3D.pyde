# sets the range of x-values
xmin = -10
xmax = 10

# sets the range of y-values
ymin = -10
ymax = 10

# calculates the respective ranges
rangex = xmax - xmin
rangey = ymax - ymin

t = 0
frame = 0

def setup():
  global xscl, yscl
  size(600,600)
  # sets the scale factors for drawing on the grid
  xscl = width/rangex
  yscl = -height/rangey
  
  noFill()

def draw():
  global xscl,yscl,t,frame
  # preprocessing
  background(255) # set background to white
  translate(width/2, height/2)
  grid(xscl, yscl)

  # rot = map(mouseX, 0, width, 0, TWO_PI)
  # tilt = map(mouseY, 0, width, 0, TWO_PI)
  rot = t*0.25
  tilt = t*0.5

  transformedMatrix = transpose( multMatrix( rottilt(rot, tilt), transpose(fmatrix) ) ) # calculates the new transformed matrix
  
  strokeWeight(2) # a slightly thicker line
  stroke(255,0,0) # sets line color to red

  graphPoints(transformedMatrix, edges)

  save('frames/matrices3D ' + str(frame) + '.jpg')
  frame += 1
  t += 0.02
  
  if frame == 300:
      exit()

# coordinates of vertices of a 'f' shape
# we need to define the z-axis for our f-shape
# 2D objects have a z-value of 0
fmatrix = [ [0,0,0],
            [1,0,0],
            [1,2,0],
            [2,2,0],
            [2,3,0],
            [1,3,0],
            [1,4,0],
            [3,4,0],
            [3,5,0],
            [0,5,0] ]

# we add the exact same f-shape, however the z-value is 1 across the board
# the result is a boxy f-shape
# we can't exactly see how it is 3D, so we will need to transform it
fmatrix += [ [0,0,1],
             [1,0,1],
             [1,2,1],
             [2,2,1],
             [2,3,1],
             [1,3,1],
             [1,4,1],
             [3,4,1],
             [3,5,1],
             [0,5,1] ]

# since we defined two layers for the f-shape, we need to connect the points on the front layer with those on the rear layer
# this list will be used to keep track of which points are going where
# ex. [0,10] draws a segment between point 0 (0,0,0) and point 10 (0,0,1) *the upper F*
edges = [ [0,1], # draws the first F
          [1,2],
          [2,3],
          [3,4],
          [4,5],
          [5,6],
          [6,7],
          [7,8],
          [8,9],
          [9,0],
          [10,11], # draws the rear F
          [11,12],
          [12,13],
          [13,14],
          [14,15],
          [15,16],
          [16,17],
          [17,18],
          [18,19],
          [19,10],
          [0,10], # draws edges to connect the Fs
          [1,11],
          [2,12],
          [3,13],
          [4,14],
          [5,15],
          [6,16],
          [7,17],
          [8,18],
          [9,19] ]
          
# note that vector notation is different than coordinate notation
# for example, the vector (1,2) would be represented as [ 1 ] like as 2x1 matrix, rather than a 1x2 matrix                                               [ 2 ]
# this means that we need to transpose our fmatrix so that we can properly multiply properly


# rotation_matrix = [ [1,0],
                     # [0,1]  ]
# rotation_matrix = [ [0,-1],
                    #  [1,0]  ]

### 8-1 More Transformation Matrices
## Check out what happens if you change the transformation matrix to these
# rotation_matrix = [ [1,0],
                    # [1,-1]  ]
# rotation_matrix = [ [0,-1],
                    # [-1,0]  ]
# rotation_matrix = [ [-1,1],
                    # [1,1]  ]

def graphPoints(pointList, edges): # function to graph points, given a matrix of points
  # pointList will be the f-matrix
  # edges will be the edges-matrix that we defined earlier

  # this loop draws a line beginning from the point list to the next defined edge
  for e in edges: 
    # let e = [0,1]
    # pointList[e[0]][0] = 0
    # pointList[e[0]][1] = 0
    # pointList[e[1]][0] = 1
    # pointList[e[1]][1] = 0
    line(pointList[e[0]][0]*xscl, pointList[e[0]][1]*yscl, pointList[e[1]][0]*xscl, pointList[e[1]][1]*yscl)
    # print(pointList[e[0]][0]*xscl, pointList[e[0]][1]*yscl, pointList[e[1]][0]*xscl, pointList[e[1]][1]*yscl)

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

# rotates/tilts the grid depending on mouse location
def rottilt(rot, tilt):
  # returns the matrix for rotating some number of degrees
  # rot is functionally equivalent to theta
  # tilt is also functionally equivalent to theta
  # it happens to rot_y will rotate, rot_x will tilt
  rotmatrix_Y = [ [cos(rot) , 0.0, sin(rot)], # the y-axis serves as the axis of rotation here
                  [0.0      , 1  , 0.0     ],
                  [-sin(rot), 0.0, cos(rot)] ]

  rotmatrix_X = [ [1.0      , 0.0       , 0.0      ], # the x-axis serves as the axis of rotation
                  [0.0      , cos(tilt) , sin(tilt)],
                  [0.0      , -sin(tilt), cos(tilt)] ]

  return multMatrix(rotmatrix_Y, rotmatrix_X)
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
