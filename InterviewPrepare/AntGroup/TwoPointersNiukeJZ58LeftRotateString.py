class Solution:
    def LeftRotateString(self, str: str, n: int) -> str:
        if n == 0 or len(str) <= 1:
            return str
        # write code here
        move = n % len(str)
        left = str[0:move]
        right = str[move::]
        return right+left
