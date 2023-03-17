class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        cntr, w = Counter(s1), len(s1)

        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1
            if i >= w and s2[i-w] in cntr:
                cntr[s2[i-w]] += 1

            if all([cntr[i] == 0 for i in cntr]):  # see optimized code below
                return True

        return False


s1 = "ab"
s2 = "eidboaoo"
s1 = "ab"
s2 = "eidbaoo"
# s1 = "adc"
# s2 = "dcda"
sol = Solution()
res = sol.checkInclusion(s1, s2)
print(res)
