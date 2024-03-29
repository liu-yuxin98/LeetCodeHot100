# class Solution:
#     def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
#         import heapq
#         import math
#         # deafult min heap
#         minHeap = []
#         for i in range(k):
#             item = (-math.fabs(arr[i]-x), arr[i])
#             heapq.heappush(minHeap, item)

#         for i in range(k, len(arr)):
#             if math.fabs(arr[i]-x) < -minHeap[0][0]:
#                 heapq.heappop(minHeap)
#                 item = (-math.fabs(arr[i]-x), arr[i])
#                 heapq.heappush(minHeap, item)

#         res = []
#         while len(minHeap) > 0:
#             res.append(heapq.heappop(minHeap)[1])
#         res.sort()

#         return res


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left = 0
        right = len(arr)-1
        while right-left >= k:
            if x-arr[left] > arr[right]-x:
                left += 1
            else:
                right -= 1
        return arr[left:right+1]


arr = [1, 2, 3, 4, 5]
k = 4
x = 3

arr = [1, 2, 3, 4, 5]
k = 4
x = -1
sol = Solution()
res = sol.findClosestElements(arr, k, x)
print(res)
