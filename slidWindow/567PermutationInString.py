class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        counter = Counter(s1)
        for i in range(len(s2)):
            if s2[i] not in counter:
                counter = Counter(s1)
            if i >= len(s1) and s2[i-len(s1)] in counter:
                counter[s2[i-len(s1)]] += 1

            if s2[i] in counter:
                counter[s2[i]] -= 1
                for c in counter:
                    if counter[c] != 0:
                        break
                else:
                    return True

        return False


s1 = "ab"
s2 = "eidboaoo"
# s1 = "ab"
# s2 = "eidbaoo"
s1 = "adc"
s2 = "dcda"
sol = Solution()
res = sol.checkInclusion(s1, s2)
print(res)
