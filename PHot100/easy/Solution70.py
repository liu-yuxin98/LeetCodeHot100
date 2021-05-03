class Solution70:
    hashdict = {1: 1, 2: 2, 3: 3}
    def climbStairs(self, n):
        if n == 2:
            return 2
        elif n == 1:
            return 1
        else:
            if n in self.hashdict:
                return self.hashdict[n]
            else:
                self.hashdict[n] = self.climbStairs(n-1)+ self.climbStairs(n-2)
                return self.hashdict[n]


s = Solution70

print(s.climbStairs(s,38))

