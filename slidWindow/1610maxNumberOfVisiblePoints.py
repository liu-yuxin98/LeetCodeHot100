class Solution:
    def visiblePoints(self, points: list[list[int]], angle: int, location: list[int]) -> int:
        import math
        # convert  to radis
        arr, extra = [], 0
        xx, yy = location
        for x, y in points:
            if x == xx and y == yy:
                extra += 1
                continue
            arr.append(math.atan2(y - yy, x - xx))

        arr.sort()
        # append same arr at back
        arr = arr + [x + 2.0 * math.pi for x in arr]
        angle = math.pi * angle / 180

        left = ans = 0
        for right in range(len(arr)):
            while arr[right] - arr[left] > angle:
                left += 1
            ans = max(ans, right-left+1)

        return ans+extra


points = [[2, 1], [2, 2], [3, 3]]
angle = 90
location = [1, 1]

sol = Solution()

sol.visiblePoints(points, angle, location)
