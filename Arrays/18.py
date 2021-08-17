# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:40:08 2021

@author: Lenovo
"""


def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    output = []
    for i in range(0, len(nums)-3):
        for j in range(i+1, len(nums)-2):
            pk = j+1
            pl = len(nums)-1
            while True:
                temp = [nums[i], nums[j]]
                if pk >= pl:
                    break
                sum_value = nums[i] + nums[j] + nums[pk] + nums[pl]
                if sum_value > target:
                    pl -= 1
                elif sum_value < target:
                    pk += 1
                else:
                    temp.extend([nums[pk], nums[pl]])
                    if temp not in output:
                        output.append(temp)
                    pk += 1
    return output

nums = [-3,-2,-1,0,0,1,2,3]
target = 0
output = fourSum(nums, target)