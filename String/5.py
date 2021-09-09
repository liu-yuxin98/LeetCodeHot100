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


class TestStringMethods(unittest.TestCase):

    def test_longestPalindrome(self):
        self.assertIn(longestPalindrome("babad"), ['bab' , 'aba'])
        self.assertEqual(longestPalindrome("cbbd"), 'bb')
        self.assertEqual(longestPalindrome("a"), 'a')
        self.assertEqual(longestPalindrome("ac"), 'a')
        self.assertEqual(longestPalindrome("aaaaa"), 'aaaaa')
if __name__ == '__main__':
    unittest.main()


