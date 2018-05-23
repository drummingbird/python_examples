# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:18:06 2018

@author: Reuben
"""
import numpy as np

'''
Basics
----------------
'''
# Assignment
# =============
x = 7
y = 5 * x + 4

# In place:
x += 2 # Add 2
x -= 2 # Subtract 2
x *= 2 # Multiply by 2
x /= 2 # Divide by 2
x //= 1.25 # Floor divide - divide by 1.25 and discard remainder

# Modulus
35 % 5


# Integers
i = 4
print(type(i))

# Strings
string = 'here is a string using apostrophes'
string2 = "Here's a string using quotes"
string3 = 'Here\'s another way to write it'
string4 = '''Here's a really good way to write it too'''
print(type(string))

# Joining strings:
a = 'The quick brown fox '
b = 'jumps over the lazy dog.'
sentence = a + b

# Floats
f = 5.467
print(type(f))

# Tuples
tuple_a = ('a', 5, 5.4)


# Lists
list_a = [0, 1, 'term', 3, 4.1, 5]

# Dictionaries
dict_a = {'height': 4.4, 'width': 5, 'param': 'string'}




# Functions
# ============

def y(x):
    y = 5 * x + 4
    return y

y(2)


# Control logic
# -------------

cond = 'something'

if cond == 'something else':
    print('here')
elif cond == 'something':
    print('there')
elif cond == 5:
    print('Cond is 5')
elif cond >= 7:
    print('Cond is greater than or equal to 7')
elif cond < 2:
    print('Cond is less than 2')
else:
    print('nowhere')


names = ['Bob', 'George', 'Howard']
if 'Howard' in names:
    print('match')


i = 0
while i < 10:
    print('here')
    i += 1


items = [1, 3, 65, 87, 2]
for item in items:
    # Do stuff
    print(item)
    
dictionary = {'a': 4.4, 5: 'slht', 'something else': 'string'}
for key, val in dictionary.items():
    # Do stuff
    print(key + ': ' + val)
    

# Zipping
apples = [3, 6, 5, 7]
pears = [44, 55, 66, 77]
for apple, pear in zip(apples, pears):
    print(apple)
    print(pear)

# List comprehensions:
items = [1, 3, 65, 87, 2]
new_list = [item * 7 for item in items if item in [1, 2, 3]]


# Objects
# =========

class Line():
    ''' A model of a line with gradient and intercept ''' 
    
    def __init__(self, m, c):
        self.m = m
        self.c = c

    def y(self, x):
        y = self.m * x + self.c
        return y

line = Line(m=5, c=4)
line.y(2)

line.m = 3
line.y(2)



def increment(arg):
    arg = arg + 1
    return arg

x = 0
x = increment(x)
x = increment(x)
print(x)

class X():
    ''' A demo class '''
    
    def __init__(self, val):
        self._val = val
    
    def increment(self):
        self._val += 1
        
    def __repr__(self):
        return str(self._val)

x = X(0)
x.increment()
x.increment()
print(x)


# Imports / packages / modules

from scipy.optimize import fsolve

# Custom modules
# __init__.py

from . import fileIO, cables, dxf


