# -*- coding: utf-8 -*-
"""
Created on Sun May  9 10:34:20 2021

@author: yuxin
"""


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 2:
        return max(nums)
    else:
        f = [0]*len(nums)
        f[0] = nums[0]
        f[1] = max(f[0], nums[1])
        for i in range(2, len(nums)):
            f[i] = max(f[i-1], f[i-2]+nums[i])
    return f[-1]



nums = [4,1]

print(rob(nums))

print(False or True)
