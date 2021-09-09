# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:20:28 2021

@author: Lenovo
"""

def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]
    # compare first and last
    if nums[0] == nums[-1]:
        p0 = 0
        p1 = len(nums)-1
        while True:
            if p0 >= len(nums):
                return nums[0]
            if p0 == len(nums)-1:
                return min(nums[p0], nums[-1])
            if p1 <= 0:
                return nums[0]
            if p1 == 1:
                return min(nums[0], nums[p1])
            if nums[p0] > nums[p0+1]:
                return nums[p0+1]
            if nums[p1] < nums[p1-1]:
                return nums[p1]
            p0 += 1
            p1 -= 1
    elif nums[0] > nums[-1]:
        p0 = 0
        p1 = 1
        while True:
            if nums[p0] > nums[p0+1]:
                return nums[p0+1]
            if nums[p1] < nums[p1-1]:
                return nums[p1]
            p0 += 1
            p1 -= 1
    else:
        # nums[0] < nums[-1] means the nums is sorted
        return nums[0]

nums = [3,3,1,3]
output = findMin(nums)