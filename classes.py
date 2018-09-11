import pygame
from pygame import Rect
from time import sleep

dims = (800, 450)

colors = {'?' : (0,0,0)}
grids = []

def convert(string, num):
    try:
        return int(string) != num
    except ValueError:
        return True

class Grid:
    
    def __init__(self, index, dot):
        self.grid = grids[index]
        width = dims[0] // len(self.grid[0])
        height = dims[1] // len(self.grid)
        self.boxSize = min(width, height)
        self.sizeCalc = self.boxSize+1
        self.screen = self.startScreen()
        self.dots = [dot]
        
    def startScreen(self):
        pygame.display.quit()
        pygame.display.init()
        gridWidth = len(self.grid[0])
        gridHeight = len(self.grid)
        width = gridWidth * self.sizeCalc - 1
        height = gridHeight * self.sizeCalc - 1
        screen = pygame.display.set_mode((width, height))
        return screen
        
    def draw(self):
        self.drawWithDelay(1)
    
    def drawWithDelay(self, delay):
        self.screen.fill((255,255,255))
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                item = self.grid[row][col]
                color = colors[item]
                rect = Rect(col*self.sizeCalc,row*self.sizeCalc,self.boxSize,self.boxSize)
                pygame.draw.rect(self.screen, color, rect)
        for dot in self.dots:
            dotRect = Rect(dot.c*self.sizeCalc, dot.r*self.sizeCalc,self.boxSize,self.boxSize)
            img = dot.img if dot.alive else dot.deadImg
            img = pygame.transform.rotate(img, -90*dot.direction)
            self.screen.blit(img, dotRect)
        pygame.display.flip()
        self.tick(delay)
        
    def tick(self, delay):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit(pygame.quit())
        sleep(delay)

					
class Dot:
	
    grid = None
    colors = ["blue"]
    
    def __init__(self, level=0, color="blue"):
        if color not in Dot.colors:
            raise ValueError(str(color) + " is not a valid color.")
        if Dot.grid == None:
            Dot.grid = Grid(level, self)
        else:
            Dot.grid.dots.append(self)
        self.direction = 0
        self.r = 0
        self.c = 0
        found = False
        for r in range(len(Dot.grid.grid)):
            for c in range(len(Dot.grid.grid[r])):
                if not found and Dot.grid.grid[r][c] == '?':
                    self.r, self.c = r, c
                    Dot.grid.grid[r][c] = '#'
                    found = True
        self.alive = self.legalMove(self.r, self.c)
        self.img = pygame.image.load(color + "dot.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (Dot.grid.boxSize, Dot.grid.boxSize))
        self.deadImg = pygame.image.load("reddot.png").convert_alpha()
        self.deadImg = pygame.transform.scale(self.deadImg, (Dot.grid.boxSize, Dot.grid.boxSize))
        Dot.grid.draw()
    
    def legalMove(self, r, c):
        return self.inBounds(r, c) and Dot.grid.grid[r][c] != '+'
    
    def inBounds(self, r, c):
        return r >= 0 and r < len(Dot.grid.grid) and c >= 0 and c < len(Dot.grid.grid[0])
    
    def pickUpTrash(self):
        if Dot.grid.grid[self.r][self.c] == '@' and self.alive:
            Dot.grid.grid[self.r][self.c] = '#'
            Dot.grid.draw()
    
    def move(self):
        if self.alive:
            r = self.r + self.deltaR()
            c = self.c + self.deltaC()
            if self.inBounds(r,c):
                self.r = r
                self.c = c
            self.alive = self.legalMove(r, c)
            Dot.grid.draw()
        
    def turnRight(self):
        if self.alive:
            self.direction = (self.direction + 1) % 4
            Dot.grid.draw()
    
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