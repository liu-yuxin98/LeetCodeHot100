# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 18:03:52 2021

@author: Lenovo
"""

def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    stack = []
    res = [0 for i in range(len(temperatures))]
    for i in range(len(temperatures)):
        if stack != []:
            while stack and temperatures[stack[-1]] < temperatures[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
        stack.append(i)
    return res

temperatures = [73,74,75,71,69,72,76,73]
answer = dailyTemperatures(temperatures)
