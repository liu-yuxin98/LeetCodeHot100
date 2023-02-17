class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1]*len(nums)  # dp[i] max increasing length end with i

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)


nums = [4, 10, 4, 3, 8, 9]

s = Solution()

print(s.lengthOfLIS(nums))
