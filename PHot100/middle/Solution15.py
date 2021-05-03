class Solution15:
    def threeSum(self, nums):
        if len(nums)<3:
            return []

        nums.sort()
        if nums[0]>0 or nums[-1]<0:
            return []
        else:
            res = []
            i = 0
            while True:
                # boundary
                if i> len(nums)-3 or nums[i]>0:
                    break
                goal = 0-nums[i]
                # to find j,k in nums[i+1::] to make sum(j,k) = goal
                j = i+1
                k = len(nums)-1
                while True:
                    if j>=k:
                        break
                    if nums[j]+nums[k] == goal:
                        if [nums[i],nums[j],nums[k]] not in res:
                            res.append([nums[i],nums[j],nums[k]])

                    if nums[j]+nums[k] < goal:
                        j += 1
                    else:
                        k-=1
                i += 1
        return res


s = Solution15
nums = [-1,0,1,2,-1,-4]

print(s.threeSum(s,nums))
