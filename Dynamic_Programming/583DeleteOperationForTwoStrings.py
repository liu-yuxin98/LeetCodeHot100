class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # find longest common substring then it is easy to get res.
        # similar to 1143
        m = len(word1)
        n = len(word2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        maxCommonLength = max(max(dp))
        print(maxCommonLength)
        res = m+n-2*maxCommonLength
        return res


s = Solution()
word1 = "sea"
word2 = "eat"

word1 = "leetcode"
word2 = "etco"

word1 = ""
word2 = "dd"

word1 = "park"
word2 = "spake"
print(s.minDistance(word1, word2))
