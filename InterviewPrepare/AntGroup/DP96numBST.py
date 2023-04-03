class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1]*(n+1)
        for i in range(1, n+1):
            dp[i] = sum([dp[j]*dp[i-j-1] for j in range(i)])
        return dp[n]
