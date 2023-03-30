class Solution:
    def multiply(self, A: list[int]) -> list[int]:
        # write code here
        b = [1]*len(A)
        # left to right
        for i in range(1, len(A)):
            b[i] *= b[i-1]*A[i]

        product = 1
        for j in range(len(A)-1, -1, -1):
            b[j] *= product
            product *= A[j]
        return b
