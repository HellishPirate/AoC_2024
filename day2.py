# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:11:25 2024

@author: diana
"""

import numpy as np

day2input = open("day2.txt").readlines()
safeCountPart1 = 0
safeCountPart2 = 0
safeRows = np.zeros((len(day2input),))

for i in range(len(day2input)):
    entry = np.fromstring(day2input[i], dtype=int, sep=" ")
    differences = np.zeros((len(entry)-1,))
    _, counts = np.unique(entry, return_counts=True)
    test = (entry == np.sort(entry))
    test1 = (entry == np.flip(np.sort(entry)))
    test2 = (sum(counts) == len(counts))
    if (all(test) or all(test1)) and test2 == True:
        for j in range(len(entry)-1):
            differences[j] = np.abs(entry[j] - entry[j+1])
        test3 = differences <= 3 
        if all(test3):
            safeCountPart1 = safeCountPart1 + 1
            safeRows[i] = 1
            
print("Part 1: %d" %safeCountPart1)

safeFlag = 0
for i in range(len(day2input)):
    entry = np.fromstring(day2input[i], dtype=int, sep=" ")
    safeFlag = 0
    for j in range(len(entry)):
        entry1 = np.delete(entry, j)
        differences = np.zeros((len(entry1)-1,))
        _, counts = np.unique(entry1, return_counts=True)
        test = (entry1 == np.sort(entry1))
        test1 = (entry1 == np.flip(np.sort(entry1)))
        test2 = (sum(counts) == len(counts))
        if (all(test) or all(test1)) and test2 == True and safeRows[i] == 0 and safeFlag == 0:
            for k in range(len(entry1)-1):
                differences[k] = np.abs(entry1[k] - entry1[k+1])
            test3 = differences <= 3 
            if all(test3):
                safeCountPart2 = safeCountPart2 + 1
                safeFlag = 1

safeCountPart2 = safeCountPart1 + safeCountPart2
print("Part 2: %d" %safeCountPart2)