ballList = [] # contains the Ball objects
frame = 0

class Ball:
    def __init__(self, x, y): # defines the constructor for a Ball
        self.xcor = x
        self.ycor = y
        self.xvel = random(-2,2)
        self.yvel = random(-2,2)
        self.color = color(random(255), random(255), random(255))
        self.radius = random(5, 50)
  
    # defines conditions to simulate 'bouncing'
    # for instance, 0 is defined as the left side of the window; width is defined as the right side of the window
    # 0 is also the top of the window; height is the bottom side of the window 
    # if any of these conditions are met, then we will reverse the velocity to simulate bouncing
    def update(self):
        if self.xcor > width or self.xcor < 0:
            self.xvel = -self.xvel
        elif self.ycor > height or self.ycor < 0:
            self.yvel = -self.yvel
        self.xcor += self.xvel
        self.ycor += self.yvel

        fill(self.color) # colors the balls randomly

        ellipse(self.xcor, self.ycor, 2*self.radius, 2*self.radius)

def setup():
    size(600,600)
    
    for i in range(50): # adds Ball objects of random width and height to the list
        ballList.append(Ball(random(width), random(height))) 
def draw():
    global frame
    background(0) # black background
    
    for ball in ballList: # updates the position of each ball every time the program loops
        ball.update()
        
        
    save('frames/bouncingBall ' + str(frame) + '.jpg')
    frame += 1
    if frame == 300:
        exit()
