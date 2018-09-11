import pygame
from pygame import Rect
import game
from time import sleep

colors = {'?' : (0,0,0)}
grids = []

def convert(string, num):
    try:
        return int(string) != num
    except ValueError:
        return True

class Grid:
    
    def __init__(self, index, maxDims, dot, screen):
        self.grid = grids[index]
        self.screen = screen
        width = maxDims[0] // len(self.grid[0])
        height = maxDims[1] // len(self.grid)
        self.boxSize = min(width, height)
        self.sizeCalc = self.boxSize+1
        self.dotImg = pygame.image.load("bluedot.png").convert_alpha()
        self.dotImg = pygame.transform.scale(self.dotImg, (self.boxSize, self.boxSize))
        self.deadImg = pygame.image.load("reddot.png").convert_alpha()
        self.deadImg = pygame.transform.scale(self.deadImg, (self.boxSize, self.boxSize))
        #Create dots
        self.dot = dot
        
    def resizeScreen(self):
        pygame.display.quit()
        pygame.display.init()
        gridWidth = len(self.grid[0])
        gridHeight = len(self.grid)
        width = gridWidth * self.sizeCalc - 1
        height = gridHeight * self.sizeCalc - 1
        self.screen = pygame.display.set_mode((width, height))
        self.draw()
        return self.screen
        
    def draw(self):
        self.screen.fill((255,255,255))
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                item = self.grid[row][col]
                color = colors[item]
                rect = Rect(col*self.sizeCalc,row*self.sizeCalc,self.boxSize,self.boxSize)
                pygame.draw.rect(self.screen, color, rect)
        dotRect = Rect(self.dot.c*self.sizeCalc, self.dot.r*self.sizeCalc,self.boxSize,self.boxSize)
        img = self.dotImg if self.dot.alive else self.deadImg
        img = pygame.transform.rotate(img, -90*self.dot.direction)
        self.screen.blit(img, dotRect)
        pygame.display.flip()
        sleep(1)

					
class Dot:
	
    def __init__(self, level):
        self.grid = game.play(self, level)
        self.direction = 0
        self.r = 0
        self.c = 0
        found = False
        for r in range(len(self.grid.grid)):
            for c in range(len(self.grid.grid[r])):
                if not found and self.grid.grid[r][c] == '?':
                    self.r, self.c = r, c
        self.alive = self.legalMove(self.r, self.c)
        self.grid.resizeScreen()
    
    def legalMove(self, r, c):
        return self.inBounds(r, c) and self.grid.grid[r][c] != '+'
    
    def inBounds(self, r, c):
        return r >= 0 and r < len(self.grid.grid) and c >= 0 and c < len(self.grid.grid[0])
    
    def pickUpTrash(self):
        if self.grid.grid[self.r][self.c] == '@' and self.alive:
            self.grid.grid[self.r][self.c] = '#'
            self.grid.draw()
    
    def move(self):
        if self.alive:
            r = self.r + self.deltaR()
            c = self.c + self.deltaC()
            if self.inBounds(r,c):
                self.r = r
                self.c = c
            self.alive = self.legalMove(r, c)
            self.grid.draw()
        
    def turnRight(self):
        if self.alive:
            self.direction = (self.direction + 1) % 4
            self.grid.draw()
    
    def deltaC(self):
        return 0 if self.direction % 2 == 0 else self.direction - 2

    def deltaR(self):
        if self.direction == 0:
            return 1
        elif self.direction == 2:
            return -1
        else:
            return 0

    def honorableDeath(self):
        pygame.quit()
             
#Read colors and grid maps from levels.dat file
with open("levels.dat", "r") as file:
    file = iter(file.read().splitlines())
    line = next(file).split(" ")
    while line[0] != '?':
        colors[line[0]] = (int(line[1]), int(line[2]), int(line[3]))
        line = next(file).split(" ")
    while True:
        try:
            height = int(next(file))
            grid = []
            for r in range(height):
                temp = []
                row = next(file)
                for c in row:
                    temp.append(c)
                grid.append(temp)
            grids.append(grid)
        except:
            break