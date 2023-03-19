class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        l = {}
        for i in range(len(nums)):
            if nums[i] not in l:
                l[nums[i]] = i
            else:
                if i-l[nums[i]] <= k:
                    return True
                else:
                    l[nums[i]] = i
        return False


nums = [1, 2, 3, 1]
k = 3

nums = [1, 0, 1, 1]
k = 1

nums = [1, 2, 3, 1, 2, 3]
k = 2
sol = Solution()
res = sol.containsNearbyDuplicate(nums, k)
print(res)
