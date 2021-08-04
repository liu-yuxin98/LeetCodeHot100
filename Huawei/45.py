# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    step = 0
    if nums == [0] or nums == [1]:
        return 0
    while i+nums[i] < len(nums)-1:
        max_reach = i
        next_pos = i
        for j in range(i+1, i+nums[i]+1):
            if j+nums[j] > max_reach:
                next_pos = j
                max_reach = j+nums[j]
        i = next_pos
        step += 1
    return step+1

nums = [2,3,1,1,4]
step = jump(nums)
