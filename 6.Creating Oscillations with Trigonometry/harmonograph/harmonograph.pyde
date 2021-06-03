def setup():
    size(600,600)
    noStroke()
    
def draw():
    
    background(255) # white background
    translate(width/2, height/2)
    
    t = 0
    points = []
    
    while t < 1000: # saves 1000 points so that we don't have to draw everything 
        points.append(harmonograph(t)) # saves the coordinates to the lsit
        t += 0.01 # increments time
        # in this way, we don't have to watch the program draw the picture slowly
        # but all at once
        
    
    for i, pnt in enumerate(points): # draws the points based on the harmonograph function
        stroke(0) # sets line color to black
        if i < len(points) - 1: # stops one point from the last one to avoid bounds error
            line(pnt[0], pnt[1], points[i+1][0], points[i+1][1]) # draws line from one points to the very next one
            # this creates a very smooth drawing
    
def harmonograph(t): # define the harmonograph function
    
    a1,a2 = 200,200    # amplitudes
    f1,f2 = 3,3.025       # frequencies
    p1,p2 = PI/6, PI/2    # phase shifts
    d1,d2 = 0.02, 0.02 # decay constants
    
    ## note that this is the location of the pen as a result of oscillation
    # note that this is still only ONE pendulum affecting the x and y of the pen
    x = a1*cos(f1*t + p1)*exp(-d1*t) # equations for the oscillatory motion 
    y = a2*sin(f2*t + p2)*exp(-d2*t) # without the exp, program will draw the same lines infinitely due to oscillatory behaviours
    # but, the exp 'chips' away at the amplitude of the pattern
    
    return [x, y] # returns the values of the x and y coordinate
