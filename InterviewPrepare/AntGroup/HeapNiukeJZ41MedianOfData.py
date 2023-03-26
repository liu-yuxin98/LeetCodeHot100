class Solution:

    def __init__(self) -> None:
        self.minheap = []
        self.maxheap = []  # store negative of real val,

    def Insert(self, num):
        import heapq
        # write code here
        if self.minheap == [] and self.maxheap == []:
            heapq.heappush(self.maxheap, -num)
        elif self.minheap == []:
            heapq.heappush(self.maxheap, -num)
            v = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -v)
        else:
            if len(self.minheap) == len(self.maxheap):
                heapq.heappush(self.minheap, num)
                v = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -v)
            elif len(self.maxheap) > len(self.minheap):
                heapq.heappush(self.maxheap, -num)
                v = heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, -v)

    def GetMedian(self):
        # write code here
        if self.minheap == [] and self.maxheap == []:
            return
        elif len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0])/2
        else:
            return -self.maxheap[0]


num = [5, 2, 3, 4, 1, 6, 7, 0, 8]

sol = Solution()
for n in num:
    sol.Insert(n)
    print(sol.maxheap)
    print(sol.minheap)
    print(sol.GetMedian())
    print('-------------')
