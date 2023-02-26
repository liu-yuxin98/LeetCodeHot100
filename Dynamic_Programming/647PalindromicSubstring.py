class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        # dp[i][j] = 1 if s[i:j]is palindrom, else 0
        # initial
        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1):
            for j in range(i+1, n):
                if j == i+1 and s[i] == s[j]:
                    dp[i][j] = 1
                else:
                    # decide if dp[i][j] is 1 or  0,  s[i:j]
                    if s[i] == s[j] and dp[i+1][j-1] == 1:
                        dp[i][j] = 1
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if j == i+1 and s[i] == s[j]:
                    dp[i][j] = 1
                else:
                    # decide if dp[i][j] is 1 or  0,  s[i:j]
                    if s[i] == s[j] and dp[i+1][j-1] == 1:
                        dp[i][j] = 1
        cnt = sum([sum(row) for row in dp])
        print(dp)
        return cnt


sol = Solution()
s = "aaaaaa"
print(sol.countSubstrings(s))
