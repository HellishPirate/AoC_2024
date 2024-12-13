# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:32:51 2024

@author: diana
"""

import numpy as np
import re

day13input = open("day13.txt").readlines()

tokens = np.zeros((len(day13input),))
tokensPart2 = np.zeros((len(day13input),))
for i in range(0,len(day13input),4):
    Arow1 = re.findall("\\d{2,}", day13input[i])
    Arow2 = re.findall("\\d{2,}", day13input[i+1])
    B = re.findall("\\d{2,}", day13input[i+2])
    B = np.array([int(B[0]), int(B[1])])
    BPart2 = np.array([int(B[0]), int(B[1])]) + 10000000000000
    A = np.array([[int(Arow1[0]), int(Arow2[0])], [int(Arow1[1]), int(Arow2[1])]])
    determinantInv = 1/(A[0,0]*A[1,1] - A[0,1]*A[1,0])
    AInv = np.array([[A[1,1], -A[0,1]], [-A[1,0], A[0,0]]]) * determinantInv
    sol = np.round(AInv@B)
    solPart2  = np.round(AInv@BPart2)
    checkSol = A@sol
    checkSolPart2 = A@solPart2
    
    cond = all(checkSol == B)
    condPart2 = all(checkSolPart2 == BPart2)
    if cond:
        tokens[i] = 3*(sol[0]) + (sol[1])
    if condPart2:
        tokensPart2[i] = 3*(solPart2[0]) + (solPart2[1])
    
tokensTotal = np.sum(tokens)
tokensTotalPart2 = np.sum(tokensPart2)
print("Part 1: %d" %tokensTotal)
print("Part 2: %d" %tokensTotalPart2)
