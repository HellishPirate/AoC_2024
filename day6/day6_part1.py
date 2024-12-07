# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:08:47 2024

@author: diana
"""

import numpy as np
import re

day6input = open("day6.txt").readlines()

mapNum = []
mapNumArr = np.zeros((len(day6input),len(day6input)))
testArr = np.zeros((len(day6input),len(day6input)))

for i in range(len(day6input)):
    mapRow = day6input[i]
    mapRow = re.sub("\\^", "2", mapRow)
    mapRow = re.sub("\\.", "0", mapRow)
    mapRow = re.sub("\\#", "1", mapRow)
    mapNum.append(mapRow)
    mapNumArrRow = np.frombuffer(mapRow.encode(), np.int8) - ord('0')
    mapNumArr[i,:] = np.delete(mapNumArrRow, -1)
    
guardPos = np.where(mapNumArr == 2)

x = guardPos[0]; y = guardPos[1]
direction = "up"
posCount = 3
while y >= 0 and x >= 0:
    try:
        if direction == "up":
            if mapNumArr[x-1, y] == 0:
                # posCount = posCount + 1
                mapNumArr[x, y] = posCount
                testArr[x, y] = 1
                x = x - 1
            elif mapNumArr[x-1, y] == 1:
                direction = "right"
            elif mapNumArr[x-1, y] == 2:
                x = x - 1
            elif mapNumArr[x-1, y] >= 3:
                mapNumArr[x, y] = posCount
                testArr[x, y] = 1
                x = x - 2
        
        if direction == "right":
            if mapNumArr[x, y+1] == 0:
                # posCount = posCount + 1
                mapNumArr[x, y] = posCount
                testArr[x, y] = 1
                y = y + 1
            elif mapNumArr[x, y+1] == 1:
                direction = "down"
            elif mapNumArr[x, y+1] == 2:
                y = y + 1
            elif mapNumArr[x, y+1] >= 3:
                mapNumArr[x, y] = posCount
                testArr[x, y] = 1
                y = y + 2
                
        if direction == "down":
            if mapNumArr[x+1, y] == 0:
                # posCount = posCount + 1
                mapNumArr[x, y] = posCount
                testArr[x, y] = 1
                x = x + 1
            elif mapNumArr[x+1, y] == 1:
                direction = "left"
            elif mapNumArr[x+1, y] == 2:
                x = x + 1
            elif mapNumArr[x+1, y] >= 3:
                mapNumArr[x, y] = posCount
                testArr[x, y] = 1
                x = x + 2
        
        if direction == "left":
            if mapNumArr[x, y-1] == 0:
                # posCount = posCount + 1
                mapNumArr[x, y] = posCount
                testArr[x, y] = 1
                y = y - 1
            elif mapNumArr[x, y-1] == 1:
                direction = "up"
            elif mapNumArr[x, y-1] == 2:
                y = y - 1
            elif mapNumArr[x, y-1] >= 3:
                mapNumArr[x, y] = posCount
                testArr[x, y] = 1
                y = y - 2
    except:
        break
posCount = posCount - 3
sumUnique = np.sum(testArr)
print("Part 1: %d" %sumUnique)