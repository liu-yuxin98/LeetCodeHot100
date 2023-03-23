class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        # o(NlogN)
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i
