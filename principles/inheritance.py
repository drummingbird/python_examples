# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:18:06 2018

@author: Reuben
"""
import numpy as np

from .encapsulation import Spring

class Flexure(Spring):
    ''' A simple flexure class '''
    
    def __init__(self, k_s=8100, F_preload=68, thickness=0.001):
        super().__init__(k_s=k_s, F_preload=F_preload)
        self.thickness = thickness
        
    def fatigue_life(self, F):
        life = self._complicated_method(F)
        return life
    
    def _complicated_method(self, F):
        a = 4.3562e4 / F
        b = np.cos(0.034)
        return a * b
    
class Coil(Spring):
    ''' A simple coil spring class '''
    
    def __init__(self, k_s=8100, F_preload=68, diameter=0.01):
        super().__init__(k_s=k_s, F_preload=F_preload)
        self.diameter = diameter
        
    def fatigue_life(self, F):
        life = self._totally_different_method(F)
        return life
    
    def _totally_different_method(self, F):
        return 1e4 / F
    
flexure = Flexure(k_s=7000)
coil = Coil(k_s=5000)

def demonstrate(spring=flexure):
    ''' Simple illustration of spring force
    
    Note dependency injection in first argument. '''
    
    print('Spring force = ' + str(flexure.push(0.02)))
    print('Fatigue life = ' + str(flexure.fatigue_life(500)))

