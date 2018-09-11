import pygame
from pygame.locals import *
from classes import *
from time import sleep
from random import randint as rand

pygame.init()
dims = (800,450)
screen = pygame.display.set_mode(dims)

def play(dot, level):
    grid = Grid(level,dims, dot, screen)
    return grid