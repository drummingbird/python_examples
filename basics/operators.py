# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:18:06 2018

@author: Reuben

A really simple set of operator examples.

(Note: there are also bitwise operators.)

"""


# Assignment
x = 13
y = 3

# Normal operators (int, float, etc)
add = x + y # 16
subtract = x - y # 10
multiply = x * y # 39
divide = x / y # 4.33333
floor_divide = x // y  # 4
modulus = x % y # 1
power = x ** y # 2197


# In place modification:
x += y # 16
x -= y # 13
x *= y # 39
x /= y # 13
x //= y # 4

# Joining strings:
a = 'The quick brown fox '
b = 'jumps over the lazy dog.'
sentence = a + b
