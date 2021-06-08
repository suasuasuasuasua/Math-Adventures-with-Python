frame = 0

def setup():
    size(600,600)

def draw():
    global frame
    
    background(255) # white background
    translate(width/2, 3 * height/4)
    level = int(map(mouseX, 0, width, 0, 15)) # tracks the mouse in the x-direction, returning values between 0 and 10, as the mouse moves between the left and right edges of the window
    y(100, level)

    save('frames/fractals ' + str(frame) + '.jpg')
    frame += 1
    
    if frame == 300:
        exit()

def y(sz,level):
    if level > 0:
        line(0,0,0,-sz) # draws a parent branch depending on given size
        translate(0,-sz) # moves to the end of the trunk/parent branch
        angle = map(mouseY, 0, height, 0, 180) # tracks the mouse in the y-direction, returning values between 0 and 180, as the mouse moves between the top and bottom of the window
        rotate(radians(angle)) # rotates at the end of the line, preparing to draw more lines branching outward
        y(0.8*sz,level-1) # creates pattern emenating from the original trunk going rightward
        rotate(radians(-2 * angle)) # rotates the other direction, such that both branches the 30 deg with respect to the parent branch normal
        y(0.8*sz,level-1) # creates pattern emenating from the original trunk going leftward this time
        rotate(radians(angle)) # rotates back to normal
        translate(0,sz) # returns to the original location of the parent branch
        
