# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:02:19 2023

@author: U27571
"""

import pandas as pd

# Read the dataset
df = pd.read_csv('C:/Users/u27571/Downloads/popularity.csv')
print(df.head(5))

# Get the column names as a list
column_names = df.columns.tolist()

# Print the column names
print("Column names:")
for column in column_names:
    print(column)

# Remove rows with 5 missing values
#marks = marks.dropna(thresh=marks.shape[1]-5)
#marks = marks[marks.isnull().sum(axis=1) != 5]

# Print the number of missing values in each column
missing_values = df.isnull().sum()
print(missing_values)

print(df[' shares'].describe())
mode_value = df[' num_keywords'].mode()[0]
mean_value_Shares = df[' shares'].mean()
median_value_Shares = df[' shares'].median()

# Calculate the 78th percentile of the specified column
percentile_78_shares = df[' shares'].quantile(0.78)
percentile_60_shares = df[' shares'].quantile(0.60)
percentile_70_shares = df[' shares'].quantile(0.70)
percentile_80_shares = df[' shares'].quantile(0.80)
percentile_95_shares = df[' shares'].quantile(0.95)

# Print the mode
print("The mode of num_keywords is: ",mode_value)
print(f"The mean of shares is: {mean_value_Shares}")
print(f"The median of shares is: {median_value_Shares}")
print(f"The 78th percentile of shares is: {percentile_78_shares}")
print(f"The 60th percentile of shares is: {percentile_60_shares}")
print(f"The 70th percentile of shares is: {percentile_70_shares}")
print(f"The 80th percentile of shares is: {percentile_80_shares}")

print(f"The 95th percentile of shares is: {percentile_95_shares}")

#remove outliers
df_final =  df[df[' shares'] <= percentile_95_shares]

#compute mean after removing outliers
mean_final = df_final[' shares'].mean()

#find stand. dev
std_deviation = df_final[' shares'].std()

print(f"The final mean of shares after removing outliers: {mean_final}")
print(f"The approx Std Dev shares after removing outliers: {std_deviation}")


# Calculate the percentage of data points retained
percentage_retained = (len(df_final) / len(df)) * 100

# Calculate the percentage of data points removed
percentage_removed = 100 - percentage_retained
print(f"Percentage of data points removed: {percentage_removed:.2f}%")

