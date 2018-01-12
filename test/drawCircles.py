# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *

white = 255,255,255
blue = 0,0,200
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Circles")
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            pygame.quit()
            sys.exit()
    screen.fill(blue)

    color = white
    position = 100,250
    radius = 100
    width = 5
    pygame.draw.circle(screen,color,position,radius,width)
    pygame.display.update()

