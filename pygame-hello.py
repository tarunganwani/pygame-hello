import pygame, sys

from pygame.locals import *

pygame.init()

DIMX = 1000
DIMY = 1000

MARGIN_X = 5
MARGIN_Y = 5
RECT_W = 30
RECT_H = 30

GRID_W = 2*MARGIN_X + RECT_W
GRID_H = 2*MARGIN_Y + RECT_H

ROW_COUNT=int(DIMX/GRID_W)
COL_COUNT=int(DIMY/GRID_H)

DISPLAYSURF = pygame.display.set_mode((DIMX, DIMY))

WHITE=(255,255,255)
GREEN=(0,150,0)
BLUE=(0,0,150)
PINK=(255,20,147)
BLACK=(0,0,0)
YELLOW=(255,255,51)

DISPLAYSURF.fill(GREEN)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.display.set_caption('Hello World!')

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(ROW_COUNT):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(COL_COUNT):
        grid[row].append(0)  # Append a cell
        


while True: # main game loop

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION: # MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            row = pos[0] // (GRID_W)
            column = pos[1] // (GRID_H)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    for i in range(0,ROW_COUNT):
        for j in range(0,COL_COUNT):
            color = WHITE
            if grid[i][j] == 1:
                color = YELLOW # BLACK # PINK
            pygame.draw.rect(DISPLAYSURF,color,(i*GRID_W + MARGIN_X, j*GRID_H + MARGIN_Y ,RECT_W,RECT_H))
            
    # Limit to 60 frames per second
    clock.tick(60)
    
    pygame.display.update()
