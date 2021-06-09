GRID_W = 41 # number of cells for width and height
GRID_H = 41

generation = 0

frame = 0

# define a cell class

class Cell:
    def __init__(self,col,row,state=0): # initializes the cell
        self.col = col
        self.row = row
        self.state = state

    def display(self): # displays the cell depending on the cell's state
        if self.state == 1:
            fill(0) # fills in black square if cell if alive
        else:
            fill(255) # otherwise, the cell is white
        rect(SZ*self.row, SZ*self.col, SZ, SZ)
    
    def checkNeighbors(self):
        if self.state == 1: # cells that are on will stay on
            return 1
        
        neighbors = 0

        for dr, dc in [ [-1,0], [1,0], [0,-1], [0,1] ]: # if any cell above, below, to the right, or left of the cell is alive, then increment neighbors
            try: # try literally means 'try to run this piece of code; if you get an error message, then do something
                if cellList[self.row + dr][self.col + dc].state == 1:
                    neighbors += 1
            except IndexError: # if there is an index error ( where the array goes out of bounds on the edges, then just skip them )
                continue

        if neighbors in [1,4]: # if neighbors is equal to 1 or 4, then return 1
            return 1
        else:
            return 0

def setup():
    global cellList, SZ
    size(600,600)
    
    SZ = width // GRID_W + 1 # sets dynamic grid size depending on the window
    # the +1 accounts for the outlines and more accurately fills in the window

    cellList = createCellList()

def draw():
    global generation, cellList, frame
    grid()

    frameRate(10)

    cellList = update(cellList)
    for row in cellList:
        for cell in row:
            cell.display()
    
    generation += 1
    if generation == 30:
        generation = 1
        cellList = createCellList()
    
    save('frames/cellularAutomata ' + str(frame) + '.jpg')

    frame += 1
    print(frame)
    if frame == 300:
        exit()


def createCellList():
    cellList = []

    for j in range(GRID_W): # adds empty cells for all of the rows and columns
        cellList.append([])
        for i in range(GRID_H): 
            cellList[j].append(Cell(i,j,0)) 
    cellList[GRID_H//2][GRID_W//2].state = 1  # the middle cell is alive

    return cellList

def update(cellList):
    newList = []
    for r, row in enumerate(cellList):
        newList.append([])
        for c, cell in enumerate(row):
            newList[r].append(Cell(c,r,cell.checkNeighbors())) 
            # creates rows and appends cells, placing them at the proper location using the c and r indices
            # then we use checkNeighbors() to pass a boolean value for whether the cell is alive or not
    return newList[::] # returns new cellList

def grid(): # draws the grid for the cells
    global SZ
    for column in range(GRID_W):
        for row in range(GRID_H):
            rect(column*SZ,row*SZ,SZ,SZ)
