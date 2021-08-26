# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 01:00:51 2021

@author: Lenovo
"""


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    
    combined = []
    if nums1 == []:
        combined = nums2
    elif nums2 == []:
        combined = nums1
    else:
        p1 = 0
        p2 = 0
        while True:
            if nums1[p1] >= nums2[p2]:
                combined.append(nums2[p2])
                p2 += 1
                if p2 >= len(nums2):
                    combined += nums1[p1::]
                    break
            else:
                combined.append(nums1[p1])
                p1 += 1
                if p1 >= len(nums1):
                    combined += nums2[p2::]
                    break
    n = len(combined)
    if n % 2 == 0:
        return float(combined[n//2-1] + combined[n//2])/2
    else:
        return combined[n//2]


nums1 = [1, 2]
nums2 = [3, 4]
output = findMedianSortedArrays(nums1, nums2)