# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 22:04:02 2021

@author: Lenovo
"""


def threeSum(nums):
    nums.sort()
    output = []
    for i in range(0, len(nums)-2):
        # double pointer
        p1 = i+1
        p2 = len(nums)-1
        target = -nums[i]
        while True:
            if p1 >= p2:
                break
            if nums[p1] + nums[p2] == target:
                if [nums[i], nums[p1], nums[p2]] not in output:
                    output.append([nums[i], nums[p1], nums[p2]])
                p1 += 1
                p2 -= 1
            elif nums[p1] + nums[p2] > target:
                p2 -= 1
            else:
                p1 += 1
    return output




nums = [-1, 0, 1, 2, -1, -4]
output = threeSum(nums)
