frame = 0

def setup():
    size(600,600)
    rectMode(CENTER)
    colorMode(HSB)

t = 0 # time variable

def draw():
    global t, frame
    
    translate(width/2,height/2)
    background(255) # sets background to white
    # note that this paints a background over and over and over, such that you get 
    # clean animation, and not just a bunch of overlapping lines
    
    rotate(radians(t)) # rotates the grid, such that the sketch mimics an animation
    # triangle(0,0,100,100,200,-200) # bad way to create triangles
    # equalTri(200) # calls the function to draw an equilateral triangle
    
    ### 5-1 Spin Cycle
    ## Create a circle of equilaterla triangles 
    ### 5-2 Rainbow Triangles
    ## Color each triangle with stroke(), giving a rainbow patter
    
    numTri = 120
    
    for i in range(1, numTri + 1): # animates a circle of 90 triangles
    
        rotate(radians(360/numTri)) # rotates to new position in circle
        pushMatrix() # sets default location
        translate(200, 0) # moves the outer bound of circle
        rotate(radians(t + 3*i * (360/numTri))) # rotates grid itself such that the triangles spin
        # t + i means that subsequent triangles will have different phase shifts
        # we multiply by 360/90 to line up all of the triangles, creating a seamless pattern
        # therefore, the phase shifts must add up to a multiple to 360 degrees
        stroke(i * (255/numTri), 255, 255) # gives triangles a rainbow color
        equalTri(90) # creates a triangle with length 50 (based on 30-60-90)
        popMatrix() # resets back to original grid location
    
    save('frames/triangles ' + str(frame) + '.jpg')
    
    t += 0.5
    frame += 1
    
    if frame == 180:
        exit()
     
def equalTri(length): # length is defined as the hypotenuse of an arbitrary 30-60-90 triangle
    noFill()
    # draws an equilateral triangle around the center of triangle, based on length
    triangle(0, -length, -length*sqrt(3)/2, length/2, length*sqrt(3)/2, length/2)
