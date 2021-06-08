frame = 0

def setup():
    size(600,600)

def draw():
    global frame

    background(255)
    
    level = int(map(mouseX,0,width,0,7)) # mouse-X determines how many levels will exist
    sz = map(mouseY,0,height,0,400) # mouse-Y determine the sz
    
    translate(-sz/2+width/2,-sz/(2*sqrt(3))+height/2) # centers the triangle perfectly
    
    snowflake(sz,level)

    save('frames/snowflake ' + str(frame) + '.jpg')
    frame += 1
    if frame == 300:
        exit()

def snowflake(sz,level):
    for i in range(3): # draws 3 sides of an equilateral triangle
        segment(sz,level)
        rotate(radians(120)) # rotates such that the triangle's interior angle is 60

def segment(sz, level):
    if level == 0: # default case just draws a line 
        line(0,0,sz,0)
        translate(sz,0)
    else:
        # segments of the same level are the same sz
        segment(sz/3.0, level-1)
        # line(0,0,sz/3.0,0) # draws a line that is one-third of the sz
        # translate(sz/3.0,0) # moves to the end of the line
        rotate(radians(-60)) # rotates 60 degrees left

        segment(sz/3.0, level-1)
        # line(0,0,sz/3.0,0) 
        # translate(sz/3.0,0)
        rotate(radians(120)) # rotates back down

        segment(sz/3.0, level-1)
        # line(0,0,sz/3.0,0)
        # translate(sz/3.0,0)
        rotate(radians(-60)) # turns left, starting at the same initial position

        # line(0,0,sz/3.0,0)
        # translate(sz/3.0,0)
        segment(sz/3.0, level-1)
