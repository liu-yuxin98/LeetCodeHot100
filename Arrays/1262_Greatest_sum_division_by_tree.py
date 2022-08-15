
def maxSumDivThree(nums: list[int]) -> int:
    # dp[0] = largest sum which is divisible by 3
    # dp[1] = largest sum when divided by 3, remainder = 1
    # dp[2] = largest sum when divided by 3, remainder = 2

    dp = [0,0,0]
    for num in nums:
        for i in dp[:]:
            dp[(i+num)%3] = max(dp[(i+num)%3], i+num)

    return dp[0]

# https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/431077/JavaC%2B%2BPython-One-Pass-O(1)-space




nums = [3,6,5,1,8]
res = maxSumDivThree(nums)
print(res)