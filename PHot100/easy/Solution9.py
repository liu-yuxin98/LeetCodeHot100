class Solution(object):
    def isPalindrome(self, x):
        if(x<0):
            return False
        else:
            l = list()
            while(x>0):
                l.append(x%10)
                x //= 10
            lr = l[::-1]
            return lr == l


s1 = Solution
print(s1.isPalindrome(s1,1))
print(s1.isPalindrome(s1,111))
print(s1.isPalindrome(s1,121))
print(s1.isPalindrome(s1,0))
print(s1.isPalindrome(s1,-1))
print(s1.isPalindrome(s1,123))
print(s1.isPalindrome(s1,1123))