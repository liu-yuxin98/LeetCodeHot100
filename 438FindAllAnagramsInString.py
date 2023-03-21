class Solution:
    # https://leetcode.com/problems/find-all-anagrams-in-a-string/
    # beats 99% 
    def findAnagrams(self, s: str, p: str) -> list[int]:

        if len(s) < len(p):
            return []
        if len(p) == 1:
            res = []
            for i in range(len(s)):
                if s[i] == p:
                    res.append(i)
            return res
        n = len(s)
        i = 0
        j = 0
        pdict = dict()
        for c in p:
            pdict[c] = pdict.get(c, 0)+1

        res = []
        while i < n and j < n:
            if s[i] in pdict:
                tdict = dict()
                tdict[s[i]] = 1
                j = i+1
                while j < n:
                    if s[j] not in pdict:
                        i = j+1
                        break
                    else:
                        tdict[s[j]] = tdict.get(s[j], 0)+1
                        if tdict[s[j]] > pdict[s[j]]:
                            # move i forward until s[i] = s[j]
                            while s[i] != s[j]:
                                i += 1
                            i += 1
                            break
                        else:
                            if tdict == pdict:
                                res.append(i)
                                j += 1
                                # move till s[i]!=s[j]
                                while i < n and j < n:
                                    if s[i] == s[j]:
                                        res.append(i+1)
                                        i += 1
                                        j += 1
                                    else:
                                        break
                            else:
                                j += 1
            else:
                i += 1

        return res



# class Solution:
#     # https://leetcode.com/problems/find-all-anagrams-in-a-string/
#     def findAnagrams(self, s: str, p: str) -> list[int]:
#         return 0

s = "cbaebabacd"
p = "abc"
s = "abab"
p = "ab"

# s = "a"
# p = "ab"
sol = Solution()
res = sol.findAnagrams(s, p)
print(res)
