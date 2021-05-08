# -*- coding: utf-8 -*-
"""
Created on Sat May  8 14:54:41 2021

@author: Lenovo
"""
def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    n = len(cost)
    f = [0]*(n+1)
    f[0] = 0
    f[1] = 0
    for i in range(2, n+1):
        f[i] = min(f[i-2]+cost[i-2], f[i-1]+cost[i-1])
    return f[n]


cost = [10, 15, 20]
print(minCostClimbingStairs(cost))
