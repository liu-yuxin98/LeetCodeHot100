class Solution121:
    # 动态规划 前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
    def maxProfit(self, prices):
        profit = [0]
        for i in range(1,len(prices)):
            profit.append(prices[i] - prices[i-1])
            prices[i] = min(prices[i],prices[i-1])
        return max(profit)







