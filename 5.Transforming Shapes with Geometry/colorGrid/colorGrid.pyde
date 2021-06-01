def setup():
    size(600,600)
    rectMode(CENTER)
    colorMode(HSB) # defines HSB color standard

def draw():
    background(0) # sets background to black
    
    # for x in range(20): # creates a 20x20 grid of squares that are all 25x25 pixels large
        # for y in range(20):
            # rect(30*x, 30*y, 25, 25)
    for x in range(30): # creates the grid again, only with color
        for y in range(30):
            d = dist(30*x, 30*y, mouseX, mouseY) # dist() measures the distance of the mouse to the respective location (the square)
            fill(0.5*d, 255, 255) # sets the color depending on the distance
            rect(30*x, 30*y, 25, 25) # draws the rectangle with the color in mind
