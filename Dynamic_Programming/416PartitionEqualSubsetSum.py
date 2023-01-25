class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if(total % 2 == 1):
            return False
        half = total//2
        nums.sort
        # try to find items from nums that can add to half
        dp = [0]*(half+1)
        for i in range(len(nums)):
            for j in range(half, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
            print(dp)
        if dp[half] == half:
            return True
        return False


s = Solution()
nums = [1, 5, 5, 11]
print(s.canPartition(nums))
