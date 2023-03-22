class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        from collections import deque
        cnt = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(pos):
            fringe = [pos]
            while fringe:
                node = fringe.pop()
                x = node[0]
                y = node[1]
                visited[x][y] = True
                neighbors = [[x+direct[0], y+direct[1]]
                             for direct in directions]
                validneighbors = [neighbor for neighbor in neighbors if neighbor[0] >=
                                  0 and neighbor[0] < m and neighbor[1] >= 0 and neighbor[1] < n and grid[neighbor[0]][neighbor[1]] == "1"]
                for neighbor in validneighbors:
                    if not visited[neighbor[0]][neighbor[1]]:
                        dfs(neighbor)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if not visited[i][j]:
                        cnt += 1
                        dfs([i, j])
                        # start bfs from (i,j)
                        # fringe = deque([])
                        # fringe.append([i, j])
                        # while fringe:
                        #     curPos = fringe.popleft()
                        #     x = curPos[0]
                        #     y = curPos[1]
                        #     visited[x][y] = True
                        #     neighbors = [[x+direct[0], y+direct[1]]
                        #                  for direct in directions]
                        #     validneighbors = [neighbor for neighbor in neighbors if neighbor[0] >=
                        #                       0 and neighbor[0] < m and neighbor[1] >= 0 and neighbor[1] < n and grid[neighbor[0]][neighbor[1]] == "1"]
                        #     for neighbor in validneighbors:
                        #         if not visited[neighbor[0]][neighbor[1]]:
                        #             fringe.append(neighbor)
                        #             visited[neighbor[0]][neighbor[1]] = True

        return cnt


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

sol = Solution()

res = sol.numIslands(grid)
print(res)
