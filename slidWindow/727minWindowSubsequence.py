class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cdict = dict()
        start = 0
        end = 0
        maxL = 0
        while end < len(s):
            if s[end] in cdict:
                maxL = max(maxL, end-start)
                # move start forward and del c along the way from cdict
                pre_pos = cdict[s[end]]
                for i in range(start, pre_pos):
                    del cdict[s[i]]
                start = pre_pos+1
                # update cdict[s[end]]
                cdict[s[end]] = end
            else:
                cdict[s[end]] = end
            end += 1
        maxL = max(maxL, end-start)
        return maxL


sol = Solution()
s = "abcabcbb"

s = "bbbbb"

res = sol.lengthOfLongestSubstring(s)
print(res)
