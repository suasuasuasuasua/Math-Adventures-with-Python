r1 = 300.0
r2 = 175.0
r3 = 5.0

prop = 0.5

x1 = 0
y1 = 0
t = 0
points = []

def setup():
    size(600,600)

def draw():
    
    global r1,r2,r3,x1,y1,t,prop,points
    
    background(255)
    translate(width/2, height/2)
    noFill()
    
    stroke(0)
    ellipse(x1, y1, 2*r1, 2*r1)
    
    x2 = cos(t)*(r1 - r2) 
    y2 = sin(t)*(r1 - r2)
    ellipse(x2, y2, 2*r2, 2*r2) # the inner circle will spin within the circumference of the outer circle
    
    x3 = x2+prop*(r2 - r3)*cos( -((r1-r2)/r2)*t )
    y3 = y2+prop*(r2 - r3)*sin( -((r1-r2)/r2)*t ) # solves for the positions of the drawing dot
    fill(255,0,0)
    ellipse(x3, y3, 2*r3, 2*r3)
    
    points = [[x3, y3]] + points[:2000] # we need to know both the x and y points, so we save them both in a list to the greater list
    for i, pnt in enumerate(points): # iterates over all of the points in the list
        if i < len(points) - 1: # draws up to the next to lsat point
            stroke(255,0,0) # red lines 
            line(pnt[0],pnt[1],points[i+1][0],points[i+1][1]) # draws lines between the current point and the point immediately after it
    
    t += 0.05
