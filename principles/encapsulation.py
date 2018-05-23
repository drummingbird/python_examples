# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:27:53 2018

@author: Reuben
"""

from .abstraction import demonstrate

class Spring():
    ''' A modified simple spring class.
    
    Note how the external call remains unchanged, but the internals
    have changed.    
    '''
    
    def __init__(self, k_s=8100, F_preload=68):
        self.k_s = k_s
        self.F_preload = F_preload
        
    def push(self, x):
        F_x = max(self._F_nominal(x), 0)
        return F_x
    
    def _F_nominal(self, x):
        F_nominal = -x * self.k_s - self.F_preload
        return F_nominal
    

spring = Spring() # An instance of this newly defined Spring class
# Now try calling demonstrate(spring)
# The function is unchanged, but the Spring class has changed how it calculates