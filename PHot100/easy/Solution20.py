class Solution20:
    def isValid(self, s: str) -> bool:
        dict = {'(':')','{':'}','[':']','x':'x'}
        stack = ['x']
        for c in s:
            if c in dict:
                stack.append(c)
            elif dict[stack.pop()] != c:
                return False
        if len(stack) == 1:
            return True
        else:
            return False





s20 = Solution20
s = "[[[{}]]][ []"
print(s20.isValid(s20,s))