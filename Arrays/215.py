# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 18:01:13 2021

@author: Lenovo
"""

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    insert_sort(nums)
    print(nums)


def select_sort(nums):
    for i in range(len(nums)-1):
        max_index = i
        for j in range(i, len(nums)):
            if nums[j] > nums[max_index]:
                max_index = j
        nums[i], nums[max_index] = nums[max_index], nums[i]


# good for nearly sorted list
def insert_sort(nums):
    for i in range(1, len(nums)):
        j = i-1
        key = nums[i]
        while j >= 0 and nums[j]>key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key


 



nums = [3,2,3,1,2,4,5,5,6]
k = 4
findKthLargest(nums, k)
