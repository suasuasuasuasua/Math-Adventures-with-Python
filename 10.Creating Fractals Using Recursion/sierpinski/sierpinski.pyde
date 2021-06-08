frame = 0

def setup():
    size(600,600)

def draw():
    global frame
    
    background(255)
    
    level = int(map(mouseX,0,width,0,10))
    sz = map(mouseY,0,height,0,400)
    
    translate(-sz/2 + width/2, sz/(2*sqrt(3)) + height/2)
    
    sierpinski(sz,level)
    
    # fill(255,255,0)
    # ellipse(0,0,20,20)
    # ellipse(sz/2.0,-sz*sqrt(3)/2.0,20,20)
    # ellipse(0,0,20,20)
    
    save('frames/sierpinski ' + str(frame) + '.jpg')
    
    frame += 1
    if frame == 300:
        exit()

def sierpinski(sz, level):
    if level == 0: # default case triangle that is black
        fill(0)
        triangle(0,0,sz,0,sz/2.0,-sz*sqrt(3)/2.0) # draws an equilateral triangle
    else:
        for i in range(3): # draws 3 other triangles
            sierpinski(sz/2.0, level - 1) # draws triangles half the size
            translate(sz/2.0,-sz*sqrt(3)/2.0)
            rotate(radians(120))
            
