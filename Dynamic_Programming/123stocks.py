class Solution:
    # pass 192/214
    # def maxProfit(self, prices: list[int]) -> int:
    #     curProfit = 0
    #     profits = []

    #     for i in range(len(prices)-1):
    #         if prices[i+1] < prices[i]:
    #             profits.append(curProfit)
    #             curProfit = 0
    #         else:
    #             curProfit += prices[i+1]-prices[i]
    #             if i == len(prices)-2:
    #                 profits.append(curProfit)
    #     print(profits)
    #     if len(profits) == 0:
    #         return 0
    #     if len(profits) == 1:
    #         return profits[0]
    #     else:
    #         profits.sort()
    #         return profits[-1]+profits[-2]
    def maxProfit(self, prices: list[int]) -> int:
        # divide one transaction into two
        n = len(prices)
        # leftProfits[i] = max profit we can get from [0->i],with one transaction
        leftProfits = [0]*n
        rightProfits = [0]*n
        # calculate left
        minSoFar = prices[0]
        for i in range(1, n):
            minSoFar = min(minSoFar, prices[i])
            leftProfits[i] = max(leftProfits[i-1], prices[i]-minSoFar)
        # calculate right
        maxSoFar = prices[-1]
        for i in range(n-2, -1, -1):
            maxSoFar = max(maxSoFar, prices[i])
            rightProfits[i] = max(rightProfits[i+1], maxSoFar-prices[i])
        print(leftProfits)
        print(rightProfits)
        # divide from pos i we can seperate it into two trans
        # leftProfits[i] : one transaction from 0 to i
        # rightProfits[i]: one transaction from i to n-1
        # thus we just need to find i to make it max(leftProfits[i]+rightProfits[i])
        res = leftProfits[0]+rightProfits[0]
        for i in range(n):
            res = max(leftProfits[i]+rightProfits[i], res)
        return res


s = Solution()
prices = [1, 2, 3, 4, 5]
prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1, 0]
# prices = [6, 1, 3, 2, 4, 7]
# prices = [3, 3, 5, 0, 0, 3, 1, 4]
# prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
print(s.maxProfit(prices))
