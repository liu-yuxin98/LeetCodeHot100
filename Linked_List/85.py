# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 19:39:21 2021

@author: Lenovo
"""

def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if matrix == []:
        return 0

    output = 0
    m = len(matrix[0])
    n = len(matrix)
    dp = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                if matrix[i][j] == '1':
                    dp[i][j] = [0, 0]
            elif i == 0:
                if matrix[i][j] == '1':
                    if dp[i][j-1] == 0:
                        dp[i][j] = [i, j]
                    else:
                        dp[i][j] = [i, dp[i][j-1][1]]
            elif j == 0:
                if matrix[i][j] == '1':
                    if dp[i-1][j] == 0:
                        dp[i][j] = [i, j]
                    else:
                        dp[i][j] = [dp[i-1][j][0], j]
            else:
                if matrix[i][j] == '1':
                    if dp[i-1][j-1] != 0:
                        if dp[i-1][j] == 0 and dp[i][j-1] == 0:
                            dp[i][j] = [i, j]
                        elif dp[i-1][j] == 0:
                            dp[i][j] = [i, dp[i][j-1][1]]
                        elif dp[i][j-1] == 0:
                            dp[i][j] = [dp[i-1][j][0], j]
                        else:
                            pos1 = [dp[i-1][j][0], dp[i-1][j][1]]
                            pos2 = [dp[i][j-1][0], dp[i][j-1][1]]
                            pos3 = [dp[i-1][j-1][0], dp[i-1][j-1][1]]
                            x1 = pos1[0]
                            y1 = pos1[1]
                            x2 = pos2[0]
                            y2 = pos2[1]
                            x3 = pos3[0]
                            y3 = pos3[1]
                            if x1 < x2:  # y1 must >= y2
                                max_area = (i-x1+1)*(j-y1+1)
                                dp[i][j] = [x1, y1]
                                if (i-x2+1)*(j-y2+1) > max_area:
                                    dp[i][j] = [x2, y2]
                                    max_area = (i-x2+1)*(j-y2+1)
                                if (i-x3+1)*(j-y3+1) > max_area:
                                    dp[i][j] = [x3, y3]
                                    max_area = (i-x3+1)*(j-y3+1)
                            elif x1 == x2:
                                dp[i][j] = [i-1, j-1]
                            else:  # x1 > x2
                                dp[i][j] = [max(dp[i-1][j][0], dp[i][j-1][0]), max(dp[i-1][j][1], dp[i][j-1][1])]

                    else:
                        if dp[i-1][j] == 0 and dp[i][j-1] == 0:
                            dp[i][j] = [i, j]
                        elif dp[i-1][j] == 0:
                            dp[i][j] = [i, dp[i][j-1][1]]
                        elif dp[i][j-1] == 0:
                            dp[i][j] = [dp[i-1][j][0], j]
                        else:
                            pos1 = [dp[i-1][j][0], dp[i-1][j][1]]
                            pos2 = [dp[i][j-1][0], dp[i][j-1][1]]
                            if i-pos1[0] >= j -pos2[1]:
                                dp[i][j] = [dp[i-1][j][0], j]
                            else:
                                dp[i][j] = [i, dp[i][j-1][1]]
    print(dp)
    output = 0
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i][j] != 0:
                dp[i][j] = (i-dp[i][j][0]+1)*(j-dp[i][j][1]+1)
                output = max(dp[i][j], output)
    return output


def maximalRectangle(matrix):
    return  0



matrix = [["0","0","0","0","0","0","1"],["0","0","0","0","1","1","1"],["1","1","1","1","1","1","1"],["0","0","0","1","1","1","1"]]

output = maximalRectangle(matrix)
