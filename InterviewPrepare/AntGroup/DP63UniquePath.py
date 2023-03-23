class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    continue
                if obstacleGrid[i-1][j-1] == 0:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[m][n]
