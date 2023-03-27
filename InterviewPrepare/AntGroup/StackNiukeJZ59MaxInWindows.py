class Solution:
    def maxInWindows(self, num: list[int], size: int) -> list[int]:
        # write code here
        from collections import deque
        if size == 0 or size > len(num):
            return []
        elif size == len(num):
            return [max(num)]
        res = []
        stack = deque([])
        stack.append([0, num[0]])
        for i in range(1, size):
            while stack:
                if stack[-1][1] <= num[i]:
                    stack.pop()
                else:
                    break
            stack.append([i, num[i]])
        res.append(stack[0][1])

        for i in range(size, len(num)):
            if i-size+1 > stack[0][0]:
                stack.popleft()
            while stack:
                if stack[-1][1] <= num[i]:
                    stack.pop()
                else:
                    break
            stack.append([i, num[i]])
            res.append(stack[0][1])

        return res


sol = Solution()

num = [10, 14, 12, 11]
size = 4
# num = [1, 3, -1, -3, 5, 3, 6, 7]
# size = 3
res = sol.maxInWindows(num, size)
print(res)
