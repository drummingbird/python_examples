# -*- coding: utf-8 -*-
"""
Created on Wed May 23 20:09:52 2018

@author: Reuben

This module contains some simple illustrations of objects.

"""


class Line():
    ''' A model of a line with gradient and intercept ''' 
    
    def __init__(self, m, c):
        self.m = m
        self.c = c

    def y(self, x):
        y = self.m * x + self.c
        return y

default_line = Line(m=5, c=4)
def demonstrate(line=default_line):
    return line.y(2)

y_1 = demonstrate(default_line)

default_line.m = 3
y_2 = demonstrate(default_line)
