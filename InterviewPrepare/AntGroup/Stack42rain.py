class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []
        max_index = height.index(max(height))
        heightSum = 0
        # left to heighest column
        rainSum = 0
        stack = [0]
        for i in range(1, max_index+1):
            if height[i] == 0:
                continue
            else:
                if height[i] <= height[stack[0]]:
                    heightSum += height[i]
                else:
                    rain = max(0,(i-stack[0]-1)*height[stack[0]] - heightSum)
                    rainSum += rain
                    heightSum = 0
                    stack[0] = i

        # from right to max_index
        heightSum = 0
        stack = [len(height)-1]
        for i in range(len(height)-1, max_index-1, -1):
            if height[i] == 0:
                continue
            else:
                if height[i] < height[stack[0]]:
                    heightSum += height[i]
                else:
                    rain = max(0,(stack[0]-i-1)*height[stack[0]]-heightSum)
                    rainSum += rain
                    stack[0] = i
                    heightSum = 0

        return rainSum


height = [4, 2, 0, 3, 2, 5]


sol = Solution()
res = sol.trap(height)

print(res)
