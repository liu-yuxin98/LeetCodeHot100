# -*- coding: utf-8 -*-
"""
Created on Sat May 29 15:07:58 2021

@author: Lenovo
"""


def all_combination(nums):

    def backcheck(res, nums, track):
        if len(track) == len(nums):
            res.append([num for num in track])
            return
        for i in range(len(nums)):
            if nums[i] in track:
                continue
            # choose
            track.append(nums[i])
            # next round
            backcheck(res, nums, track)
            # remove
            track.pop()

    res = []
    backcheck(res, nums, [])
    return res



nums = [1, 2, 3]
print(all_combination(nums))






