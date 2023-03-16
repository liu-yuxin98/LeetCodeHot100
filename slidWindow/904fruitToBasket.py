class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        numdict = dict()
        start = 0
        end = 0
        maxL = 0
        while end < len(fruits):
            if len(numdict) == 2 and fruits[end] not in numdict:
                # print(start, end, numdict, maxL)

                maxL = max(maxL, end-start)
                nums = list(numdict.keys())
                if numdict[nums[0]] < numdict[nums[1]]:
                    start = numdict[nums[0]] + 1
                    del numdict[nums[0]]
                else:
                    start = numdict[nums[1]] + 1
                    del numdict[nums[1]]
                numdict[fruits[end]] = end
                # print(start, end, numdict, maxL)
                # print('---------')
            else:
                numdict[fruits[end]] = end
            end += 1

        maxL = max(maxL, end-start)
        # print(start, end, numdict, maxL)
        # print('---------')
        return maxL


sol = Solution()
fruits = [1, 2, 1]
fruits = [0, 1, 2, 2]
fruits = [1, 2, 3, 2, 2]
res = sol.totalFruit(fruits)
print(res)
