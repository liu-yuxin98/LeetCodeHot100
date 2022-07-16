# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 18:56:22 2022

@author: yuxin_liu_1998
"""

# sol 1 better than 6%
def sortColors(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # mark first 1 and first 2's position
        l1 = 0
        l2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                # swap with l2
                nums[l2],nums[i] = nums[i],nums[l2]
                # swap with l1
                nums[l2],nums[l1] = nums[l1],nums[l2]
                l1 += 1
                l2 += 1
            elif nums[i] == 1:
                nums[l2],nums[i] = nums[i],nums[l2]
                l2 += 1


# sol 2 after optimization better than 97%
def sortColors(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # mark first 1 and first 2's position
        l1 = 0
        l2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if l1 == l2:
                    nums[i] = nums[l1]
                    nums[l1] = 0
                else:  
                    # swap with nums[l2]
                    nums[i] = 2
                    nums[l2] = 1
                    nums[l1] = 0
                l1 += 1
                l2 += 1
            elif nums[i] == 1:
                nums[l2],nums[i] = nums[i],nums[l2]
                l2 += 1


# sol3 only take care of 0 and 2, 0 move to front and 2 move to end
def sortColors(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums,i,j):
            nums[i],nums[j] = nums[j],nums[i]
        # [0,zero] -> 0
        # (zero,i) -> 1
        # (two,len(nums)-1] -> 2
        if len(nums)<=1:
            return
        zero = -1
        two = len(nums)-1
        i = 0
        while i <= two:
            if nums[i] == 0:
                zero += 1
                swap(nums,i,zero)
            elif nums[i] == 2:
                swap(nums,i,two)
                two -= 1
                i -= 1  # ! important because it could be 0 or 1
            i += 1

                
            

        




# nums = [2,0,1]
nums = [1,0,0,0,1,2,2,0,1]
sortColors(nums)  
