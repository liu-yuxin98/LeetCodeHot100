class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        curProfit = 0
        for i in range(0, len(prices)-1):
            if prices[i+1] > prices[i]:
                curProfit += prices[i+1]-prices[i]
            elif prices[i+1] == prices[i]:
                continue
            else:
                profit += curProfit
                curProfit = 0
        profit += curProfit
        return profit


s = Solution()
prices = [1, 2, 3, 4, 5]
prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1, 0]
prices = [6, 1, 3, 2, 4, 7]
print(s.maxProfit(prices))
