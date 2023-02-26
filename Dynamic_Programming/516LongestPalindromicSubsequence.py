class Solution:
    map = dict()

    def longestPalindromeSubseq(self, s: str) -> int:
        self.map = dict()
        res = self.helper(s, 0, len(s)-1)
        print(res)
        return res

    def helper(self, s, start, end):
        if (start, end) in self.map:
            return self.map[(start, end)]
        # longest palindromic between s[start:end+1]
        if start > end:
            return 0
        if end-start == 0:
            return 1
        if end-start == 1:
            if s[start] == s[end]:
                return 2
            return 1

        if s[start] == s[end]:
            return 2 + self.helper(s, start+1, end-1)

        start2 = -1
        end2 = -1
        for i in range(start+1, end):
            if s[i] == s[end]:
                start2 = i
                break
        if start2 != -1:
            length2 = self.helper(s, start2+1, end-1)+2
        else:
            length2 = self.helper(s, start+1, end-1)

        for j in range(end-1, start, -1):
            if s[j] == s[start]:
                end2 = j
                break

        if end2 != -1:
            length1 = self.helper(s, start+1, end2-1)+2
        else:
            length1 = self.helper(s, start+1, end-1)

        length3 = self.helper(s, start+1, end-1)

        res = max(length1, length2, length3)
        self.map[(start, end)] = res
        return res


class Solution2:

    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] longest palindrome substring within s[i:j+1]
        dp = [[0] * len(s) for _ in range(len(s))]
        # initial
        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]

        return 0


sol = Solution2()
s = "cbbd"
print(sol.longestPalindromeSubseq(s))
