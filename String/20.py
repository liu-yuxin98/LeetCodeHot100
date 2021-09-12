# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 21:16:45 2021

@author: Lenovo
"""

def isValid(s):
    pair = {')': '(', '}': '{', ']': '['}
    stack = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if stack == []:
                return False
            if stack[-1] == pair[c]:
                stack.pop()
            else:
                return False
    if stack != []:
        return False
    return True








import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_minWindow(self):
        self.assertEqual(isValid("{[]}"), True)
        self.assertEqual(isValid("()"), True)
        self.assertEqual(isValid("()[]{}"), True)
        self.assertEqual(isValid("([)]"), False)
        self.assertEqual(isValid("["), False)
        self.assertEqual(isValid("]"), False)
if __name__ == '__main__':
    unittest.main()
    