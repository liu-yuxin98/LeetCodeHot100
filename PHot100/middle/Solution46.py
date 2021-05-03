class Solution46:

    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        last = nums.pop()
        prevres = self.permute(self,nums)
        newpreves = []
        for item in prevres:
            for i in range(len(item)+1):
                newitem = [ x for x in item]
                newitem.insert(i,last)
                newpreves.append(newitem)
        return newpreves


s = Solution46
nums = [1,2,3]
print(s.permute(s,nums))

