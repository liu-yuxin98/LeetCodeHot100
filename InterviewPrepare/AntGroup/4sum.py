class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(0, n-3):
            if target > 0 and nums[i] > target:
                continue
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                elif nums[i]+nums[j] > target and target > 0:
                    continue
                l = j+1
                r = n-1
                while l < r:
                    sum = nums[i]+nums[j]+nums[l]+nums[r]
                    print(sum, i, j, l, r)
                    if sum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        l += 1
                        r -= 1
                    elif sum > target:
                        r -= 1
                    else:
                        l += 1

        return res


nums = [1, 0, -1, 0, -2, 2]
target = 0
nums = [2, 2, 2, 2, 2]
target = 8
sol = Solution()

res = sol.fourSum(nums, target)
print(res)
