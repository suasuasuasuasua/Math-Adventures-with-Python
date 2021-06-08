from random import choice

# define some color constants to refer to 
WHITE = color(255)
BROWN = color(102,51,0)
RED = color(255,0,0)
GREEN = color(0,102,0)
YELLOW = color(255,255,0)
PURPLE = color(102,0,204)
colorList = [WHITE, RED, YELLOW, PURPLE]

frame = 0

class Sheep:
    def __init__ (self, x, y, color):
        self.x = x # x-position
        self.y = y # y-position
        self.sz = 10 # size of Sheep
        # since walking takes energy, we will give the sheep some level of energy, decrementing as they walk around
        self.energy = 20 # energy level
        self.color = color
        self.age = 0
    def update(self):
        self.age += 1
        if self.age > 100: # the sheep may only live up to a certain age
            sheepList.remove(self)
            return
        move = 5 # max number of steps (pixels) that it can take in any direction
        # if self.color == PURPLE: # random evolutionary advantage that allows purple sheep to walk a little bit further
        # it turns out that the purple sheep will just 'outeat' and outcompete every other species
            # move = 7 # this is too broken because only purple sheep are left-over after initial fighting
        self.energy -= 1 # decrements as the sheep walks
        if self.energy <= 0:
            sheepList.remove(self) # removes the sheep ( it dies ) if its energy drops below 0
            return
        if self.energy >= 50: # if they have enough energy then they can reproduce
            self.energy -= 30 # birth takes away a lot of energy
            sheepList.append(Sheep(self.x,self.y,self.color)) # the new sheep starts where the parent is and inherits its colors
        self.x += random(-move, move) # moves the sheep in random directions
        self.y += random(-move, move)
        # makes the sheep wrap the window
        if self.x > width:
            self.x %= width
        if self.y > height:
            self.y %= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
        # i am a little unsure about this part but this is to ensure that sheep can accurately 'eat' the proper grass
        xscl = int(self.x / patchSize)
        yscl = int(self.y / patchSize)
        grass = grassList[xscl * rows_of_grass + yscl]
        if not grass.eaten: # if the grass is not yet eaten, then the sheep will gain the grass' energy and turn it brown (signalling that it is now dead)
            self.energy += grass.energy
            grass.eaten = True
        fill(self.color) # fills sheep depending on its color
        ellipse(self.x, self.y, self.sz*0.04*self.energy, self.sz*0.04*self.energy) # their sizes also depend on their energy level

class Grass:
    def __init__ (self, x, y, sz):
        self.x = x  # coordinates of the grass
        self.y = y
        self.energy = 6.5 # energy content of the grass
        self.eaten = False # has the grass been eaten?
        self.sz = sz # size of the grass
    def update(self):
        if self.eaten:
            if random(100) < 5: # if we randomly generate 1 out of 100, then the grass will respawn
                self.eaten = False
            else:
                fill(BROWN) # fills the shape if the grass is eaten
        else:
            fill(GREEN) # else, fills the shape green
        rect(self.x,self.y,self.sz,self.sz)

sheepList = [] # list to store the sheep
grassList = [] # list to store the grass
patchSize = 10 # size of the grass shapes

def setup():
    global patchSize, rows_of_grass # we will be using the earlier defined grass size

    rows_of_grass = height/patchSize

    noStroke() # removes outlines on shapes
    size(600,600)
    for i in range(100): # adds sheep to the list
        sheepList.append( Sheep(random(width), random(height), choice(colorList) ) )

    for x in range(0, width, patchSize): # adds grass to the list depending on the patch size and the window size
        for y in range(0, height, patchSize):
            grassList.append( Grass(x, y, patchSize ) )

def draw():
    global frame
    background(255)

    for grass in grassList: # note the order that this is placed in because the sheeps will now be drawn on top of the grass
        grass.update()

    for sheep in sheepList: # updates the sheep every iteration
        sheep.update()
    
    save('frames/sheepAndGrass ' + str(frame) + '.jpg')
    
    frame += 1
    
    if frame == 300:
        exit()
