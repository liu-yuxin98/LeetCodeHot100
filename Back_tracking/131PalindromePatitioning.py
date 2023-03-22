class Solution:
    def partition(self, s: str) -> list[list[str]]:
        path = []
        res = []

        def isPalindrome(s):
            for i in range(len(s)//2+1):
                if s[i] != s[len(s)-i-1]:
                    return False
            return True

        def back_track(s):
            if len(s) == 0:
                res.append(path[::])
                return

            for i in range(len(s)):
                if isPalindrome(s[0:i+1]):
                    path.append(s[0:i+1])
                    back_track(s[i+1::])
                    path.pop()

        back_track(s)

        return res


s = "aab"
s = "a"
sol = Solution()
res = sol.partition(s)
print(res)
