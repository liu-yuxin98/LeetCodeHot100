class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1]*(n+1)
        for i in range(2, n+1):
            cnt = 0
            for j in range(0, i):
                cnt += dp[j]*dp[i-j-1]
            dp[i] = cnt
        print(dp)
        return dp[-1]


s = Solution()

s.numTrees(4)
