# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 22:46:26 2022

@author: yuxin_liu_1998
"""

def two_sum(nums, target):
    pair_dict = dict()
    for i in range(len(nums)):
        if target - nums[i] in  pair_dict:
            return [pair_dict[target-nums[i]], i]
        pair_dict[nums[i]] = i
        