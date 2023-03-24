# https://www.nowcoder.com/practice/0e26e5551f2b489b9f58bc83aa4b6c68?tpId=13&tqId=11155&tab=answerKey&from=cyc_github
class Solution:
    def replaceSpace(self, s: str) -> str:
        # write code here
        newS = []
        for c in s:
            if c == " ":
                newS.append("%20")
            else:
                newS.append(c)
        res = ''.join(newS)
        return res


lst = ['1', '4']
print(''.join(lst))
