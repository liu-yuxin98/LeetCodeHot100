# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 21:52:01 2022

@author: yuxin_liu_1998
"""


# with two sum as basic algorithm
def threeSum( nums: list[int]) -> list[list[int]]:
        # sort arrays
        nums = sorted(nums)
        res = set()
        
        # iterate through nums
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            target = -nums[i]
            # using two sum algotithm to solve for each target
            value_dict = dict()
            for j in range(i+1,len(nums)):
                if target-nums[j] in value_dict:
                    temp_res = (nums[i],target-nums[j],nums[j])
                    if temp_res not in res:
                        res.add(temp_res)
                else:
                    value_dict[nums[j]] = value_dict.get(nums[j],0) + 1
        # 
        out = []
        for item in res:
            out.append(list(item))
        
        return out


# solution 2 double pointer
def threeSum( nums: list[int]) -> list[list[int]]:
        # sort arrays
        nums = sorted(nums)
        res = set()
        n = len(nums)
        i = 0
        
        while True:
            if i>=n or nums[i] > 0:
                break
            l = i+1
            r = n-1      
            while True:
                if l >= r:
                    break
                total = nums[i]+nums[l]+nums[r]
                if total == 0:
                    res.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
            i += 1
        out = list([list(item) for item in res])           
        return out



nums = [-1,0,1,2,-1,-4]
nums = [0,1,1]
nums = [0,0,0]
nums = [3,0,-2,-1,1,2]
out = threeSum(nums)