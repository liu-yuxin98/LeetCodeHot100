class Solution:

    def __init__(self) -> None:
        self.stack = [-1]

    def push(self, node):
        # write code here
        self.stack.append(node)
        self.moveUp(len(self.stack)-1)

    def pop(self):
        # write code here
        v = self.stack[1]
        self.stack[1] = self.stack[-1]
        self.stack.pop()
        self.moveDown(0)
        return v

    def moveDown(self, index):
        n = len(self.stack)-1
        last = n//2
        while True:
            if index > last:
                break
            if index == last and index*2+1 > len(self.stack):
                leftChild = index*2
                if self.stack[leftChild] < self.stack[index]:
                    self.stack[leftChild], self.stack[index] = self.stack[index], self.stack[leftChild]
                break
            leftChild = index*2
            rightChild = index*2+1
            if self.stack[index] <= self.stack[leftChild] and self.stack[index] <= self.stack[rightChild]:
                break
            elif self.stack[index] > min(self.stack[leftChild], self.stack[rightChild]):
                if self.stack[leftChild] <= self.stack[rightChild]:
                    # swap with right child
                    self.stack[index], self.stack[leftChild] = self.stack[leftChild], self.stack[index]
                    index = leftChild
                else:
                    # swap with left child
                    self.stack[index], self.stack[rightChild] = self.stack[rightChild], self.stack[index]
                    index = rightChild

    def moveUp(self, index):
        while True:
            parentIndex = index//2
            if parentIndex == 0:
                break
            elif self.stack[parentIndex] <= self.stack[index]:
                break
            else:
                self.stack[parentIndex], self.stack[index] = self.stack[index], self.stack[parentIndex]
                index = parentIndex

    def top(self):
        # write code here
        return self.stack[1]

    def min(self):
        # write code here
        return self.stack[1]


sol = Solution()
sol.push(0)
sol.push(1)
sol.push(3)
print(sol.pop())
print(sol.min())
print(sol.top())
print(sol.pop())
