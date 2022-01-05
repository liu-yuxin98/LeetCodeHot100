# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 10:45:43 2021

@author: Lenovo
"""

def dailyTemperatures( temperatures):
    waiting = [0]*len(temperatures)
    stack = []
    for i in range(len(temperatures)-1,-1,-1):
        if stack == []:
            stack.append(i)
        else:
            while True:
                if stack == []:
                    stack.append(i)
                    break
                if temperatures[i] < temperatures[stack[-1]]:
                    waiting[i] = stack[-1]-i
                    stack.append(i)
                    break
                else:
                    stack.pop()
                    
    return waiting


temperatures = [73,74,75,71,69,72,76,73]
output = dailyTemperatures(temperatures)