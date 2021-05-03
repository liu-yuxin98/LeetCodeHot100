class Solution11:
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        maxarea = min(height[left],height[right])*(right-left)

        while True:
            if left >= right:
                break
            if height[left]<=height[right]:
                left += 1
            else:
                right -= 1
            maxarea = max(maxarea,(right-left)*min(height[left],height[right]) )

        return maxarea

s = Solution11
height = [4,3,2,1,4]
print(s.maxArea(s,height))