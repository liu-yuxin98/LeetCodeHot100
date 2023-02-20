import time


class Solution:
    # recursive without record TLE
    # recursive with record TLE
    # def numDistinct(self, s: str, t: str) -> int:
    #     record = dict()
    #     res = self.numDistinctHelper(s, t, record)
    #     return res

    # def numDistinctHelper(self, s, t, record):
    #     if (s, t) in record:
    #         return record[(s, t)]
    #     if len(t) > len(s):
    #         return 0
    #     if len(t) == 0 or s == t:
    #         return 1
    #     cnt = 0
    #     for j in range(len(s)):
    #         if s[j] == t[0]:
    #             cnt += self.numDistinct(s[j+1::], t[1::])

    #     record[(s, t)] = cnt
    #     return cnt

    # dp
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[1 for j in range(len(s)+1)]for i in range(len(t)+1)]

        for i in range(len(t)-1, -1, -1):
            for j in range(len(s)-1, -1, -1):
                if t[i] == s[j]:
                    dp[i][j] += dp[i+1][j+1]
                    print(t[i], s[j], i, j, dp[i][j], dp[i+1][j+1])

        print(dp)

        return dp[0][0]


sol = Solution()

s = "rabbbit"
t = "rabbit"

s = "babgbag"
t = "bag"

# s = "daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbaeccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcaccac"
# t = "ceadbaa"
start = time.time()
print(sol.numDistinct(s, t))
end = time.time()
print(end-start)
