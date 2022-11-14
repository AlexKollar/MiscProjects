import copy, random, sys, time, os
from mods import line, banner
# setup constants
WIDTH = 84 #Width of the cell grid
HEIGHT = 25 #Height of the cell grid

ALIVE = '.'
DEAD = ' '

nextCells = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        #50/50 change of a cell starting dead or alive
        if random.randint(0,1) == 0:
            nextCells[(x,y)] = ALIVE
        else:
            nextCells[(x,y)] = DEAD

while True:
    #print('\n' * 50)
    os.system('clear') 
    print(banner)
    print(line)
    cells = copy.deepcopy(nextCells)

    #print the cells on the screen
    for y in range (HEIGHT):
        for x in range(WIDTH):
            print(cells[(x,y)], end='')
        print()
    print(line)
    print("press CTRL + C to quit")

    #calculate the next steps cells based on current cells.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            #Count number of living neighbors:
            numNeighbors = 0 
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1

            #set cell based on GOL rules:
            if cells[(x,y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[(x,y)] = ALIVE
            elif cells[(x,y)] == DEAD and numNeighbors == 3:
                nextCells[(x,y)] = ALIVE
            else:
                nextCells[(x,y)] = DEAD

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("Aint that a kick in the head!")
        sys.exit()
