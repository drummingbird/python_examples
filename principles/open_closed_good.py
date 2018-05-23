# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:32:06 2018

@author: Reuben

This module illustrates the 'open/closed' principle by giving an example
where the code is closed for modification but open for extension.

"""

import numpy as np

from abc import ABC, abstractmethod

class Shape(ABC):
    ''' The abstract base class (ABC) of a shape '''
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    ''' A rectagle '''
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def area(self):
        return self.x * self.y
        
class Circle(Shape):
    ''' A circle '''
    def __init__(self, r):
        self.r = r
        
    def area(self):
        return np.pi * self.r**2
        
class Total_Area_Calculator():
    ''' A class to calculate the total area of some shapes. '''
    
    def total_area(self, shapes):
        total = 0.0
        for shape in shapes:
            total += shape.area()
        return total

def demonstrate():
    shapes = []
    shapes.append(Rectangle(3, 5))
    shapes.append(Circle(7))
    
    calculator = Total_Area_Calculator()
    total = calculator.total_area(shapes)
    print(total)
    