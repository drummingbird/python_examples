# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:18:06 2018

@author: Reuben
"""
import numpy as np




'''
Factory pattern
----------------
'''

class Car():
    ''' A car class '''
    
    @staticmethod
    def factory(type):
        if type == "Racecar": 
            return Racecar()
        if type == "Van": 
            return Van()
        print("Bad car creation: " + type)
 
class Racecar(Car):
    ''' A fast car '''
    
    def drive(self):
        print("Racecar driving.")
 
class Van(Car):
    ''' A big car to transport things '''
    
    def drive(self):
        print("Van driving.")


def demonstrate(car_type='Racecar'):
    obj_hard_coded = Racecar()
    obj_hard_coded.drive()
    
    obj_from_factory = Car.factory(car_type)
    obj_from_factory.drive()

