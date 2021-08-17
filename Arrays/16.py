# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 20:58:04 2021

@author: Lenovo
"""


def threeSumClosest(nums, target):
    import math
    # sort nums
    nums = sorted(nums)
    best = sum(nums[0:3])
    for i in range(0, len(nums)-2):
        if nums[i] >= target and nums[i] >= 0:
            besti = sum(nums[i:i+3])
            if math.fabs(besti-target) < math.fabs(best-target):
                best = besti
                if best == target:
                    return target
        else:
            # double point
            pj = i+1
            pk = len(nums)-1
            while True:
                if pj >= pk:
                    break
                besti = nums[i] + nums[pj] + nums[pk]
                if math.fabs(besti-target) < math.fabs(best-target):
                    best = besti
                    if best == target:
                        return target
                if besti == target:
                    return target
                elif besti > target:
                    pk -= 1
                else:
                    pj += 1

    return best



# def threeSumClosest(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#     import math
#     # sort nums
#     nums = sorted(nums)
#     best = sum(nums[0:3])
#     for i in range(0, len(nums)-2):
#         if nums[i] >= target and nums[i] >= 0:
#             besti = sum(nums[i:i+3])
#             if math.fabs(besti-target) < math.fabs(best-target):
#                 best = besti
#                 if best == target:
#                     return target
#         else:
#             for j in range(i+1, len(nums)-1):
#                 if nums[i] + nums[j] >= target and nums[j] >= 0:
#                     besti = nums[i] + nums[j] + nums[j+1]
#                     if math.fabs(besti-target) < math.fabs(best-target):
#                         best = besti
#                         if best == target:
#                             return target
#                 else:
#                     for k in range(j+1, len(nums)):
#                         besti = nums[i] + nums[j] + nums[k]
#                         if besti >= target and nums[k] >= 0:
#                             if math.fabs(besti-target) < math.fabs(best-target):
#                                 best = besti
#                                 if best == target:
#                                     return target
#                             break
#                         else:
#                             if math.fabs(besti-target) < math.fabs(best-target):
#                                 best = besti
#                                 if best == target:
#                                     return target

#     return best




nums = [1,2,5,10,11]
target = 12
output = threeSumClosest(nums, target)