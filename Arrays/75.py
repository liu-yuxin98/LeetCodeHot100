# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 22:21:56 2021

@author: Lenovo
"""


def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0
    p0 = 0
    p1 = 0
    while True:
        if i >= len(nums):
            break
        if nums[i] == 0:
            nums.pop(i)
            nums.insert(p0, 0)
            p0 += 1
            p1 = max(p1, p0)
        if nums[i] == 1:
            nums.pop(i)
            nums.insert(p1, 1)
            p1 += 1
        print(i, nums)
        i += 1


nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)




