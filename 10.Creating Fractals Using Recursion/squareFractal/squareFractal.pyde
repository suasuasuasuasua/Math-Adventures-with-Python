frame = 0

def setup():
    size(600,600)
    fill(150,0,150) # sets shape color to purple
    noStroke() # removes outline
    
def draw():
    global frame
    background(255)
    
    level = int(map(mouseX, 0, width, 0, 10))
    sz = map(mouseY, 0, height, 0, 500)
    
    translate(-sz/2.0 + width/2, -sz/2.0 + height/2)

    squareFractal(sz,level)
    
    save('frames/squareFractal ' + str(frame) + '.jpg')
    
    frame += 1
    if frame == 300:
        exit()
    
def squareFractal(sz, level):
    if level == 0: # defines default case for fractal
        rect(0,0,sz,sz)
    else:
        pushMatrix() # saves the original location for the grid
        squareFractal(sz/2.0, level - 1)
        translate(sz/2.0,0) # moves to the right edge of the top left square
        squareFractal(sz/2.0, level - 1)
        translate(-sz/2.0,sz/2.0) # moves to bottom left edge of the top left square
        squareFractal(sz/2.0, level - 1)
        popMatrix() # returns to the original location for the grid
        # without this, the squares would be super misplaced
