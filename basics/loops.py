# -*- coding: utf-8 -*-
"""
Created on Wed May 23 20:05:51 2018

@author: Reuben

Some examples of how to iterate, especially over sets of data.

"""

def while_loop():
    ''' Example of iterating while a condition is true '''
    
    i = 0
    while i < 10:
        print('i=' + str(i))
        i += 1


def list_loop(items=[1, 3, 65, 87, 2]):
    ''' Example of iterating over items in a list. '''
    
    for item in items:
        # Do stuff, for example
        print(item)
    
demo_dictionary = {'a': 4.4, 5: 'slht', 'something else': 'string'}
def dictionary_loop(demo_dictionary):
    ''' Example of iterating over (key, value) pairs in a dictionary. '''
    for key, val in demo_dictionary.items():
        # Do stuff, for example
        print(str(key) + ': ' + str(val))
        

def zip_demo():
    ''' Example of using the builtin zip function '''
    
    apples = [3, 6, 5, 7]
    pears = [44, 55, 66, 77]
    for apple, pear in zip(apples, pears):
        print(apple)
        print(pear)

def list_comprehension_demo(items=[1, 3, 65, 87, 2]):
    ''' Simple example of using a list comprehension '''
    new_list = [item * 7 for item in items if item < 10]
    return new_list

