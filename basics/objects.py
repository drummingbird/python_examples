# -*- coding: utf-8 -*-
"""
Created on Wed May 23 20:09:52 2018

@author: Reuben

This module contains some simple illustrations of objects.

"""


class Line():
    ''' A model of a line with gradient and intercept ''' 
    
    def __init__(self, m, c):
        self._m = m # Assigning m to a 'protected' attribute, _m
        self._c = c # Assigning c to a 'protected' attribute, _c
        self.m = m # Also assigning m to a public attribute, m
        self.c = c # Also assigning c to a public attribute, c

    def y(self, x):
        y = self._m * x + self._c
        return y
    
    def set_m(self, m):
        self._m = m
    

default_line = Line(m=5, c=4)
def demonstrate(line=default_line):
    return line.y(2)

y_1 = demonstrate(default_line)

default_line.set_m(3)
y_2 = demonstrate(default_line)
