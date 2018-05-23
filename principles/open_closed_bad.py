# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:32:06 2018

@author: Reuben
"""

import numpy as np


class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Total_Area_Calculator_Initial():
    def total_area(self, rectangles):
        total = 0.0
        for rectangle in rectangles:
            total += rectangle.x * rectangle.y
        return total


# Then later, a circle shape is required, so we add a circle:

class Circle():
    ''' A circle class '''
    
    def __init__(self, r):
        self.r = r

# ... and add a conditional to Total_Area_Calculator


class Total_Area_Calculator():
    ''' A class to calculate the total area of some shapes. '''
    
    def total_area(self, shapes):
        total = 0.0
        for shape in shapes:
            if shape.__class__ is Rectangle:
                total += shape.x * shape.y
            elif shape.__class__ is Circle:
                total += np.pi * shape.r**2
        return total

# Total_Area_Calculator will get more and more complex the more shapes
#        we have

def demonstrate():
    shapes = []
    shapes.append(Rectangle(3, 5))
    shapes.append(Circle(7))
    
    calculator = Total_Area_Calculator()
    total = calculator.total_area(shapes)
    print(total)
    
