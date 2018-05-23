# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:30:33 2018

@author: Reuben
"""

from .inheritance import Flexure, Coil

class Beam():
    ''' A beam class '''
    
    def fatigue_life(self, F):
        life = self._some_method(F)
        return life
    
    def _some_method(self, F):
        life = 35627 / F
        return life

components = [Beam(), Flexure(), Coil()]

def demonstrate(components=components, F=500):
    for component in components:
        life = component.fatigue_life(F)
        print(component.__class__ + ': life=' + life)
