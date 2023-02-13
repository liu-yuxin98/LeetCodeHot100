class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        # do not rob first house
        dp = [0]*len(nums)
        dp[0] = 0
        dp[1] = nums[1]
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        dp[-1] = max(dp[-3]+nums[-1], dp[-2])
        first = dp[-1]

        # rob first house
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = nums[0]
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        dp[-1] = dp[-2]
        second = dp[-1]

        res = max(first, second)
        print(res)
        return res


nums = [0, 0]
s = Solution()
s.rob(nums)
