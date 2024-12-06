# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:07:20 2024

@author: diana
"""

import re
import numpy as np

with open('day3.txt', 'r') as file:
    day3input = file.read().replace('\n', '')
mulList = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)", day3input)
dodontList = re.findall("do\\(\\)|don't\\(\\)|mul\\(\\d{1,3},\\d{1,3}\\)", day3input)

mulArray = []
mulNumArray = np.zeros((len(mulList),2))

dodontArray = []
dodontNumArray = np.zeros((len(dodontList),2))

part1 = np.zeros((len(mulList),))
part2 = np.zeros((len(dodontList),))
dodontFlag = True
for i in range(len(mulList)):
    mulArray.append(re.findall("\\d{1,3},\\d{1,3}", mulList[i]))
    mulNumArray[i] = np.loadtxt(mulArray[i], delimiter=",")
    part1[i] = mulNumArray[i, 0] * mulNumArray[i, 1]
    
for i in range(len(dodontList)):
    dodontArray.append(re.findall("\\d{1,3},\\d{1,3}", dodontList[i]))
    if dodontList[i] == "do()":
        dodontFlag = True
        continue
    elif dodontList[i] == "don't()":
        dodontFlag = False
        continue
    dodontNumArray[i] = np.loadtxt(dodontArray[i], delimiter=",")
    if dodontFlag:
        part2[i] = dodontNumArray[i, 0] * dodontNumArray[i, 1]
    
    
print("Part 1: %d" %sum(part1))
print("Part 2: %d" %sum(part2))