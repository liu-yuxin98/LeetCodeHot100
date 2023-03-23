class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] = 1 if s[i:j+1] is palindrome else 0
        n = len(s)
        if n < 2:
            return s
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        maxL = 1
        begin = 0
        # length
        for Length in range(2, n+1):
            # left boundary
            for left in range(n):
                right = left+Length-1
                if right >= n:
                    break
                if s[left] != s[right]:
                    dp[left][right] = False
                else:
                    if right - left < 3:
                        dp[left][right] = True
                    else:
                        dp[left][right] = dp[left+1][right-1]

                if dp[left][right] and right-left+1 > maxL:
                    maxL = right-left+1
                    begin = left

        return s[begin:begin+maxL]


s = "cbbd"
# s = "babad"
# s = "s"
# s = "aaaa"
# s = "bananas"
sol = Solution()
res = sol.longestPalindrome(s)
print(res)
