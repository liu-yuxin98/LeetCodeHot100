class Solution:
    def GetUglyNumber_Solution(self, index: int) -> int:
        # write code here

        if index < 7:
            return index
        p2 = 0
        p3 = 0
        p5 = 0
        nums = [1]
        for _ in range(index-1):
            newNum = min(nums[p2]*2, nums[p3]*3, nums[p5]*5)
            if nums[p2]*2 == newNum:
                p2 += 1
            if nums[p3]*3 == newNum:
                p3 += 1
            if nums[p5]*5 == newNum:
                p5 += 1
            nums.append(newNum)
        return nums[-1]
