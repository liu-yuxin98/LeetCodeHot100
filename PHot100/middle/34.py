# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:42:35 2021

@author: Lenovo
"""


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if nums == []:
        return [-1, -1]
    left, right = 0, len(nums)-1
    if nums[left] > target or nums[right] < target:
        return [-1, -1]
    first = search_first(nums, target)
    last = search_last(nums, target)
    return [first, last]


def search_first(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            right = mid
            while left <= right:
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid +1
                if nums[mid] == target:
                    right = mid -1
            return left

        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1


def search_last(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            left = mid
            while left <= right:
                mid = (left+right)//2
                if nums[mid] > target:
                    right = mid -1
                if nums[mid] == target:
                    left = mid +1
            return right

        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1


nums = []   # [5, 7, 7, 8, 8, 10]
target = 6
print(searchRange(nums, target))



