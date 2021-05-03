class Solution283:
    def moveZeroes(self, nums):
        i = 0
        n = len(nums)
        while True:
            if i> len(nums)-1:
                break
            if nums[i] == 0:
                nums.pop(i)
            else:
                i+=1
        cn = len(nums)
        for i in range(n-cn):
            nums.append(0)
        return nums




