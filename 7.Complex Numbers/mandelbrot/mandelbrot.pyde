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

def setup():
    global xscl, yscl
    size(600,600)
    noStroke() # disables the outlines on lines
    colorMode(HSB)
    
    xscl = float(rangex)/width # sets the scale such that we can draw points
    yscl = float(rangey)/height
    
def draw():
    # translate(width/2,height/2)
    
    z = [0.25,0.75] # original complex number
    
    for x in range(width): # goes over all x's in the grid
        for y in range(height): # goes over all y's in the grid
            z = [ (xmin + x*xscl), (ymin + y*yscl) ] # because we want to take steps between -2 and 2, we need to 
            # scale x and y appropriately
            
            iterations = mandelbrot(z, 100) # iterations determines what color each pixel should be
            # z is a complex number that depends on the pixel's location
            # 100 is the total iterations we will attempt
            
            if iterations == 100:
                fill(0) # make the pixel black because does not diverge
            else:
                fill(255-15*iterations, 255, 255) # colors the pixel depending on the number of iterations it took
                
            rect(x, y, 1, 1) # makes a 1x1 rectangle at the pixel location  
    
    save('mandelbrot.jpg')
    
#####

def cAdd(a, b):
  # adds two complex numbers
  return [a[0] + b[0], a[1] + b[1]] # a + c, b + d

def cMult(u, v):
  return [u[0]*v[0] - u[1]*v[1], u[0]*v[1] + u[1]*v[0]] # ac - bd, ad + bc

def magnitude(z):
  return sqrt(z[0]**2 + z[1]**2) # solves for length of complex number relative to origin

def mandelbrot(z, num):
    # the mandelbrot set will operate on the complex number z
    
    # zn+1 = zn^2 + c (c = zi)
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
            z1 = cAdd(z1, z)   # then we will square z1 and add z to it to
            count += 1         # get the next iteration of z1, then check again
            # iterate the count variable each time to know how to count
    return num # if z has not diverged 
