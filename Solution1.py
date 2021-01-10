
class solution1(object):
    def twoSum(self, nums, target: int) :
        hashtable = dict()
        for i in range(0,len(nums)):
            if target-nums[i] in hashtable:
                res = []
                res.append(hashtable.get(target-nums[i]))
                res.append(i)
                return res
            else:
                hashtable[nums[i]] = i;



s1 = solution1



print(s1.twoSum(s1,[3,3],6))



