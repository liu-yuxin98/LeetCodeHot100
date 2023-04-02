class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        j = 0
        while j < len(nums):
            while nums[j] == val:
                j += 1
                if j >= len(nums):
                    return i
            nums[i] = nums[j]
            i += 1
            j += 1
        return i
