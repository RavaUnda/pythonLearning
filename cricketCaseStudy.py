# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 06:13:31 2023

@author: sanil
"""
import numpy as np

heights = [78,77,77,79,76,74,77,78,72,79,80,81,79]
np_heightsIn = np.array(heights)
np_heightsM = np_heightsIn * 0.025
#count of participants
print(len(np_heightsIn))
print(np_heightsIn.size)
print(np_heightsIn.shape)

#add weights in pounds
weights = [180,182,182,185,182,188,180,183,182,185,185,186,183]
np_weights = np.array(weights)
# convert weight to Kgs

np_wtKg = np_weights * 0.453
print("weight in Kgs ",np_wtKg)

#calculate BMI
bmi = np_wtKg / (np_heightsM ** 2)
print("BMI",bmi)

#access  element
print(bmi[-1])
print(bmi[0:6])
print(bmi[-5:])

#conditional subsetting
# bmi <22
print(bmi < 23)
underWeight = bmi[bmi < 22]
print("Underwright players",underWeight)
print("# of players who are underweight",underWeight.size)
