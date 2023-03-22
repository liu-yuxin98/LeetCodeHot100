
class Solution:

    def combine(self, n: int, k: int) -> list[list[int]]:
        nums = [i for i in range(1, n+1)]
        path = []
        res = []

        def back_track(nums, k, start_index):

            if k == 0:
                res.append(path[::])
                return
            #
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                back_track(nums, k-1, i+1)
                # backtrack
                path.pop()

        back_track(nums, k, 0)
        return res


sol = Solution()

result = sol.combine(4, 2)
print(result)
