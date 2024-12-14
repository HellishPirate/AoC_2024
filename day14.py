# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 12:57:41 2024

@author: diana
"""

import re
import numpy as np

day14input = open("day14.txt").readlines()
gridSize = [101, 103]
grid = np.zeros(gridSize)

posvel = np.zeros((len(day14input),4))
for i in range(len(day14input)):
    posvel[i,:] = re.findall("\\d{1,}|-\\d{1,}", day14input[i])
    
tFinal = 100
posvelFinal = np.zeros((len(day14input),2))
posvelFinal[:,0] = (posvel[:,2] * tFinal) + posvel[:,0]
posvelFinal[:,1] = (posvel[:,3] * tFinal) + posvel[:,1]

posvelFinal[:,0] = posvelFinal[:,0] % gridSize[0]
posvelFinal[:,1] = posvelFinal[:,1] % gridSize[1]

for i in range(len(posvelFinal)):
    x = posvelFinal[i,0].astype(int); y = posvelFinal[i,1].astype(int)
    grid[x, y] = grid[x, y] + 1
grid = grid.T

split1 = np.floor(0.5*gridSize[0]).astype(int)
split2 = np.floor(0.5*gridSize[1]).astype(int)

Q1 = (grid[0:split2,0:split1])
Q4 = (grid[split2+1:,split1+1:])
Q3 = (grid[split2+1:,0:split1])
Q2 = (grid[0:split2,split1+1:])

part1 = np.sum(Q1) * np.sum(Q2) * np.sum(Q3) * np.sum(Q4)
print("Part 1: %d" %part1)

breakCondition = False
tFinal = 1
while not breakCondition:
    grid = np.zeros(gridSize)
    posvelFinal = np.zeros((len(day14input),2))
    posvelFinal[:,0] = (posvel[:,2] * tFinal) + posvel[:,0]
    posvelFinal[:,1] = (posvel[:,3] * tFinal) + posvel[:,1]
    posvelFinal[:,0] = posvelFinal[:,0] % gridSize[0]
    posvelFinal[:,1] = posvelFinal[:,1] % gridSize[1]
    for i in range(len(posvelFinal)):
        x = posvelFinal[i,0].astype(int); y = posvelFinal[i,1].astype(int)
        grid[x, y] = grid[x, y] + 1
    grid = grid.T
    breakCondition = np.sum(grid == 2) == 0
    tFinal = tFinal + 1
    
print("Part 2: %d" %(tFinal-1))
