# -*- coding: utf-8 -*-
"""
Created on Thu May 24 08:51:39 2018

@author: Reuben

This module gives a simple example of composition, which is a more flexible
means of extending or modifying function than inheritance.

Example adapted from http://blog.thedigitalcatonline.com/blog/2014/08/20/python-3-oop-part-3-delegation-composition-and-inheritance/

"""


class Door():
    def __init__(self, number, status):
        self._number = number
        self._status = status
        
    def open(self):
        self._status = 'open'
        print('The door is open')

    def close(self):
        self._status = 'closed'
        print('The door is closed')


class ComposedDoor():
    def __init__(self, number, status):
        self._door = Door(number, status)

    def __getattr__(self, attr):
        ''' Get the door's attribute/method if not found in this class'''
        return getattr(self._door, attr)
    

class SecurityDoor():
    def __init__(self, number, status, locked=True):
        self._door = Door(number, status)
        self._locked = locked

    def open(self):
        ''' Specifying a new open method. '''
        if not self._locked():
            self._door.open()

    def toggle_lock(self):
        self._locked = not self._locked

    def __getattr__(self, attr):
        ''' Get the door's attribute/method if not found in this class'''
        return getattr(self._door, attr)

