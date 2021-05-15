# -*- coding: utf-8 -*-
"""
Created on Sat May 15 11:21:22 2021

@author: yuxin
"""


def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """

    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    dp[1][1] = 1
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i+1][j+1] = False
    print(dp)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if i == 1 and j == 1:
                pass
            elif dp[i][j] is False:
                pass
            else:
                if dp[i-1][j] and dp[i][j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif dp[i-1][j] and (not dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                elif (not dp[i-1][j]) and dp[i][j-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = 0
    if dp[m][n]:
        return dp[m][n]
    else:
        return 0


obstacleGrid = [[0],[0]]
print(uniquePathsWithObstacles(obstacleGrid))
