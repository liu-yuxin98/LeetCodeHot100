# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 16:05:30 2021

@author: Lenovo
"""


def maximalSquare(matrix):
    # dp[i][j]  max square whose right bottom corner is i,j
    # dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
    # extend matrix
    for row in matrix:
        row.insert(0, '0')
    matrix.insert(0, ['0' for i in range(len(matrix[0]))])
    dp =[[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] )+1
    maxsquare = 0
    for row in dp:
        maxsquare = max(maxsquare, max(row))
    return maxsquare


matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]


maximalSquare(matrix)
