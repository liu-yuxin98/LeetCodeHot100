class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxlength = 0
        for i in range(len(s)):
            if(s[i] == "("):
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    maxlength = max(i-stack[-1], maxlength)
        return maxlength


slist = ["", "(()", ")()())", "())()()()", "))((", "()(()", ")()(())", "(()()"]

sol = Solution()
for s in slist:
    print(s, sol.longestValidParentheses(s))
