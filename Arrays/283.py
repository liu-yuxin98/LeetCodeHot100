# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 11:53:15 2021

@author: Lenovo
"""

def moveZeroes(nums):
    # move 0 to end
    count_zero = 0
    count_others = 0
    i = 0
    while True:
        if i >= len(nums):
            break
        if count_others + count_zero >= len(nums):
            break
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            count_zero += 1
        else:
            count_others += 1
            i += 1
    return nums

nums = [0,0,0,0]
output = moveZeroes(nums)