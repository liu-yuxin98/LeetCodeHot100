class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        print(dp)
        return dp[0][0]


text1 = "ace"
text2 = "abcde"

text1 = "abc"
text2 = "abc"

text1 = "abc"
text2 = "def"

text1 = "bl"
text2 = "yby"

text1 = "ezupkr"
text2 = "ubmrapg"

s = Solution()
s.longestCommonSubsequence(text1, text2)
