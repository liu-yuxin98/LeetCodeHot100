# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 00:12:09 2021

@author: Lenovo
"""

def nextGreaterElement( nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
    
        output = []
        for i in range(len(nums1)):
            pos = nums2.index(nums1[i])
            if pos == len(nums2)-1:
                output.append(-1)
            else:
                for j in range(pos+1,len(nums2)):
                    if nums2[j] > nums1[i]:
                        output.append(nums2[j])
                        break
                else:
                    output.append(-1)
        return output

# 单调栈
def nextGreaterElement( nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = []
        stack = []
        # key is value in nums2, value is corresponding next large value
        key_map = {}
        for i in range(len(nums2)-1,-1,-1):
            if stack == []:
                stack.append(nums2[i])
                key_map[nums2[i]] = -1
            else:
                while True:
                    if stack == []:
                        stack.append(nums2[i])
                        key_map[nums2[i]] = -1
                        break
                    if stack[-1] > nums2[i]:
                        key_map[nums2[i]] = stack[-1]
                        stack.append(nums2[i])
                        break
                    else:
                        stack.pop()
        for num in nums1:
            output.append(key_map[num])

        return output

nums1 = [2,4]
nums2 = [1,2,3,4]
output = nextGreaterElement(nums1, nums2)