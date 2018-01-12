# -*- coding:UTF-8 -*- 
import sys
import math
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,500 ))
pygame.display.set_caption("Drawing Arcs")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            pygame.quit()
            sys.exit()
    screen.fill((0,0,200))
    
    #画弧形
    color = 255,0,255
    position = 100,150,200,200
    start_angle = math.radians(0)
    end_angles = math.radians(450)
    width = 2
    pygame.draw.arc(screen,color,position,start_angle,end_angles,width)
    pygame.display.update()
