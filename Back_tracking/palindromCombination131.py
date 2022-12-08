class Solution:

    res = []
    path = []

    def partition(self, s: str) -> list[list[int]]:
        self.backtrack(s, 0)
        return self.res

    def isPalindrome(self, s):
        start = 0
        end = len(s)-1
        while True:
            if start >= end:
                return True
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

    def backtrack(self, s, start):
        if start >= len(s):
            self.res.append(self.path[::])
            return

        for i in range(start, len(s)):
            if self.isPalindrome(s[start:i+1]):
                self.path.append(s[start:i+1])
            else:
                continue
            self.backtrack(s, i+1)
            self.path.pop()


s = Solution()
print(s.partition("aab"))
