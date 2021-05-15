# -*- coding: utf-8 -*-
"""
Created on Sat May  8 16:48:40 2021

@author: yuxin
"""

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i]+nums[i-1])
    return max(nums)

    # import sys
    # f = [-sys.maxsize]*len(nums)
    # f[0] = nums[0]
    # max_val = f[0]
    # for i in range(1, len(nums)):
    #     f[i] = max(nums[i], nums[i]+f[i-1])
    #     max_val = max(f[i], max_val)
    # return max_val

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))


