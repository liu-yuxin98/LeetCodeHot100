class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buyIn = prices[0]
        sellOut = prices[0]
        maxEarn = sellOut-buyIn

        i = 0
        while i < len(prices):
            if prices[i] < buyIn:
                maxEarn = max(maxEarn, sellOut-buyIn)
                buyIn = prices[i]
                sellOut = prices[i]
            else:
                sellOut = max(sellOut, prices[i])

            i += 1
        return max(sellOut-buyIn, maxEarn)
