# -*- coding: utf-8 -*-
"""
Created on Wed May 23 20:46:11 2018

@author: Reuben

Naming conventions help convey intent and make the code more readable.

This module covers a few key naming conventions.

"""

CONSTANT = 5 # Use CAPS for constants


def function_name(x):
    ''' use lower case with underscores for functions and methods ''' 
    var_a = 5 # Use lower case with underscores for variables and attributes
    return var_a

class Class_Name():
    ''' Use Title Case and underscores to name classes. '''
    
    def set_public_variable(self, x):
        ''' public means "can interact with" '''
        self.x = x

    def set_protected_variable(self, x):
        ''' protected means "don't touch" '''
        self._x = x
        
    def set_private_variable(self, x):
        ''' protected means "don't touch" '''
        self.__x = x
        


