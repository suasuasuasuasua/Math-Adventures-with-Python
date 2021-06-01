xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    xscl = width / rangex
    yscl = -height / rangey # updates scaling so that everything can show up properly on screen
    # note that the graph would actually be upside down because of the way the windows work
    # i.e. top left is 0,0; increasing x means going to the right, increasing y means going down
def draw():
    global xscl, yscl # declares that we will use the previous xscl and yscl variables for drawing
    background(255) # sets the background to white
    translate(width/2, height/2) # moves the origin to the center of the window
    
    grid(xscl, yscl) # calls the grid function to draw a grid 
    graphFunction() # calls the function to graph f(x)

def f(x):
    # simple graph for f(x) = x^2
    # return x**2
    # return 6*x**3 + 31*x**2 + 3*x - 10 # now we can tackle the problem that we saw earlier to solve f(x)
    return (2*x**2 + 7*x - 15)

def graphFunction():
    # we can't just use a for-loop to graph points because the points will be unconnected
    # therefore, we will use a different kind of loop to draw the points closer together
    # the best way to draw a connected curve is to draw the lines from point to point
    x = xmin # start the points at the minimum x value
    while x <= xmax: # continue until the maximum x value
        stroke(255,0,0) # sets color to red
        # we will draw lines from one points to a point very close to it to
        # mimic curved lines (this is the essence of calculus)
        line(x*xscl, f(x)*yscl, (x+0.1)*xscl, f(x+0.1)*yscl)
        x += 0.1 # take a small step in the x direction in order to draw the next line
        # aka. dx

def grid(xscl, yscl):
    # draws the grid for the graph
    strokeWeight(1) # sets the thickness of the line
    stroke(0,255,255) # sets the line colors; cyan, in this case
    
    for i in range(xmin, xmax+1): # creates the grid lines for the graph
        line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)
    for i in range(ymin, ymax+1): # initxcor, initycor, finxcor, finycor
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
        
    stroke(0) # sets the line to black 
    line(xmin*xscl, 0, xmax*xscl, 0)
    line(0, ymin*yscl, 0, ymax*yscl)
