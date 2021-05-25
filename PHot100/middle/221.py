# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:02:49 2021

@author: Lenovo
"""

def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    m = len(matrix)
    n = len(matrix[0])
    matrix = [[eval(matrix[i][j]) for j in range(n)] for i in range(m)]
    dp = [[0 for i in range(n)] for j in range(m)]
    max_s = 0
    for i in range(m):
        for j in range(n):
            if i == 0:
                dp[i][j] = matrix[i][j]
            elif j == 0:
                dp[i][j] = matrix[i][j]
            else:
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
                    max_s = max(max_s, dp[i][j])
                else:
                    dp[i][j] = 0
    return max_s


matrix = [["0"]]

maximalSquare(matrix)
