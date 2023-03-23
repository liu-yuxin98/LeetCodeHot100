class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cdict = {'(': ')', '[': ']', '{': '}'}
        for i in range(len(s)):
            if s[i] in {'(', '[', '{'}:
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                c = stack.pop()
                if cdict[c] != s[i]:
                    return False
        if stack != []:
            return False
        return True
