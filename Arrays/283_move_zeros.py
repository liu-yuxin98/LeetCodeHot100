# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 10:58:01 2022

@author: yuxin_liu_1998
"""
# sol 1 bubble sort ETL
def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # bubble sort  move item till meet nums != 0
    i = 0
    while i<len(nums):
        if nums[i] != 0:
            j = i -1
            while j>=0:
                if nums[j]!=0:
                    break
                nums[j],nums[j+1] = nums[j+1],nums[j]
                j -= 1
        i += 1

# snow ball !!
def moveZeroes(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # idea https://leetcode.com/problems/move-zeroes/discuss/172432/THE-EASIEST-but-UNUSUAL-snowball-JAVA-solution-BEATS-100-(O(n))-%2B-clear-explanation
        # snow ball solurion
        snowball = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                snowball += 1
            elif snowball > 0:
                nums[i],nums[i-snowball] = nums[i-snowball],nums[i]
            

            
            
            
            
        
        
        
        
    
    





nums = [0,1,2,3,0,4]
moveZeroes(nums)




























        