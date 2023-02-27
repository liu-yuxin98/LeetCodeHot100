class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        dp = [[0 for i in range(len(nums2)+1)] for j in range(len(nums1)+1)]
        for i in range(len(nums1)-1, -1, -1):
            for j in range(len(nums2)-1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        print(dp)
        return dp[0][0]


s = Solution()

nums1 = [1, 4, 2]
nums2 = [1, 2, 4]
nums1 = [2, 5, 1, 2, 5]
nums2 = [10, 5, 2, 1, 5, 2]
nums1 = [1, 3, 7, 1, 7, 5]
nums2 = [1, 9, 2, 5, 1]
s.maxUncrossedLines(nums1, nums2)
