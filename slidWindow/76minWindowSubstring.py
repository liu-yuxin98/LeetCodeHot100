class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        start = 0
        end = 0
        lessSet = set()
        needDict = dict()
        originalDict = dict()
        for c in t:
            if c not in needDict:
                needDict[c] = 1
                originalDict[c] = 1
            else:
                needDict[c] += 1
                originalDict[c] += 1
            lessSet.add(c)
        best = s
        find = False

        while start < len(s) and end < len(s):
            # s[start:end+1] does not contain t
            if s[end] in needDict:
                needDict[s[end]] -= 1
                if needDict[s[end]] == 0:
                    # this character is already satisfied in s[start:end]
                    lessSet.remove(s[end])
                # s[start:end+1] contains t
                if len(lessSet) == 0:
                    find = True
                    # move start forward
                    while start <= end:
                        if s[start] not in needDict:
                            start += 1
                        else:
                            if needDict[s[start]] == 0:
                                if end-start+1 < len(best):
                                    best = s[start:end+1]
                                needDict[s[start]] += 1
                                lessSet.add(s[start])
                                start += 1
                                break
                            else:
                                needDict[s[start]] += 1
                                start += 1
            end += 1

        if find:
            return best
        return ""


sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
s = "a"
t = "a"

s = "a"
t = "aa"

s = "ab"
t = "a"

s = "aa"
t = "aa"
res = sol.minWindow(s, t)
print(res)
