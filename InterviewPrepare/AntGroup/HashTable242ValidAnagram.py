class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = [0]*26
        n = len(s)
        for i in range(n):
            chars[ord(s[i])-ord('a')] += 1
            chars[ord(t[i])-ord('a')] -= 1
        for n in chars:
            if n != 0:
                return False
        return True
