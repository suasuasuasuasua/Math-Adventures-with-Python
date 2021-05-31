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
    yscl = width / rangey # updates scaling so that everything can show up properly on screen
def draw():
    global xscl, yscl
    background(255)
    translate(width/2, height/2)
    
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin, xmax+1):
        line(i*xscl, ymin*yscl, i*xscl, ymax*xscl)
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
