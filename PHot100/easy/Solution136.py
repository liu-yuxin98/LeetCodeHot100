class Solution136:
    def singleNumber(self, nums):
        # XOR gate
        a = 0
        for num in nums:
            a = a^num
        return a


