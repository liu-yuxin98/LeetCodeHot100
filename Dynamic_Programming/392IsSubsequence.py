class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [False]*len(s)
        start = 0

        for i in range(len(s)):
            if start >= len(t):
                break
            for j in range(start, len(t)):
                if s[i] == t[j]:
                    dp[i] = True
                    start = j+1
                    break
            else:
                return False
        print(dp)
        return dp[-1]


sol = Solution()

s = "axc"
t = "ahbgdc"
print(sol.isSubsequence(s, t))
