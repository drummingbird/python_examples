# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:18:06 2018

@author: Reuben

Simple examples of builtin types.

"""

# Integers
# ============
i = 4
type_i = type(i) # int

# Strings
# ============
string = 'here is a string using apostrophes'
string2 = "Here's a string using quotes"
string3 = 'Here\'s another way to write it'
string4 = '''Here's a really good way to write it too'''
type_string = type(string) # str

first_4_chars = string[0:5]
last_char = string[-1]


# Floats
# ============
f = 5.467
type_f = type(f) # float

# Tuples
# ============
# Tuples are immutable - they cannot be changed.
tuple_a = ('a', 5, 5.4)
tuple_b = (2.1, 4.1, 5.4)
tuple_c = (i, f, last_char, 6, 7)
first_tuple_element = tuple_c[0]
tuple_slice = tuple_c[1:3]


# Lists
# ============
# Lists are mutable - they can be changed.
list_a = [0, 1, 'term', f, i, last_char]

first_list_element = list_a[0]
last_list_element = list_a[-1]
list_slice = list_a[3:5]

index = 2
list_element_by_index = list_a[index]

list_of_tuples = [tuple_a, tuple_b, tuple_c]
list_of_lists = [list_a, list_slice, list_a]

list_b = [0, 1, 2, 3, 4, 5]
list_b.append(6)

list_c = [0, 1, 2, 3, 4, 5]
list_c.append([6, 7, 8])

list_d = [0, 1, 2, 3, 4, 5]
list_d.extend([6, 7, 8])

list_e = [0, 1, 2, 3, 4, 5]
list_f = [6, 7, 8]
list_g = list_e + list_f

list_h = [56, 73, 21, 0, 476]
list_removed_by_value = list_h.remove(73)

list_removed_by_index = [56, 73, 21, 0, 476]
del list_removed_by_index[3]


# Dictionaries
# ============
# Dictionaries are mutable too.
dict_a = {'height': 4.4,
          'width': 5,
          'description': 'string'}

item_height = dict_a['height']

param = 'width'
item_for_parameter = dict_a[param]

# They can have any kinds of objects as values
dict_b = {67: list_c,
          'second': list_h}

dict_c = {'a': 35, 'b': 23}
dict_c['c'] = 47

# Updating dictionaries
dict_d = {'b': 67, 'e': 89}
dict_d.update(dict_c) # Note key 'b' is overwritten


