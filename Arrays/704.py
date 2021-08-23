# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 14:22:00 2021

@author: Lenovo
"""

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums)-1
    while True:
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        mid = (left+right)//2
        if left >= mid:
            return -1
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid



nums = [1,2,3,4,5]
target = 3

output = search(nums, target)
