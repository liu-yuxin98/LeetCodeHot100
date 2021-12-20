# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 22:04:02 2021

@author: Lenovo
"""


# def threeSum(nums):
#     nums.sort()
#     output = []
#     for i in range(0, len(nums)-2):
#         # double pointer
#         p1 = i+1
#         p2 = len(nums)-1
#         target = -nums[i]
#         while True:
#             if p1 >= p2:
#                 break
#             if nums[p1] + nums[p2] == target:
#                 if [nums[i], nums[p1], nums[p2]] not in output:
#                     output.append([nums[i], nums[p1], nums[p2]])
#                 p1 += 1
#                 p2 -= 1
#             elif nums[p1] + nums[p2] > target:
#                 p2 -= 1
#             else:
#                 p1 += 1
#     return output


def threeSum(nums):
    nums.sort()
    res = []
    for i in range(0,len(nums)-2):
        ps = i+1
        pe = len(nums)-1
        while True:
            if ps >= pe:
                break
            if nums[ps] + nums[pe] == -nums[i]:
                if [nums[i],nums[ps],nums[pe]] not in res:
                    res.append([nums[i],nums[ps],nums[pe]])
                ps += 1
                pe -= 1
            elif nums[ps] + nums[pe] < -nums[i]:
                ps += 1
            else:
                pe -= 1
    return res
                


nums = [-1, 0, 1, 2, -1, -4]
output = threeSum(nums)
