class Solution121:
    # ��̬�滮 ǰi���������� = max{ǰi-1���������棬��i��ļ۸�-ǰi-1���е���С�۸�}
    def maxProfit(self, prices):
        profit = [0]
        for i in range(1,len(prices)):
            profit.append(prices[i] - prices[i-1])
            prices[i] = min(prices[i],prices[i-1])
        return max(profit)







