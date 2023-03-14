

class Solution:
    # priority queue
    # def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
    #     import heapq
    #     n = len(nums)
    #     res = []
    #     pq = [(-nums[i], i) for i in range(k)]
    #     heapq.heapify(pq)
    #     res.append(-pq[0][0])
    #     for i in range(k, n):
    #         heapq.heappush(pq, (-nums[i], i))
    #         while pq[0][1] < i-k+1:
    #             heapq.heappop(pq)
    #         res.append(-pq[0][0])

    #     return res

    #
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        from collections import deque
        # single stack

        n = len(nums)
        stack = deque([])
        res = []
        stack.append(0)
        print(stack[-1])

        for i in range(k):
            while len(stack) > 0 and nums[i] >= nums[stack[-1]]:
                stack.pop()
            stack.append(i)
        res.append(nums[stack[0]])
        print(stack)
        for i in range(k, n):
            if stack[0] <= i-k:
                stack.popleft()
            while len(stack) > 0 and nums[i] >= nums[stack[-1]]:
                stack.pop()
            stack.append(i)
            res.append(nums[stack[0]])

        return res


s = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
res = s.maxSlidingWindow(nums, k)
print(res)
