xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600) # defines the size of the coordinate plane
    xscl = width / rangex
    yscl = -height / rangey

def draw():


    background(255)
    
    translate(width/2, height/2) # shifts the entire grid such that 0,0 is the origin, not the top left corner
    # note that width and height become whatever numbers we use in the size() function
    strokeWeight(0.25) # sets the thickness of the line
    grid(xscl,yscl)
    
    # rotate(radians(20)) # rotates the entire grid by 20 degrees clockwise
    # note that order does matter
    # strokeWeight(1) # sets the thickness of the line
    # grid(xscl,yscl)
    
    # for i in range(12): # creates a ring of circles
        # ellipse(200, 0, 50, 50) # the ellipse will rest on the y-axis, 200 units away, and have width/height of 50
        # rotate(radians(360 / 12)) # rotates the plane by 360/12 = 30 degrees 
    
    for i in range(12): # creates a ring of squares in the same way
        rect(200, 0, 50, 50)
        rotate(radians(360 / 12))
        

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
