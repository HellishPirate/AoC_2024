print("\033[2J\033[H", end="", flush=True)
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:56:29 2024

@author: diana
"""

import numpy as np
import re 

day17input = open("day17.txt").readlines()

registers = np.zeros(3)
registers[0] = float(re.findall("\\d{1,}", day17input[0])[0])
registers[1] = float(re.findall("\\d{1,}", day17input[1])[0])
registers[2] = float(re.findall("\\d{1,}", day17input[2])[0])
memory = re.findall("\\d", day17input[-1])
instructionPointer = 0
programOutput = []
isComboFlag = False
def op_0(): # adv, division
    global instructionPointer
    isComboFlag = True
    operand = isCombo(isComboFlag)
    registers[0] = int(registers[0]/(2**operand))
    instructionPointer = instructionPointer + 2
    executeOp()
    
def op_1(): # bxl, B XOR OP
    global instructionPointer
    isComboFlag = False
    operand = isCombo(isComboFlag)
    registers[1] = int(registers[1]) ^ int(operand)
    instructionPointer = instructionPointer + 2
    executeOp()
    
def op_2(): # bst, modulo 8
    global instructionPointer
    isComboFlag = True
    operand = isCombo(isComboFlag)
    registers[1] = operand % 8
    instructionPointer = instructionPointer + 2
    executeOp()
    
def op_3(): # jnz, jump if
    global instructionPointer
    isComboFlag = False
    operand = isCombo(isComboFlag)
    if registers[0] == 0:
        instructionPointer = instructionPointer + 2
    elif registers[0] != 0:
        instructionPointer = int(operand)
    executeOp()

def op_4(): # bxc, B XOR C
    global instructionPointer
    # isComboFlag = False
    # operand = isCombo(isComboFlag)
    registers[1] = int(registers[1]) ^ int(registers[2])
    instructionPointer = instructionPointer + 2
    executeOp()

def op_5(): # out, output modulus 8
    global programOutput, instructionPointer
    isComboFlag = True
    operand = isCombo(isComboFlag)
    programOutput.append(str(int(operand % 8)))
    instructionPointer = instructionPointer + 2
    executeOp()
    
def op_6(): # bdv, div sto in B
    global instructionPointer
    isComboFlag = True
    operand = isCombo(isComboFlag)
    registers[1] = int(registers[0]/(2**operand))
    instructionPointer = instructionPointer + 2
    executeOp()

def op_7(): # cdv, adv sto in A
    global instructionPointer
    isComboFlag = True
    operand = isCombo(isComboFlag)
    registers[2] = int(registers[0]/(2**operand))
    instructionPointer = instructionPointer + 2
    executeOp()

def isCombo(flag):
    operand = float(memory[instructionPointer+1])
    if flag == True:
        if operand >= 0 and operand <= 3:
            return operand
        elif operand == 4:
            return registers[0]
        elif operand == 5:
            return registers[1]
        elif operand == 6:
            return registers[2]
        elif operand == 7:
            return 0
    else:
        return operand
    
def executeOp():
    try:
        opNo = float(memory[instructionPointer])
        match opNo:
            case 0:
                op_0()
            case 1:
                op_1()
            case 2:
                op_2()
            case 3:
                op_3()
            case 4:
                op_4()
            case 5:
                op_5()
            case 6:
                op_6()
            case 7:
                op_7()
    except:
        return 0
            
executeOp()

print("Part 1:")
print(*programOutput, sep=",")
