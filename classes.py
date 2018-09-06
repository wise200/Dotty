import pygame
from pygame import Rect

colors = {'?' : (0,0,0)}
grids = []

def convert(string, num):
    try:
        return int(string) != num
    except ValueError:
        return True

class Grid:
    
    def __init__(self, index, maxDims, screen):
        self.grid = grids[index]
        self.screen = screen
        width = maxDims[0] // len(self.grid[0])
        height = maxDims[1] // len(self.grid)
        self.boxSize = min(width, height)
        self.sizeCalc = self.boxSize+1
        self.dotImg = pygame.image.load("bluedot.png").convert_alpha()
        self.dotImg = pygame.transform.scale(self.dotImg, (self.boxSize, self.boxSize))
        
        #Create dots
        
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
        screen.fill((255,255,255))
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                item = self.grid[row][col]
                color = colors[item]
                rect = Rect(col*self.sizeCalc,row*self.sizeCalc,self.boxSize,self.boxSize)
                pygame.draw.rect(screen, color, rect)
        

					
class Dot:
	
	def __init__(self, grid):
		self.grid = grid
		self.direction = 0
		self.r = 0
		self.c = 0
		found = False
		for r in range(len(self.grid)):
			for c in range(len(self.grid[row])):
				if not found and self.grid[r][c] == '?':
					self.r, self.c = r, c
    
    def move(self):
        self.r += self.deltaY()
        self.c += self.deltaX()
        
    def turnRight(self):
        self.direction = (self.direction + 1) % 4
    
    def deltaX(self):
        return 0 if self.direction % 2 != 0 else self.direction - 2
        
    def deltaY(self):
        if self.direction == 0:
            return 1
        elif self.direction == 3:
            return -1
        else
            return 0
	
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