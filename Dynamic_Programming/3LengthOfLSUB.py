class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        i = 0
        j = 0
        maxL = 1
        n = len(s)
        cdict = dict()
        while j < n:
            print(i, j, maxL)
            if s[j] not in cdict:
                cdict[s[j]] = j
            else:
                maxL = max(maxL, j-i)
                i = max(cdict[s[j]]+1, i)
                cdict[s[j]] = j
            j += 1
        maxL = max(maxL, j-i)
        return maxL


s = "abcabcbb"

sol = Solution()
res = sol.lengthOfLongestSubstring(s)
print(res)
