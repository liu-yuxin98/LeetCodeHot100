class Solution:
    # def maxProfit(self, k: int, prices: list[int]) -> int:
    #     if len(prices) <= 1:
    #         return 0
    #     n = len(prices)
    #     priceDiff = [prices[i]-prices[i-1] for i in range(1, n)]
    #     # remove negatives from front and rear

    #     start = 0
    #     while start < len(priceDiff) and priceDiff[start] <= 0:
    #         start += 1
    #     end = len(priceDiff)-1
    #     while end > 0 and priceDiff[end] <= 0:
    #         end -= 1
    #     if start == len(priceDiff):
    #         return 0

    #     priceDiff = priceDiff[start:end+1]
    #     if len(priceDiff) == 0:
    #         return 0

    #     positiveDiff = [diff for diff in priceDiff if diff > 0]
    #     negativeDiff = [diff for diff in priceDiff if diff < 0]
    #     negatives = len(negativeDiff)
    #     print(priceDiff)

    #     if k > negatives:
    #         return sum(positiveDiff)
    #     else:
    #         # k <= negatives
    #         for i in range(k-1):
    #             cur_min = min(priceDiff)
    #             min_index = priceDiff.index(cur_min)
    #             priceDiff[min_index] = 1001  # because prices[i]<=1000
    #         # after that we can get a new priceDiff seperate by 1001, our goal is to find max profit within each segement
    #         print(priceDiff)

    #         profit = 0
    #         start = 0
    #         end = 0
    #         while True:
    #             if start >= len(priceDiff):
    #                 break
    #             if end >= len(priceDiff):
    #                 segment = priceDiff[start:end]
    #                 profit += self.maxSum(segment)
    #                 break
    #             if priceDiff[start] == 1001:
    #                 start += 1
    #                 end += 1
    #             else:
    #                 if (priceDiff[end] == 1001):
    #                     segment = priceDiff[start:end]
    #                     profit += self.maxSum(segment)
    #                     start = end+1
    #                     end = start
    #                 else:
    #                     end += 1

    #     return profit

    # def maxSum(self, nums):
    #     accumulateSum = 0
    #     maxValue = accumulateSum
    #     for i in range(len(nums)):
    #         accumulateSum = max(accumulateSum+nums[i], 0)
    #         maxValue = max(maxValue, accumulateSum)
    #     return maxValue

    # method 1 dp-> O(n*k)
    # def maxProfit(self, k: int, prices: list[int]) -> int:
    #     n = len(prices)

    #     # solve special cases
    #     if not prices or k == 0:
    #         return 0

    #     if 2*k > n:
    #         res = 0
    #         for i, j in zip(prices[1:], prices[:-1]):
    #             res += max(0, i - j)
    #         return res

    #     # dp[i][used_k][ishold] = balance
    #     # ishold: 0 nothold, 1 hold
    #     dp = [[[-math.inf]*2 for _ in range(k+1)] for _ in range(n)]

    #     # set starting value
    #     dp[0][0][0] = 0
    #     dp[0][1][1] = -prices[0]

    #     # fill the array
    #     for i in range(1, n):
    #         for j in range(k+1):
    #             # transition equation
    #             dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
    #             # you can't hold stock without any transaction
    #             if j > 0:
    #                 dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])

    #     res = max(dp[n-1][j][0] for j in range(k+1))
    #     return res

    # method 2 O(n(n-k))
    def maxProfit(self, k: int, prices: list[int]) -> int:
        # special cases O(1)
        if len(prices) <= 1 or k == 0:
            return 0
        profit = 0

        # transcation time is no longer a limit O(n)
        if 2*k > len(prices):
            for first, second in zip(prices[0:-1], prices[1::]):
                profit += max(0, second-first)
            return profit

        # get all continue increasing prices O(n)
        transactions = []
        start = 0
        end = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                end = i
            else:
                if end > start:
                    transactions.append([start, end])
                start = i
        if end > start:
            transactions.append([start, end])

        # all increasing trans can be made O(k)
        if k >= len(transactions):
            for trans in transactions:
                profit += prices[trans[1]]-prices[trans[0]]
            return profit

        # we need merge some trans to get max profit
        # we should merge or remove trans till len(trans)=k
        # O（n*(n/2-k))
        while True:
            if len(transactions) == k:
                break

            # every time we should delete one trans or merge two trans to loos less

            # find min loss if delete O(n/2)
            deleteIndex = 0
            minLossDelete = prices[transactions[0]
                                   [0]] - prices[transactions[0][1]]
            for i in range(1, len(transactions)):
                if prices[transactions[i][0]] - prices[transactions[i][1]] > minLossDelete:
                    minLossDelete = prices[transactions[i]
                                           [0]] - prices[transactions[i][1]]
                    deleteIndex = i

            # find i that max( trans[i][0] -trans[i-1][1]) and merge trans[i] and trans[i-1]
            # find min loss if merge 0(n/2)
            mergeIndex = 1
            minLossMerge = prices[transactions[1][0]] - \
                prices[transactions[0][1]]
            for i in range(1, len(transactions)):
                trans1 = transactions[i-1]
                trans2 = transactions[i]
                trans1Sell = prices[trans1[1]]
                trans2Buy = prices[trans2[0]]
                if trans2Buy-trans1Sell > minLossMerge:
                    mergeIndex = i
                    minLossMerge = trans2Buy-trans1Sell

            # O(n/2)
            if minLossMerge > minLossDelete:
                # merge
                transactions[mergeIndex-1] = [transactions[mergeIndex-1]
                                              [0], transactions[mergeIndex][1]]
                transactions.pop(mergeIndex)  # O(n/2)
            else:
                # delete
                transactions.pop(deleteIndex)
        for trans in transactions:
            profit += prices[trans[1]] - prices[trans[0]]

        return profit


k = 1
prices = [6, 1, 6, 4, 3, 0, 2]

s = Solution()
print(s.maxProfit(k, prices))
