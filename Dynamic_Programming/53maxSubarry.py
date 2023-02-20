class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # dp[i]  max subarray end with nums[i]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
        print(dp)
        return max(dp)


s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [1]
nums = [5, 4, -1, 7, 8]
nums = [-2, 1]

s.maxSubArray(nums)
