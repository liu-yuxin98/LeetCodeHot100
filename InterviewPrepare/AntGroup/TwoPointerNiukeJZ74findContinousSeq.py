class Solution:
    def FindContinuousSequence(self, sum: int) -> list[list[int]]:
        # write code here
        start = sum//2
        end = sum-start
        if start == end:
            start -= 1
        res = []
        curSum = start+end
        cnt = 2
        while start > 0:
            print(start, end, curSum)
            if curSum == sum:
                res.append([i for i in range(start, end+1)])
                curSum -= end
                curSum += 2*start-3
                end -= 1
                start -= 2
                cnt += 1
            elif curSum > sum:
                end -= 1
                start -= 1
                curSum -= cnt
            else:
                # curSum < sum
                start -= 1
                cnt += 1
                curSum += start
        return res[::-1]


sol = Solution()

sum = 9

res = sol.FindContinuousSequence(sum)

print(res)
