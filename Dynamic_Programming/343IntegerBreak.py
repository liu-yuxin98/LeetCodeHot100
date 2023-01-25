class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        return self.helperBreak(n)

    def helperBreak(self, n):
        if n <= 4:
            return n
        return 3*self.helperBreak(n-3)


s = Solution()

for i in range(2, 12):
    print(i, s.integerBreak(i))
