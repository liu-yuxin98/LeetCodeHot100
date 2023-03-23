class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        front = 0
        end = len(nums)-1
        while front < end:
            if nums[front] == val:
                if nums[end] == val:
                    end -= 1
                else:
                    nums[front], nums[end] = nums[end], nums[front]
                    front += 1
                    end -= 1
            else:
                front += 1
