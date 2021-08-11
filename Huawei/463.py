# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 16:11:36 2021

@author: Lenovo
"""


def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    def inArea(grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return False
        return True

    # def dfs(grid, i, j):
    #     if not inArea(grid, i, j):
    #         return
    #     if grid[i][j] == 1:
    #         grid[i][j] = 2
    #         dfs(grid, i, j-1)
    #         dfs(grid, i-1, j)
    #         dfs(grid, i, j+1)
    #         dfs(grid, i+1, j)

    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if grid[i][j] == 1:
    #             dfs(grid, i, j)

    def count_side(grid, i, j):
        side = 0
        four_directions = [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]
        for pos in four_directions:
            if not inArea(grid, pos[0], pos[1]):
                side += 1
            else:
                if grid[pos[0]][pos[1]] == 0:
                    side += 1
        return side
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += count_side(grid, i, j)

    return perimeter

grid = [[1,0]]
print(islandPerimeter(grid))
