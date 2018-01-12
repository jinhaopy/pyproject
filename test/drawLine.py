# -*- coding:UTF-8 -*- 

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Lines")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            pygame.quit()
            sys.exit()
    screen.fill((0,80,0))

    #画一条直线
    color = 100,255,200
    width = 8
    startPoint = 100,100
    endPoint = 300,480
    pygame.draw.line(screen,color,startPoint,endPoint,width)
    pygame.display.update()



