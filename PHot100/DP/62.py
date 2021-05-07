# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:36:45 2021

@author: Yuxin liu
"""


def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    f = [[0 for i in range(n+1)] for j in range(m+1)]
    f[0][1] = 1
    print(f)
    for i in range(1, m+1):
        for j in range(1, n+1):
            f[i][j] = f[i-1][j] + f[i][j-1]
    return f[m][n]


print(uniquePaths(3,3))

