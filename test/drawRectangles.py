# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
import random

#定义随机颜色
def randColor():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return red,green,blue

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Rectangles")
pos_x = 300
pos_y = 250
vel_x =2
vel_y = 3

blue = 0,0,200
white = 255,255,255
color = white
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            pygame.quit()
            sys.exit()
    screen.fill(blue)

    #移动矩形
    pos_x += vel_x
    pos_y += vel_y

    #判断矩形是否全显示在屏幕中
    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x
        color = randColor()
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y
        color = randColor()

    #画矩形
    width = 4
    pos = pos_x,pos_y,50,80
    pygame.draw.rect(screen,color,pos,width)
    pygame.display.update()






