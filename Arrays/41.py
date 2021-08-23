# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 10:02:56 2021

@author: Lenovo
"""


def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    import math
    N = len(nums)
    for i in range(N):
        if nums[i] <= 0:
            nums[i] = N+10
    for i in range(N):
        pos = math.fabs(nums[i])
        if pos <= N:
            nums[int(pos-1)] = -1*int(math.fabs(nums[int(pos-1)]))
    for i in range(N):
        if nums[i] > 0:
            return i+1
    return N+1



nums = [1,1]
output = firstMissingPositive(nums)
print(output)
 