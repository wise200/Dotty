import pygame
from pygame.locals import *
import sys
from classes import Dot
from pygame import mouse

dims = (800,450)
if len(sys.argv) < 3:
    raise ValueError("This file can only be run with command line arguments to specify grid size")
grid = [['#' for x in range(int(sys.argv[2]))] for x in range(int(sys.argv[1]))]
width = dims[0] // len(grid[0])
height = dims[1] // len(grid)
boxSize = min(width, height)
sizeCalc = boxSize+1
gridWidth = len(grid[0])
gridHeight = len(grid)
width = gridWidth * sizeCalc - 1
height = gridHeight * sizeCalc - 1
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

colors = {'?' : (255,50,160)}

with open("levels.dat", "r") as file:
    file = iter(file.read().splitlines())
    line = next(file).split(" ")
    while line[0] != '?':
        colors[line[0]] = (int(line[1]), int(line[2]), int(line[3]))
        line = next(file).split(" ")

keys = {K_KP0:0, K_KP1:1, K_KP2:2, K_KP3:3, K_KP4:4, K_KP5:5, K_KP6:6, K_KP7:7, K_KP8:8, K_KP9:9}
inputList = ['#','+','?','@', '$', '!']
mode = '+'

def mouseCol():
    return mouse.get_pos()[0] // sizeCalc
    
def mouseRow():
    return mouse.get_pos()[1] // sizeCalc
        
def drawBox(row, col, item):
    color = colors[item]
    rect = Rect(col*sizeCalc,row*sizeCalc,boxSize,boxSize)
    pygame.draw.rect(screen, color, rect)
        
def exit():
    with open("levels.dat", "a") as file:
        file.write(str(len(grid)) +"\n")
        for row in grid:
            string = ""
            for item in row:
                string += item
            file.write(string + "\n")
    sys.exit(pygame.quit())
        
while True:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            elif event.key in keys:
                mode = inputList[keys[event.key]]
        #if event.type == MOUSEBUTTONDOWN:
            #grid[mouseRow()][mouseCol()] = mode
        if event.type == QUIT:
            sys.exit(pygame.quit())
    
    if mouse.get_pressed()[0]:
        grid[mouseRow()][mouseCol()] = mode
    
    screen.fill((255,255,255))
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            item = grid[row][col]
            drawBox(row, col, item)

    if mouseCol() >= 0 and mouseCol() < len(grid[0]) and mouseRow() >= 0 and mouseRow() < len(grid):
        drawBox(mouseRow(), mouseCol(), mode)
    
    
    pygame.display.flip()