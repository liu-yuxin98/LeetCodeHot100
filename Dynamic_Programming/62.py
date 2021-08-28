# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 22:17:00 2021

@author: Lenovo
"""


# using dynamic programming
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    dp = [[i for i in range(n)] for j in range(m)]
    dp[0][0] = 1
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if i == 0:
                dp[i][j] = 1
            elif j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]


# using probablity
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    # it is same as choose m step to go up from (m+n) step C(m+n, m)
    def f(n):
        if n == 0:
            return 1
        else:
            return n*f(n-1)

    return int(f(m+n-2)/(f(n-1)*f(m-1)))

res = uniquePaths(3, 7)