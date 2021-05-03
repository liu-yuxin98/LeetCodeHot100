class Solution169:
    def majorityElement(self, nums):
        nums = sorted(nums)
        mid = int(len(nums)/2)
        return nums[mid]

