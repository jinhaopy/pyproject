# !/usr/bin/env python
# -*- coding:UTF-8 -*- 

import sys,pygame
from pygame.locals import *

class Travia (object):
    def __init__(self,filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.colors = [white,white,white,white]

        #从filename 文件中读取travia data
        f = open(filename,"r")
        travia_data = f.readlines()
        f.close()

        for text_line in travia_data:
            self.data.append(text_line.strip())
            self.total += 1





