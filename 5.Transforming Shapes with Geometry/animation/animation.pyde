xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangex = xmax - xmin
rangey = ymax - ymin

t = 0 # time variable

def setup():
    global xscl, yscl
    size(1000,1000) # defines the size of the coordinate plane
    xscl = width / rangex
    yscl = -height / rangey
    
    rectMode(CENTER) # sets the rectangle's center as the center, not the top left

def draw():

    global t
    # sets up the grid to look pretty and centered
    background(255)
    translate(width/2, height/2) # shifts the entire grid such that 0,0 is the origin, not the top left corner
    # note that width and height become whatever numbers we use in the size() function
    strokeWeight(0.25) # sets the thickness of the line
    grid(xscl,yscl)
    
    rotate(radians(t)) # rotates grid by 1 degrees
    
    # for i in range(12): # circle rotation
        # rect(200,0,50,50)
        # grid(xscl,yscl)
        # rotate(radians(360/12))
    
    
    # for i in range(12): # crazy rotations about themselves
        # translate(200,0)
        # rotate(radians(t))
        # rect(0,0,50,50)
        # # grid(xscl,yscl)
        # rotate(radians(360/12))
    
    for i in range(12): # using new functions to properly rotate the squares
        pushMatrix() # saves the orientation
        # grid(xscl,yscl)
        translate(200,0)
        rotate(radians(5*t))
        # grid(xscl,yscl)
        rect(0,0,50,50)
        popMatrix() # returns to the saved orientation
        # grid(xscl,yscl)
        rotate(radians(360/12))
        
    t += 1 # increments time variable

def grid(xscl, yscl):
    # draws the grid for the graph
    stroke(0,255,255) # sets the line colors; cyan, in this case
    
    for i in range(xmin, xmax+1): # creates the grid lines for the graph
        line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)
    for i in range(ymin, ymax+1): # initxcor, initycor, finxcor, finycor
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
        
    stroke(0) # sets the line to black 
    line(xmin*xscl, 0, xmax*xscl, 0)
    line(0, ymin*yscl, 0, ymax*yscl)
