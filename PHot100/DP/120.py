# -*- coding: utf-8 -*-
"""
Created on Sun May 16 15:00:15 2021

@author: yuxin
"""

def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
    return min(triangle[-1])

triangle = [[-10]]
print(minimumTotal(triangle))