# encoding= gbk
class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # ö���Ӵ��ĳ��� l+1
        for l in range(n):
            # ö���Ӵ�����ʼλ�� i����������ͨ�� j=i+l �õ��Ӵ��Ľ���λ��
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans





S1 = Solution
s = "aabbaa"
result = S1.longestPalindrome(S1,s)
print(result)
