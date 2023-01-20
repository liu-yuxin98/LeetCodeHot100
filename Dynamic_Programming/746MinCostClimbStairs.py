class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        if(n == 2):
            return min(cost[0], cost[1])

        cost.append(0)
        dp = [0]*(n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n+1):
            dp[i] = min(dp[i-1], dp[i-2])+cost[i]
        return dp[n]
