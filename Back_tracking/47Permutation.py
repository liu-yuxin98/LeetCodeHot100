class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        path = []
        res = set()

        def back_track(nums):
            if nums == []:
                item = tuple(path)
                res.add(item)
                return

            for i in range(len(nums)):
                path.append(nums[i])
                next_nums = nums[0:i]+nums[i+1::]
                back_track(next_nums)
                path.pop()

        back_track(nums)
        result = []
        for item in res:
            result.append(list(item))
        return result


nums = [1, 1, 2]

sol = Solution()

res = sol.permuteUnique(nums)

print(res)
