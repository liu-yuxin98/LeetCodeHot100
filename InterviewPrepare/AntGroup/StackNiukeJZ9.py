# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = [-1]*1000
        self.cnt = 0

    def push(self, node):
        # write code here
        self.cnt += 1
        self.stack1[-self.cnt] = node

    def pop(self):
        v = self.stack1.pop()
        self.cnt -= 1
        return v


sol = Solution()

sol.push(1)
sol.push(2)
print(sol.pop())
sol.push(3)
sol.push(4)
print(sol.pop())
print(sol.pop())
sol.push(6)
print(sol.pop())
print(sol.pop())
