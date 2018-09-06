import pygame
from pygame.locals import *
from classes import *
from time import sleep
from random import randint as rand

pygame.init()
frameRate = 30

dims = (800,450)
screen = pygame.display.set_mode(dims)
smallfont = pygame.font.SysFont("consolas", 30)
bigfont = pygame.font.SysFont("consolas", 60)
clock = pygame.time.Clock()

def play():
    grid = Grid(2,dims)
    global screen
    screen = grid.resizeScreen(screen)
    pygame.display.flip()

    
play()
sleep(10)
import game