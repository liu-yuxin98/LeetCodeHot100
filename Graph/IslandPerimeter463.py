class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        # step 1 find all squre belongs to the island and store them in set
        m = len(grid)
        n = len(grid[0])
        island = set()  # store squre belongs to island

        # dfs
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             # dfs to find all squre belongs to grid
        #             fringe = []  # FILO
        #             fringe.append((i, j))
        #             while fringe:
        #                 next = fringe.pop()
        #                 island.add(next)
        #                 children = [(next[0], next[1]-1), (next[0], next[1]+1),
        #                             (next[0]-1, next[1]), (next[0]+1, next[1])]
        #                 for child in children:
        #                     if child not in island and child[0] >= 0 and child[0] < m and child[1] >= 0 and child[1] < n and grid[child[0]][child[1]] == 1:
        #                         fringe.append(child)
        #             break

        # bfs
        from collections import deque
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # bfs to find all squre belongs to grid
                    fringe = deque()  # FIFO
                    fringe.append((i, j))
                    while fringe:
                        next = fringe.popleft()  # FIFO
                        island.add(next)
                        children = [(next[0], next[1]-1), (next[0], next[1]+1),
                                    (next[0]-1, next[1]), (next[0]+1, next[1])]
                        for child in children:
                            if child not in island and child[0] >= 0 and child[0] < m and child[1] >= 0 and child[1] < n and grid[child[0]][child[1]] == 1:
                                fringe.append(child)
                    break

        primeter = 0
        # calculate perimeter
        for square in island:
            i = square[0]
            j = square[1]
            children = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
            surround = 0
            for child in children:
                if child in island:
                    surround += 1
            primeter += 4-surround
        print(primeter)
        return primeter


s = Solution()
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]


s.islandPerimeter(grid)
