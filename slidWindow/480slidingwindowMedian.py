# class Solution:
# def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
#     import heapq
#     n = len(nums)
#     temp = nums[0:k]
#     temp.sort()
#     print(temp)
#     res = []
#     bigq = []
#     smallq = []

#     for i in range(k):
#         heapq.heappush(smallq, (nums[i], i))

#     for _ in range(k//2):
#         item = heapq.heappop(smallq)
#         newitem = (-item[0], item[1])
#         heapq.heappush(bigq, newitem)

#     heapq.heapify(bigq)
#     heapq.heapify(smallq)

#     print(smallq)
#     print(bigq)
#     print('----------')
#     # len(smallq) >= len(bigq)
#     for i in range(k, n):
#         # insert nums[i] to either two heaps
#         if nums[i] <= -bigq[0][0]:
#             heapq.heappush(bigq, (-nums[i], i))
#         elif nums[i] > bigq[0][0] and nums[i] <= smallq[0][0]:
#             if len(smallq) <= len(bigq):
#                 heapq.heappush(smallq, (nums[i], i))
#             else:
#                 heapq.heappush(bigq, (-nums[i], i))
#         else:
#             heapq.heappush(smallq, (nums[i], i))

#         # keep in range
#         while len(smallq) > 0 and smallq[0][1] <= i-k:
#             heapq.heappop(smallq)

#         while len(bigq) > 0 and bigq[0][1] <= i-k:
#             heapq.heappop(bigq)

#         # keep balance
#         while len(bigq)-len(smallq) > 0:
#             item = heapq.heappop(bigq)
#             newitem = (-item[0], item[1])
#             heapq.heappush(smallq, newitem)

#         while len(smallq)-len(bigq) > 1:
#             item = heapq.heappop(smallq)
#             newitem = (-item[0], item[1])
#             heapq.heappush(bigq, newitem)

#         print(smallq)
#         print(bigq)
#         print('----------')
#         #
#         if len(smallq) == len(bigq):
#             res.append((smallq[0][0]-bigq[0][0])/2)
#         else:
#             res.append(smallq[0][0])
#     return res

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        if k == 2:
            return [(nums[i]+nums[i+1])/2 for i in range(0, len(nums)-1)]
        import heapq
        n = len(nums)
        minheap = []
        maxheap = []
        res = []
        for i in range(k):
            heapq.heappush(minheap, (nums[i], i))

        for _ in range(k//2):
            item = heapq.heappop(minheap)
            newitem = (-item[0], item[1])
            heapq.heappush(maxheap, newitem)

        if k % 2 == 0:
            res.append((minheap[0][0]-maxheap[0][0])/2)
        else:
            res.append(minheap[0][0])

        print('minheap', minheap)
        print('maxheap', maxheap)
        print('-----------')
        for i in range(k, n):
            if nums[i] <= minheap[0][0]:
                item = (-nums[i], i)
                heapq.heappush(maxheap, item)
                if nums[i-k] >= minheap[0][0]:
                    # situation 1 , nums[i] <=minheap[0][0] and nums[i-k] in minheap
                    item = heapq.heappop(maxheap)
                    newitem = (-item[0], item[1])
                    heapq.heappush(minheap, newitem)
                else:
                    pass
                    # situation 2 , nums[i] <=minheap[0][0] and nums[i-k] in maxheap

            else:
                item = (nums[i], i)
                heapq.heappush(minheap, item)
                if nums[i-k] >= minheap[0][0]:
                    pass
                    # situation 3 , nums[i] > minheap[0][0] and nums[i-k] in minheap
                else:
                    # situation 4 , nums[i] > minheap[0][0] and nums[i-k] in maxheap
                    item = heapq.heappop(minheap)
                    newitem = (-item[0], item[1])
                    heapq.heappush(maxheap, newitem)
            #
            leftBoundary = i-k

            while len(minheap) > 0 and minheap[0][1] <= leftBoundary:
                heapq.heappop(minheap)

            while len(maxheap) > 0 and maxheap[0][1] <= leftBoundary:
                heapq.heappop(maxheap)

            print('minheap', minheap)
            print('maxheap', maxheap)

            if k % 2 == 0:
                res.append((minheap[0][0]-maxheap[0][0])/2)
            else:
                res.append(minheap[0][0])
            print(res)

        return res


s = Solution()
nums = [-2, -2, 1, -2, -2, -2,
        1, 1, 1, 1, -2, 1, -2]
k = 2

res = s.medianSlidingWindow(nums, k)
print(res)
