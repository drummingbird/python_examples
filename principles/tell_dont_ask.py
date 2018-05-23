# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:18:06 2018

@author: Reuben

This module illustrates the "Tell; don't ask" principle.

"""


class Dumb():
    ''' A dumb class that doesn't know how to calculate the total '''
    
    def __init__(self):
        self._data = [0, 1, 2, 3, 4, 5, 6]
    
dumb = Dumb()
data = dumb._data  # Asking
total = sum(data) # Outside class. Can't reuse. Harder to check & maintain.

class Smart():
    ''' A smart class that knows how to calculate the total '''
    
    def __init__(self):
        self._data = [0, 1, 2, 3, 4, 5, 6]

    def total(self):
        return sum(self._data)

smart = Smart()
total = smart.total() # Telling



