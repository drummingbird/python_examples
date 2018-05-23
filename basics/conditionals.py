# -*- coding: utf-8 -*-
"""
Created on Wed May 23 20:01:23 2018

@author: Reuben
"""

# Control logic
# -------------

def conditional_function(cond='something'):
    if cond == 'something else':
        print("cond = 'something else'")
    elif cond == 'something':
        print("cond = 'something'")
    elif cond == 5:
        print('Cond = 5')
    elif cond >= 7:
        print('Cond is greater than or equal to 7')
    elif cond < 2:
        print('Cond is less than 2')
    else:
        print('Cond is not recognised')


def check_if_string_in_list(name='Howard',
                            names=['Bob', 'George', 'Howard']):
    if name in names:
        print('match')

