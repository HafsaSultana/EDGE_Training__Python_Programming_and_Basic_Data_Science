# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:47:08 2024

@author: Hafsa
"""

import pandas as pd
pd.__version__


data = pd.Series([0.25, 0.5, 0.75, 1.0])
data

"""The `Series` combines a sequence of values with an explicit sequence of indices, which we can access with the `values` and `index` attributes.
The `values` are simply a familiar NumPy array:
"""

data.values

"""The `index` is an array-like object of type `pd.Index`, which we'll discuss in more detail momentarily:"""

data.index

"""Like with a NumPy array, data can be accessed by the associated index via the familiar Python square-bracket notation:"""

data[1]

data[1:3]