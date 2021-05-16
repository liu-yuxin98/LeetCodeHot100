# -*- coding: utf-8 -*-
"""
Created on Sun May 16 16:06:46 2021

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
        n = len(nums)
        # rob first
        f1 = [0 for i in range(n)]
        f1[0] = nums[0]
        f1[1] = nums[0]
        for i in range(2, n-1):
            f1[i] = max(f1[i-1], f1[i-2]+nums[i])
        # rob last
        f2 = [0 for i in range(n)]
        f2[0] = 0
        f2[1] = nums[1]
        for i in range(2, n):
            f2[i] = max(f2[i-1], f2[i-2] + nums[i])
    return max(f1[n-2], f2[n-1])

nums = [1, 2, 3, 1]
print(rob(nums))

