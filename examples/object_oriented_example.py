# -*- coding: utf-8 -*-
"""
Created on Wed May 23 20:09:52 2018

@author: Reuben

This module illustrates an object oriented approach to incrementing a number.

"""

class X():
    ''' A demo class '''
    
    def __init__(self, val):
        self._val = val
    
    def increment(self):
        self._val += 1
        
    def __repr__(self):
        return str(self._val)

x = X(0)
x.increment()
x.increment()
