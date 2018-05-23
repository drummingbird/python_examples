# -*- coding: utf-8 -*-
"""
Created on Thu May 24 07:39:09 2018

@author: Reuben

This module demonstrates the template pattern.

"""


class Component():
    ''' A template '''
    
    def configure(self):  pass
    def check_stress(self, F): pass

    def report(self, F):
        self.configure()
        stress = self.check_stress(F)
        return stress

class Tensioned(Component):
    ''' A subclass that uses the template '''
    
    def configure(self):
        self.A = 0.02

    def check_stress(self, F):
        return F / self.A

class Bending(Component):
    ''' Another subclass that uses the template '''
    
    def configure(self):
        self.I = 1e-3
        self.y = 0.1
        self.length = 2.0

    def check_stress(self, F):
        M = F * self.length
        return M * self.y / self.I

def demonstrate(components=[Bending(), Tensioned()], F=1e3):
    stresses = []
    for component in components:
        stresses.append(component.report(F=F))
    return stresses
