
class Solution:
    def dicesProbability(self, n: int) -> list[float]:
        dp = [1 / 6] * 6
        for i in range(2, n + 1):
            tmp = [0] * (5 * i + 1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j + k] += dp[j] / 6
            dp = tmp
        return dp

    # def dicesProbability(self, n: int) -> list[float]:
    #     dp = self.dicProb(n,6*n)
    #     return dp[n][1::]

    # def dicProb(self,n, s):
    #     # dp[i][j] i dices have dp[i][j] different ways to sum to j

    #     dp = [[0 for _ in range(s+1)] for _ in range(n+1)]
    #     for j in range(1, min(7, s+1)):
    #         dp[1][j] = 1

    #     # for i in range(1, n+1):
    #     #     dp[i][i] = 1

    #     for i in range(2, n+1):
    #         for j in range(i, min(6*i+1, s+1)):
    #             for k in range(1, i):
    #                 for m in range(1*k,  min(6*k+1, j+k-i+1)):
    #                     dp[i][j] += dp[k][m]*dp[i-k][j-m]
    #     #                 if i == 2 and j == 7:
    #     #                     print(dp[i][j], i, j)
    #     #                     print(dp[k][m], k, m)
    #     #                     print(dp[i-k][j-m], i-k, j-m)
    #     #                     print('-------------')
    #     # print(dp)
    #     for i in range(1, len(dp)):
    #         total = 6**i
    #         for j in range(i, len(dp[i])):
    #             dp[i][j] /= total
    #     # print(dp)
    #     return dp


# n = 2
# res = dicProb(n, 6*n)
# print(res)
