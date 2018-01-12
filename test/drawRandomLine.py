# !/usr/bin/env python
# -*- coding:UTF-8 -*- 

import random
import pygame
from pygame.locals import *

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Draw Random Line")

screen.fill((0,0,200))
width = 2
color = 200,80,60
bool = True
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            pygame.quit()
            sys.exit()
    if bool:
        for i in range(0,1000):
            x1 = random.randint(1,600)
            y1 = random.randint(1,500)
            x2 = random.randint(1, 600)
            y2 = random.randint(1, 500)
            pygame.draw.line(screen,color,(x1,y1),(x2,y2),width)
        bool =False
    pygame.display.update()

