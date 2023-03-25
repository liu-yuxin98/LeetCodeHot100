class Solution:
    def FirstNotRepeatingChar(self, str: str) -> int:
        # write code here
        cdict = dict()
        for c in str:
            cdict[c] = cdict.get(c, 0)+1

        for i in range(len(str)):
            if cdict[str[i]] == 1:
                return i
        return -1


sol = Solution()
s = "google"
res = sol.FirstNotRepeatingChar(s)
print(res)
