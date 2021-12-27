# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:25:19 2021

@author: Lenovo
"""
import unittest


def longestPalindrome(s):
    if len(s) <= 1:
        return s
    mid_left = 0
    solution = s[0]
    while True:
        if mid_left >= len(s):
            break
        if mid_left <= len(s)-2:
            mid_right = mid_left
            while True:
                if mid_right >= len(s):
                    mid_right -= 1
                    break
                if s[mid_left] != s[mid_right]:
                    mid_right -= 1
                    break
                if s[mid_right] == s[mid_left]:
                    mid_right += 1
            left = mid_left
            right = mid_right
            while True:
                if left < 0:
                    break
                if right >= len(s):
                    break
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left + 1 >= len(solution):
                solution = s[left:right+1]
        mid_left += 1
    return solution


def longestPalindrome(s):
        def is_palindrome(s):
            i = 0
            j = len(s)-1
            while True:
                if i >= j:
                    break
                if s[i]!= s[j]:
                    return False
                i += 1
                j -= 1   
            return True
        
        if len(s) <= 1 or is_palindrome(s):
            return s
    
        max_s = s[0]
        mid = 0
        while True:
            if mid > len(s)-1:
                break
            elif mid == len(s)-1:
                if len(max_s) <= len(s[mid::]):
                    max_s =  s[mid::]
            else: 
                if s[mid]!= s[mid+1]:
                    left = mid -1
                    right = mid + 1
                else:                
                    left = mid-1
                    mid_right = mid+1
                    while True:
                        if mid_right>=len(s):
                            right = mid_right                        
                            break
                        if s[mid] != s[mid_right]:
                            right = mid_right                      
                            break
                        mid_right += 1
                    if len(max_s) <= mid_right-mid:
                        max_s = s[mid:mid_right]
    
                while True:
                    if left < 0 or right > len(s)-1:
                        break
                    if is_palindrome(s[left:right+1]):
                        if right + 1 - left >= len(max_s):
                            max_s = s[left:right+1]
                    left -= 1
                    right += 1
            mid += 1
        return max_s


# dp
def longestPalindrome(s):

        if len(s) <= 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            return s[0]
        else:
        

s = "ffffggg"
output = longestPalindrome(s)


# class TestStringMethods(unittest.TestCase):

#     def test_longestPalindrome(self):
#         self.assertIn(longestPalindrome("babad"), ['bab' , 'aba'])
#         self.assertEqual(longestPalindrome("cbbd"), 'bb')
#         self.assertEqual(longestPalindrome("a"), 'a')
#         self.assertEqual(longestPalindrome("ac"), 'a')
#         self.assertEqual(longestPalindrome("aaaaa"), 'aaaaa')
# if __name__ == '__main__':
#     unittest.main()


