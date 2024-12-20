# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 15:23:45 2024

@author: diana
"""

import numpy as np
day1input = np.loadtxt("day1.txt") # numpy reads this in as a 2D array
sortedInput = np.zeros((len(day1input), 2)) # preallocate array for sorted input
distances = np.zeros((len(day1input), 1)) # preallocate array for individual distances
similarityScore = np.zeros((len(day1input), 1)) # preallocate array for individual similarities

for i in range(len(day1input)):
    list1Min = np.nanargmin(day1input[:,0]) # finds the indices of the first occurrence of the min val
    list2Min = np.nanargmin(day1input[:,1]) # does the same but for the 2nd column
    sortedInput[i, 0] = day1input[list1Min,0]
    sortedInput[i, 1] = day1input[list2Min,1]
    distances[i] = np.abs(sortedInput[i, 0] - sortedInput[i, 1])
    day1input[list1Min,0] = np.nan # change to nan to ignore on next loop
    day1input[list2Min,1] = np.nan   
totalDistance = np.sum(distances)
print("Part 1: %d" %totalDistance)

for i in range(len(day1input)):
    similarityScore[i] = sortedInput[i,0] * np.sum((sortedInput[i,0] == sortedInput[:,1]))
totalSimilarity = np.sum(similarityScore)
print("Part 2: %d" %totalSimilarity)
