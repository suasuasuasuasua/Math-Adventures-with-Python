def setup():
    size(600,600)
    
def draw():
    
    translate(width/2,height/2)
    
    # beginShape()
    # for i in range(6):
    #     vertex(100,100)
    #     rotate(radians(60))
    # endShape(CLOSE)
    ## note that this notation will not work because we wannt use the rotate() function
    ## inside a shape
    
    polygon(10, 100)
    save('polygon.jpg')


def polygon(numSides, radius): # draws any polygon based on number of sides and radius
    beginShape()
    for i in range(numSides): # draws vertices for how many sides there are
        vertex(radius*cos(radians((360/numSides)*i)), radius*sin(radians((360/numSides)*i))) # remember to use the radians() function to convert
    endShape(CLOSE)
