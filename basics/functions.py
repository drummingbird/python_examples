# -*- coding: utf-8 -*-
"""
Created on Wed May 23 19:56:27 2018

@author: Reuben

Simple examples of functions.

"""

def basic(x):
    ''' A really basic function. '''
    
    y = 5 * x + 4
    return y

y = basic(2) # 14


default = 5
def use_default_argument(arg1, arg2=default):
    ''' This function has a default for arg2, so it's optional '''
    
    output = basic(arg1) + arg2
    return output

arg1 = 8
result = use_default_argument(arg1) # 49

# Named arguments can be passed in any order, but after unnammed ones.
result_2 = use_default_argument(arg2=3, arg1=6) # 67

def return_demo():
    ''' The 'return' command returns the value to the caller and exits. '''
    
    # some code
    return 'first return'
    # more code
    return 'second return'

return_string = return_demo() # 'first return'


def packing_unpacking_demo(*args, **kwargs):
    string = ''
    string += 'args were: '
    for arg in args:
        string += str(arg) + ', '
    string = string[0:-2]
    string += '. kwargs were: '
    for key, val in kwargs.items():
        string += "'" + str(key) + "': " + str(val) + ', '
    string = string[0:-2]
    return string

args = [5, 'string']
kwargs = {'a': 67, 'b': 33}
return_string_b = packing_unpacking_demo(*args, **kwargs)
