class Solution17:
    def letterCombinations(self, digits):
        if digits == "":
            return []
        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        res = ['']
        for num in digits:
            res =[f+s for f in res for s in KEY[num]]
        return res





s = Solution17
digits = "23"
print(s.letterCombinations(s,digits))




