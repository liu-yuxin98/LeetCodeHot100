# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:56:10 2021

@author: Lenovo
"""

# hash dict
# def twoSum(nums, target):
#     res_dict = dict()
#     for i in range(len(nums)):
#         if target - nums[i] in res_dict:
#             return [res_dict[target-nums[i]], i]
#         res_dict[nums[i]] = i
#     return []


# double pointer
def twoSum(nums, target):
    origin_nums = [n for n in nums]
    nums.sort()
    p1 = 0
    p2 = len(nums)-1

    while True:
        if p1 >= p2:
            break
        if nums[p1] + nums[p2] == target:
            first = origin_nums.index(nums[p1])
            for second in range(len(origin_nums)):
                if second != first and origin_nums[second] == nums[p2]:
                    break
            return [min(first, second), max(first, second)]
        elif nums[p1] + nums[p2] > target:
            p2 -= 1
        else:
            p1 += 1
    return []



nums = [-1,-2,-3,-4,-5]
target = -8
res = twoSum(nums, target)