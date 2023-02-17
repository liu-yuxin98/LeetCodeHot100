class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        sold, hold, reset = float('-inf'), float('-inf'), 0
        for i in range(len(prices)):
            pre_sold = sold
            sold = hold + prices[i]
            hold = max(hold, reset-prices[i])
            reset = max(pre_sold, reset)

        return max(sold, reset)


s = Solution()
prices = [1, 2, 3, 4, 5]
prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1, 0]
# prices = [6, 1, 3, 2, 4, 7]
# prices = [3, 3, 5, 0, 0, 3, 1, 4]
# prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
print(s.maxProfit(prices))
