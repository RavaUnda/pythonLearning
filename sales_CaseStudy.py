# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:54:51 2023

@author: U27571
"""

# All imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format
# Read file 
# Read file and set 1st two columns as index
sales = pd.read_excel('C:/Users/u27571/Downloads/sales.xlsx', index_col = [0,1])


#print(sales)
# print("\n",sales.tail(2))
# print(sales.info())
# print(sales.describe())

# sales[["Sales", "Profit"]].plot(kind= "box", subplots= True)
# plt.show()
# print(sales["Profit"])


# Displays pandas float values in 2 decimals
print(sales.Sales)
print(type(sales.Sales))

#df[['col_x', 'col_y']]
print(sales[['Sales','Profit']])
