# -*- coding: utf-8 -*-
"""
Created on Sun May 16 10:32:51 2021

@author: yuxin
"""
def numTrees(n):
    """
    :type n: int
    :rtype: int
    """
    g = [0 for i in range(n+1)]
    f = [[0 for i in range(n+1)] for j in range(n+1)]
    g[0] = 1
    g[1] = 1
    for j in range(2, n+1):
        g[j] = 0
        for i in range(1, j+1):
            f[i][j] = g[i-1]*g[j-i]
            g[j] += f[i][j]
    return g[n]

print(numTrees(3))