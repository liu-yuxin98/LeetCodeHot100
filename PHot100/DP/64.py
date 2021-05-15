# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:18:25 2021

@author: yuxin
"""
def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    # expand another line and column
    dp = [[0 for i in range(n)] for j in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            if i == 0:
                if j == 0:
                    pass
                else:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]

    return dp[m-1][n-1]


grid = [[1,2,3],[4,5,6]]
print(minPathSum(grid))