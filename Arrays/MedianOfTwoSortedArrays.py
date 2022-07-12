# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 20:46:32 2022

@author: yuxin_liu_1998
"""

def findMedianSortedArrays( nums1: list[int], nums2: list[int]) -> float:
    m = len(nums1)
    n = len(nums2)
    # the pos of the median
    aim = (m+n)//2
    s1 = 0
    s2 = 0
    e1 = m-1
    e2 = n-1
    nums1_all = False
    nums2_all = False
    # store the numbers before median
    first_half = []
    while True:
        if len(first_half) >= aim+1:
            break

        if not nums1_all:
            if nums2_all:
                s2 = -1
            while nums1[s1] <= nums2[s2] :
                mid = (s1+e1)//2
                # check if we need to switch to another list
                if nums1[mid] > nums2[s2]:
                    first_half.extend(nums1[s1:s1+1])
                    s1 += 1
                    break
                # decide if exceed boundary: (mid-s1+1)+ len(first_half) >= aim +1
                if mid -s1 + 1 + len(first_half) >= aim + 1:
                    e1 = mid
                    break
                first_half.extend(nums1[s1:mid+1])
                s1 = mid +1
                if s1 > e1:
                    nums1_all = True
                    break

        if not nums2_all:
            if nums1_all:
                s1 = -1
            while nums2[s2] <= nums1[s1] :
                mid = (s2+e2)//2
                # check if we need to switch to another list
                if nums2[mid] > nums1[s1]:
                    first_half.extend(nums1[s2:s2+1])
                    s2 += 1
                    break
                # decide if exceed boundary: (mid-s1+1)+ len(first_half) >= aim +1
                if mid -s2 + 1 + len(first_half) >= aim + 1:
                    e2 = mid
                    break
                first_half.extend(nums2[s2:mid+1])
                s2 = mid +1
                if s2 > e2:
                    nums2_all = True
                    break

    if (m+n)%2==1:
        return first_half[-1]
    else:
        return (first_half[-1]+first_half[-2])/2
    

nums1 = [1,3]
nums2 = [2]
out = findMedianSortedArrays(nums1,nums2)