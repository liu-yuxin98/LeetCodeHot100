# -*- coding:utf-8 -*-
class Solution:

    def __init__(self) -> None:
        from collections import deque
        self.stack = deque([])
        self.moreThanOnce = set()
        self.Once = set()
    # 返回对应char

    def FirstAppearingOnce(self):
        while self.stack:
            if self.stack[0] in self.Once:
                return self.stack[0]
            else:
                self.stack.popleft()
        return "#"

    def Insert(self, char):
        if char not in self.Once and char not in self.moreThanOnce:
            self.stack.append(char)
            self.Once.add(char)
        elif char in self.Once:
            self.Once.remove(char)
            self.moreThanOnce.add(char)


s = "google"
s = "abcdee"
sol = Solution()
res = []
for i in range(len(s)):
    sol.Insert(s[i])
    fa = sol.FirstAppearingOnce()
    print(s[0:i+1])
    print(sol.Once)
    print(sol.moreThanOnce)
    print(sol.stack)
    print(fa)
    res.append(fa)
    print('--------------')

print(res)
