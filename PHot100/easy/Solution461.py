class Solution461:
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')



