# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 14:28:33 2023

@author: U27571
"""

import pandas as pd

cars_per_cap = [809, 731, 588, 18, 200, 70, 45]
country = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
drives_right = [True, False, False, False, True, True, True]

data = {"cars_per_cap": cars_per_cap, "country": country, "drives_right": drives_right}

print(data)
cars  = pd.DataFrame(data)
print("\n",cars)
print(type(cars))

