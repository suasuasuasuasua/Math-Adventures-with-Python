# notes on complex numbers

## introduction
- complex numbers are extremely real!
- complex numbers are extensively used in electromagnetism and other applications
- a complex number is defined in this form:
  - a + bi, where a and b are both real numbers; i is the square root of -1
  - therefore, complex numbers have two parts to worry about
- in Python, one-dimensional objects suddenly become two-dimensional objects

## plotting
- complex number addition works analogously to vector addition
  - simply add the respective components
- we can think (x,y) as z = x + iy, where z is the complex number
- we can imagine the x-axis as the real number line, and the y-axis as the imaginary number line

## multiplying complex numbers
- because i represents the square root of -1, multiplying complex numbers by i will rotate the number 90 degrees about the origin
- through the foil method, the general form for (a + bi)(c + di) is [ac - bd, ad + bc]

## mandelbrot set
- the mandelbrot set is defined by: zn+1 = zn^2 + c, where c is the original complex number, z is iterated
