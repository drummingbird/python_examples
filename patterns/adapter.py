# -*- coding: utf-8 -*-
"""
Created on Thu May 24 07:58:21 2018

@author: Reuben
"""

from abc import ABC, abstractmethod


class Interface(ABC):
    ''' Define the interface needed by the client '''

    def __init__(self, adaptee):
        ''' Wrap the adapted instance '''
        self._adaptee = adaptee

    @abstractmethod
    def request(self):
        pass


class Adapter(Interface):
    ''' Adapt the client interface to the adaptee interface '''

    def request(self, x, y):
        return self._adaptee.add(x, y)


class Adaptee:
    ''' The class that needs adapting '''

    def add(self, x, y):
        return x + y


def demonstrate(x=5, y=8):
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    print(adapter.request(x, y))