# t = 0
# points = []

def setup():
    size(600,600)
    noStroke()
    colorMode(HSB)
    
def draw():
    # global t, points
    background(255) # white background
    translate(width/2, height/2)
    
    t = 0
    points = []
    
    while t < 255: # saves 255 points so that we don't have to draw everything in real time
        # 250 points is the best balance between too much going to and too little going on 
        points.append(harmonograph(t)) # saves the coordinates to the lsit
        t += 0.01 # increments time
        # in this way, we don't have to watch the program draw the picture slowly
        # but all at once
    
    # points.append(harmonograph(t)) # saves the coordinates to the lsit
    
    
    for i, pnt in enumerate(points): # draws the points based on the harmonograph function
        stroke(i/100,255,255) # sets line color to rainbow(?)
        if i < len(points) - 1: # stops one point from the last one to avoid bounds error
            line(pnt[0], pnt[1], points[i+1][0], points[i+1][1]) # draws line from one points to the very next one
            # this creates a very smooth drawing
    
    # t += 0.01
    
def harmonograph(t): # define the harmonograph function
    
    a1,a2,a3,a4 = 100,100,100,100         # amplitudes
    f1,f2,f3,f4 = 2.01,3,3,2              # frequencies
    p1,p2,p3,p4 = -PI/2,0,-PI/16,0        # phase shifts
    d1,d2,d3,d4 = 0.00085,0.0065,0,0      # decay constants
    
    ## note that this is the location of the pen as a result of oscillation
    # note that this is still only ONE pendulum affecting the x and y of the pen
    x = a1*cos(f1*t + p1)*exp(-d1*t) + a3*cos(f3*t + p3)*exp(-d3*t) # equations for double oscillatory motion 
    # note that we just add another term of the general oscillatory motion equation 
    y = a2*sin(f2*t + p2)*exp(-d2*t) + a4*sin(f4*t + p4)*exp(-d4*t) # without the exp, program will draw the same lines infinitely due to oscillatory behaviours
    # but, the exp 'chips' away at the amplitude of the pattern
    
    return [x, y] # returns the values of the x and y coordinate
