# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 20:05:24 2021

@author: Lenovo
"""


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    news = [c.upper() for c in s if 
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')]
    front = 0
    end = len(news)-1
    print(news)
    while front <= end:
        if news[front] != news[end]:
            return False
        front += 1
        end -= 1
    return True



import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_minWindow(self):
        self.assertEqual(isPalindrome('A'), True)
        self.assertEqual(isPalindrome('A man, a plan, a canal: Panama'), True)
        self.assertEqual(isPalindrome('0P'), False)
        self.assertEqual(isPalindrome('ab_a'), True)
if __name__ == '__main__':
    unittest.main()