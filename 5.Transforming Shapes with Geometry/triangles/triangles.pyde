def setup():
    size(600,600)
    rectMode(CENTER)
    colorMode(HSB)

t = 0 # time variable

def draw():
    global t
    
    translate(width/2,height/2)
    background(255) # sets background to white
    
    rotate(radians(t)) # rotates the grid, such that the sketch mimics an animation
    # triangle(0,0,100,100,200,-200) # bad way to create triangles
    # equalTri(200) # calls the function to draw an equilateral triangle
    
    ### 5-1 Spin Cycle
    ## Create a circle of equilaterla triangles 
    for i in range(12): # animates a circle of triangles like before
        pushMatrix() # sets default location
        translate(200, 0) # moves the outer bound of circle
        rotate(radians(t)) # rotates triangle itself
        fill(t * 0.05 * i,255,255) # fills in a different color
        equalTri(50) # creates a triangle with length 50 (based on 30-60-90)
        popMatrix() # resets back to original grid location
        rotate(radians(360/12)) # rotates to new position in circle
    
    t += 0.5
     
def equalTri(length): # length is defined as the hypotenuse of an arbitrary 30-60-90 triangle
    # draws an equilateral triangle around the center of triangle, based on length
    triangle(0, -length, -length*sqrt(3)/2, length/2, length*sqrt(3)/2, length/2)
