# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:31:24 2018

@author: Reuben
"""

from ..principles.inheritance import Coil, Flexure
from ..principles.polymorphism import Beam

class Fatigue_Analysis_nonDI():
    ''' A simple fatigue analysis calculation class ''' 
    
    def get_fatigue_lives(self, F):
        lives = []
        component_list = [Coil(k_s=5000),
                          Coil(k_s=3000),
                          Flexure(k_s=8000)]
        for component in component_list:
            lives.append(component.fatigue_life(F)) # Using polymorphism
        return lives


class Fatigue_Analysis():
    ''' A analysis class where objects are injected. ''' 
    
    def add_components(self, component_list):
        self.component_list = component_list  
    
    def get_fatigue_lives(self, F):
        lives = []
        for component in self.component_list:
            lives.append(component.fatigue_life(F))
        return lives



class Fatigue_Check():
    ''' A class where the methods, not classes, are injected '''
    
    def __init__(self, F=100):
        self.F = F
    
    def warn(self, fatigue_lives_method):
        lives = fatigue_lives_method(self.F)
        if min(lives) < 1e6:
            print('WARNING: Premature fatigue failure possible on at least \
                  one component.')
            

components = [Beam(), Flexure(), Coil()]

def demonstrate(components=components, F=500):
    fa = Fatigue_Analysis()
    fa.add_components(components)
    print(fa.get_fatigue_lives(F))
    
    fc = Fatigue_Check()
    fc.warn(fa.get_fatigue_lives)
    
    
    