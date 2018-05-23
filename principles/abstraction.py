# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:27:22 2018

@author: Reuben
"""

class Spring():
    ''' A simple spring class '''
    def __init__(self, k_s=8100, F_preload=68):
        self.k_s = k_s
        self.F_preload = F_preload
        
    def push(self, x):
        F_x = -x * self.k_s - self.F_preload
        return F_x
    
spring = Spring(k_s=5000, F_preload=100)

def demonstrate(spring): 
    ''' An example of calculating a spring force.
    
    Note dependency injection (a Spring instance is the first argument) '''
    
    F_x = spring.push(0.02)
    print(F_x)
    return F_x
