class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        profit = 0
        empty = 0
        hold = -prices[0]
        for i in range(n):
            pre_hold = hold
            hold = max(pre_hold, empty-prices[i])
            empty = max(empty, pre_hold+prices[i]-fee)
        return empty


prices = [1, 3, 2, 8, 4, 9]
fee = 2

s = Solution()
print(s.maxProfit(prices, fee))
