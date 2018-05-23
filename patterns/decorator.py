# -*- coding: utf-8 -*-
"""
Created on Thu May 24 07:43:32 2018

@author: Reuben

This module demonstrates the decorator pattern.

"""

from abc import ABC, abstractmethod


class Component(ABC):
    ''' The abstract base class for a component. '''

    @abstractmethod
    def operate(self, x):
        ''' A key method. '''
        pass


class Decorator(Component, ABC):
    ''' Maintain the same interface as Component in the Decorator. '''

    def __init__(self, component):
        self._component = component

    @abstractmethod
    def operate(self):
        pass


class Prefix_With_String(Decorator):
    ''' Print a string before performing the operation. '''

    def operate(self, x):
        print('About to perform operation...')
        # ...
        ret = self._component.operate(x)
        # ...
        return ret


class Multiply_Output_By_2(Decorator):
    ''' Multiply the output by 2. '''

    def operate(self, x):
        # ...
        ret = self._component.operate(x)
        # ...
        ret_2 = ret * 2
        return ret_2


class Adder(Component):
    """
    Define an object to which additional responsibilities can be
    attached.
    """

    def operate(self, x):
        return x + 5


def demonstrate():
    adder = Adder()
    multiplied = Multiply_Output_By_2(adder)
    ret_a = multiplied.operate(3)
    print('Return A is ' + str(ret_a))
    
    # Now stacking another decorator
    prefixed = Prefix_With_String(multiplied)
    ret_b = prefixed.operate(4)
    print('Return B is ' + str(ret_b))
