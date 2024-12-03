print("\033[2J\033[H", end="", flush=True)
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
    test = all(entry == np.sort(entry))
    test1 = all(entry == np.flip(np.sort(entry)))
    test2 = (sum(counts) == len(counts))
    if (test or test1) and test2:
        for j in range(len(entry)-1):
            differences[j] = np.abs(entry[j] - entry[j+1])
        test3 = all(differences <= 3)
        if test3:
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
        test = all(entry1 == np.sort(entry1))
        test1 = all(entry1 == np.flip(np.sort(entry1)))
        test2 = (sum(counts) == len(counts))
        if (test or test1) and test2 and not safeRows[i] and not safeFlag:
            for k in range(len(entry1)-1):
                differences[k] = np.abs(entry1[k] - entry1[k+1])
            test3 = all(differences <= 3) 
            if test3:
                safeCountPart2 = safeCountPart2 + 1
                safeFlag = 1

safeCountPart2 = safeCountPart1 + safeCountPart2
print("Part 2: %d" %safeCountPart2)
