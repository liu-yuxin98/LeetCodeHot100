# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 17:50:48 2021

@author: Lenovo
"""
# one line input
line = input('the input:').strip()
print(line)

# serval lines
n = eval(input('number of times').strip())
for i in range(n):
    line = input('the input:').strip().split()
    print(line)


def twoSum(nums, target):
    hashdict = dict()
    for i in range(len(nums)):
        if target-nums[i] in  hashdict:
            return [hashdict[target-nums[i]],i]
        hashdict[nums[i]] = i
    return []