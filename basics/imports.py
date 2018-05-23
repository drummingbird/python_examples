# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:18:06 2018

@author: Reuben

Some examples of import statements. This package also provides more examples.

Check the __init__.py files for more examples of imports.

"""

# Imports usually go at the top of the file (a 'module')
import numpy as np # numpy is a package
from numpy.linalg import norm  # linalg is a numpy module.

a = np.array([2, 5, 7])

norm_a = norm(a)
