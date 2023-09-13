# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:56:42 2023

@author: U27571
"""

# All imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read file 
# Read file and set 1st two columns as index
ratings_data = pd.read_csv('C:/Users/u27571/Downloads/rating.csv')
print("------------------------------------------/n")
#print(weather_data[(weather_data['Sunshine']>5) & (weather_data['MaxTemp']>35)])
# print("------------------------------------------/n")
# print(pd.DatetimeIndex(weather_data['Date']).year)
# weather_data["Year"] = pd.DatetimeIndex(weather_data['Date']).year

ratings_data["Training"] = ratings_data["Rating"].apply(lambda x:"Yes" if x<=3.5 else "No" )
print(ratings_data.head(5))

ratings_effi = ratings_data.groupby(by=['Department'])
print(ratings_effi)

# weather_data["Month"] = pd.DatetimeIndex(weather_data['Date']).month
# weather_data["Day"] = pd.DatetimeIndex(weather_data['Date']).day
# print("------------------------------------------/n")
# print("------------------------------------------/n")
# print("------------------------------------------/n")
# #convert the temp into Farenheit
# weather_data["MaxTemp_F"] = weather_data['MaxTemp'] * 9/5 + 32


#implement lambda functions in data frame
#to add a new 
# weather_data["RainyorNot"] = weather_data['Rainfall'].apply(lambda x: "Rainy" if x>50 else "Not Rainy") 
# print(weather_data.head(10))
