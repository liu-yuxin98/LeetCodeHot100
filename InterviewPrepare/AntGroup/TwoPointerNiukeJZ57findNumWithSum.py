class Solution:
    def FindNumbersWithSum(self, array: list[int], sum: int) -> list[int]:
        # write code here
        start = 0
        end = len(array)-1
        while start < end:
            if (array[start]+array[end]) == sum:
                return [array[start], array[end]]
            elif(array[start]+array[end]) < sum:
                start += 1
            else:
                end -= 1
        return []


sol = Solution()

array = [1, 2, 4, 7, 11, 15]
sum = 15

res = sol.FindNumbersWithSum(array, sum)
print(res)
