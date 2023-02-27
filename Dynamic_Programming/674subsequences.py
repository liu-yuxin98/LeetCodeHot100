class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1]+1
            else:
                dp[i] = 1
        return max(dp)
