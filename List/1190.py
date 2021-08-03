# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 20:22:45 2021

@author: Lenovo
"""

def reverseParentheses(s):
    """
    :type s: str
    :rtype: str
    """
    i = 0
    stack = []
    while True:
        if i > len(s)-1:
            break
        if s[i] != ')':
            stack.append(s[i])
        else:
            temp = []
            while True:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    temp.append(stack.pop())
            stack.extend(temp)
        i += 1
    return ''.join(stack)





s = "a(bcdefghijkl(mno)p)q"
res = reverseParentheses(s)