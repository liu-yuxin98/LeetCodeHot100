# class Solution:
# min heap
#     def __init__(self) -> None:
#         self.stack = [-1]

#     def push(self, node):
#         # write code here
#         self.stack.append(node)
#         self.moveUp()

#     def pop(self):
#         # write code here
#         v = self.stack[1]
#         self.stack[1] = self.stack[-1]
#         self.stack.pop()
#         self.moveDown()
#         return v

#     def moveDown(self):
#         index = 1
#         n = len(self.stack)-1
#         last = n//2
#         while True:
#             if index > last:
#                 break
#             # no right child
#             if index == last and index*2+1 > len(self.stack)-1:
#                 leftChild = index*2
#                 if self.stack[leftChild] < self.stack[index]:
#                     self.stack[leftChild], self.stack[index] = self.stack[index], self.stack[leftChild]
#                 break
#             leftChild = index*2
#             rightChild = index*2+1
#             if self.stack[index] <= self.stack[leftChild] and self.stack[index] <= self.stack[rightChild]:
#                 break
#             elif self.stack[index] > min(self.stack[leftChild], self.stack[rightChild]):
#                 if self.stack[leftChild] <= self.stack[rightChild]:
#                     # swap with left child
#                     self.stack[index], self.stack[leftChild] = self.stack[leftChild], self.stack[index]
#                     index = leftChild
#                 else:
#                     # swap with right child
#                     self.stack[index], self.stack[rightChild] = self.stack[rightChild], self.stack[index]
#                     index = rightChild

#     def moveUp(self):
#         index = len(self.stack)-1
#         while True:
#             parentIndex = index//2
#             if parentIndex == 0:
#                 break
#             elif self.stack[parentIndex] <= self.stack[index]:
#                 break
#             else:
#                 self.stack[parentIndex], self.stack[index] = self.stack[index], self.stack[parentIndex]
#                 index = parentIndex

#     def top(self):
#         # write code here
#         return self.stack[-1]

#     def min(self):
#         # write code here
#         return self.stack[1]
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self) -> None:
        self.stack = []
        self.minStack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minStack == []:
            self.minStack.append(node)
        else:
            self.minStack.append(min(self.stack[-1], node))

    def pop(self):
        # write code here
        self.pop()
        self.minStack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.min


sol = Solution()
sol.push(5)
sol.push(4)
sol.push(3)
sol.push(2)
sol.push(1)
print(sol.stack)
print(sol.pop())
print(sol.pop())
print(sol.stack)
