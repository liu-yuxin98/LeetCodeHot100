class Solution448:
    def findDisappearedNumbers(self, nums):
        return set([i for i in range(1,1+len(nums))]) - set(nums)

