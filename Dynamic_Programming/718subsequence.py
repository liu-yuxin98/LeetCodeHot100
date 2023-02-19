class Solution:
    def findLength(self, A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
        return max(max(row) for row in memo)


S = Solution()
nums1 = [1, 2, 3, 2, 1]
nums2 = [3, 2, 1, 4, 7]

S.findLength(nums1, nums2)
