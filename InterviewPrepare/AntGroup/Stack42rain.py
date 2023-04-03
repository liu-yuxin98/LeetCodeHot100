class Solution:
    # sol 2  beates 87%
    def trap(self, height: list[int]) -> int:
        rightHeighest = height[::]
        leftHeightest = height[::]
        rightMax = height[-1]
        for i in range(len(height)-2, -1, -1):
            if height[i] > rightMax:
                rightMax = height[i]
            else:
                rightHeighest[i] = rightMax
        leftMax = height[0]
        for i in range(1, len(height)):
            if height[i] > leftMax:
                leftMax = height[i]
            else:
                leftHeightest[i] = leftMax
        rainSum = 0
        # print(leftHeightest)
        # print(rightHeighest)
        for i in range(len(height)):
            rainSum += min(rightHeighest[i], leftHeightest[i])-height[i]
        return rainSum
    # stack beats 45%
    # def trap(self, height: list[int]) -> int:
    #     stack = []
    #     max_index = height.index(max(height))
    #     heightSum = 0
    #     # left to heighest column
    #     rainSum = 0
    #     stack = [0]
    #     for i in range(1, max_index+1):
    #         if height[i] == 0:
    #             continue
    #         else:
    #             if height[i] <= height[stack[0]]:
    #                 heightSum += height[i]
    #             else:
    #                 rain = max(0, (i-stack[0]-1)*height[stack[0]] - heightSum)
    #                 rainSum += rain
    #                 heightSum = 0
    #                 stack[0] = i

    #     # from right to max_index
    #     heightSum = 0
    #     stack = [len(height)-1]
    #     for i in range(len(height)-1, max_index-1, -1):
    #         if height[i] == 0:
    #             continue
    #         else:
    #             if height[i] < height[stack[0]]:
    #                 heightSum += height[i]
    #             else:
    #                 rain = max(0, (stack[0]-i-1)*height[stack[0]]-heightSum)
    #                 rainSum += rain
    #                 stack[0] = i
    #                 heightSum = 0
    #     return rainSum


height = [4, 2, 0, 3, 2, 5]

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
sol = Solution()
res = sol.trap(height)

print(res)
