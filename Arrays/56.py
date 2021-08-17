# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 12:48:42 2021

@author: Lenovo
"""

def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    # sort
    intervals.sort(key=lambda x: x[0])
    i = 0
    while True:
        if i >= len(intervals)-1:
            break
        while intervals[i][1] >= intervals[i+1][0]:
            intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
            intervals.pop(i+1)
            if i >= len(intervals)-1:
                break
        i += 1

    return intervals



intervals =  [[1,3],[2,16],[8,10],[15,18]]
output = merge(intervals)