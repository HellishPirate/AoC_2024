# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 15:23:45 2024

@author: diana
"""
print("\033[2J\033[H", end="", flush=True)

import numpy as np

day1input = np.loadtxt("day1.txt")

sortedInput = np.zeros((len(day1input), 2))
distances = np.zeros((len(day1input), 1))

similarityScore = np.zeros((len(day1input), 1))

for i in range(len(day1input)):
    list1Min = np.nanargmin(day1input[:,0])
    list2Min = np.nanargmin(day1input[:,1])
    
    # list1Min = np.where(day1input[:,0] == np.min(day1input[:,0]))
    # list2Min = np.where(day1input[:,1] == np.min(day1input[:,1]))
    
    sortedInput[i, 0] = day1input[list1Min,0]
    sortedInput[i, 1] = day1input[list2Min,1]
    
    distances[i] = np.abs(sortedInput[i, 0] - sortedInput[i, 1])
    
    day1input[list1Min,0] = np.nan
    day1input[list2Min,1] = np.nan
    
    
totalDistance = np.sum(distances)

test = np.sum((sortedInput[1,0] == sortedInput[:,1]))
for i in range(len(day1input)):
    similarityScore[i] = sortedInput[i,0] * np.sum((sortedInput[i,0] == sortedInput[:,1]))
totalSimilarity = np.sum(similarityScore)