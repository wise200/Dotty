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

def play(dot, level):
    grid = Grid(level,dims, dot, screen)
    return grid