from math import sqrt

# range of x-values
xmin = -2
xmax = 2

# range of y-values
ymin = -2
ymax = 2

# range of values
rangex = xmax - xmin
rangey = ymax - ymin


t = 0

def setup():
    global xscl, yscl
    size(600,600)
    noStroke() # disables the outlines on lines
    colorMode(HSB)
    
    xscl = float(rangex)/width # sets the scale such that we can draw points
    yscl = float(rangey)/height
    
def draw():
    # global xscl, yscl
    global t
    # translate(width/2,height/2)
    # c = [-0.8, 0.156]
    # c = [-0.4, 0.6]
    c = [0.285, 0.01]
    
    for x in range(width):
        for y in range(height):
            z = [ (xmin + x*xscl), (ymin + y*yscl) ]
            
            iteration = julia(z, c, 100)
            
            if iteration == 100:
                fill(0)
            else:
                fill(3 * iteration, 255, 255)
            rect(x, y, 1, 1)
    
    save('julia3.jpg')
    
#####

def cAdd(a, b):
  # adds two complex numbers
  return [a[0] + b[0], a[1] + b[1]] # a + c, b + d

def cMult(u, v):
  return [u[0]*v[0] - u[1]*v[1], u[0]*v[1] + u[1]*v[0]] # ac - bd, ad + bc

def magnitude(z):
  return sqrt(z[0]**2 + z[1]**2) # solves for length of complex number relative to origin

def julia(z, c, num):
    # the julia set will operate on the complex number z
    
    # zn+1 = zn^2 + c (c = some constant complex number, not z)
    count = 0
    z1 = z # z1 will be the iterated complex number
    # z will be the original, constant complex number
    
    while count <= num:
        # print(magnitude(z1)) # displays length of complex number after every iteration
        # checks for divergence
        if magnitude(z1) > 2.0: # our rule is that if the magnitude is greater than 2.0, then complex number diverges
            return count
        else:
            z1 = cMult(z1, z1) # if the length of z1 is not greater than 2.0
            z1 = cAdd(z1, c)   # then we will square z1 and add z to it to
            count += 1         # get the next iteration of z1, then check again
            # iterate the count variable each time to know how to count
    return num # if z has not diverged 
