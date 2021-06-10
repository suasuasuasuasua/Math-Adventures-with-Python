sz = 2
rows = 1000
cols = 1000

# ruleset = [0,0,0,1,1,1,1,0] # rule 30
# ruleset = [1,0,0,1,0,0,1,0] # rule 73
# ruleset = [1,0,0,1,0,1,0,1] # rule 75
ruleset = [1,0,1,1,0,1,0,0] # rule 90

def rules(a,b,c):
    return ruleset[7 - (4*a + 2*b + c)] # pseudo-way of converting to binary

def generate():
    for i, row in enumerate(cells):
        for j in range(1, len(row)-1):
            left = row[j-1]
            me = row[j]
            right = row[j+1]

            if i < len(cells) - 1:
                cells[i+1][j] = rules(left, me, right) # changes the cell's status according to the ruleset
    return cells # returns the new cells to draw

def setup():
    global cells
    size(600,600)
    noStroke()

    cells = []
    for r in range(rows):
        cells.append([])
        for c in range(cols):
            cells[r].append(0) # sets all cells to be dead
    
    cells[0][cols//2] = 1 # sets the middle cell to be alive

    cells = generate()

def draw():
    
    background(255)

    for i, cell in enumerate(cells): # iterates through all of the rows
        for j, v in enumerate(cell): # iterates through all of the columns
            if v == 1:
                fill(0) # if the cell is alive, then set the color to black
            else:
                fill(255)
            rect(j*sz-(cols*sz-width)/2, sz*i, sz, sz)
    
    save('elementaryCA90.jpg')
