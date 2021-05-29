# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:21:24 2021

@author: Lenovo
"""

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums:
        return -1
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[0] <= nums[mid]:
            if nums[0] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[len(nums) - 1]:
                l = mid + 1
            else:
                r = mid - 1
    return -1



nums = [1, 2, 3]
target = 2
search(nums, target)