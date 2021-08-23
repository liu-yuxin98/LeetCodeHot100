# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 10:01:19 2021

@author: Lenovo
"""

def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # find the highest and its h_index
    index = 0  # index for the heighest
    for i in range(len(height)):
        if height[i] > height[index]:
            index = i
    area = 0
    temp_heighest = height[0]
    for i in range(0, index):
        if height[i] > temp_heighest:
            temp_heighest = height[i]
        area += temp_heighest - height[i]

    temp_heighest = height[-1]
    for i in range(len(height)-1, index, -1):
        if height[i] > temp_heighest:
            temp_heighest = height[i]
        area += temp_heighest - height[i]
    return area