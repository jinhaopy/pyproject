# !/usr/bin/env python
# -*- coding:UTF-8 -*-

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Draw Ellipse")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            pygame.quit()
            sys.exit()

    color = 200,80,60
    screen.fill((0,0,200))
    pygame.draw.ellipse(screen,color,(100,100,300,100),2)

    pygame.display.update()



