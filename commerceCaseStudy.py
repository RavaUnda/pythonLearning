# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:56:42 2023

@author: U27571
"""

# All imports
import pandas as pd

# Read file 
# Read file and set 1st two columns as index
weather_data = pd.read_csv('C:/Users/u27571/Downloads/Operations+in+Pandas/New folder/weatherdata.csv')
#print(weather_data.head)
print("------------------------------------------/n")
#print(weather_data[(weather_data['Sunshine']>5) & (weather_data['MaxTemp']>35)])
print("------------------------------------------/n")
print(pd.DatetimeIndex(weather_data['Date']).year)
weather_data["Year"] = pd.DatetimeIndex(weather_data['Date']).year

weather_data["Month"] = pd.DatetimeIndex(weather_data['Date']).month
weather_data["Day"] = pd.DatetimeIndex(weather_data['Date']).day
print("------------------------------------------/n")
print("------------------------------------------/n")
print("------------------------------------------/n")
#convert the temp into Farenheit
weather_data["MaxTemp_F"] = weather_data['MaxTemp'] * 9/5 + 32


#implement lambda functions in data frame
#to add a new 
weather_data["RainyorNot"] = weather_data['Rainfall'].apply(lambda x: "Rainy" if x>50 else "Not Rainy") 
print(weather_data.head(10))
print("------------------------------------------/n")
print("------------------------------------------/n")

#groupBy and aggregation
weather_data_byLocation = weather_data.groupby(by=['Location']).mean()
print(weather_data_byLocation.sort_values("Rainfall",ascending=False))
print("------------------------------------------/n")
print("------------------------------------------/n")
data_bymonth = weather_data.groupby(by = ['Month']).mean()
print(data_bymonth.sort_values("MinTemp"))
