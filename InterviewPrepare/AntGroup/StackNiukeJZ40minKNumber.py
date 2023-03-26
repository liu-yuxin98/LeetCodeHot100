class Solution:
    def GetLeastNumbers_Solution(self, input: list[int], k: int) -> list[int]:
        # write code here
        import heapq
        if k == 0:
            return []
        maxHeap = [-num for num in input[0:k]]
        heapq.heapify(maxHeap)
        for i in range(k, len(input)):
            print(maxHeap)
            if input[i] < -maxHeap[0]:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, -input[i])
        return [-num for num in maxHeap]


input = [0, 1, 2, 1, 2]
k = 3

input = [1]
k = 0
sol = Solution()

res = sol.GetLeastNumbers_Solution(input, k)
print(res)
