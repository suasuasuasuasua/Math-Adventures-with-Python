r1 = 100
r2 = 10

circleList = []

t = 0

def setup():
    size(600,600)

def draw():
    background(255)
    translate(width/4, height/2)
    noFill()
    stroke(0)
    
    global t, circleList
    
    ## big circle
    ellipse(0, 0, 2*r1, 2*r1) # the last parameters are not radius, but width and height
    
    ## little red circle
    fill(255,0,0)
    x = r1*cos(t)
    y = -r1*sin(t) # reverses direction to draw properly
    
    circleList = [y] + circleList[:200] # adds y value to the start of a 200 length list
    ellipse(x, y, r2, r2)
    
    ## green ball that tracks the 'height' of the red ball
    stroke(0,255,0) # changes color to green
    line(x, y, 200, y) # this starts at the red ball's location (x,y), then ends at the green ball's location (200,y), as it depends on the red ball's height
    fill(0,255,0)
    ellipse(200, y, r2, r2) # x position is fixed, by its y will mirror the red ball's
     
    for i, y, in enumerate(circleList): # draws the sine waves based on the height of the red ball
        ellipse(200+i, y, 5, 5)
    
    t += 0.05
