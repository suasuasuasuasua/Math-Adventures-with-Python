def setup():
    size(600,600) # defines the size of the coordinate plane

def draw():
    
    translate(width/2, height/2) # shifts the entire grid such that 0,0 is the origin, not the top left corner
    # note that width and height become whatever numbers we use in the size() function
    rect(50,100,100,60)
    
