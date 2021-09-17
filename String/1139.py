# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 00:23:02 2021

@author: Lenovo
"""

def largest1BorderedSquare(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    max_length = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                p = i
                # line
                while True:
                    if p < 0:
                        p += 1
                        break
                    if grid[p][j] == 0:
                        p += 1
                        break
                    p -= 1
                # column
                q = j
                while True:
                    if q < 0:
                        q += 1
                        break
                    if grid[i][q] == 0:
                        q += 1
                        break
                    q -= 1
                # a is the largest possible square length with (i,j) as right corner
                a = min(i-p+1, j-q+1)
                left = i - a + 1
                up = j - a + 1
                # check left corner (left--,up--)
                print(i, j, left, up)
                while True:
                    if left == i and up == j:
                        max_length = max(max_length, 1)
                        break
                    else:
                        form_square = True
                        for left_i in range(left, i):
                            if grid[left_i][up] == 0:
                                form_square = False
                                break
                        for up_j in range(up, j):
                            if grid[left][up_j] == 0:
                                form_square = False
                                break
                        if form_square:
                            max_length = max(i-left+1, max_length)
                            break
                    left += 1
                    up += 1
    return max_length*max_length




grid = [[1,1,1],[1,0,1],[1,1,1]]
output = largest1BorderedSquare(grid)

