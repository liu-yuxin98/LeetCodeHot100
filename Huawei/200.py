# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 09:20:07 2021

@author: Lenovo
"""

# ---------------disjoint union set -----------------

# class UnionFind:
#     def __init__(self, grid):
#         m, n = len(grid), len(grid[0])
#         self.count = 0
#         self.parent = [-1] * (m * n)
#         self.rank = [0] * (m * n)
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     self.parent[i * n + j] = i * n + j
#                     self.count += 1

#     def find(self, i):
#         if self.parent[i] != i:
#             self.parent[i] = self.find(self.parent[i])
#         return self.parent[i]

#     def union(self, x, y):
#         rootx = self.find(x)
#         rooty = self.find(y)
#         if rootx != rooty:
#             if self.rank[rootx] < self.rank[rooty]:
#                 rootx, rooty = rooty, rootx
#             self.parent[rooty] = rootx
#             if self.rank[rootx] == self.rank[rooty]:
#                 self.rank[rootx] += 1
#             self.count -= 1

#     def getCount(self):
#         return self.count


# def numIslands(grid):
#     for i in range(len(grid)):
#         grid[i].insert(0, '0')
#         grid[i].append('0')
#     grid.insert(0, ['0' for i in range(len(grid[0]))])
#     grid.append(['0' for i in range(len(grid[0]))])
#     m = len(grid)
#     n = len(grid[0])
#     unionfind = UnionFind(grid)
#     for i in range(1, m-1):
#         for j in range(1, n-1):
#             if grid[i][j] == '1':
#                 if grid[i][j-1] == '1':
#                     unionfind.union(i*n+j-1, i*n+j)
#                 if grid[i-1][j] == '1':
#                     unionfind.union((i-1)*n+j, i*n+j)
#                 if grid[i][j+1] == '1':
#                     unionfind.union(i*n+j+1, i*n+j)
#                 if grid[i+1][j] == '1':
#                     unionfind.union((i+1)*n+j, i*n+j)
#     return unionfind.count



# ----------------------DFS ----------------
def numIslands(grid):
    def no_1_in_grid(grid):
        for row in grid:
            if 1 in row:
                return False
        else:
            return True
    
    def dfs(grid, i, j):
        if not inArea(grid, i, j):
            return
        if grid[i][j] == 0 or grid[i][j] == 2:
            pass
        elif grid[i][j] == 1:
            grid[i][j] = 2
            dfs(grid, i, j-1)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i+1, j)
    
    def inArea(grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        return True
    import copy
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = eval(grid[i][j])
    m = len(grid)
    n = len(grid[0])
    islands = 0
    no_1 = False
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                tgrid = copy.deepcopy(grid)
                dfs(grid, i, j)
                if tgrid != grid:
                    islands += 1
    return islands


# ---------------BFS ----------------



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))
print(grid)

