class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # inplace
        n = len(s)

        for i in range(n//2):
            s[i], s[n-i-1] = s[n-i-1], s[i]
